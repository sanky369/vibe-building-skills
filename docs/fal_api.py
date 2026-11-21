"""
FAL.ai Nanobanana Pro API Integration Module
Handles all interactions with FAL.ai nanobanana pro image generation model
"""

import os
import re
import json
import unicodedata
import requests
from typing import Optional, Dict, Any, List
from pathlib import Path, PurePosixPath, PureWindowsPath
from datetime import datetime

_BIDI_AND_CTRL_RE = re.compile(r"[\x00-\x1f\x7f\u200b-\u200f\u202a-\u202e\u2060-\u206f\ufeff]")


def _sanitize_segment(raw: str, sep: str = "-") -> str:
    """Normalize and sanitize a user-supplied name into a single safe path segment."""
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError("Path segment must be a non-empty string")
    cleaned = _BIDI_AND_CTRL_RE.sub("", unicodedata.normalize("NFC", raw)).strip()
    if (
        cleaned.startswith(("/", "\\"))
        or ".." in PurePosixPath(cleaned).parts
        or ".." in PureWindowsPath(cleaned).parts
        or PureWindowsPath(cleaned).drive
    ):
        raise ValueError(f"Unsafe path traversal segment rejected: {raw!r}")
    # Replace path separators and whitespace with sep; keep Unicode word chars and Arabic marks
    cleaned = re.sub(r"[/\\:\s]+", sep, cleaned.lower())
    cleaned = re.sub(r"[^\w\-\u064b-\u065f\u0670]", "", cleaned, flags=re.UNICODE)
    cleaned = re.sub(rf"{re.escape(sep)}+", sep, cleaned).strip(f".{sep}_")
    if not cleaned or cleaned in {".", ".."}:
        raise ValueError(f"Path segment resolves to empty after sanitization: {raw!r}")
    return cleaned


def _resolve_within_base(base_dir: Path, *segments: str) -> Path:
    """Join segments under base_dir and verify the resolved path stays inside base_dir."""
    base_resolved = base_dir.resolve()
    candidate = base_resolved.joinpath(*segments).resolve()
    try:
        candidate.relative_to(base_resolved)
    except ValueError as exc:
        raise ValueError(f"Resolved path escapes output_dir: {candidate}") from exc
    return candidate

class NanobananProClient:
    """Client for FAL.ai nanobanana pro image generation API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize nanobanana pro API client
        
        Args:
            api_key: FAL.ai API key (defaults to FAL_API_KEY or FAL_KEY env var)
        """
        # Try both FAL_API_KEY and FAL_KEY environment variables
        self.api_key = api_key or os.getenv("FAL_API_KEY") or os.getenv("FAL_KEY")
        if not self.api_key:
            raise ValueError(
                "FAL_API_KEY or FAL_KEY not found. Set one of these environment variables or pass api_key parameter."
            )
        
        self.base_url = "https://api.fal.ai/v1"
        self.model_id = "fal-ai/nano-banana-pro"
        self.headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_image(
        self,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        enable_web_search: bool = False,
        sync_mode: bool = False
    ) -> Dict[str, Any]:
        """
        Generate image using nanobanana pro
        
        Args:
            prompt: Text description of image to generate
            num_images: Number of images to generate (1-4, default 1)
            aspect_ratio: Image aspect ratio (default "1:1")
                Options: 21:9, 16:9, 3:2, 4:3, 5:4, 1:1, 4:5, 3:4, 2:3, 9:16
            resolution: Image resolution (default "2K")
                Options: 1K, 2K, 4K
            output_format: Output format (default "png")
                Options: jpeg, png, webp
            enable_web_search: Enable Google Search integration (default False)
            sync_mode: Return as data URI (default False)
        
        Returns:
            Dictionary with generated images and metadata
        """
        
        # Validate inputs
        if not prompt or not isinstance(prompt, str):
            raise ValueError("Prompt must be a non-empty string")
        
        if num_images < 1 or num_images > 4:
            raise ValueError("num_images must be between 1 and 4")
        
        valid_aspect_ratios = ["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"]
        if aspect_ratio not in valid_aspect_ratios:
            raise ValueError(f"aspect_ratio must be one of {valid_aspect_ratios}")
        
        valid_resolutions = ["1K", "2K", "4K"]
        if resolution not in valid_resolutions:
            raise ValueError(f"resolution must be one of {valid_resolutions}")
        
        valid_formats = ["jpeg", "png", "webp"]
        if output_format not in valid_formats:
            raise ValueError(f"output_format must be one of {valid_formats}")
        
        # Prepare request payload
        payload = {
            "prompt": prompt,
            "num_images": num_images,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
            "output_format": output_format,
            "sync_mode": sync_mode,
            "enable_web_search": enable_web_search
        }
        
        # Make API request
        endpoint = f"{self.base_url}/models/{self.model_id}/requests"
        
        try:
            response = requests.post(
                endpoint,
                json=payload,
                headers=self.headers,
                timeout=300
            )
            response.raise_for_status()
            
            result = response.json()
            return result
            
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"FAL.ai API error: {str(e)}")
    
    def get_request_status(self, request_id: str) -> Dict[str, Any]:
        """
        Get status of a submitted request
        
        Args:
            request_id: ID of the request
        
        Returns:
            Request status and result if complete
        """
        endpoint = f"{self.base_url}/models/{self.model_id}/requests/{request_id}"
        
        try:
            response = requests.get(
                endpoint,
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"FAL.ai API error: {str(e)}")
    
    def download_image(self, image_url: str, output_path: str) -> str:
        """
        Download generated image from URL
        
        Args:
            image_url: URL of the image to download
            output_path: Path where to save the image
        
        Returns:
            Path to saved image
        """
        try:
            response = requests.get(image_url, timeout=30)
            response.raise_for_status()
            
            # Create directory if it doesn't exist
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            
            # Save image
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            return output_path
            
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to download image: {str(e)}")


class CreativeAssetGenerator:
    """High-level interface for generating creative assets with nanobanana pro"""
    
    def __init__(self, api_key: Optional[str] = None, output_dir: str = "./assets"):
        """
        Initialize creative asset generator
        
        Args:
            api_key: FAL.ai API key
            output_dir: Base directory for saving assets
        """
        self.client = NanobananProClient(api_key)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_product_photo(
        self,
        product_name: str,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        save: bool = True
    ) -> Dict[str, Any]:
        """
        Generate product photography
        
        Args:
            product_name: Name of the product
            prompt: Detailed prompt for product photo
            num_images: Number of variations to generate
            aspect_ratio: Image aspect ratio
            resolution: Image resolution
            save: Whether to save images to disk
        
        Returns:
            Dictionary with image URLs and metadata
        """
        
        # Create product directory safely inside output_dir
        safe_product_dir = _sanitize_segment(product_name, sep="-")
        safe_product_file = _sanitize_segment(product_name, sep="_")
        product_dir = _resolve_within_base(self.output_dir, "product-photography", safe_product_dir)
        product_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate images
        result = self.client.generate_image(
            prompt=prompt,
            num_images=num_images,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format="png"
        )
        
        # Download and save images
        if save and "images" in result:
            saved_paths = []
            for i, image_data in enumerate(result["images"]):
                image_url = image_data.get("url")
                if image_url:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{safe_product_file}_{i+1}_{timestamp}.png"
                    filepath = _resolve_within_base(product_dir, filename)
                    
                    self.client.download_image(image_url, str(filepath))
                    saved_paths.append(str(filepath))
            
            result["saved_paths"] = saved_paths
        
        return result
    
    def generate_social_graphic(
        self,
        platform: str,
        topic: str,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        save: bool = True
    ) -> Dict[str, Any]:
        """
        Generate social media graphics
        
        Args:
            platform: Social platform (instagram, linkedin, twitter, tiktok, pinterest)
            topic: Topic of the graphic
            prompt: Detailed prompt for the graphic
            num_images: Number of variations
            aspect_ratio: Image aspect ratio
            resolution: Image resolution
            save: Whether to save images
        
        Returns:
            Dictionary with image URLs and metadata
        """
        
        # Create social directory safely inside output_dir
        safe_platform = _sanitize_segment(platform, sep="-")
        safe_topic = _sanitize_segment(topic, sep="_")
        social_dir = _resolve_within_base(self.output_dir, "social-graphics", safe_platform)
        social_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate images
        result = self.client.generate_image(
            prompt=prompt,
            num_images=num_images,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format="png"
        )
        
        # Download and save images
        if save and "images" in result:
            saved_paths = []
            for i, image_data in enumerate(result["images"]):
                image_url = image_data.get("url")
                if image_url:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{safe_platform}_{safe_topic}_{i+1}_{timestamp}.png"
                    filepath = _resolve_within_base(social_dir, filename)
                    
                    self.client.download_image(image_url, str(filepath))
                    saved_paths.append(str(filepath))
            
            result["saved_paths"] = saved_paths
        
        return result
    
    def generate_brand_asset(
        self,
        asset_type: str,
        brand_name: str,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        save: bool = True
    ) -> Dict[str, Any]:
        """
        Generate brand assets (logos, icons, patterns)
        
        Args:
            asset_type: Type of asset (logo, icon, pattern, illustration, texture)
            brand_name: Name of the brand
            prompt: Detailed prompt for the asset
            num_images: Number of variations
            aspect_ratio: Image aspect ratio
            resolution: Image resolution
            save: Whether to save images
        
        Returns:
            Dictionary with image URLs and metadata
        """
        
        # Create brand directory safely inside output_dir
        safe_brand = _sanitize_segment(brand_name, sep="-")
        safe_asset_type = _sanitize_segment(asset_type, sep="_")
        brand_dir = _resolve_within_base(self.output_dir, "brand-assets", safe_brand, safe_asset_type)
        brand_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate images
        result = self.client.generate_image(
            prompt=prompt,
            num_images=num_images,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format="png"
        )
        
        # Download and save images
        if save and "images" in result:
            saved_paths = []
            for i, image_data in enumerate(result["images"]):
                image_url = image_data.get("url")
                if image_url:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{safe_asset_type}_{i+1}_{timestamp}.png"
                    filepath = _resolve_within_base(brand_dir, filename)
                    
                    self.client.download_image(image_url, str(filepath))
                    saved_paths.append(str(filepath))
            
            result["saved_paths"] = saved_paths
        
        return result
    
    def generate_custom(
        self,
        asset_category: str,
        asset_name: str,
        prompt: str,
        num_images: int = 1,
        aspect_ratio: str = "1:1",
        resolution: str = "2K",
        output_format: str = "png",
        enable_web_search: bool = False,
        save: bool = True
    ) -> Dict[str, Any]:
        """
        Generate custom asset with full control
        
        Args:
            asset_category: Category for organizing assets
            asset_name: Name of the asset
            prompt: Detailed prompt
            num_images: Number of variations
            aspect_ratio: Image aspect ratio
            resolution: Image resolution
            output_format: Output format (png, jpeg, webp)
            enable_web_search: Enable Google Search integration
            save: Whether to save images
        
        Returns:
            Dictionary with image URLs and metadata
        """
        
        # Create directory safely inside output_dir
        safe_category = _sanitize_segment(asset_category, sep="-")
        safe_name_dir = _sanitize_segment(asset_name, sep="-")
        safe_name_file = _sanitize_segment(asset_name, sep="_")
        asset_dir = _resolve_within_base(self.output_dir, safe_category, safe_name_dir)
        asset_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate images
        result = self.client.generate_image(
            prompt=prompt,
            num_images=num_images,
            aspect_ratio=aspect_ratio,
            resolution=resolution,
            output_format=output_format,
            enable_web_search=enable_web_search
        )
        
        # Download and save images
        if save and "images" in result:
            saved_paths = []
            for i, image_data in enumerate(result["images"]):
                image_url = image_data.get("url")
                if image_url:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    ext = output_format if output_format in ["png", "jpeg", "webp"] else "png"
                    filename = f"{safe_name_file}_{i+1}_{timestamp}.{ext}"
                    filepath = _resolve_within_base(asset_dir, filename)
                    
                    self.client.download_image(image_url, str(filepath))
                    saved_paths.append(str(filepath))
            
            result["saved_paths"] = saved_paths
        
        return result
