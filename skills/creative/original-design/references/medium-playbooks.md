# Medium Playbooks — Translating the Design Language into a Deliverable

Once the Design Language Brief is locked, translate the *world* into the specific artifact. The brief is the source of truth; everything below is how the same world shows up per medium. Hand off to the matching production skill in this repo.

## Contents
- Infographic
- Video storyboard
- Website
- Mobile app UI/UX

## Infographic

The infographic is a *single map* of the world. Every section is a region of the same universe.

- **Layout:** one governing grid; sections = chapters of the world (mirror how the source method numbers steps 1→7).
- **Icons & illustrations:** drawn only from the Phase 2 vocabulary; honor the Phase 5 constraint (e.g. "everything hand-drawn").
- **Color:** the 3–5 DNA colors; one accent reserved for emphasis/numbers.
- **Typography:** one display voice (often world-flavored) + one readable body.
- **Mascot (if any):** appears as a guide/narrator threading the sections.
- **Test:** could a reader screenshot any one section and still know it belongs to this world?
- **Hand off to:** `social-graphics`, `image-generation`, `brand-asset`.

## Video storyboard

A storyboard is the world *in motion over time*. Motion DNA matters most here.

- **Frames:** each frame is an artifact of the world; establish the world in the first 3 seconds.
- **Motion:** the Phase 3 motion philosophy governs every transition (e.g. "springy & playful" → overshoot eases; "calm & weightless" → slow fades/parallax).
- **Beats:** map a narrative arc (hook → build → payoff); annotate each beat with shot, on-screen elements (from vocabulary), motion, and audio/VO.
- **Mascot (if any):** often the narrator or guide.
- **Texture & color:** carry the DNA across every frame so cuts feel continuous.
- **Hand off to:** `remotion-script-writer`, `product-video`, `creative-strategist`.

## Website

A website is an *explorable* world; users move through regions.

- **Design tokens first:** encode the DNA (colors → tokens, type scale, spacing, radii from shape families, motion durations/easings) before building components. → `design-foundation`, `color-system`, `typography-system`.
- **Components:** each component is an artifact (cards = the world's "objects"); reuse vocabulary shapes consistently. → `component-architecture`.
- **Sections:** hero establishes the world; each section is a region, not a generic "feature block."
- **Motion:** scroll/hover/transition motion all obey the one motion philosophy; respect `prefers-reduced-motion`.
- **Constraint:** the Phase 5 rule becomes a lint-able guideline (e.g. "no stock photos", "single accent color").
- **Hand off to:** `frontend-orchestrator` (it sequences the frontend-design skills).

## Mobile app UI/UX

A mobile app is the world *in your hand* — small surfaces, so the world must read at a glance.

- **Tokens & system:** same as website; mobile spacing/touch targets. → `design-foundation`, `layout-system`.
- **Signature surfaces:** make the world unmistakable on the surfaces users see most — app icon, splash, empty states, loading, onboarding. These are where the mascot and constraint shine.
- **Motion:** micro-interactions express the motion DNA (the "feel" of taps, sheets, transitions). → `interaction-physics`.
- **Components:** a consistent component library drawn from the vocabulary. → `component-architecture`.
- **Test:** remove the logo from a screenshot — is the app still identifiable? (Originality Test Q3.)
- **Hand off to:** `frontend-orchestrator`.
