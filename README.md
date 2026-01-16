# Vibe Building Skills

A comprehensive system of 25 Claude Skills for building world-class digital products. From marketing strategy to creative asset generation to frontend design excellence—everything you need to create products that are loved.

## 🎯 What Is This?

Vibe Creator's Skills is a complete, production-ready system of Claude Skills built on the philosophy of **uncommon care**—designing and building with deep intention, reducing until it's clear, and refining until it's right.

This repository contains:

- **10 Marketing Skills** — Direct response marketing, SEO, email, content strategy
- **7 Creative Skills** — AI-powered image generation, video planning, social graphics
- **8 Frontend Design Skills** — Design systems, responsive layouts, typography, accessibility
- **Complete Documentation** — Philosophy, research, implementation guides, code examples
- **Automation Tools** — Python CLI for creative asset generation with FAL.ai nanobanana pro

**Total: 25 professional skills + comprehensive guidance + automation tools**

## 📦 What's Included

### Skills by Category

#### Marketing Skills (10 skills)
Transform your marketing from generic to direct response, from scattered to strategic.

1. **orchestrator** — Diagnose your marketing situation and sequence skills optimally
2. **brand-voice** — Define your unique voice and positioning
3. **positioning-angles** — Find your differentiation with 8 frameworks
4. **keyword-research** — The 6 Circles Method for keyword strategy
5. **lead-magnet** — Create compelling free offers
6. **direct-response-copy** — Write copy that converts
7. **seo-content** — Create ranking content
8. **newsletter** — 6 newsletter formats
9. **email-sequences** — Welcome, nurture, conversion, launch sequences
10. **content-atomizer** — Repurpose content 15 ways

**Path:** Start with orchestrator to assess your situation, then follow the recommended sequence.

#### Creative Skills (7 skills + automation)
Generate professional creative assets with AI, powered by FAL.ai nanobanana pro.

1. **orchestrator** — Coordinate all creative skills
2. **creative-strategist** — Define your visual direction
3. **image-generation** — Generate images with nanobanana pro
4. **product-photography** — Create professional product shots
5. **product-video** — Plan animated product videos
6. **social-graphics** — Platform-optimized social content
7. **brand-asset** — Logos, icons, patterns, brand elements
8. **talking-head** — Presenter and UGC-style videos

**Plus:** Python automation system for CLI-based and Claude Code asset generation

**Path:** Start with creative-strategist to define your visual direction, then use orchestrator to sequence remaining skills.

#### Frontend Design Skills (8 skills)
Build design systems and interfaces that feel timeless and loved.

1. **frontend-orchestrator** — Assess design maturity and sequence skills
2. **design-foundation** — Design tokens, principles, component structure
3. **layout-system** — Responsive layouts, Flexbox, Grid, Container Queries
4. **typography-system** — Type scales, hierarchy, readability
5. **color-system** — Color theory, accessibility, theming, dark mode
6. **component-architecture** — Reusable components, atomic design
7. **interaction-design** — Animations, microinteractions, feedback
8. **accessibility-excellence** — WCAG compliance, inclusive design

**Path:** Start with frontend-orchestrator to assess your situation, then follow the recommended sequence.

### Documentation

- **PHILOSOPHY.md** — The designer's thought process and philosophy of uncommon care
- **RESEARCH.md** — Expert insights, recommended books, design principles
- **Creative Automation** — Python CLI and Claude Code integration for asset generation

## 🚀 Quick Start

### 1. Clone This Repository

```bash
git clone https://github.com/yourusername/vibe-creators-skills.git
cd vibe-creators-skills
```

### 2. Install Skills in Claude

Each skill is a standalone `.md` file in the `SKILL.md` format that Claude understands.

**Option A: Install Individual Skills**
- Go to Claude Settings > Capabilities > Skills
- Click "Add Skill"
- Upload the SKILL.md file from each skill directory

**Option B: Install All Skills at Once**
- Download the entire repository
- Create a ZIP file of the skills directory
- Upload to Claude

### 3. Start with the Orchestrator

Begin with the orchestrator skill for your category:

```
"I'm using the orchestrator skill. Here's my situation:
[Describe your current state, goals, constraints]

What should I focus on first?"
```

### 4. Follow the Recommended Path

The orchestrator will recommend a sequence of skills tailored to your situation. Work through them systematically with Claude's help.

## 📚 Directory Structure

```
vibe-creators-skills/
├── README.md                          # This file
├── skills/
│   ├── marketing/                     # 10 marketing skills
│   │   ├── 01-brand-voice/
│   │   ├── 02-positioning-angles/
│   │   ├── ... (8 more skills)
│   │   ├── 10-orchestrator/
│   │   └── README.md
│   ├── creative/                      # 7 creative skills + automation
│   │   ├── 00-orchestrator/
│   │   ├── 01-creative-strategist/
│   │   ├── ... (5 more skills)
│   │   ├── INTERACTIVE_GUIDE.md
│   │   └── README.md
│   └── frontend-design/               # 8 frontend design skills
│       ├── 00-frontend-orchestrator/
│       ├── 01-design-foundation/
│       ├── ... (6 more skills)
│       └── README.md
└── docs/
    ├── PHILOSOPHY.md                  # Designer's thought process
    ├── RESEARCH.md                    # Expert insights and books
    ├── README.md                      # Creative automation guide
    ├── fal_api.py                     # FAL.ai nanobanana pro integration
    ├── creative_cli.py                # CLI tool for asset generation
    ├── claude_integration.py           # Claude Code integration
    ├── examples.py                    # Usage examples
    └── requirements.txt               # Python dependencies
```

## 🎓 Implementation Paths

### Marketing Skills Paths

**Path 1: Pre-Launch** — Build your marketing foundation before launch
**Path 2: Low Conversions** — Improve conversion rates
**Path 3: Can't Scale** — Scale your content and reach
**Path 4: Established but Stuck** — Break through plateaus

### Creative Skills Paths

**Path 1: E-Commerce** — Product photography, social graphics, brand assets
**Path 2: SaaS** — Screenshots, explainer videos, social content
**Path 3: Personal Brand** — Headshots, social graphics, video content
**Path 4: Content Creator** — Video thumbnails, social graphics, brand assets

### Frontend Design Paths

**Path A: Building from Scratch** — 8-12 weeks, high effort
**Path B: Formalizing Existing** — 4-8 weeks, medium effort
**Path C: Improving Mature System** — 4-6 weeks, low-medium effort
**Path D: Accessibility-First** — 6-10 weeks, high effort

## 💡 Key Principles

These skills are built on a philosophy of **uncommon care**:

> "Design with uncommon care. Reduce until it's clear. Refine until it's right. Create products that are loved. Interfaces that feel timeless. Experiences that welcome you in and anticipate your needs. Software that feels right. Like it was made by someone who took the time to apply an almost unreasonable level of consideration."

### The Four Pillars

1. **User-Centered** — All decisions start with user needs
2. **Intentional** — Every choice has a reason
3. **Consistent** — Patterns build trust and reduce friction
4. **Accessible** — Design for everyone, including those with disabilities

## 🔧 Creative Automation Setup

The creative skills include Python automation for generating assets with FAL.ai nanobanana pro.

### Installation

```bash
cd docs
pip install -r requirements.txt
export FAL_API_KEY="your_api_key_here"
```

### Usage

**Via CLI:**
```bash
python creative_cli.py generate-product-photo --description "Modern laptop on wooden desk"
```

**Via Claude Code:**
```
"Can you generate 5 product photos for my e-commerce store using the creative automation system?"
```

Claude Code will automatically use the Python modules to generate and save assets.

## 📖 Documentation

### For Marketing
- Each skill includes frameworks, prompts, and examples
- See `skills/marketing/README.md` for complete guide
- Use the orchestrator to get a personalized roadmap

### For Creative
- Each skill includes prompting techniques for nanobanana pro
- See `skills/creative/README.md` for setup and usage
- See `docs/README.md` for automation system details

### For Frontend Design
- Each skill includes methodologies, patterns, and code examples
- See `skills/frontend-design/README.md` for complete guide
- See `docs/PHILOSOPHY.md` for design thinking framework

## 🌟 What You'll Achieve

By working through these skills systematically:

**Marketing:**
- ✅ Clear brand positioning and voice
- ✅ Consistent, high-converting copy
- ✅ SEO-optimized content
- ✅ Effective email sequences
- ✅ Scalable content strategy

**Creative:**
- ✅ Professional product photography
- ✅ Platform-optimized social graphics
- ✅ Consistent brand assets
- ✅ Video planning and concepts
- ✅ Automated asset generation

**Frontend Design:**
- ✅ Consistent design system with tokens
- ✅ Responsive layouts across all devices
- ✅ Beautiful, readable typography
- ✅ Harmonious, accessible colors
- ✅ Reusable, well-documented components
- ✅ Delightful interactions and animations
- ✅ WCAG AA accessibility compliance

## 📚 Research and Philosophy

### PHILOSOPHY.md
Deep dive into the designer's thought process, the three pillars of uncommon care, and how to apply design thinking to any project.

**Covers:**
- Foundational principles (Dieter Rams, Don Norman, Steve Krug)
- The craft of execution (design systems, tokens, components)
- The designer's mindset (reduction and refinement)
- Role of AI in designing with care

### RESEARCH.md
Synthesis of wisdom from industry experts, recommended books, and proven design principles.

**Covers:**
- 12 essential books for designers
- Jakob Nielsen's 10 Usability Heuristics
- Dieter Rams' 10 Principles of Good Design
- Modern trends in 2025
- Key principles across all expert sources

## 🤝 Contributing

This is a public repository. Feel free to:
- Fork and customize for your needs
- Submit improvements and suggestions
- Share your implementations
- Build on these skills

## 📝 License

These skills are provided as-is for your use. Feel free to modify and adapt them to your needs.

## 🎯 Getting Started

1. **Clone the repository**
2. **Read PHILOSOPHY.md** to understand the mindset
3. **Choose your category** (marketing, creative, or frontend design)
4. **Start with the orchestrator** for your category
5. **Follow the recommended path**
6. **Work with Claude** to implement each skill
7. **Iterate and refine** until your product feels right

## 💬 Questions?

Each skill includes comprehensive documentation, examples, and integration guides. Start with the orchestrator for your category—it will guide you through the entire process.

---

**Created with uncommon care.**

Transform your business, your creative process, and your products. Build things that are loved.

🚀 **Let's create something great together.**
