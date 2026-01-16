# Vibe Creative Automation System — Nanobanana Pro Edition

Complete automation system for generating professional creative assets with **nanobanana pro** from FAL.ai. Integrates seamlessly with Claude Code for automatic asset generation.

## What This Is

This is a Python automation system that enables Claude Code to directly generate professional creative assets using nanobanana pro (Google's state-of-the-art image generation model). No manual API calls needed—just ask Claude and it generates everything automatically.

## Key Features

✅ **Nanobanana Pro Only** — Uses Google's latest image generation model  
✅ **Claude Code Ready** — Claude can run Python to generate assets automatically  
✅ **Professional Quality** — Studio-quality output for commercial use  
✅ **Multiple Asset Types** — Product photos, social graphics, brand assets, custom  
✅ **Batch Generation** — Generate multiple assets in one command  
✅ **Web Search Integration** — Real-time data visualization  
✅ **Text Rendering** — Excellent text in images for infographics  
✅ **Character Consistency** — Maintain character identity across images  
✅ **High Resolution** — Up to 4K native resolution  
✅ **Organized Output** — Automatic folder structure for assets  
✅ **CLI Tool** — Command-line interface for direct generation  

## What is Nanobanana Pro?

Nanobanana Pro is Google's state-of-the-art image generation model that excels at:

- **Text Rendering** — Renders legible, stylized text in images
- **Professional Quality** — Studio-quality output suitable for commercial use
- **Character Consistency** — Maintains character identity with reference images
- **Web Search** — Real-time data visualization
- **High Resolution** — Up to 4K native resolution
- **Editing** — Conversational edits without re-generating

**Cost**: $0.08-$0.15 per image (significantly cheaper than alternatives)

## Quick Start

### 1. Extract Files

Extract `vibe-creative-automation.zip` to your project:

```
your-project/
├── vibe-creative-automation/
│   ├── fal_api.py
│   ├── creative_cli.py
│   ├── claude_integration.py
│   ├── requirements.txt
│   └── README.md
└── assets/  (created automatically)
```

### 2. Install Dependencies

```bash
pip install requests
```

### 3. Get FAL.ai API Key

1. Go to https://fal.ai
2. Sign up or log in
3. Get your API key from settings
4. Set it as environment variable:

```bash
export FAL_API_KEY="your_fal_api_key_here"
```

Or use `FAL_KEY`:

```bash
export FAL_KEY="your_fal_api_key_here"
```

### 4. Test Connection

```bash
python creative_cli.py test
```

Expected output:
```
✅ API connection successful!
Generated image URL: https://...
```

### 5. Generate Your First Asset

```bash
python creative_cli.py product \
  --product-name "Luxury Watch" \
  --prompt "A luxury leather watch with gold accents on white background, professional product photography, studio lighting, 4K, sharp focus"
```

## Usage Methods

### Method 1: Ask Claude (Recommended)

The easiest way—just ask Claude to generate assets:

```
Generate 3 product photos for my luxury watch using nanobanana pro
```

Claude will automatically:
1. Read the Creative Orchestrator skill
2. Understand your requirements
3. Craft the perfect prompt
4. Run Python code to generate
5. Save images to organized folders
6. Show you the results

### Method 2: Command Line Interface

Generate assets directly from terminal:

```bash
# Generate product photo
python creative_cli.py product \
  --product-name "Watch" \
  --prompt "A luxury watch..." \
  --num-images 3 \
  --resolution 2K

# Generate social graphic
python creative_cli.py social \
  --platform instagram \
  --topic "Product Launch" \
  --prompt "Instagram post graphic..." \
  --num-images 2

# Generate brand asset
python creative_cli.py brand \
  --asset-type logo \
  --brand-name "TechCorp" \
  --prompt "Modern tech logo..." \
  --num-images 1

# Generate custom asset
python creative_cli.py custom \
  --category "infographics" \
  --name "tech-trends" \
  --prompt "Infographic of tech trends..." \
  --web-search

# Test API
python creative_cli.py test

# Specify output directory
python creative_cli.py product \
  --output-dir /path/to/assets \
  --product-name "Watch" \
  --prompt "..."
```

### Method 3: Python API

Use in Claude Code or your own scripts:

```python
from claude_integration import (
    generate_product,
    generate_social,
    generate_brand,
    generate_asset,
    batch_generate_assets
)

# Generate product photo
result = generate_product(
    product_name="Watch",
    description="Luxury leather watch with gold accents",
    style="professional product photography",
    num_variations=3
)
print(f"Generated: {result['images']}")

# Generate social post
result = generate_social(
    platform="instagram",
    topic="Product Launch",
    description="Eye-catching launch post",
    num_variations=1
)
print(f"Generated: {result['images']}")

# Generate brand element
result = generate_brand(
    brand_name="TechCorp",
    element_type="logo",
    description="Modern tech logo",
    num_variations=1
)
print(f"Generated: {result['images']}")

# Generate custom asset
result = generate_asset(
    category="infographics",
    name="tech-trends",
    prompt="Infographic of tech trends based on current data",
    num_variations=1
)
print(f"Generated: {result['images']}")

# Batch generate multiple assets
assets = [
    {"type": "product", "name": "watch", "description": "Luxury watch", "num_variations": 2},
    {"type": "social", "platform": "instagram", "topic": "launch", "description": "Launch post", "num_variations": 1},
    {"type": "brand", "brand_name": "MyBrand", "element_type": "logo", "description": "Brand logo", "num_variations": 1},
]

results = batch_generate_assets(assets)
for result in results:
    print(f"{result['asset_name']}: {result['images']}")
```

### Method 4: Low-Level API

Direct FAL.ai API access:

```python
from fal_api import NanobananProClient, CreativeAssetGenerator

# Direct API access
client = NanobananProClient()
result = client.generate_image(
    prompt="A luxury watch on white background...",
    num_images=1,
    resolution="2K",
    aspect_ratio="1:1"
)

# High-level interface
generator = CreativeAssetGenerator()
result = generator.generate_product_photo(
    product_name="Watch",
    prompt="A luxury watch...",
    num_images=1
)
```

## Nanobanana Pro Parameters

### Resolution Options

```
1K   — Small, fast generation (~10 seconds)
2K   — Default, balanced quality (~20 seconds)
4K   — Maximum detail, slower (~40 seconds)
```

### Aspect Ratios

```
21:9  — Ultra-wide
16:9  — Widescreen
3:2   — Standard
4:3   — Square-ish
5:4   — Square-ish
1:1   — Square (default)
4:5   — Portrait
3:4   — Portrait
2:3   — Portrait
9:16  — Mobile portrait
```

### Output Formats

```
png   — Lossless, best for graphics (default)
jpeg  — Compressed, smaller file size
webp  — Modern format, good compression
```

### Web Search Integration

Enable Google Search for real-time data:

```python
result = generate_asset(
    category="infographics",
    name="stock-trends",
    prompt="Visualize current stock market trends",
    enable_web_search=True
)
```

## Asset Organization

Generated assets are automatically organized by type and category:

```
assets/
├── product-photography/
│   ├── luxury-watch/
│   │   └── luxury_watch_1_20260115_053000.png
│   └── premium-wallet/
│       └── premium_wallet_1_20260115_053001.png
├── social-graphics/
│   ├── instagram/
│   │   └── product_launch_1_20260115_053002.png
│   ├── linkedin/
│   │   └── product_launch_1_20260115_053003.png
│   └── twitter/
│       └── product_launch_1_20260115_053004.png
├── brand-assets/
│   └── techcorp/
│       ├── logo/
│       │   └── logo_1_20260115_053005.png
│       ├── icon/
│       │   └── icon_1_20260115_053006.png
│       └── pattern/
│           └── pattern_1_20260115_053007.png
└── infographics/
    └── tech-trends/
        └── tech_trends_1_20260115_053008.png
```

## Workflow Examples

### Workflow 1: E-Commerce Product Launch

```python
from claude_integration import batch_generate_assets

assets = [
    # Product photos
    {"type": "product", "name": "watch", "description": "Luxury watch", "num_variations": 4},
    {"type": "product", "name": "wallet", "description": "Premium wallet", "num_variations": 3},
    
    # Social graphics
    {"type": "social", "platform": "instagram", "topic": "launch", "description": "Instagram post", "num_variations": 2},
    {"type": "social", "platform": "linkedin", "topic": "launch", "description": "LinkedIn post", "num_variations": 1},
    {"type": "social", "platform": "twitter", "topic": "launch", "description": "Twitter post", "num_variations": 1},
    
    # Brand assets
    {"type": "brand", "brand_name": "MyBrand", "element_type": "logo", "description": "Brand logo", "num_variations": 2},
]

results = batch_generate_assets(assets)
print(f"Generated {len(results)} asset groups")
```

### Workflow 2: Content Creator Series

```python
from claude_integration import generate_social, generate_asset

topics = ["AI Trends", "Web3", "Blockchain", "NFTs", "Metaverse"]

for topic in topics:
    # Generate thumbnail
    thumbnail = generate_asset(
        category="thumbnails",
        name=f"video-{topic.lower()}",
        prompt=f"YouTube thumbnail for {topic} video, bold design, eye-catching",
        num_variations=1
    )
    
    # Generate social post
    post = generate_social(
        platform="twitter",
        topic=topic,
        description=f"Tweet about {topic}",
        num_variations=1
    )
    
    print(f"{topic}: thumbnail={thumbnail['images']}, post={post['images']}")
```

### Workflow 3: Brand Refresh

```python
from claude_integration import batch_generate_assets

assets = [
    # New brand identity
    {"type": "brand", "brand_name": "NewBrand", "element_type": "logo", "description": "Modern logo", "num_variations": 3},
    {"type": "brand", "brand_name": "NewBrand", "element_type": "icon", "description": "App icons", "num_variations": 1},
    {"type": "brand", "brand_name": "NewBrand", "element_type": "pattern", "description": "Brand pattern", "num_variations": 1},
    
    # Marketing graphics
    {"type": "social", "platform": "instagram", "topic": "rebrand", "description": "Rebrand announcement", "num_variations": 2},
    {"type": "social", "platform": "linkedin", "topic": "rebrand", "description": "LinkedIn announcement", "num_variations": 1},
]

results = batch_generate_assets(assets)
print(f"Brand refresh complete: {len(results)} assets generated")
```

## Common Prompts

### Product Photography

```
A luxury leather watch with gold accents on white background, 
professional product photography, studio lighting with rim light, 
centered composition, sharp focus, 4K, highly detailed
```

### Viral Thumbnail

```
Design a viral video thumbnail with bold colors, eye-catching text overlay, 
high contrast, professional quality, 4K, trending design
```

### Infographic

```
Create a clean, modern infographic summarizing key information. 
Include charts, icons, and legible text. 
Professional quality, 4K, suitable for presentation
```

### Brand Logo

```
Modern tech company logo, geometric style, blue and white colors, 
minimalist design, scalable, professional, clean lines, 
suitable for all media
```

### Social Media Graphic

```
Instagram post graphic for product launch, vibrant colors, 
eye-catching composition, modern design, professional quality, 
trending aesthetic
```

## File Structure

```
vibe-creative-automation/
├── fal_api.py              — FAL.ai API client (400+ lines)
├── creative_cli.py         — Command-line interface (350+ lines)
├── claude_integration.py   — Claude Code integration (450+ lines)
├── requirements.txt        — Python dependencies
└── README.md              — This file
```

## Modules

### fal_api.py

Low-level FAL.ai API integration:

- `NanobananProClient` — Direct API access
- `CreativeAssetGenerator` — High-level interface
- Automatic image downloading
- Error handling and retries

### creative_cli.py

Command-line interface:

- `product` — Generate product photos
- `social` — Generate social graphics
- `brand` — Generate brand assets
- `custom` — Generate custom assets
- `test` — Test API connection

### claude_integration.py

Claude Code integration layer:

- `ClaudeCreativeAssistant` — Main class
- `generate_product()` — Quick product generation
- `generate_social()` — Quick social generation
- `generate_brand()` — Quick brand generation
- `generate_asset()` — Quick custom generation
- `batch_generate_assets()` — Batch generation
- `get_summary()` — Asset summary

## Troubleshooting

### API Key Not Found

```
Error: FAL_API_KEY or FAL_KEY not found
```

**Solution**:
```bash
export FAL_API_KEY="your_key_here"
```

Or:
```bash
export FAL_KEY="your_key_here"
```

### No Images Generated

**Check**:
1. API key is valid and set correctly
2. Internet connection is working
3. Prompt is detailed and specific
4. FAL.ai service is available

### Images Don't Match Style

**Solution**:
- Add more specific style descriptors to prompt
- Reference your Creative Strategist guide
- Generate multiple variations
- Use conversational editing

### Generation Too Slow

**Solution**:
- Reduce resolution from 4K to 2K
- Reduce num_images to 1
- Use simpler, shorter prompts

## Integration with Creative Skills

This automation system works with the Creative Skills package:

- **00-orchestrator** — Master coordinator (tells Claude how to use this system)
- **01-creative-strategist** — Define your visual direction
- **02-image-generation** — Learn prompting techniques
- **03-product-photography** — Product photo frameworks
- **04-lead-magnet** — Lead magnet visuals
- **05-direct-response-copy** — Copy for graphics
- **06-seo-content** — Content visuals
- **07-newsletter** — Newsletter graphics
- **08-email-sequences** — Email graphics
- **09-social-graphics** — Social media content
- **10-brand-asset** — Brand elements

## Pricing

Nanobanana Pro on FAL.ai:
- **$0.08-$0.15 per image**
- Commercial use allowed
- Free preview available
- Significantly cheaper than alternatives

## Next Steps

1. ✅ Extract and install files
2. ✅ Install dependencies: `pip install requests`
3. ✅ Set API key: `export FAL_API_KEY="your_key"`
4. ✅ Test connection: `python creative_cli.py test`
5. ✅ Generate your first asset: `python creative_cli.py product ...`
6. ✅ Install Creative Skills in Claude
7. ✅ Ask Claude to generate assets
8. ✅ Organize and use your assets

## Support

For issues:
- **FAL.ai API**: https://fal.ai/docs
- **Nanobanana Pro**: https://fal.ai/models/fal-ai/nano-banana-pro
- **Creative Skills**: See skill documentation

---

**You're ready to automate professional creative asset generation with nanobanana pro. Start creating! 🚀**
