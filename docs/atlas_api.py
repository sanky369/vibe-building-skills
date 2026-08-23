"""Atlas Cloud provider for the creative asset generation helpers."""

import json
import os
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from urllib.parse import quote, urlsplit

import requests


class AtlasCloudError(RuntimeError):
    """An Atlas Cloud error that does not expose credentials."""


class AtlasConfirmationRequired(AtlasCloudError):
    """Raised after a read-only plan when billable submission is not approved."""

    def __init__(self, plan: Dict[str, Any]):
        price = plan.get("price", {}).get("actual", {}).get("base_price", "unknown")
        payload = json.dumps(plan["payload"], separators=(",", ":"))
        super().__init__(
            "Atlas plan ready: "
            f"model={plan['model']}, current base_price={price}. "
            f"payload={payload}. Review the live quote and payload, then rerun "
            "with --confirm-submit."
        )
        self.plan = plan


class AtlasCloudClient:
    """One-submit Atlas Cloud Nano Banana Pro client with bounded GET polling."""

    API_ORIGIN = "https://api.atlascloud.ai"
    CATALOG_URL = f"{API_ORIGIN}/api/v1/models"
    GENERATE_URL = f"{API_ORIGIN}/api/v1/model/generateImage"
    PREDICTION_URL = f"{API_ORIGIN}/api/v1/model/prediction/{{request_id}}"
    MODEL_ID = "google/nano-banana-pro/text-to-image"
    TERMINAL_SUCCESSES = {"completed", "succeeded", "success"}
    TERMINAL_FAILURES = {"failed", "timeout", "canceled", "cancelled"}

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        confirm_submit: bool = False,
        poll_attempts: int = 60,
        poll_interval: float = 3.0,
        session: Any = requests,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.api_key = api_key or os.getenv("ATLASCLOUD_API_KEY")
        self.confirm_submit = confirm_submit
        self.poll_attempts = poll_attempts
        self.poll_interval = poll_interval
        self.session = session
        self.sleep = sleep

    @staticmethod
    def _unwrap(response: Dict[str, Any]) -> Any:
        if "code" not in response:
            return response
        if str(response.get("code")) != "200":
            raise AtlasCloudError(
                str(response.get("message") or "Atlas Cloud request failed")
            )
        return response.get("data")

    @staticmethod
    def _json(response: Any, action: str) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            body = response.json()
        except (requests.RequestException, ValueError) as exc:
            raise AtlasCloudError(f"Atlas Cloud {action} failed") from exc
        if not isinstance(body, dict):
            raise AtlasCloudError(f"Atlas Cloud {action} returned invalid JSON")
        return body

    @staticmethod
    def _validate_schema_url(url: str) -> None:
        parsed = urlsplit(url)
        if (
            parsed.scheme != "https"
            or parsed.hostname != "static.atlascloud.ai"
            or parsed.username
            or parsed.password
            or parsed.port not in (None, 443)
        ):
            raise AtlasCloudError("Atlas Cloud returned an untrusted schema URL")

    def _live_model_and_schema(self) -> tuple[Dict[str, Any], Dict[str, Any]]:
        try:
            catalog_response = self.session.get(
                self.CATALOG_URL,
                headers={"Accept": "application/json"},
                timeout=30,
            )
        except requests.RequestException as exc:
            raise AtlasCloudError("Atlas Cloud model catalog read failed") from exc
        catalog = self._unwrap(self._json(catalog_response, "model catalog read"))
        if not isinstance(catalog, list):
            raise AtlasCloudError("Atlas Cloud model catalog has an invalid shape")
        matches = [
            item
            for item in catalog
            if isinstance(item, dict) and item.get("model") == self.MODEL_ID
        ]
        if len(matches) != 1:
            raise AtlasCloudError(f"model not found in live catalog: {self.MODEL_ID}")
        model = matches[0]
        schema_url = model.get("schema")
        if not isinstance(schema_url, str) or not schema_url:
            raise AtlasCloudError("Atlas Cloud model has no input schema")
        self._validate_schema_url(schema_url)
        try:
            schema_response = self.session.get(
                schema_url,
                headers={"Accept": "application/json"},
                timeout=30,
            )
        except requests.RequestException as exc:
            raise AtlasCloudError("Atlas Cloud model schema read failed") from exc
        schema_document = self._json(schema_response, "model schema read")
        schema = (
            schema_document.get("components", {})
            .get("schemas", {})
            .get("Input")
        )
        if not isinstance(schema, dict):
            raise AtlasCloudError("Atlas Cloud model schema has an invalid shape")
        return model, schema

    @staticmethod
    def _validate_payload(payload: Dict[str, Any], schema: Dict[str, Any]) -> None:
        properties = schema.get("properties")
        required = schema.get("required", [])
        if not isinstance(properties, dict) or not isinstance(required, list):
            raise AtlasCloudError("Atlas Cloud model schema is malformed")
        missing = [name for name in required if name not in payload]
        if missing:
            raise AtlasCloudError(
                f"Atlas Cloud payload is missing: {', '.join(sorted(missing))}"
            )
        unknown = sorted(set(payload) - set(properties))
        if unknown:
            raise AtlasCloudError(
                f"Atlas Cloud payload has unsupported fields: {', '.join(unknown)}"
            )
        for name, value in payload.items():
            definition = properties.get(name)
            if not isinstance(definition, dict):
                continue
            allowed = definition.get("enum")
            if isinstance(allowed, list) and value not in allowed:
                raise AtlasCloudError(f"invalid Atlas Cloud {name}: {value!r}")

    def plan_image(
        self,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        enable_web_search: bool = False,
        sync_mode: bool = False,
    ) -> Dict[str, Any]:
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt must be a non-empty string")
        if num_images != 1:
            raise ValueError("Atlas Cloud currently supports one image per submission")
        if output_format not in {"png", "jpeg"}:
            raise ValueError("Atlas Cloud output_format must be png or jpeg")
        payload = {
            "model": self.MODEL_ID,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution.lower(),
            "output_format": output_format,
            "enable_web_search": enable_web_search,
            "enable_sync_mode": sync_mode,
            "enable_base64_output": False,
        }
        model, schema = self._live_model_and_schema()
        self._validate_payload(payload, schema)
        return {
            "provider": "atlas",
            "model": self.MODEL_ID,
            "price": model.get("price") or {},
            "payload": payload,
        }

    def _submit_once(self, payload: Dict[str, Any]) -> str:
        if not self.api_key:
            raise AtlasCloudError("ATLASCLOUD_API_KEY is not set")
        try:
            response = self.session.post(
                self.GENERATE_URL,
                json=payload,
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                timeout=300,
            )
        except requests.RequestException as exc:
            raise AtlasCloudError(
                "Atlas Cloud generation submission failed and was not retried"
            ) from exc
        data = self._unwrap(self._json(response, "generation submission"))
        request_id = data.get("id") if isinstance(data, dict) else None
        if not isinstance(request_id, str) or not request_id:
            raise AtlasCloudError("Atlas Cloud submission returned no request ID")
        return request_id

    def _poll_prediction(self, request_id: str) -> Dict[str, Any]:
        if self.poll_attempts < 1 or self.poll_interval < 0:
            raise AtlasCloudError("poll attempts and interval must be non-negative")
        if not self.api_key:
            raise AtlasCloudError("ATLASCLOUD_API_KEY is not set")
        url = self.PREDICTION_URL.format(request_id=quote(request_id, safe=""))
        last_error: Optional[Exception] = None
        for attempt in range(self.poll_attempts):
            try:
                response = self.session.get(
                    url,
                    headers={
                        "Accept": "application/json",
                        "Authorization": f"Bearer {self.api_key}",
                    },
                    timeout=30,
                )
                data = self._unwrap(self._json(response, "prediction read"))
                last_error = None
            except (requests.RequestException, AtlasCloudError) as exc:
                last_error = exc
                data = None
            if data is not None:
                if not isinstance(data, dict):
                    raise AtlasCloudError("Atlas Cloud prediction has an invalid shape")
                status = str(data.get("status") or "").lower()
                if status in self.TERMINAL_SUCCESSES:
                    outputs = data.get("outputs")
                    if not isinstance(outputs, list) or not outputs:
                        raise AtlasCloudError("completed prediction has no outputs")
                    return data
                if status in self.TERMINAL_FAILURES:
                    raise AtlasCloudError(
                        str(data.get("error") or f"prediction ended with {status}")
                    )
            if attempt + 1 < self.poll_attempts:
                self.sleep(min(self.poll_interval * (2**attempt), 15.0))
        if last_error:
            raise AtlasCloudError(
                f"prediction polling exhausted after {self.poll_attempts} reads"
            ) from last_error
        raise AtlasCloudError(
            f"prediction did not complete after {self.poll_attempts} reads"
        )

    def generate_image(
        self,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        enable_web_search: bool = False,
        sync_mode: bool = False,
    ) -> Dict[str, Any]:
        plan = self.plan_image(
            prompt=prompt,
            num_images=num_images,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format=output_format,
            enable_web_search=enable_web_search,
            sync_mode=sync_mode,
        )
        if not self.confirm_submit:
            raise AtlasConfirmationRequired(plan)
        request_id = self._submit_once(plan["payload"])
        prediction = self._poll_prediction(request_id)
        images: List[Dict[str, str]] = []
        for output in prediction["outputs"]:
            url = output if isinstance(output, str) else output.get("url")
            if isinstance(url, str) and url:
                images.append({"url": url})
        if not images:
            raise AtlasCloudError("completed prediction has no usable image URLs")
        return {
            "images": images,
            "request_id": request_id,
            "model": plan["model"],
            "price": plan["price"],
        }

    def download_image(self, image_url: str, output_path: str) -> str:
        try:
            response = self.session.get(image_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise AtlasCloudError("Atlas Cloud output download failed") from exc
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_bytes(response.content)
        return output_path
