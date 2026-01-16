# Vibe Frontend Design Skills

A comprehensive system of Claude Skills for transforming basic MVPs into world-class digital experiences. Built on the philosophy of "uncommon care"—designing with deep intention, reducing until it's clear, and refining until it's right.

## Overview

This package contains 8 interconnected Claude Skills that guide you through every aspect of frontend design, from foundational design systems to delightful interactions. Each skill is designed to work with Claude Code, providing practical guidance, design critique, and actionable frameworks.

## The Skills

### 00-frontend-orchestrator
**Master Coordinator**

The entry point to your design journey. This skill diagnoses your application's design maturity level and sequences all other skills in the optimal order for your situation.

**Use when:**
- You're starting a design system from scratch
- You need to prioritize which design improvements to make
- You want a personalized roadmap for design excellence
- You're unsure which skill to focus on next

**Key features:**
- Design maturity assessment (5 levels)
- Gap analysis and opportunity identification
- 4 implementation paths (Building from Scratch, Formalizing Existing, Improving Mature, Accessibility-First)
- Ongoing orchestration as you implement skills

### 01-design-foundation
**Design System and Tokens**

Establish or formalize your design system foundation. Create design tokens (color, typography, spacing, shadows, borders), define component architecture, and document design principles.

**Use when:**
- You're starting a new project and need a design system
- You have inconsistent design and need to formalize it
- You want to migrate to a token-based system
- You need to support theming or dark mode

**Key features:**
- Token hierarchy (global, semantic, component)
- Design principles documentation
- Color system definition
- Typography system definition
- Spacing system definition
- Component library structure

### 02-layout-system
**Responsive Layouts**

Master responsive layout design using modern CSS (Flexbox, Grid), mobile-first approach, and breakpoint strategies. Create layouts that adapt beautifully across all devices.

**Use when:**
- You're building responsive layouts
- Your mobile experience needs improvement
- You want to implement container queries
- You need to ensure accessibility in layouts

**Key features:**
- Mobile-first responsive design
- Flexbox and Grid mastery
- Container queries
- Responsive breakpoint strategy
- Accessibility considerations (touch targets, reading line length, whitespace)
- Common responsive patterns

### 03-typography-system
**Type Scales and Hierarchy**

Master typography design with font selection, type scales, hierarchy, readability, and accessibility. Create consistent, beautiful typography that works across all devices.

**Use when:**
- You're defining your typography system
- Your text hierarchy needs improvement
- You want to implement fluid typography
- You need to improve readability

**Key features:**
- Modular type scales (Major Second, Major Third, Perfect Fifth, Golden Ratio)
- Font selection and pairing
- Type hierarchy and emphasis
- Readability and accessibility (line height, line length, contrast)
- Responsive typography
- Variable fonts and advanced techniques

### 04-color-system
**Color Design and Accessibility**

Master color design with color theory, accessibility, theming, and dark mode. Create harmonious color systems that work across contexts and support accessibility standards.

**Use when:**
- You're defining your color palette
- You need to ensure color contrast compliance
- You want to implement dark mode
- You need a color-blind friendly palette

**Key features:**
- Color harmony techniques (monochromatic, analogous, complementary, triadic)
- Token-based color systems
- WCAG contrast requirements
- Dark mode implementation
- Color-blind friendly design
- Semantic color tokens

### 05-component-architecture
**Reusable Components**

Design and build reusable, well-documented components. Master component composition, prop design, variant systems, and documentation.

**Use when:**
- You're building a component library
- You want to improve component reusability
- You need to document your components
- You want to refactor complex components

**Key features:**
- Atomic design methodology (atoms, molecules, organisms, templates, pages)
- Component design principles (single responsibility, composition, props interface)
- Component variants and states
- Component documentation templates
- Accessibility in components

### 06-interaction-design
**Animations and Microinteractions**

Master microinteractions, animations, transitions, and feedback systems. Create intentional, delightful interactions that guide users and provide clear feedback.

**Use when:**
- You want to add delight to your product
- You need to provide better feedback for user actions
- You want to improve loading states
- You need to optimize animation performance

**Key features:**
- Microinteraction anatomy
- Animation principles (timing, easing, distance)
- Common microinteractions (button states, form validation, loading, notifications, transitions)
- Performance optimization (GPU-accelerated properties)
- Accessibility considerations (reduced motion, keyboard navigation)

### 07-accessibility-excellence
**WCAG Compliance and Inclusive Design**

Master web accessibility to ensure your product is usable by everyone, including people with disabilities. Covers WCAG standards, semantic HTML, keyboard navigation, and inclusive design.

**Use when:**
- You need to ensure WCAG AA compliance
- You want to improve keyboard navigation
- You need to fix color contrast issues
- You want to support screen readers

**Key features:**
- WCAG 2.1 standards (Perceivable, Operable, Understandable, Robust)
- Semantic HTML
- Keyboard navigation and focus management
- Screen reader support (ARIA)
- Color contrast verification
- Inclusive design practices

## Implementation Paths

Choose the path that matches your current situation:

### Path A: Building from Scratch (Functional MVP → Refined Experience)
1. frontend-orchestrator — Assess and plan
2. design-foundation — Establish tokens and system
3. layout-system — Create responsive layouts
4. typography-system — Define type scales
5. color-system — Establish color system
6. component-architecture — Build components
7. accessibility-excellence — Ensure compliance
8. interaction-design — Add delight

**Timeline:** 8-12 weeks  
**Effort:** High (comprehensive system building)  
**Best for:** New projects, startups, teams starting from scratch

### Path B: Formalizing Existing Design (Inconsistent → System-Driven)
1. frontend-orchestrator — Assess and plan
2. design-foundation — Document existing patterns
3. component-architecture — Extract components
4. layout-system — Standardize layouts
5. typography-system — Standardize typography
6. color-system — Standardize colors
7. accessibility-excellence — Audit and improve
8. interaction-design — Add intentionality

**Timeline:** 4-8 weeks  
**Effort:** Medium (formalizing existing work)  
**Best for:** Existing products with inconsistent design

### Path C: Improving Mature System (System-Driven → Transcendent)
1. frontend-orchestrator — Assess and plan
2. interaction-design — Add delight
3. accessibility-excellence — Comprehensive audit
4. typography-system — Refinement
5. color-system — Refinement
6. component-architecture — Refinement
7. layout-system — Refinement
8. design-foundation — Review and update

**Timeline:** 4-6 weeks  
**Effort:** Low-Medium (refinement and polish)  
**Best for:** Mature products needing polish and delight

### Path D: Accessibility-First (Any State → Accessible Foundation)
1. frontend-orchestrator — Assess and plan
2. accessibility-excellence — Comprehensive audit and remediation
3. design-foundation — Ensure tokens support accessibility
4. component-architecture — Ensure components are accessible
5. layout-system — Ensure layouts are accessible
6. typography-system — Ensure typography is accessible
7. color-system — Ensure colors are accessible
8. interaction-design — Ensure interactions are accessible

**Timeline:** 6-10 weeks  
**Effort:** High (comprehensive accessibility work)  
**Best for:** Products with accessibility issues or compliance requirements

## How to Use These Skills with Claude

### 1. Start with the Orchestrator

```
"I'm using the frontend-orchestrator skill. Here's my situation:
- We have a functional MVP built with React and Tailwind
- We have no design system yet
- Our biggest pain point is inconsistency
- We have one designer and three developers
- We want to improve user retention

What's my design maturity level, and which skills should I focus on first?"
```

### 2. Follow the Recommended Path

Claude will recommend a sequence of skills. Follow them in order:

```
"I'm ready to start with design-foundation. Can you help me:
1. Audit my current design decisions
2. Create a design token system
3. Document my component library
4. Set up the structure for design system evolution?"
```

### 3. Implement Each Skill

Work through each skill systematically:

```
"I've completed design-foundation. Now I'm ready for layout-system.
Can you help me:
1. Audit my current layouts for mobile-first compliance
2. Create responsive layout patterns
3. Implement container queries
4. Ensure accessibility in layouts?"
```

### 4. Iterate and Refine

As you complete skills, return to the orchestrator for guidance:

```
"We've implemented design-foundation and layout-system. Our consistency
has improved significantly. What should we focus on next? Are there any
quick wins we're missing?"
```

## Key Principles

These skills are built on the philosophy of "uncommon care":

**1. Reduce Until It's Clear**
Simplify until the essential emerges. Remove everything that doesn't serve the user.

**2. Refine Until It's Right**
Polish every detail. Apply an almost unreasonable level of consideration.

**3. Design with Intention**
Every decision should have a reason. Avoid arbitrary choices.

**4. Accessibility is Foundational**
Design for all users, including those with disabilities. Accessibility is not a feature; it's a requirement.

**5. Consistency Builds Trust**
Patterns should be predictable. Users should recognize them across your product.

**6. Performance Matters**
A beautiful interface that's slow is not good design. Speed matters.

**7. Timelessness Over Trends**
Avoid trends. Design for longevity.

## Integration with Claude Code

These skills are designed to work seamlessly with Claude Code:

1. **Practical Guidance** — Each skill provides frameworks and best practices you can implement immediately
2. **Code Generation** — Claude Code can generate HTML, CSS, React components based on skill guidance
3. **Design Critique** — Ask Claude to critique your current design using the skill frameworks
4. **Automation** — Claude Code can automate repetitive tasks (generating components, creating documentation, etc.)

## What You'll Achieve

By working through these skills systematically, you'll transform your MVP into a world-class experience:

- ✅ **Consistent Design System** — Tokens, components, and patterns that work together
- ✅ **Responsive Layouts** — Beautiful on all devices, from mobile to desktop
- ✅ **Beautiful Typography** — Readable, hierarchical, and intentional
- ✅ **Harmonious Colors** — Accessible, meaningful, and cohesive
- ✅ **Reusable Components** — Well-documented, flexible, and scalable
- ✅ **Delightful Interactions** — Intentional animations and feedback
- ✅ **Accessible to All** — WCAG AA compliant, usable by everyone
- ✅ **Timeless Design** — Not trendy, but enduring and loved

## Philosophy

These skills are grounded in the philosophy of Interface Craft and the wisdom of design pioneers like Dieter Rams, Don Norman, and Steve Krug. They embody the principle that great design is not about trends or speed, but about craft, care, and respect for the user.

> "Design with uncommon care. Reduce until it's clear. Refine until it's right. Create products that are loved. Interfaces that feel timeless. Experiences that welcome you in and anticipate your needs. Software that feels right. Like it was made by someone who took the time to apply an almost unreasonable level of consideration."

## Getting Started

1. **Download and install** all skills into Claude
2. **Start with frontend-orchestrator** to assess your situation
3. **Follow the recommended path** for your situation
4. **Work through each skill** systematically
5. **Use Claude Code** to implement the guidance
6. **Iterate and refine** until your product feels right

## Support and Resources

Each skill includes:
- Comprehensive methodology and frameworks
- Practical examples and patterns
- Integration guidance with other skills
- Design critique capabilities
- Checklists for completeness

For more information on design principles and best practices, refer to:
- Interface Craft (https://www.interfacecraft.dev/)
- Nielsen Norman Group (https://www.nngroup.com/)
- Interaction Design Foundation (https://www.interaction-design.org/)
- Web Content Accessibility Guidelines (https://www.w3.org/WAI/WCAG21/quickref/)

## License

These skills are provided as-is for your use in Claude. Feel free to customize and adapt them to your needs.

---

**Ready to create beautiful, accessible, delightful digital experiences?**

Start with the frontend-orchestrator skill and let Claude guide you on your design journey.

Good luck! 🚀
