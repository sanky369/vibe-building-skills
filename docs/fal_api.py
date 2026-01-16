"""
FAL.ai Nanobanana Pro API Integration Module
Handles all interactions with FAL.ai nanobanana pro image generation model
"""

import os
import json
import requests
from typing import Optional, Dict, Any, List
from pathlib import Path
from datetime import datetime

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
        
        # Create product directory
        product_dir = self.output_dir / "product-photography" / product_name.lower().replace(" ", "-")
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
                    filename = f"{product_name.lower().replace(' ', '_')}_{i+1}_{timestamp}.png"
                    filepath = product_dir / filename
                    
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
        
        # Create social directory
        social_dir = self.output_dir / "social-graphics" / platform.lower()
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
                    filename = f"{platform}_{topic.lower().replace(' ', '_')}_{i+1}_{timestamp}.png"
                    filepath = social_dir / filename
                    
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
        
        # Create brand directory
        brand_dir = self.output_dir / "brand-assets" / brand_name.lower().replace(" ", "-") / asset_type.lower()
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
                    filename = f"{asset_type}_{i+1}_{timestamp}.png"
                    filepath = brand_dir / filename
                    
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
        
        # Create directory
        asset_dir = self.output_dir / asset_category.lower() / asset_name.lower().replace(" ", "-")
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
                    filename = f"{asset_name.lower().replace(' ', '_')}_{i+1}_{timestamp}.{ext}"
                    filepath = asset_dir / filename
                    
                    self.client.download_image(image_url, str(filepath))
                    saved_paths.append(str(filepath))
            
            result["saved_paths"] = saved_paths
        
        return result
