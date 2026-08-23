import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "docs"))

from atlas_api import AtlasCloudClient, AtlasConfirmationRequired
from fal_api import CreativeAssetGenerator, NanobananProClient


class Response:
    def __init__(self, payload, content=b""):
        self.payload = payload
        self.content = content

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def catalog():
    return {
        "code": 200,
        "data": [
            {
                "model": AtlasCloudClient.MODEL_ID,
                "schema": "https://static.atlascloud.ai/model/schema/model.json",
                "price": {"actual": {"base_price": "0.14"}},
            }
        ],
    }


def schema():
    return {
        "components": {
            "schemas": {
                "Input": {
                    "required": ["model", "prompt"],
                    "properties": {
                        "model": {"type": "string"},
                        "prompt": {"type": "string"},
                        "aspect_ratio": {"enum": ["1:1", "16:9"]},
                        "resolution": {"enum": ["1k", "2k", "4k"]},
                        "output_format": {"enum": ["png", "jpeg"]},
                        "enable_web_search": {"type": "boolean"},
                        "enable_sync_mode": {"type": "boolean"},
                        "enable_base64_output": {"type": "boolean"},
                    },
                }
            }
        }
    }


class AtlasCloudClientTests(unittest.TestCase):
    def test_plan_reads_live_catalog_and_schema_without_posting(self):
        session = Mock()
        session.get.side_effect = [Response(catalog()), Response(schema())]
        client = AtlasCloudClient(session=session)

        plan = client.plan_image("A precise image", aspect_ratio="16:9")

        self.assertEqual(plan["model"], AtlasCloudClient.MODEL_ID)
        self.assertEqual(plan["price"]["actual"]["base_price"], "0.14")
        self.assertEqual(plan["payload"]["resolution"], "2k")
        session.post.assert_not_called()

    def test_generation_requires_confirmation_and_does_not_post(self):
        session = Mock()
        session.get.side_effect = [Response(catalog()), Response(schema())]
        client = AtlasCloudClient(api_key="secret", session=session)

        with self.assertRaises(AtlasConfirmationRequired) as raised:
            client.generate_image("A precise image")

        self.assertEqual(raised.exception.plan["model"], AtlasCloudClient.MODEL_ID)
        session.post.assert_not_called()

    def test_confirmed_generation_posts_once_and_polls_with_get(self):
        session = Mock()
        session.get.side_effect = [
            Response(catalog()),
            Response(schema()),
            requests.ConnectionError("temporary"),
            Response({"code": 200, "data": {"status": "running"}}),
            Response(
                {
                    "code": 200,
                    "data": {
                        "status": "completed",
                        "outputs": ["https://example.com/image.png"],
                    },
                }
            ),
        ]
        session.post.return_value = Response(
            {"code": 200, "data": {"id": "request-1"}}
        )
        sleeps = []
        client = AtlasCloudClient(
            api_key="secret",
            confirm_submit=True,
            poll_attempts=3,
            poll_interval=1,
            session=session,
            sleep=sleeps.append,
        )

        result = client.generate_image("A precise image")

        self.assertEqual(result["images"], [{"url": "https://example.com/image.png"}])
        self.assertEqual(session.post.call_count, 1)
        self.assertEqual(sleeps, [1, 2])

    def test_post_failure_is_not_retried(self):
        session = Mock()
        session.get.side_effect = [Response(catalog()), Response(schema())]
        session.post.side_effect = requests.ConnectionError("offline")
        client = AtlasCloudClient(
            api_key="secret",
            confirm_submit=True,
            session=session,
        )

        with self.assertRaisesRegex(RuntimeError, "not retried"):
            client.generate_image("A precise image")

        self.assertEqual(session.post.call_count, 1)

    def test_atlas_rejects_multiple_images_and_webp(self):
        client = AtlasCloudClient(session=Mock())
        with self.assertRaisesRegex(ValueError, "one image"):
            client.plan_image("A precise image", num_images=2)
        with self.assertRaisesRegex(ValueError, "png or jpeg"):
            client.plan_image("A precise image", output_format="webp")

    def test_generator_keeps_fal_as_default(self):
        with tempfile.TemporaryDirectory() as directory:
            generator = CreativeAssetGenerator(
                api_key="fal-secret",
                output_dir=directory,
            )
            self.assertIsInstance(generator.client, NanobananProClient)

    def test_generator_selects_atlas_only_when_requested(self):
        with tempfile.TemporaryDirectory() as directory:
            generator = CreativeAssetGenerator(
                output_dir=directory,
                provider="atlas",
            )
            self.assertIsInstance(generator.client, AtlasCloudClient)


if __name__ == "__main__":
    unittest.main()
