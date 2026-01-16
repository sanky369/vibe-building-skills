---
name: Frontend Design Orchestrator
description: Master coordinator skill that diagnoses your application's design maturity level and sequences all frontend design skills in the optimal order. Analyzes current state, identifies gaps, and creates a personalized implementation roadmap for transforming your MVP into a world-class experience.
---

# Frontend Design Orchestrator

## Overview

The Frontend Design Orchestrator is your strategic guide for applying the philosophy of "uncommon care" to your digital product. Rather than randomly applying design skills, this orchestrator helps you understand where your application stands, what matters most right now, and which skills to deploy in what sequence.

This skill embodies the principle: **"Reduce until it's clear, refine until it's right."** It helps you identify what's essential for your current stage and focuses your effort there first.

## Core Methodology: Design Maturity Assessment

Every application exists at one of five design maturity levels. Understanding your level is the first step to improvement.

### The Five Maturity Levels

**Level 1: Functional MVP**
Your application works. Users can accomplish their core goals. But the experience feels rough, inconsistent, or confusing. Design feels like an afterthought. This is where most startups begin.

**Level 2: Consistent Foundation**
You've established basic consistency. Components look similar, colors are somewhat coordinated, spacing has some logic. But the system isn't documented, and new features often break the pattern. Accessibility is partial or missing.

**Level 3: System-Driven**
You have a documented design system with tokens, components, and clear patterns. New features follow the system. Accessibility is integrated. But the system might feel generic, lacking personality or delight. Interactions feel mechanical.

**Level 4: Refined Experience**
Your system is mature and well-executed. Every detail has been considered. Interactions feel smooth and intentional. Accessibility is excellent. Users notice the care. But the experience might not yet feel timeless or anticipatory.

**Level 5: Transcendent Design**
This is rare. Your product doesn't just work well—it feels loved. The experience anticipates user needs. Every interaction delights. The design feels timeless, not trendy. Users recommend it not because they have to, but because they want to.

## The Orchestrator's Diagnostic Process

### Step 1: Current State Assessment

Before recommending skills, the orchestrator asks these diagnostic questions:

**Foundation Questions:**
- What is your primary goal right now? (Shipping fast, improving retention, reducing support tickets, building brand love?)
- How many users are actively using your product?
- What's your team's design maturity? (No designer, junior designer, experienced designer, design team?)
- How much technical debt do you have in your UI/CSS?

**Design System Questions:**
- Do you have a documented design system?
- Are you using a CSS framework (Tailwind, CSS-in-JS, vanilla CSS)?
- How consistent is your current design across the application?
- Do you have design tokens or design system documentation?

**User Experience Questions:**
- What's your biggest user frustration right now?
- How many accessibility issues have been reported?
- What's your mobile experience like compared to desktop?
- Do users comment on the feel or polish of your product?

**Interaction Questions:**
- How much thought has gone into animations and transitions?
- Do users understand what actions are available to them?
- How clear is your error messaging and feedback?
- Do interactions feel responsive and intentional?

### Step 2: Gap Analysis

Based on the assessment, the orchestrator identifies which skills will have the highest impact on your specific situation.

| Current State | Highest Impact Skill | Why | Secondary Skills |
| :--- | :--- | :--- | :--- |
| Functional MVP, no system | design-foundation | Establishing a foundation prevents future technical debt and enables faster, more consistent development. | layout-system, typography-system |
| Inconsistent design, partial system | design-foundation | Documenting and formalizing what exists prevents regressions and enables team alignment. | component-architecture, color-system |
| System exists, but feels generic | interaction-design | Adding intentionality to interactions transforms a functional product into one that feels loved. | typography-system, accessibility-excellence |
| Good system, poor accessibility | accessibility-excellence | Accessibility is foundational and affects all other skills. Fixing it first ensures all future work is accessible. | component-architecture, interaction-design |
| Mature system, needs refinement | interaction-design, typography-system | Refinement happens at the margins—in the details of how things move, feel, and communicate. | accessibility-excellence (audit), color-system (audit) |

### Step 3: Skill Sequencing

The orchestrator recommends one of four implementation paths based on your situation:

**Path A: Building from Scratch (Functional MVP → Refined Experience)**
1. design-foundation — Establish tokens, system structure, component library
2. layout-system — Create responsive, accessible layout patterns
3. typography-system — Define type scales and hierarchy
4. color-system — Establish color system with accessibility in mind
5. component-architecture — Build reusable, well-documented components
6. accessibility-excellence — Audit and improve accessibility across all layers
7. interaction-design — Add intentionality to animations and transitions

**Path B: Formalizing Existing Design (Inconsistent → System-Driven)**
1. design-foundation — Document and formalize existing patterns
2. component-architecture — Extract and document existing components
3. layout-system — Audit and standardize layout patterns
4. typography-system — Audit and standardize typography
5. color-system — Audit and standardize color usage
6. accessibility-excellence — Audit and improve accessibility
7. interaction-design — Add intentionality to interactions

**Path C: Improving Mature System (System-Driven → Transcendent)**
1. interaction-design — Add delight and intentionality
2. accessibility-excellence — Comprehensive audit and improvement
3. typography-system — Refinement of type scales and hierarchy
4. color-system — Refinement of color system and theming
5. component-architecture — Refinement of component patterns and documentation
6. layout-system — Refinement of responsive behavior and edge cases
7. design-foundation — Review and update design tokens and system documentation

**Path D: Accessibility-First (Any State → Accessible Foundation)**
1. accessibility-excellence — Comprehensive accessibility audit and remediation
2. design-foundation — Ensure tokens and system support accessibility
3. component-architecture — Ensure all components are accessible
4. layout-system — Ensure all layouts are accessible
5. typography-system — Ensure typography supports accessibility
6. color-system — Ensure color system supports accessibility
7. interaction-design — Ensure interactions are accessible

## How to Use This Skill with Claude Code

### Diagnostic Conversation

Start by asking Claude Code:

```
"I'm using the frontend-orchestrator skill. Here's my situation:
- We have a functional MVP built with React and Tailwind
- We have no design system yet
- Our biggest pain point is inconsistency
- We have one designer and three developers
- We want to improve user retention

What's my design maturity level, and which skills should I focus on first?"
```

Claude Code will use this skill to:
1. Assess your maturity level
2. Identify your highest-impact opportunities
3. Recommend a skill sequence
4. Explain why that sequence makes sense for your situation

### Implementation Roadmap

Once you have a sequence, Claude Code can help you execute each skill in order:

```
"I'm ready to start with design-foundation. Can you help me:
1. Audit my current design decisions
2. Create a design token system
3. Document my component library
4. Set up the structure for design system evolution?"
```

### Ongoing Orchestration

As you implement skills, you can return to the orchestrator:

```
"We've implemented design-foundation and layout-system. Our consistency has improved significantly. What should we focus on next? Are there any quick wins we're missing?"
```

The orchestrator will re-assess your situation and adjust recommendations based on what you've accomplished.

## Design Critique Integration

The orchestrator can also critique your current design and suggest improvements:

```
"Can you analyze my current design using the orchestrator skill?
- What's working well?
- What's the biggest opportunity for improvement?
- What's one thing I could change today that would have the highest impact?"
```

## Key Principles

**1. Start with Your Biggest Pain Point**
Don't follow a generic path. Start with the skill that addresses your most pressing problem. If inconsistency is killing you, start with design-foundation. If accessibility is a liability, start with accessibility-excellence.

**2. Build Momentum**
Choose the first skill that will give you the quickest win and build confidence. Success breeds momentum.

**3. Create Interdependencies**
Each skill builds on the previous one. The orchestrator ensures you're not building on sand.

**4. Respect Your Constraints**
The orchestrator considers your team size, timeline, and technical constraints. It won't recommend a path that's unrealistic for your situation.

**5. Iterate and Refine**
Design is never "done." The orchestrator helps you iterate and refine over time, always moving toward that transcendent level.

## Common Scenarios and Recommended Paths

### Scenario 1: "We're Shipping Fast, Design Quality is Suffering"
**Maturity Level:** Functional MVP
**Recommended Path:** Path A (Building from Scratch)
**Quick Win:** Start with design-foundation to establish tokens and component structure. This will slow you down initially but will speed you up dramatically within weeks.

### Scenario 2: "We Have a Design System, But It's Not Being Used"
**Maturity Level:** System-Driven (but not enforced)
**Recommended Path:** Path B (Formalizing Existing Design)
**Quick Win:** Start with component-architecture to extract and document existing components. Make the system visible and useful.

### Scenario 3: "Our System Works, But It Feels Generic"
**Maturity Level:** System-Driven
**Recommended Path:** Path C (Improving Mature System)
**Quick Win:** Start with interaction-design to add intentionality and delight. Small changes in animations and transitions can dramatically improve the feel.

### Scenario 4: "We're Getting Accessibility Complaints"
**Maturity Level:** Any
**Recommended Path:** Path D (Accessibility-First)
**Quick Win:** Start with accessibility-excellence to audit and fix the most egregious issues. This will immediately reduce support tickets and improve user satisfaction.

## Integration with Other Skills

The orchestrator works in concert with all other frontend design skills:

- **design-foundation** — Establishes the system the orchestrator uses to make recommendations
- **layout-system** — Implements responsive, accessible layouts
- **typography-system** — Implements type scales and hierarchy
- **color-system** — Implements color systems and theming
- **component-architecture** — Implements reusable components
- **accessibility-excellence** — Ensures all recommendations are accessible
- **interaction-design** — Adds intentionality to all interactions

## The Philosophy Behind the Orchestrator

The orchestrator embodies the principle of "uncommon care." It doesn't recommend a one-size-fits-all approach. Instead, it takes time to understand your situation, your constraints, and your goals. It then recommends a path that respects your reality while moving you toward excellence.

This is design thinking at its best: empathy, strategy, and execution working in concert.

## When to Re-Run the Orchestrator

- Every 3-6 months, or when you've completed a skill
- When your business priorities shift
- When you add new team members
- When you're considering a major redesign
- When user feedback suggests a new direction

The orchestrator is not a one-time tool. It's a strategic guide that evolves with your product.
