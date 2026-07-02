---
name: seo-strategy
description: "Build a complete, prioritized SEO strategy for a site: topical authority map, winnable-keyword shortlist, content production pipeline, link-building plan, and technical baseline. Use when the user wants to grow organic traffic, asks 'how do I rank on Google', 'why isn't my site getting traffic', 'build me an SEO plan/strategy', 'what keywords should I target', 'how do I get backlinks', or wants to audit or scale their SEO — even if they never say the word 'strategy'. Produces an SEO Strategy Document with a scored keyword shortlist, a phased action plan sequenced by dependency, and a measurement plan."
---

# SEO Strategy

Produce a written SEO strategy the user can execute immediately: where they can win (topical authority map + winnable keywords), what to publish (content pipeline), how to earn authority (links), and what technical floor must hold. **Prime directive: only recommend fights the site can win.** A "low difficulty" score is not the same as a winnable keyword — every recommendation must survive a manual SERP check.

## When to use / when not to

- Use for site-level strategy: keyword targeting, content roadmaps, link building, SEO audits, "grow my organic traffic."
- If the user needs **one article written**, hand off to `skills/marketing/seo-content` (bring the target keyword and intent with you).
- If the user only needs **a keyword list**, not a full strategy, use `skills/marketing/keyword-research`.
- If the user's real problem is messaging or conversion, not traffic, route to `skills/marketing/positioning-angles` or `skills/marketing/direct-response-copy`.

## Intake

Ask in one batch, only what's missing:

1. **Site URL and what the business sells** (and to whom).
2. **Current state** — roughly how much organic traffic, any existing content, domain age. Access to Google Search Console data if available.
3. **Topics of genuine expertise** — what could they credibly write 20+ articles about?
4. **Constraints** — content capacity (articles per month they can realistically produce/review) and budget for tools or outreach.

Infer from the site itself whenever you can (crawl/fetch it, inspect existing pages). If the user gives a URL and a one-line goal, state your assumptions about the rest and proceed — don't stall.

## Workflow

### 1. Situate the site

Classify the site, because it changes everything downstream:

- **New/weak site** (little content, few links) → strategy is long-tail winnable keywords only (KGR-qualified), heavy topical clustering, foundational links.
- **Established site with content that doesn't rank** → strategy leads with a content audit: fix intent mismatches, consolidate cannibalizing pages, internal linking, then expand.
- **Ranking site that plateaued** → strategy leads with link building and topical gap-filling against the top competitor.

Identify the 2–3 organic competitors actually occupying the SERPs the user wants (not who the user *thinks* competes with them).

### 2. Build the topical authority map

Google ranks sites that demonstrate comprehensive expertise in a topic, not isolated pages. Define 3–5 core topics where the user has genuine expertise (E-E-A-T: experience, expertise, authoritativeness, trust), and for each, 10–30 supporting subtopics. Each core topic = one pillar page + supporting cluster articles interlinked to it. If the user can't credibly cover a topic in depth, cut it — a thin cluster is worse than no cluster.

### 3. Qualify winnable keywords

For each cluster, expand candidates (Google Autocomplete, People Also Ask, Reddit/forum questions, Google Keyword Planner, Search Console queries the site almost ranks for). Then qualify — **never trust a tool's difficulty score alone**:

- **Manual SERP check**: forums, Quora, thin listicles, or outdated pages on page 1 = opportunity. All big brands with exact-match titles = skip.
- **KGR (Keyword Golden Ratio)** for new/weak sites: `allintitle count ÷ monthly search volume`. KGR < 0.25 = prime target. (Heuristic, not law — still eyeball the SERP.)
- **Intent**: classify each keyword as informational / commercial / transactional / navigational and note the content format Google is rewarding. Wrong format = no ranking regardless of quality.
- **Score** each surviving keyword 1–5 on: intent match to the business, winnability, business value, SERP opportunity. Shortlist those scoring 14+/20; the shortlist goes in the output document.

### 4. Design the content pipeline

Match pipeline ambition to the user's stated capacity — never plan more than they can review for quality:

- **Editorial pace** (≤8 articles/month): brief each article individually; execution goes through `skills/marketing/seo-content`.
- **Programmatic scale** (data-backed page sets: locations, integrations, comparisons, templates): design one template (meta title/description, H1, intent-matching intro, H2 sections, FAQ block, internal links, schema), a data source per page, and a mandatory human editorial review step. AI drafts; a human owns strategy, fact-checking, and quality control — flag this split explicitly.

Every article slots into a cluster and links to its pillar. Specify the internal-linking rule in the plan (each new article links to its pillar + 2–4 siblings).

### 5. Plan link acquisition

Prioritize in this order:

1. **Linkable assets** — 1–2 pieces built to attract links: original research/data, free tools, comprehensive canonical guides, templates. Pick the asset type that fits the niche (data journalism niches → original research; practitioner niches → tools/templates).
2. **Targeted outreach** — build a list of ~50 sites that already link to comparable content; personalized pitch referencing their specific article; make linking frictionless (direct URL, suggested anchor, preview); one follow-up after 5–7 days, then stop.
3. **Digital PR** — HARO/journalist requests, podcast guesting, guest posts on relevant sites only.

Hard rule: never recommend paid link schemes or exchanges with low-quality/irrelevant sites — one relevant, authoritative link beats a pile of junk links, and junk links carry penalty risk.

### 6. Set the technical floor

Don't produce a full technical audit unless the site is established and underperforming (Step 1). Minimum bar for every strategy: pages indexable and in the sitemap, Core Web Vitals passing (LCP < 2.5s, CLS < 0.1), mobile-friendly, appropriate schema markup (FAQ/Article/Product/LocalBusiness) on templated and pillar pages. Anything failing this floor goes in Phase 1 of the plan before content scales.

### 7. Assemble the strategy document

Sequence the plan by dependency, not by calendar: foundation (audit fixes + topical map + keyword shortlist) → content production (pillars first, then clusters) → link acquisition (needs content to link to) → review-and-expand (needs ranking data to act on). Define the measurement plan: Search Console (impressions, clicks, average position per cluster), index coverage, referring domains. Set expectations honestly — new content typically needs months, not days, to rank; say so rather than promising traffic numbers.

## Required output format

Deliver the strategy as this document (markdown, concise):

```
# SEO Strategy — [site]

## Situation
- Site class: [new/weak | established-not-ranking | plateaued] — [evidence]
- Real SERP competitors: [2–3, with one-line strength notes]
- Biggest blocker to organic growth: [one sentence]

## Topical Authority Map
| Core topic (pillar) | Why credible (E-E-A-T) | Supporting subtopics (count) |
| ... | ... | ... |

## Winnable Keyword Shortlist
| Keyword | Intent | Volume (est.) | Winnability evidence (SERP note / KGR) | Score /20 | Cluster |
| ... | ... | ... | ... | ... | ... |
(Top 10–20 only; full candidate list in an appendix if generated)

## Content Pipeline
- Mode: [editorial | programmatic] — [why]
- Cadence: [n articles/pages per month, matched to user capacity]
- Order of production: [pillar/cluster sequence with rationale]
- Internal-linking rule: [rule]
- [If programmatic] Template spec + data source + editorial review step

## Link Plan
- Linkable asset(s): [what + why this type fits the niche]
- Outreach: [target profile, list size, pitch angle]
- Digital PR: [1–2 channels worth the effort, or "skip for now"]

## Technical Floor
- [ ] Pass/fail per item: indexability, sitemap, CWV, mobile, schema
- Fixes required before scaling content: [list or "none"]

## Phased Plan (by dependency)
1. Foundation: [tasks]
2. Content: [tasks]
3. Links: [tasks]
4. Review & expand: [what data triggers what decision]

## Measurement
- Track: [GSC metrics per cluster, index coverage, referring domains]
- Review cadence: after each content batch; kill/fix/scale rule: [rule]
```

## Quality bar

Before delivering, verify:

- [ ] Every shortlisted keyword has **SERP-check evidence written down**, not just a tool score.
- [ ] Every keyword's intent is classified and the planned content format matches it.
- [ ] Every planned article belongs to a cluster in the map — no orphan topics.
- [ ] Content cadence ≤ the user's stated review capacity.
- [ ] No traffic guarantees, no invented benchmark statistics; rules of thumb (e.g., KGR < 0.25) labeled as heuristics.
- [ ] No paid-link or link-scheme recommendations.
- [ ] Plan is sequenced by dependency with no calendar-week scaffolding.

## Integration

- `skills/marketing/keyword-research` — feeds this skill a raw candidate keyword list; this skill qualifies and prioritizes it.
- `skills/marketing/seo-content` — consumes the keyword shortlist + cluster map; hand each keyword over with its intent and SERP notes.
- `skills/marketing/content-atomizer` — consumes published articles as seed content for social distribution.
- `skills/marketing/newsletter` — consumes SEO traffic as its subscriber-acquisition source; note the capture mechanism in the strategy if audience-building is a goal.
- `skills/marketing/orchestrator` — routes here when a user's growth problem is organic acquisition.

## References

- `references/Complete_SEO_Playbook.md` — the full agency playbook: detailed keyword-research walkthroughs, programmatic SEO build-out, outreach scripts, technical checklists, and case detail. Read it when you need step-by-step depth on any single workflow step (e.g., building the programmatic template, running the outreach campaign) or when the user asks "how exactly do I do X".
