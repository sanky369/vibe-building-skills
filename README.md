# Vibe Building Skills

A comprehensive system of **31 Claude Skills** for building world-class digital products. From marketing strategy to creative asset generation to frontend design excellence—everything you need to create products that are loved.

## 🎯 What Is This?

Vibe Creator's Skills is a complete, production-ready system of Claude Skills built on the philosophy of focus and care — designing and building with deep intention, reducing until it's clear, and refining until it's right.

This repository contains:

- **10 Marketing Skills** — Direct response marketing, SEO, email, content strategy
- **7 Creative Skills** — AI-powered image generation with nanobanana pro, video planning, social graphics
- **13 Frontend Design Skills** — Design systems, responsive layouts, typography, interactions, performance, accessibility
- **Complete Documentation** — Philosophy, research, implementation guides, code examples
- **Automation Tools** — Python CLI for creative asset generation with FAL.ai nanobanana pro

**Total: 31 professional skills + comprehensive guidance + automation tools**

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
11. **seo-strategy** — Plan complete SEO strategy for your product
13. **tweet-writer** — Search for suitable viral tweet format for the purpose and writes tweets accordingly

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

#### Frontend Design Skills (13 skills) ✨ ENHANCED

Build design systems and interfaces that feel timeless and loved. Now with 5 additional skills based on research insights.

**Foundation Layer (2 skills):**
1. **frontend-orchestrator** — Assess design maturity and sequence all 13 skills optimally
2. **design-foundation** — Design tokens, principles, component structure

**Visual Layer (4 skills):**
3. **layout-system** — Responsive layouts, Flexbox, Grid, Container Queries
4. **typography-system** — Type scales, hierarchy, readability
5. **color-system** — Color theory, accessibility, theming, dark mode
6. **visual-hierarchy-refactoring** — NEW! Size, weight, contrast, whitespace, Gestalt principles

**Component Layer (1 skill):**
7. **component-architecture** — Reusable components, atomic design

**Interaction Layer (4 skills):**
8. **interaction-physics** — Animations, momentum, gesture physics, feedback
9. **loading-states** — NEW! Skeleton screens, spinners, progress bars, empty states
10. **error-handling-recovery** — NEW! Error states, recovery workflows, graceful degradation
11. **performance-optimization** — NEW! Perceived latency, optimistic UI, Core Web Vitals

**Quality Layer (2 skills):**
12. **accessibility-excellence** — WCAG compliance, inclusive design
13. **design-engineer-mindset** — NEW! Bridge design and implementation, code as material

**5 Implementation Paths:**
- **Path A** — Building from Scratch
- **Path B** — Formalizing Existing Design
- **Path C** — Improving Mature System
- **Path D** — Fixing Performance Issues
- **Path E** — Improving Accessibility

**Path:** Start with frontend-orchestrator to assess your situation, then follow the recommended sequence.

### Documentation

- **PHILOSOPHY.md** — The designer's thought process and philosophy of uncommon care
- **RESEARCH.md** — Expert insights, recommended books, design principles
- **Creative Automation** — Python CLI and Claude Code integration for asset generation
- **skills/frontend-design/README.md** — Complete guide to all 13 frontend design skills

## 🎯 Key Enhancements

### Frontend Design Skills Improvements

Based on comprehensive research from Interface Craft, design experts, and industry best practices:

**5 New Skills Added:**
- **visual-hierarchy-refactoring** — Master visual hierarchy through Gestalt principles, size, weight, contrast, and whitespace
- **loading-states** — Design skeleton screens, spinners, progress bars, and empty states
- **error-handling-recovery** — Design error states and recovery workflows that guide users
- **performance-optimization** — Master perceived latency through optimistic UI and Core Web Vitals
- **design-engineer-mindset** — Bridge the gap between design and implementation, understand code as design material

**Skill Renamed:**
- **interaction-design** → **interaction-physics** — More precise naming reflecting momentum, gesture physics, and natural interactions

**Enhanced Skills:**
- **frontend-orchestrator** — Now coordinates all 13 skills with 5 implementation paths
- All visual layer skills — Integrated with visual hierarchy principles
- All interaction skills — Integrated with performance considerations

## 🚀 Quick Start

### 1. Clone This Repository

```bash
git clone https://github.com/sanky369/vibe-building-skills.git
cd vibe-building-skills
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

**Option C: Install by Category**
- Install Marketing Skills: `skills/marketing/*/SKILL.md`
- Install Creative Skills: `skills/creative/*/SKILL.md`
- Install Frontend Design Skills: `skills/frontend-design/*/SKILL.md`

### 3. Start with the Orchestrator

Begin with the orchestrator skill for your category:

```
"I'm using the [marketing/creative/frontend-design]-orchestrator skill.
Here's my situation: [describe your current state]
Can you assess my maturity level and recommend a skill sequence?"
```

### 4. Follow the Recommended Path

Work through skills in the sequence recommended by the orchestrator. Each skill builds on previous ones.

### 5. Use Claude Code for Implementation

Each skill includes guidance for Claude Code:

```
"I'm using the [skill-name] skill. Can you help me:
- [Specific task]
- [Implementation details]
- [Integration with other skills]"
```

## 📊 Repository Structure

```
vibe-building-skills/
├── README.md (this file)
├── PHILOSOPHY.md
├── RESEARCH.md
├── docs/
│   ├── PHILOSOPHY.md
│   ├── RESEARCH.md
│   ├── DESIGN-PHILOSOPHY-RESEARCH.md
│   ├── fal_api.py (Creative automation)
│   ├── creative_cli.py
│   ├── claude_integration.py
│   ├── requirements.txt
│   └── examples.py
└── skills/
    ├── marketing/
    │   ├── orchestrator/SKILL.md
    │   ├── brand-voice/SKILL.md
    │   ├── positioning-angles/SKILL.md
    │   ├── keyword-research/SKILL.md
    │   ├── lead-magnet/SKILL.md
    │   ├── direct-response-copy/SKILL.md
    │   ├── seo-content/SKILL.md
    │   ├── newsletter/SKILL.md
    │   ├── email-sequences/SKILL.md
    │   ├── content-atomizer/SKILL.md
    │   └── README.md
    ├── creative/
    │   ├── orchestrator/SKILL.md
    │   ├── creative-strategist/SKILL.md
    │   ├── image-generation/SKILL.md
    │   ├── product-photography/SKILL.md
    │   ├── product-video/SKILL.md
    │   ├── social-graphics/SKILL.md
    │   ├── brand-asset/SKILL.md
    │   ├── talking-head/SKILL.md
    │   └── README.md
    └── frontend-design/
        ├── frontend-orchestrator/SKILL.md
        ├── design-foundation/SKILL.md
        ├── layout-system/SKILL.md
        ├── typography-system/SKILL.md
        ├── color-system/SKILL.md
        ├── component-architecture/SKILL.md
        ├── interaction-physics/SKILL.md
        ├── accessibility-excellence/SKILL.md
        ├── visual-hierarchy-refactoring/SKILL.md
        ├── loading-states/SKILL.md
        ├── error-handling-recovery/SKILL.md
        ├── performance-optimization/SKILL.md
        ├── design-engineer-mindset/SKILL.md
        └── README.md
```

## 🎓 Implementation Workflows

### Marketing Workflow

```
1. Start: marketing-orchestrator
   ↓
2. Choose path based on situation
   ↓
3. Follow skill sequence
   ↓
4. Implement each skill with Claude Code
   ↓
5. Iterate and refine
```

### Creative Workflow

```
1. Start: creative-orchestrator
   ↓
2. Define visual direction with creative-strategist
   ↓
3. Generate assets with image-generation + automation
   ↓
4. Adapt for specific platforms (social-graphics, product-photography)
   ↓
5. Repurpose and scale
```

### Frontend Design Workflow

```
1. Start: frontend-orchestrator
   ↓
2. Assess design maturity (5 levels)
   ↓
3. Choose implementation path (5 options)
   ↓
4. Follow skill sequence
   ↓
5. Implement with Claude Code
   ↓
6. Iterate and refine
```

## 💡 Philosophy

These skills embody the principle of **"uncommon care"** from Interface Craft:

> "Design with uncommon care. Reduce until it's clear. Refine until it's right. Create products that are loved. Interfaces that feel timeless. Experiences that welcome you in and anticipate your needs. Software that feels right. Like it was made by someone who took the time to apply an almost unreasonable level of consideration."

This is not about trends or speed. This is about craft. This is about respect for the user. This is about creating something that endures.

## 🔧 Creative Asset Generation

The creative skills include a complete Python automation system for generating assets with FAL.ai nanobanana pro.

### Setup

```bash
cd docs
pip install -r requirements.txt
export FAL_API_KEY="your_api_key_here"
```

### Usage

**Command Line:**
```bash
python creative_cli.py generate-product-photo "Blue wireless headphones"
```

**Python:**
```python
from fal_api import CreativeAssetGenerator

generator = CreativeAssetGenerator(api_key="your_key")
image = generator.generate_product_photo("Blue wireless headphones")
```

**Claude Code:**
```
"Can you generate 5 product photos for my new headphones?
Use the image-generation skill and the automation system."
```

## 📚 Research & Philosophy

This system is built on research and wisdom from:

- **Interface Craft** — Philosophy of uncommon care
- **Refactoring UI** — Systematic design decisions
- **Don Norman** — Design principles and affordances
- **Steve Krug** — Usability and accessibility
- **Rauno Freiberg** — Interaction physics and invisible details
- **Linear Method** — Speed as a feature
- **WCAG Standards** — Inclusive design
- **Core Web Vitals** — Performance metrics

See `PHILOSOPHY.md` and `RESEARCH.md` for detailed insights.

## 🎯 What You'll Achieve

### Marketing
- ✅ Direct response marketing system
- ✅ SEO strategy and content
- ✅ Email sequences that convert
- ✅ Lead magnets that work
- ✅ Content strategy and atomization

### Creative
- ✅ Professional image generation
- ✅ Product photography
- ✅ Social media graphics
- ✅ Brand assets
- ✅ Video planning and concepts

### Frontend Design
- ✅ Consistent design system
- ✅ Responsive layouts
- ✅ Beautiful typography
- ✅ Harmonious colors
- ✅ Reusable components
- ✅ Delightful interactions
- ✅ Accessible to all
- ✅ Optimized performance
- ✅ Clear error handling
- ✅ Confident loading states
- ✅ Timeless design

## 🚀 Getting Started

1. **Clone the repository**
2. **Choose your starting skill** (orchestrator for your category)
3. **Install skills in Claude**
4. **Follow the recommended path**
5. **Use Claude Code for implementation**
6. **Iterate and refine**

## 📝 Contributing

This is a living system. Feel free to:
- Fork and customize for your needs
- Submit improvements and enhancements
- Share your implementations
- Suggest new skills or improvements

## 📄 License

These skills are provided as-is for your use. Feel free to customize and adapt them to your needs.

## 🙏 Acknowledgments

Built with research and insights from:
- Interface Craft (interfacecraft.dev)
- Nielsen Norman Group
- Interaction Design Foundation
- Web Content Accessibility Guidelines
- The design and development community

**Special thanks for inspiration:**
- [@boringmarketer](https://x.com/boringmarketer) — Marketing skills inspiration
- [@joshpuckett](https://x.com/joshpuckett) — Design and creative inspiration

## 🎉 Ready to Begin?

Start your journey to world-class products today:

1. **Marketing:** `skills/marketing/orchestrator/SKILL.md`
2. **Creative:** `skills/creative/orchestrator/SKILL.md`
3. **Frontend Design:** `skills/frontend-design/frontend-orchestrator/SKILL.md`

Choose one, install it in Claude, and ask for help with your specific situation.

---

**Remember:** Great products are not built in a day. They're built with care, intention, and respect for the user. Start today, iterate continuously, and watch your product transform.

Good luck! 🚀
