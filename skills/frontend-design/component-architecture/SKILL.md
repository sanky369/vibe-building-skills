---
name: component-architecture
description: "Audit and refactor a frontend codebase's component structure, or design a component library from scratch, using atomic design, composition, and disciplined prop interfaces. Use when the user says 'my components are a mess', 'this component is 800 lines', 'refactor my components', 'build a component library', 'how should I structure my components', 'too much prop drilling', 'we keep rebuilding the same button', or asks where a new component should live — even if they never say 'atomic design'. Produces a component inventory audit, refactored component code (extracted atoms/molecules, typed prop interfaces, variant systems), and per-component documentation."
---

# Component Architecture

Turn a tangle of one-off components into a composable system: audit what exists, classify it into atomic levels, then refactor the worst offenders into small, typed, documented pieces. **The prime directive: a component earns its existence by having one responsibility and a prop interface that makes invalid states unrepresentable.** Deliver working refactored code plus an audit the user can act on — never just advice.

## When to use / when not to

Use for: component decomposition, prop interface design, variant systems, extracting a shared library, deciding controlled vs uncontrolled, component documentation.

Hand off instead when the real need is:
- Visual tokens (spacing, color, type scales) → `skills/frontend-design/design-foundation`
- Animation/feedback inside components → `skills/frontend-design/interaction-physics`
- Keyboard/ARIA behavior of components → `skills/frontend-design/accessibility-excellence`
- Render performance (memoization, re-renders) → `skills/frontend-design/performance-optimization`
- Unsure where to start across the whole frontend → `skills/frontend-design/frontend-orchestrator`

## Step 0 — Inspect the codebase, then ask only what's left

Before proposing anything, build a component inventory from the actual code:

1. Locate component directories (`components/`, `ui/`, `src/app/**`, `lib/`). Note the framework and styling approach (Tailwind, CSS Modules, CSS-in-JS, vanilla) — match it; never introduce a new styling system uninvited.
2. Count components and flag: files > ~200 lines, components that both fetch data and render detailed markup, duplicated UI (multiple button/input/card implementations), inline styles repeating the same values, class-based inheritance.
3. Check for an existing design system or UI kit (shadcn/ui, MUI, Chakra, internal package). If one exists, extend its conventions — don't build a parallel system.

Ask the user (one batch, only what the code didn't answer): **scope** (whole app, one feature, or one painful component?) and **whether a shared library/package is the goal or just cleaner local structure**. If the request already implies scope ("refactor this file"), don't ask — state assumptions and proceed.

## Workflow

### 1. Classify the inventory into atomic levels

- **Atoms** — indivisible, no component dependencies: Button, Input, Label, Icon, Badge, Spinner.
- **Molecules** — small compositions of atoms with one purpose: FormInput (Label+Input+Error), SearchBar.
- **Organisms** — sections with business purpose and often state: NavBar, Card, Modal, Form.
- **Templates** — page layouts arranging organisms; not reusable across page types.
- **Pages** — templates with real data; use them to find edge cases.

Decision rule: if you can't classify a component, it's doing too much — that's a refactor candidate, not a taxonomy problem.

### 2. Prioritize refactors by leverage

Order: (1) duplicated atoms (consolidate first — everything else builds on them), (2) god components violating single responsibility, (3) prop interfaces that allow invalid states, (4) missing variants forcing copy-paste. Propose the top 3–5 refactors with a one-line payoff each; have the user confirm scope before rewriting broadly. For a single-component request, skip the vote and refactor it.

### 3. Refactor with these decision rules

- **Split rule:** a component that fetches data, manages form state, AND renders detailed markup becomes an orchestrator plus focused children. Split by responsibility, not by line count.
- **Composition over inheritance, always.** Variants are props (`variant`, `size`), presets are thin wrappers — never subclasses.
- **Controlled vs uncontrolled:** if any other UI must react to the value while editing (live validation, dependent fields, character counts) → controlled. Fire-and-forget input read once on submit → uncontrolled is fine. Never mix modes in one component.
- **Prop interface rules:** union types instead of booleans that can conflict (`variant: 'primary' | 'danger'`, not `isPrimary` + `isDanger`); constrain to valid options; pass through `className` and ARIA attributes; callbacks named `on<Event>`. If two boolean props can combine into an invalid state, redesign the interface.
- **Extraction threshold:** extract a shared component at the 2nd–3rd duplication *if* the copies are genuinely the same concept. Two things that look alike but change for different reasons stay separate — wrong abstractions cost more than duplication.

Canonical shape for an atom (full gallery in `references/patterns.md`):

```typescript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export const Button = ({ variant = 'primary', size = 'md', disabled, loading, ...rest }: ButtonProps) => (
  <button
    className={`button button--${variant} button--${size}`}
    disabled={disabled || loading}
    {...rest}
  />
);
```

### 4. Document what you build

Every extracted/refactored shared component gets docs: purpose, props table, variants with when-to-use, states, accessibility notes, edge cases. Use the template in `references/patterns.md`. Put docs where the team will see them (Storybook stories if Storybook exists, otherwise a colocated `README.md` or JSDoc).

## Required output format

Deliver both artifacts:

**1. The code** — refactored/created component files, edited in place, following the project's existing styling and naming conventions. All call sites updated; the app must still compile.

**2. Component Architecture Audit** (markdown):

```
## Component Inventory
| Component | File | Level | Verdict | Issue |
| Button (x3 impls) | src/... | atom | consolidate | 3 duplicate implementations |
| UserProfile | src/... | ??? | split | fetches + validates + renders (412 lines) |
| Card | src/... | organism | keep | — |

## Refactors applied
1. [name] — what changed, files touched, why (one line each)

## Refactors recommended (not applied)
1. [name] — payoff, estimated blast radius

## Conventions going forward
- Directory structure: [atoms/molecules/organisms or project's own scheme]
- Prop rules adopted: [union variants, no conflicting booleans, ...]
- When to extract: [the 2–3 rule as applied to this codebase]
```

## Quality bar (check before delivering)

- [ ] Every refactored component has exactly one responsibility you can state in one sentence
- [ ] No prop interface permits an invalid state (no conflicting booleans, no unconstrained strings for variants)
- [ ] No inheritance for variants anywhere in delivered code
- [ ] Each shared component is explicitly controlled or uncontrolled, never both
- [ ] Interactive components keep keyboard operability and visible focus (don't strip what existed)
- [ ] All call sites updated; imports resolve; existing styling system respected
- [ ] Every new shared component has docs (purpose, props, variants, states)
- [ ] Audit table covers the inspected scope, not just the files you touched

Hard don'ts: don't rename the user's public component APIs without flagging it as breaking; don't introduce a new state-management or styling library as a side effect; don't atomize prematurely — a 40-line coherent component doesn't need splitting.

## Integration

- `skills/frontend-design/design-foundation` → feeds this skill the token vocabulary components should consume (spacing/color/type variables).
- `skills/frontend-design/interaction-physics` ← consumes your component states (hover/active/loading) and animates them.
- `skills/frontend-design/loading-states` and `skills/frontend-design/error-handling-recovery` ← consume your component inventory to add loading/error variants systematically.
- `skills/frontend-design/accessibility-excellence` ← audits the components you produce; build with semantic elements so it has less to fix.

## References

- `references/patterns.md` — full code examples per atomic level, single-responsibility before/after, controlled/uncontrolled implementations, the component documentation template, and size conventions. Read it when actually writing the refactored code or docs.
