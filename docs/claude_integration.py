"""
Claude Code Integration Module
Provides functions for Claude Code to call for asset generation with nanobanana pro
"""

import os
import json
from pathlib import Path
from typing import Optional, List, Dict, Any
from fal_api import CreativeAssetGenerator


class ClaudeCreativeAssistant:
    """Assistant class for Claude Code to generate creative assets with nanobanana pro"""
    
    def __init__(self, output_dir: str = "./assets"):
        """Initialize the assistant"""
        self.generator = CreativeAssetGenerator(output_dir=output_dir)
        self.output_dir = Path(output_dir)
    
    def generate_product_photo(
        self,
        product_name: str,
        description: str,
        style: str = "professional photography",
        lighting: str = "studio lighting",
        background: str = "white background",
        num_variations: int = 1,
        resolution: str = "2K",
        aspect_ratio: str = "1:1"
    ) -> Dict[str, Any]:
        """
        Generate product photography
        
        Args:
            product_name: Name of the product
            description: What the product looks like
            style: Photography style
            lighting: Lighting setup
            background: Background description
            num_variations: Number of variations to generate
            resolution: Image resolution (1K, 2K, 4K)
            aspect_ratio: Image aspect ratio
        
        Returns:
            Dictionary with generated image paths and metadata
        """
        
        prompt = f"{description}, {style}, {lighting}, {background}, sharp focus, 4K, professional quality"
        
        result = self.generator.generate_product_photo(
            product_name=product_name,
            prompt=prompt,
            num_images=num_variations,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            save=True
        )
        
        return {
            "success": "saved_paths" in result,
            "images": result.get("saved_paths", []),
            "prompt_used": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio
        }
    
    def generate_social_post(
        self,
        platform: str,
        topic: str,
        description: str,
        style: str = "modern design",
        mood: str = "professional",
        num_variations: int = 1,
        resolution: str = "2K",
        aspect_ratio: str = "1:1"
    ) -> Dict[str, Any]:
        """
        Generate social media post graphics
        
        Args:
            platform: Social platform (instagram, linkedin, twitter, tiktok, pinterest)
            topic: Topic of the post
            description: What should be in the graphic
            style: Design style
            mood: Mood of the graphic
            num_variations: Number of variations
            resolution: Image resolution
            aspect_ratio: Image aspect ratio
        
        Returns:
            Dictionary with generated image paths and metadata
        """
        
        prompt = f"{description}, {style}, {mood}, eye-catching, professional quality, 4K, trending on {platform}"
        
        result = self.generator.generate_social_graphic(
            platform=platform,
            topic=topic,
            prompt=prompt,
            num_images=num_variations,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            save=True
        )
        
        return {
            "success": "saved_paths" in result,
            "images": result.get("saved_paths", []),
            "prompt_used": prompt,
            "platform": platform,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio
        }
    
    def generate_brand_element(
        self,
        brand_name: str,
        element_type: str,
        description: str,
        style: str = "modern",
        colors: str = "professional colors",
        num_variations: int = 1,
        resolution: str = "2K",
        aspect_ratio: str = "1:1"
    ) -> Dict[str, Any]:
        """
        Generate brand elements (logo, icons, patterns)
        
        Args:
            brand_name: Name of the brand
            element_type: Type of element (logo, icon, pattern, illustration, texture)
            description: What the element should look like
            style: Design style
            colors: Color description
            num_variations: Number of variations
            resolution: Image resolution
            aspect_ratio: Image aspect ratio
        
        Returns:
            Dictionary with generated image paths and metadata
        """
        
        prompt = f"{description}, {style}, {colors}, professional quality, 4K, scalable design"
        
        result = self.generator.generate_brand_asset(
            asset_type=element_type,
            brand_name=brand_name,
            prompt=prompt,
            num_images=num_variations,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            save=True
        )
        
        return {
            "success": "saved_paths" in result,
            "images": result.get("saved_paths", []),
            "prompt_used": prompt,
            "element_type": element_type,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio
        }
    
    def generate_custom_asset(
        self,
        category: str,
        name: str,
        prompt: str,
        num_variations: int = 1,
        resolution: str = "2K",
        aspect_ratio: str = "1:1",
        output_format: str = "png",
        enable_web_search: bool = False
    ) -> Dict[str, Any]:
        """
        Generate custom asset with full control
        
        Args:
            category: Asset category
            name: Asset name
            prompt: Full detailed prompt
            num_variations: Number of variations
            resolution: Image resolution
            aspect_ratio: Image aspect ratio
            output_format: Output format (png, jpeg, webp)
            enable_web_search: Enable Google Search integration
        
        Returns:
            Dictionary with generated image paths and metadata
        """
        
        result = self.generator.generate_custom(
            asset_category=category,
            asset_name=name,
            prompt=prompt,
            num_images=num_variations,
            resolution=resolution,
            aspect_ratio=aspect_ratio,
            output_format=output_format,
            enable_web_search=enable_web_search,
            save=True
        )
        
        return {
            "success": "saved_paths" in result,
            "images": result.get("saved_paths", []),
            "prompt_used": prompt,
            "category": category,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "web_search_enabled": enable_web_search
        }
    
    def batch_generate(
        self,
        assets: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Generate multiple assets in batch
        
        Args:
            assets: List of asset specifications
                Each should have: type, name, description, and type-specific fields
        
        Returns:
            List of results for each asset
        """
        
        results = []
        
        for asset in assets:
            asset_type = asset.get("type", "custom").lower()
            
            try:
                if asset_type == "product":
                    result = self.generate_product_photo(
                        product_name=asset.get("name", "product"),
                        description=asset.get("description", ""),
                        style=asset.get("style", "professional photography"),
                        lighting=asset.get("lighting", "studio lighting"),
                        background=asset.get("background", "white background"),
                        num_variations=asset.get("num_variations", 1),
                        resolution=asset.get("resolution", "2K"),
                        aspect_ratio=asset.get("aspect_ratio", "1:1")
                    )
                
                elif asset_type == "social":
                    result = self.generate_social_post(
                        platform=asset.get("platform", "instagram"),
                        topic=asset.get("topic", asset.get("name", "post")),
                        description=asset.get("description", ""),
                        style=asset.get("style", "modern design"),
                        mood=asset.get("mood", "professional"),
                        num_variations=asset.get("num_variations", 1),
                        resolution=asset.get("resolution", "2K"),
                        aspect_ratio=asset.get("aspect_ratio", "1:1")
                    )
                
                elif asset_type == "brand":
                    result = self.generate_brand_element(
                        brand_name=asset.get("brand_name", "brand"),
                        element_type=asset.get("element_type", "logo"),
                        description=asset.get("description", ""),
                        style=asset.get("style", "modern"),
                        colors=asset.get("colors", "professional colors"),
                        num_variations=asset.get("num_variations", 1),
                        resolution=asset.get("resolution", "2K"),
                        aspect_ratio=asset.get("aspect_ratio", "1:1")
                    )
                
                else:  # custom
                    result = self.generate_custom_asset(
                        category=asset.get("category", "custom"),
                        name=asset.get("name", "asset"),
                        prompt=asset.get("prompt", asset.get("description", "")),
                        num_variations=asset.get("num_variations", 1),
                        resolution=asset.get("resolution", "2K"),
                        aspect_ratio=asset.get("aspect_ratio", "1:1"),
                        output_format=asset.get("format", "png"),
                        enable_web_search=asset.get("web_search", False)
                    )
                
                result["asset_name"] = asset.get("name", "unknown")
                results.append(result)
                
            except Exception as e:
                results.append({
                    "success": False,
                    "error": str(e),
                    "asset_name": asset.get("name", "unknown")
                })
        
        return results
    
    def get_asset_summary(self) -> Dict[str, Any]:
        """
        Get summary of all generated assets
        
        Returns:
            Dictionary with asset counts and organization
        """
        
        summary = {
            "total_assets": 0,
            "by_category": {},
            "asset_dir": str(self.output_dir)
        }
        
        if self.output_dir.exists():
            for category_dir in self.output_dir.iterdir():
                if category_dir.is_dir():
                    count = len(list(category_dir.rglob("*.png"))) + len(list(category_dir.rglob("*.jpeg"))) + len(list(category_dir.rglob("*.webp")))
                    if count > 0:
                        summary["by_category"][category_dir.name] = count
                        summary["total_assets"] += count
        
        return summary


# Global assistant instance
_assistant = None


def get_assistant(output_dir: str = "./assets") -> ClaudeCreativeAssistant:
    """Get or create the global assistant instance"""
    global _assistant
    if _assistant is None:
        _assistant = ClaudeCreativeAssistant(output_dir=output_dir)
    return _assistant


# Convenience functions for Claude Code
def generate_product(
    product_name: str,
    description: str,
    style: str = "professional photography",
    num_variations: int = 1
) -> Dict[str, Any]:
    """Quick function to generate product photos"""
    assistant = get_assistant()
    return assistant.generate_product_photo(
        product_name=product_name,
        description=description,
        style=style,
        num_variations=num_variations
    )


def generate_social(
    platform: str,
    topic: str,
    description: str,
    num_variations: int = 1
) -> Dict[str, Any]:
    """Quick function to generate social graphics"""
    assistant = get_assistant()
    return assistant.generate_social_post(
        platform=platform,
        topic=topic,
        description=description,
        num_variations=num_variations
    )


def generate_brand(
    brand_name: str,
    element_type: str,
    description: str,
    num_variations: int = 1
) -> Dict[str, Any]:
    """Quick function to generate brand elements"""
    assistant = get_assistant()
    return assistant.generate_brand_element(
        brand_name=brand_name,
        element_type=element_type,
        description=description,
        num_variations=num_variations
    )


def generate_asset(
    category: str,
    name: str,
    prompt: str,
    num_variations: int = 1
) -> Dict[str, Any]:
    """Quick function to generate custom assets"""
    assistant = get_assistant()
    return assistant.generate_custom_asset(
        category=category,
        name=name,
        prompt=prompt,
        num_variations=num_variations
    )


def batch_generate_assets(assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Quick function to batch generate assets"""
    assistant = get_assistant()
    return assistant.batch_generate(assets)


def get_summary() -> Dict[str, Any]:
    """Get summary of generated assets"""
    assistant = get_assistant()
    return assistant.get_asset_summary()
