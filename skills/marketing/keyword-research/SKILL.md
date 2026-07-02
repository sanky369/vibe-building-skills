---
name: keyword-research
description: "Build a prioritized keyword cluster map using the 6 Circles Method — keywords at the intersection of positioning alignment, customer language, competitor blind spots, workable search volume, real expertise, and business intent. Use when the user asks 'what keywords should I target', 'what should I write about', 'find SEO opportunities', 'plan my content strategy', 'what does my audience search for', or before any SEO content is written. Produces a Keyword Map: scored keywords grouped into topic clusters, each cluster mapped to the article that should target it, ready to hand to content production."
---

# Keyword Research

Produce a **keyword map**: a scored, clustered list of search terms worth targeting, each tied to the content that should win it. Governing principle: **a keyword is only worth targeting if it survives all six circles** — aligned with the positioning, phrased in the customer's language, under-served by competitors, actually searched, winnable with the user's real expertise, and connected to revenue. Traffic that fails circle 6 is vanity.

## When to use / when not to

- Use before writing SEO content, when planning a content calendar, or when the user wants to know what their audience searches for.
- If no positioning statement exists, run `skills/marketing/positioning-angles` first (or infer a provisional one and label it) — circle 1 is unworkable without it.
- If the user wants the *full* organic program — link building, technical SEO, programmatic pages, domain authority — use `skills/marketing/seo-strategy`; this skill is the keyword-selection layer only.
- If keywords already exist and the user wants the article written, go straight to `skills/marketing/seo-content`.

## Intake

One batch; reuse anything already produced by `skills/marketing/orchestrator` or `skills/marketing/positioning-angles`:

1. Your positioning statement (or: what you sell, to whom, and what makes it different).
2. Your 2–3 closest competitors' websites.
3. Any sources of raw customer language — support tickets, sales calls, reviews, community threads — or paste examples of how customers describe the problem.
4. Site status: domain age, roughly how much content published, any current rankings? (Determines how competitive a keyword you can win.)
5. Access to a keyword tool (Ahrefs, Semrush, Google Keyword Planner)? If yes, the user runs volume lookups when asked; if no, proceed with estimates.

**Don't stall:** with a positioning statement and a recognizable market you can draft the full map from knowledge and web research — label all volumes and difficulty as estimates and list them for the user to verify in a tool.

## Workflow — the 6 Circles Method

Run the circles as sequential filters: generate wide in circles 1–2, then cut in 3–6.

### Circle 1 — Positioning alignment (seed)
Expand the positioning statement into 20–40 seed keywords. Take each element of the claim (audience, problem, mechanism, outcome) and list the searches that element implies.
Rule: **seeds come from the angle, not the category.** "Project management tool for remote teams" seeds *remote-team* keywords (async standups, distributed team communication), not generic *project management* keywords the incumbents own.

### Circle 2 — Customer language (rephrase)
Rewrite every seed in the words customers actually type, harvested from the intake sources. Kill jargon: if customers say "remote work tools", drop "distributed workforce management solutions". Add the question-form variants ("how do I…", "best X for Y", "X vs Y") — those carry the clearest intent.

### Circle 3 — Competitor blind spots (cut or boost)
Check each surviving keyword against the competitors' content (crawl their blog/sitemap or search `site:competitor.com <keyword>`).
- Competitors rank with strong, current content → cut, unless the user has a decisively better asset.
- Competitors ignore it or cover it thinly/outdated → boost priority. These gaps are the map's best entries.

### Circle 4 — Search volume (screen)
Screen for workable volume. Heuristic (label it as such): **target roughly 100–10,000 searches/month** — below ~100 rarely repays an article; above ~10,000 is usually incumbent territory for a young domain.
Decision rules: established domain with authority (from intake Q4) → the upper bound relaxes; brand-new domain → stay in the low hundreds-to-low-thousands band. If no tool access, estimate from autocomplete breadth, "People also ask" density, and ad presence — and flag every estimate.

### Circle 5 — Expertise (cut)
Keep only keywords where the user can honestly out-write the current top results — first-hand experience, proprietary data, a named mechanism, or a sharper niche take. If the user can't add anything the top 3 results lack, cut the keyword regardless of volume.

### Circle 6 — Business intent (score)
Score what remains by distance to revenue:
- **High:** buying/comparison intent — "best X for Y", "X vs Y", "X pricing", "X alternative".
- **Medium:** problem-aware how-tos the offer solves — "how to manage remote teams".
- **Low:** informational adjacency — "remote work statistics". Keep low-intent keywords only as cluster support, never as the cluster head.

### Cluster and prioritize
Group survivors into topic clusters (one head keyword + 3–8 supporting keywords that one strong article or hub can cover). Priority order: **high intent + competitor blind spot first**, then high intent + contested, then medium intent gaps. Propose the top 3–5 clusters and have the user confirm the order before content production starts.

## Required output format

```
# Keyword Map — [Brand]

**Positioning it serves:** "[claim from skills/marketing/positioning-angles]"
**Volume/difficulty source:** [tool name | estimates — user to verify]

## Priority clusters
### Cluster 1: [name] — Priority: HIGH
Target article: "[working title]" — intent: [high/med] — feeds: [lead magnet / product page]
| Keyword | Role | Est. volume | Competition note | Intent |
|---|---|---|---|---|
| [head keyword] | Head | ~N/mo | [gap / thin / contested] | High |
| [supporting] | Support | ... | ... | ... |

### Cluster 2: ...
(3–5 clusters total)

## Cut list (why keywords were rejected)
- "[keyword]" — failed circle [n]: [one-line reason]
(representative sample, not exhaustive)

## Assumptions & verification queue
- [every estimated volume or inferred competitor read, listed for tool verification]

**Next step:** write Cluster 1's target article via skills/marketing/seo-content.
```

## Quality bar (check before delivering)

- [ ] Every cluster head passed all six circles; the failing circle is named for every cut shown.
- [ ] No cluster head is a generic category term the incumbents own.
- [ ] Every keyword uses customer phrasing — zero internal jargon survives.
- [ ] All volumes labeled with their source; estimates explicitly flagged, never presented as tool data.
- [ ] Every cluster names the article that targets it and the business asset it feeds.
- [ ] 3–5 clusters delivered, priority-ordered and user-confirmed — not an undifferentiated keyword dump.

## Integration

- **Upstream:** `skills/marketing/positioning-angles` supplies the claim that seeds circle 1; `skills/marketing/orchestrator` routes here on awareness and scale paths.
- **Downstream:** `skills/marketing/seo-content` consumes the cluster map one cluster at a time (head keyword + supports + working title cross the boundary); `skills/marketing/seo-strategy` consumes it as the keyword layer of a full program; `skills/marketing/content-atomizer` uses cluster themes to steer repurposing.
