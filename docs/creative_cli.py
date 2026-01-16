#!/usr/bin/env python3
"""
Creative Asset Generation CLI
Command-line interface for generating creative assets with nanobanana pro
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional
from fal_api import CreativeAssetGenerator, NanobananProClient


def print_success(message: str):
    """Print success message"""
    print(f"✅ {message}")


def print_error(message: str):
    """Print error message"""
    print(f"❌ {message}", file=sys.stderr)


def print_info(message: str):
    """Print info message"""
    print(f"ℹ️  {message}")


def generate_product_photo(args):
    """Generate product photography"""
    try:
        generator = CreativeAssetGenerator(output_dir=args.output_dir)
        
        print_info(f"Generating product photo for: {args.product_name}")
        print_info(f"Prompt: {args.prompt}")
        print_info(f"Resolution: {args.resolution}")
        print_info(f"Aspect ratio: {args.aspect_ratio}")
        print_info(f"Generating {args.num_images} image(s)...")
        
        result = generator.generate_product_photo(
            product_name=args.product_name,
            prompt=args.prompt,
            num_images=args.num_images,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            save=True
        )
        
        if "saved_paths" in result:
            print_success(f"Generated {len(result['saved_paths'])} image(s)")
            for path in result["saved_paths"]:
                print(f"  📸 {path}")
        else:
            print_error("No images were generated")
            return 1
        
        return 0
        
    except Exception as e:
        print_error(f"Failed to generate product photo: {str(e)}")
        return 1


def generate_social_graphic(args):
    """Generate social media graphics"""
    try:
        generator = CreativeAssetGenerator(output_dir=args.output_dir)
        
        print_info(f"Generating {args.platform} graphic for: {args.topic}")
        print_info(f"Prompt: {args.prompt}")
        print_info(f"Resolution: {args.resolution}")
        print_info(f"Aspect ratio: {args.aspect_ratio}")
        print_info(f"Generating {args.num_images} image(s)...")
        
        result = generator.generate_social_graphic(
            platform=args.platform,
            topic=args.topic,
            prompt=args.prompt,
            num_images=args.num_images,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            save=True
        )
        
        if "saved_paths" in result:
            print_success(f"Generated {len(result['saved_paths'])} image(s)")
            for path in result["saved_paths"]:
                print(f"  📱 {path}")
        else:
            print_error("No images were generated")
            return 1
        
        return 0
        
    except Exception as e:
        print_error(f"Failed to generate social graphic: {str(e)}")
        return 1


def generate_brand_asset(args):
    """Generate brand assets"""
    try:
        generator = CreativeAssetGenerator(output_dir=args.output_dir)
        
        print_info(f"Generating {args.asset_type} for: {args.brand_name}")
        print_info(f"Prompt: {args.prompt}")
        print_info(f"Resolution: {args.resolution}")
        print_info(f"Aspect ratio: {args.aspect_ratio}")
        print_info(f"Generating {args.num_images} image(s)...")
        
        result = generator.generate_brand_asset(
            asset_type=args.asset_type,
            brand_name=args.brand_name,
            prompt=args.prompt,
            num_images=args.num_images,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            save=True
        )
        
        if "saved_paths" in result:
            print_success(f"Generated {len(result['saved_paths'])} image(s)")
            for path in result["saved_paths"]:
                print(f"  🎨 {path}")
        else:
            print_error("No images were generated")
            return 1
        
        return 0
        
    except Exception as e:
        print_error(f"Failed to generate brand asset: {str(e)}")
        return 1


def generate_custom(args):
    """Generate custom asset"""
    try:
        generator = CreativeAssetGenerator(output_dir=args.output_dir)
        
        print_info(f"Generating {args.category}/{args.name}")
        print_info(f"Prompt: {args.prompt}")
        print_info(f"Resolution: {args.resolution}")
        print_info(f"Aspect ratio: {args.aspect_ratio}")
        print_info(f"Format: {args.format}")
        if args.web_search:
            print_info("Web search: ENABLED")
        print_info(f"Generating {args.num_images} image(s)...")
        
        result = generator.generate_custom(
            asset_category=args.category,
            asset_name=args.name,
            prompt=args.prompt,
            num_images=args.num_images,
            aspect_ratio=args.aspect_ratio,
            resolution=args.resolution,
            output_format=args.format,
            enable_web_search=args.web_search,
            save=True
        )
        
        if "saved_paths" in result:
            print_success(f"Generated {len(result['saved_paths'])} image(s)")
            for path in result["saved_paths"]:
                print(f"  ✨ {path}")
        else:
            print_error("No images were generated")
            return 1
        
        return 0
        
    except Exception as e:
        print_error(f"Failed to generate custom asset: {str(e)}")
        return 1


def test_api(args):
    """Test nanobanana pro API connection"""
    try:
        print_info("Testing nanobanana pro API connection...")
        
        client = NanobananProClient()
        
        print_info("Generating test image...")
        result = client.generate_image(
            prompt="A red cube on a white background, minimalist, professional quality, 4K",
            num_images=1,
            resolution="2K"
        )
        
        if "images" in result and len(result["images"]) > 0:
            print_success("API connection successful!")
            print_info(f"Generated image URL: {result['images'][0].get('url', 'N/A')}")
            return 0
        else:
            print_error("API returned no images")
            return 1
            
    except Exception as e:
        print_error(f"API test failed: {str(e)}")
        return 1


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Creative Asset Generation CLI - Generate images with nanobanana pro",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate product photo
  python creative_cli.py product --product-name "Luxury Watch" --prompt "A luxury watch on white background..."
  
  # Generate social graphic
  python creative_cli.py social --platform instagram --topic "Product Launch" --prompt "Instagram post graphic..."
  
  # Generate brand asset
  python creative_cli.py brand --asset-type logo --brand-name "TechCorp" --prompt "Modern tech logo..."
  
  # Generate custom asset with web search
  python creative_cli.py custom --category "thumbnails" --name "video-1" --prompt "YouTube thumbnail..." --web-search
  
  # Test API connection
  python creative_cli.py test
        """
    )
    
    parser.add_argument(
        "--output-dir",
        default="./assets",
        help="Output directory for generated assets (default: ./assets)"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Product photo command
    product_parser = subparsers.add_parser("product", help="Generate product photography")
    product_parser.add_argument("--product-name", required=True, help="Name of the product")
    product_parser.add_argument("--prompt", required=True, help="Detailed prompt for the image")
    product_parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        choices=["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"],
        help="Image aspect ratio (default: 1:1)"
    )
    product_parser.add_argument(
        "--resolution",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Image resolution (default: 2K)"
    )
    product_parser.add_argument(
        "--num-images",
        type=int,
        default=1,
        help="Number of images to generate (1-4, default: 1)"
    )
    product_parser.set_defaults(func=generate_product_photo)
    
    # Social graphic command
    social_parser = subparsers.add_parser("social", help="Generate social media graphics")
    social_parser.add_argument(
        "--platform",
        required=True,
        choices=["instagram", "linkedin", "twitter", "tiktok", "pinterest"],
        help="Social platform"
    )
    social_parser.add_argument("--topic", required=True, help="Topic of the graphic")
    social_parser.add_argument("--prompt", required=True, help="Detailed prompt for the image")
    social_parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        choices=["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"],
        help="Image aspect ratio (default: 1:1)"
    )
    social_parser.add_argument(
        "--resolution",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Image resolution (default: 2K)"
    )
    social_parser.add_argument(
        "--num-images",
        type=int,
        default=1,
        help="Number of images to generate (1-4, default: 1)"
    )
    social_parser.set_defaults(func=generate_social_graphic)
    
    # Brand asset command
    brand_parser = subparsers.add_parser("brand", help="Generate brand assets")
    brand_parser.add_argument(
        "--asset-type",
        required=True,
        choices=["logo", "icon", "pattern", "illustration", "texture"],
        help="Type of brand asset"
    )
    brand_parser.add_argument("--brand-name", required=True, help="Name of the brand")
    brand_parser.add_argument("--prompt", required=True, help="Detailed prompt for the image")
    brand_parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        choices=["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"],
        help="Image aspect ratio (default: 1:1)"
    )
    brand_parser.add_argument(
        "--resolution",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Image resolution (default: 2K)"
    )
    brand_parser.add_argument(
        "--num-images",
        type=int,
        default=1,
        help="Number of images to generate (1-4, default: 1)"
    )
    brand_parser.set_defaults(func=generate_brand_asset)
    
    # Custom asset command
    custom_parser = subparsers.add_parser("custom", help="Generate custom asset")
    custom_parser.add_argument("--category", required=True, help="Asset category")
    custom_parser.add_argument("--name", required=True, help="Asset name")
    custom_parser.add_argument("--prompt", required=True, help="Detailed prompt for the image")
    custom_parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        choices=["21:9", "16:9", "3:2", "4:3", "5:4", "1:1", "4:5", "3:4", "2:3", "9:16"],
        help="Image aspect ratio (default: 1:1)"
    )
    custom_parser.add_argument(
        "--resolution",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Image resolution (default: 2K)"
    )
    custom_parser.add_argument(
        "--format",
        default="png",
        choices=["png", "jpeg", "webp"],
        help="Output format (default: png)"
    )
    custom_parser.add_argument(
        "--num-images",
        type=int,
        default=1,
        help="Number of images to generate (1-4, default: 1)"
    )
    custom_parser.add_argument(
        "--web-search",
        action="store_true",
        help="Enable Google Search integration for real-time data"
    )
    custom_parser.set_defaults(func=generate_custom)
    
    # Test API command
    test_parser = subparsers.add_parser("test", help="Test nanobanana pro API connection")
    test_parser.set_defaults(func=test_api)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute command
    if args.command:
        return args.func(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
