# Vibe Creative Skills for Claude

Complete creative system with 7 integrated Claude Skills for AI-powered visual content generation. Each skill uses FAL.ai's nanobanana pro and FLUX models for high-quality image generation.

## What You're Getting

7 professional-grade Creative Claude Skills:

1. **01-creative-strategist** — Define your visual direction and brand aesthetics
2. **02-image-generation** — Generate images using FAL.ai FLUX models
3. **03-product-photography** — Create professional product shots and hero images
4. **04-product-video** — Plan animated product videos and reveals
5. **05-social-graphics** — Generate platform-optimized social media content
6. **06-brand-asset** — Create logos, icons, patterns, and brand elements
7. **07-talking-head** — Plan presenter and UGC-style video content

## Key Features

✅ **FAL.ai Integration** — Uses nanobanana pro and FLUX models  
✅ **API Key Configuration** — Easy setup with environment variables  
✅ **Comprehensive Prompting** — Advanced image generation techniques  
✅ **Platform Optimization** — Social media specs for all major platforms  
✅ **Brand Consistency** — Style guide framework for cohesion  
✅ **Production Ready** — Professional-quality output  
✅ **Integrated System** — All skills work together seamlessly

## 🔒 Security First: API Key Management

**IMPORTANT:** Your FAL.ai API key is sensitive. Never commit it to version control or share it publicly.

- ✅ Use environment variables
- ✅ Store in `.env` file (add to `.gitignore`)
- ✅ Rotate keys periodically
- ❌ Never hardcode keys in files
- ❌ Never commit `.env` files
- ❌ Never share keys in issues or PRs

For detailed security guidelines, see [SECURITY.md](../../SECURITY.md)

## Setup: FAL.ai API Integration

### Step 1: Get Your API Key

1. Sign up at [fal.ai](https://fal.ai)
2. Create an API key in your account settings
3. Store it securely

### Step 2: Configure Environment Variable

**Option A: System Environment Variable**
```bash
export FAL_API_KEY="your_api_key_here"
```

**Option B: In Claude Skill Settings**
Add to your skill configuration:
```
FAL_API_KEY=your_api_key_here
```

**Option C: .env File (Development)**
Create `.env` file:
```
FAL_API_KEY=your_api_key_here
```

### Step 3: Test Connection

Ask Claude:
```
Test my FAL.ai API connection. Generate a simple test image with the prompt:
"A red cube on a white background, minimalist, 4K"
```

## How to Install

Each skill is a folder containing a SKILL.md file. To install:

### Method 1: Individual Installation

1. Navigate to each skill folder (e.g., `01-creative-strategist`)
2. Copy the entire folder
3. In Claude, go to Settings > Capabilities > Skills
4. Click "Add Skill" and upload the folder
5. Enable the skill in your settings

### Method 2: Batch Installation

1. Create a `.skill` folder in your Claude directory
2. Copy all 7 skill folders into `.skill`
3. Claude will automatically recognize and load all skills
4. Enable each skill in Settings > Capabilities > Skills

### Method 3: ZIP Installation

1. Compress each skill folder as a ZIP file
2. In Claude, upload the ZIP file as a skill
3. Claude will extract and install automatically

## Skill Sequencing

### Recommended Order

1. **Creative Strategist** — Define your visual direction first
2. **Image Generation** — Learn to generate images with FAL.ai
3. **Product Photography** — Create product shots
4. **Product Video** — Plan video content
5. **Social Graphics** — Create social media assets
6. **Brand Asset** — Build brand elements
7. **Talking Head** — Plan presenter content

### Timeline

- Creative Strategist: 1-2 weeks
- Image Generation: 1-2 weeks
- Product Photography: 2-3 weeks
- Product Video: 1-2 weeks
- Social Graphics: 2-3 weeks
- Brand Asset: 1-2 weeks
- Talking Head: 1 week

**Total**: 9-15 weeks to master all skills

## Available Models

### FLUX.1 [dev]
- **Quality**: Highest, most detailed
- **Speed**: 30-60 seconds
- **Best For**: Product photography, hero images
- **Recommended**: Yes, for quality

### FLUX.1 [schnell]
- **Quality**: High, good detail
- **Speed**: 5-15 seconds
- **Best For**: Testing, iterations, social media
- **Recommended**: For speed

### FLUX.2
- **Quality**: Latest, improved
- **Speed**: 20-40 seconds
- **Best For**: Production work
- **Recommended**: When you need the best

## Image Generation Parameters

### Image Sizes
```
512x512    — Small, fast
768x768    — Medium, balanced
1024x1024  — Large, recommended
1536x1536  — Extra large
2048x2048  — 4K, maximum detail
```

### Guidance Scale
```
3.5  — Creative freedom
5.0  — Balanced (recommended)
7.5  — Strict adherence
```

### Inference Steps
```
20   — Fast
28   — Balanced (default)
40   — High quality
50   — Maximum quality
```

## How to Use These Skills

### Getting Started

1. **Enable all 7 skills** in Claude Settings > Capabilities
2. **Start with Creative Strategist** to define your visual direction
3. **Ask Claude for help** with each skill
4. **Follow the frameworks** provided in each skill
5. **Implement one skill at a time**

### Example Usage

**For Image Generation:**
```
Generate an image with this prompt:
"A luxury watch on a white background, professional product photography, 
studio lighting, sharp focus, 4K, centered composition, warm gold tones"

Use these parameters:
- Model: FLUX.1 [dev]
- Size: 1024x1024
- Guidance: 5.0
- Steps: 28
```

**For Product Photography:**
```
Generate a product shot using the Product Photography skill.
Product: [Your product]
Type: Clean product shot
Background: White
Lighting: Studio
Composition: Centered
```

**For Social Graphics:**
```
Generate a social media graphic using the Social Graphics skill.
Platform: Instagram
Topic: [Your topic]
Colors: [Your color palette]
Style: Modern, eye-catching
```

## Prompt Engineering Guide

### Basic Formula
```
[SUBJECT] + [STYLE] + [QUALITY] + [COMPOSITION] + [LIGHTING] + [COLOR] + [TECHNICAL]
```

### Example
```
A luxury leather watch, professional product photography, 
white background, studio lighting, sharp focus, 4K, 
centered composition, brown and gold tones, 
high-end product photography, trending on behance
```

### Key Principles

1. **Specificity** — Be detailed about what you want
2. **Style Consistency** — Use modifiers from your Creative Strategist guide
3. **Quality Descriptors** — "Highly detailed," "professional," "4K"
4. **Composition** — Specify how elements should be arranged
5. **Lighting** — Describe lighting setup and mood
6. **Color Palette** — Reference your brand colors
7. **Technical Specs** — Image size, quality level, format

## Integration with Marketing Skills

These creative skills work with the Vibe Marketing Skills package:

- **Brand Voice** — Your voice guides creative direction
- **Positioning Angles** — Your positioning informs creative strategy
- **Direct Response Copy** — Copy accompanies creative assets
- **Content Atomizer** — Creative assets get repurposed
- **Social Graphics** (Marketing) — Uses creative graphics

## Common Use Cases

### E-Commerce
1. Product Photography — Create product shots
2. Social Graphics — Create promotional graphics
3. Brand Asset — Create brand elements
4. Product Video — Create product demos

### SaaS
1. Creative Strategist — Define visual direction
2. Image Generation — Create UI mockups
3. Social Graphics — Create marketing graphics
4. Talking Head — Create educational videos

### Personal Brand
1. Creative Strategist — Define personal aesthetic
2. Image Generation — Create personal brand assets
3. Social Graphics — Create social media content
4. Talking Head — Create personal brand videos

### E-Learning
1. Creative Strategist — Define course aesthetic
2. Image Generation — Create course graphics
3. Product Video — Create course videos
4. Talking Head — Create instructor videos

## Pro Tips

**Consistency**: Use same style across all assets  
**Testing**: Generate multiple variations before choosing  
**Refinement**: Iterate based on results  
**Documentation**: Keep your Creative Strategist guide updated  
**Branding**: Maintain brand identity across all assets  
**Quality**: Use high image sizes for final assets  
**Organization**: Keep generated assets organized by type

## Troubleshooting

### API Key Issues
- Verify FAL_API_KEY environment variable is set
- Check API key is valid in FAL.ai account
- Ensure key has proper permissions

### Image Quality Issues
- Use FLUX.1 [dev] for highest quality
- Increase image size to 1024x1024 or larger
- Increase inference steps to 40+
- Add quality descriptors to prompt

### Style Inconsistency
- Reference your Creative Strategist guide in prompts
- Use consistent color palette
- Maintain same style modifiers
- Test multiple variations

### Generation Too Slow
- Use FLUX.1 [schnell] for faster generation
- Reduce image size to 768x768
- Reduce inference steps to 20
- Generate during off-peak hours

## Support

Each skill includes:
- Clear methodology and frameworks
- Step-by-step processes
- Complete prompt examples
- Integration with other skills
- Troubleshooting guides

Ask Claude to help you with any skill. Claude can:
- Clarify frameworks and techniques
- Generate prompts for your specific use case
- Help you implement skills
- Review your work
- Answer any questions

## Next Steps

1. **Configure FAL.ai API** — Set up your API key
2. **Enable all 7 skills** in Claude Settings
3. **Start with Creative Strategist** — Define your visual direction
4. **Follow the skill sequence** — Implement one at a time
5. **Generate your first assets** — Start creating
6. **Iterate and refine** — Improve based on results
7. **Build your brand** — Create comprehensive visual identity

## Resources

- **FAL.ai Docs**: https://docs.fal.ai/
- **FLUX Models**: https://fal.ai/models/fal-ai/flux/dev/api
- **Image Prompting Guide**: See included image_prompting_guide.md
- **Prompt Engineering**: https://learnprompting.org/

---

**Total Value**: $199 (Creative Skills package price)  
**Real Value**: Unlimited (if you implement it)

Start creating professional visual content with AI. Good luck! 🚀
