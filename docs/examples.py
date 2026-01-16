#!/usr/bin/env python3
"""
Creative Asset Automation Examples
Shows how to use the automation system in different scenarios
"""

from claude_integration import (
    generate_product,
    generate_social,
    generate_brand,
    generate_asset,
    batch_generate_assets,
    get_summary,
    ClaudeCreativeAssistant
)


def example_1_single_product():
    """Example 1: Generate a single product photo"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Generate Single Product Photo")
    print("="*60)
    
    result = generate_product(
        product_name="Luxury Watch",
        description="A luxury leather watch with gold accents and leather strap",
        style="professional product photography",
        num_variations=2
    )
    
    print(f"Success: {result['success']}")
    print(f"Images generated:")
    for img in result['images']:
        print(f"  - {img}")
    print(f"Prompt used: {result['prompt_used']}")


def example_2_social_campaign():
    """Example 2: Generate social media graphics for multiple platforms"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Generate Social Campaign")
    print("="*60)
    
    platforms = ["instagram", "linkedin", "twitter"]
    
    for platform in platforms:
        result = generate_social(
            platform=platform,
            topic="Product Launch",
            description=f"Eye-catching {platform} post for new product launch",
            num_variations=1
        )
        
        print(f"\n{platform.upper()}:")
        print(f"  Success: {result['success']}")
        print(f"  Images: {result['images']}")


def example_3_brand_identity():
    """Example 3: Generate complete brand identity"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Generate Brand Identity")
    print("="*60)
    
    brand_name = "TechCorp"
    
    elements = ["logo", "icon", "pattern"]
    
    for element in elements:
        result = generate_brand(
            brand_name=brand_name,
            element_type=element,
            description=f"Modern {element} for tech company",
            num_variations=1
        )
        
        print(f"\n{element.upper()}:")
        print(f"  Success: {result['success']}")
        print(f"  Images: {result['images']}")


def example_4_batch_generation():
    """Example 4: Batch generate multiple assets"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Batch Generation")
    print("="*60)
    
    assets = [
        {
            "type": "product",
            "name": "Watch",
            "description": "Luxury leather watch with gold accents",
            "style": "professional product photography",
            "num_variations": 1
        },
        {
            "type": "product",
            "name": "Wallet",
            "description": "Premium leather wallet",
            "style": "professional product photography",
            "num_variations": 1
        },
        {
            "type": "social",
            "platform": "instagram",
            "topic": "Product Launch",
            "description": "Instagram post for product launch",
            "num_variations": 1
        },
        {
            "type": "brand",
            "brand_name": "TechCorp",
            "element_type": "logo",
            "description": "Modern tech company logo",
            "num_variations": 1
        }
    ]
    
    results = batch_generate_assets(assets)
    
    print(f"\nGenerated {len(results)} assets:")
    for result in results:
        print(f"\n{result['asset_name']}:")
        print(f"  Success: {result['success']}")
        if result['success']:
            print(f"  Images: {result['images']}")
        else:
            print(f"  Error: {result.get('error', 'Unknown error')}")


def example_5_custom_assets():
    """Example 5: Generate custom assets with full control"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Custom Assets with Full Control")
    print("="*60)
    
    # YouTube thumbnail
    result = generate_asset(
        category="thumbnails",
        name="youtube-video-1",
        prompt="YouTube thumbnail for tech tutorial, bold red and white colors, eye-catching text overlay, high contrast, 1280x720",
        size="1024x1024",
        num_variations=2
    )
    
    print("\nYouTube Thumbnail:")
    print(f"  Success: {result['success']}")
    print(f"  Images: {result['images']}")
    
    # Blog header
    result = generate_asset(
        category="blog-headers",
        name="ai-trends-2026",
        prompt="Blog header image for AI trends article, futuristic design, blue and purple gradient, modern aesthetic, 1200x600",
        size="1024x1024",
        num_variations=1
    )
    
    print("\nBlog Header:")
    print(f"  Success: {result['success']}")
    print(f"  Images: {result['images']}")


def example_6_assistant_class():
    """Example 6: Using the assistant class directly"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Using Assistant Class Directly")
    print("="*60)
    
    assistant = ClaudeCreativeAssistant(output_dir="./assets")
    
    # Generate with more control
    result = assistant.generate_product_photo(
        product_name="Premium Headphones",
        description="High-end wireless headphones with premium materials",
        style="professional product photography",
        lighting="studio lighting with rim light",
        background="gradient background",
        num_variations=3,
        model="fal-ai/flux/dev"
    )
    
    print(f"\nProduct Photography:")
    print(f"  Success: {result['success']}")
    print(f"  Generated {len(result['images'])} variations")
    for img in result['images']:
        print(f"    - {img}")


def example_7_asset_summary():
    """Example 7: Get summary of generated assets"""
    print("\n" + "="*60)
    print("EXAMPLE 7: Asset Summary")
    print("="*60)
    
    summary = get_summary()
    
    print(f"\nAsset Summary:")
    print(f"  Total assets generated: {summary['total_assets']}")
    print(f"  Assets directory: {summary['asset_dir']}")
    print(f"\n  By category:")
    for category, count in summary['by_category'].items():
        print(f"    - {category}: {count} assets")


def main():
    """Run all examples"""
    print("\n" + "="*80)
    print("CREATIVE ASSET AUTOMATION SYSTEM - EXAMPLES")
    print("="*80)
    
    try:
        # Uncomment examples to run
        example_1_single_product()
        example_2_social_campaign()
        example_3_brand_identity()
        example_4_batch_generation()
        example_5_custom_assets()
        example_6_assistant_class()
        example_7_asset_summary()
        
        print("\n" + "="*80)
        print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {str(e)}")
        print("Make sure:")
        print("  1. FAL_API_KEY environment variable is set")
        print("  2. requests library is installed: pip install requests")
        print("  3. You have internet connection")


if __name__ == "__main__":
    main()
