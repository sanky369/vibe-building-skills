---
name: seo-content
description: "Write a publish-ready, search-optimized article for a target keyword: SERP-validated brief, full draft matched to search intent, on-page metadata (title tag, meta description, URL slug), and schema markup. Use when the user says 'write a blog post about X', 'write an article that ranks', 'create SEO content', 'I need content for this keyword', or hands over a keyword/content brief from an SEO plan — even if they never say 'SEO'. Also use to rewrite or upgrade an existing article that isn't ranking. Produces the complete article plus a metadata block and an on-page checklist result."
---

# SEO Content

Write one article that ranks *and* reads: search-optimized for the target keyword, genuinely useful to the human who typed it. **Prime directive: match search intent exactly** — Google rewards the format searchers want, and the wrong format doesn't rank no matter how good the writing is. The second directive: every article must contain something the current top results don't (an example, data point, angle, or depth), or there is no reason for it to outrank them.

## When to use / when not to

- Use for writing or rewriting a single search-targeted article (blog post, guide, listicle, comparison).
- If the user has no keyword and no strategy — asks "what should I even write about?" — run `skills/marketing/seo-strategy` (or `skills/marketing/keyword-research` for just a keyword list) first.
- If the piece is a landing/sales page where conversion beats ranking, use `skills/marketing/direct-response-copy`.
- If the user wants social or email derivatives of an article, that's `skills/marketing/content-atomizer`.

## Intake

Ask in one batch, only what's missing:

1. **Target keyword** (and secondary keywords if they have them).
2. **Audience and product** — who reads this, and what does the business want the reader to do next (the CTA)?
3. **Unique material** — first-hand experience, examples, data, or customer stories you can use. This is the E-E-A-T fuel; press for at least one concrete item.
4. **Voice** — an existing brand-voice guide or 2–3 sample posts to match. If `skills/marketing/brand-voice` output exists, use it.

If the request arrives from `skills/marketing/seo-strategy` with a keyword, intent, and SERP notes, skip straight to Step 2. If details are missing, state assumptions (audience, intent, CTA) and proceed — don't stall.

## Workflow

### 1. Validate the SERP and lock the intent

Search the target keyword (use web search when available). Classify intent and let it dictate format:

| Intent | Searcher wants | You write |
|---|---|---|
| Informational | to learn/do | How-to guide or ultimate guide |
| Commercial | to compare/choose | Listicle, comparison, review |
| Transactional | to buy | Product/pricing page → hand off to `skills/marketing/direct-response-copy` |
| Navigational | a specific brand | Usually skip — you can't outrank the brand |

Note from the top 5 results: content length and depth, structure, subtopics covered, and — most importantly — **the gap**: what's thin, outdated, unanswered, or missing. If you cannot name a gap, tell the user the keyword is a bad bet and suggest returning to `skills/marketing/seo-strategy` for a better target. If web search is unavailable, say so, infer intent from the keyword's grammar, and label the SERP analysis as assumption.

### 2. Write the brief

Fill this in before drafting (it becomes part of the deliverable):

- Primary keyword, secondary keywords, intent, target length
- Content angle: the one-line reason this article beats the current results
- H2 outline (5–8 sections for a full article), including an FAQ section
- E-E-A-T elements: which first-hand example/data goes where
- Internal links (3–5 pages on the user's site), external links (2–3 authoritative sources)
- CTA: the single action the reader is asked to take

Length by competition (heuristic — comprehensiveness is the real target, padding actively hurts): low competition 1,500–2,000 words; medium 2,000–3,000; high 3,000+. Never exceed what the intent needs.

### 3. Draft

Read `references/article-templates.md` for the full skeleton of the chosen format (How-To, Listicle, or Ultimate Guide) and follow it. While drafting:

- **Open by answering the query** in the first 2–3 sentences, then earn continued reading. No throat-clearing intros.
- **Keyword placement**: title tag (early), H1, first 100 words, 2–3 natural body uses, URL slug. Secondary keywords in H2s where natural. Never stuff.
- **Structure**: one H1; H2 every major section; subhead every 200–300 words; paragraphs ≤3 sentences; bullets for any list of 3+; bold the takeaways.
- **E-E-A-T on the page**: at least one first-hand example or case; cite 2–3 authoritative external sources; concrete numbers over vague claims.
- **FAQ section**: 4–6 exact-phrasing questions with 40–60 word answers (featured-snippet bait).
- **Close** with 3–5 bullet takeaways and exactly one CTA.

The user supplies lived experience; you supply structure and polish. Never fabricate first-hand experience, testimonials, or statistics — if the user gave no unique material, use clearly-general examples and tell them where to insert their own.

### 4. Metadata and schema

Produce: title tag (50–60 chars, keyword early, compelling), meta description (150–160 chars, keyword + soft CTA), URL slug (short, keyword, hyphenated), image alt-text suggestions, and JSON-LD schema (FAQ schema if there's an FAQ; Article schema otherwise — copy-paste blocks in `references/article-templates.md`).

### 5. Self-review, then deliver

Run the quality bar below. Fix failures before presenting. Deliver in the required output format, and recommend tracking via Google Search Console (impressions, clicks, CTR, average position) with a check-in after the article has had time to index and settle.

## Required output format

````
# [Article Title]

## Brief
- Primary keyword: … · Secondary: … · Intent: [type]
- Angle (why this beats the SERP): …
- Target length: … · CTA: …
- Gap exploited: [what top results miss]

## Metadata
- Title tag (50–60 chars): "…" [char count]
- Meta description (150–160 chars): "…" [char count]
- URL slug: /…
- Schema: [FAQ / Article] (JSON-LD below article)

## Article
[Full draft, H1 through conclusion, with [INTERNAL LINK: page] and
[EXTERNAL LINK: source] markers inline, image suggestions as
[IMAGE: description — alt text: "…"]]

## Schema markup
```json
[JSON-LD block]
```

## On-page checklist
[Each quality-bar item with pass/fail]

## Next steps
- Insert your own examples at: [marked spots, if any]
- Track in GSC: [what to watch, and the decision each signal triggers]
````

## Quality bar

Check every item; fix before delivering:

- [ ] Format matches validated search intent
- [ ] Title tag 50–60 chars with keyword; meta description 150–160 chars — count the characters, don't eyeball
- [ ] Exactly one H1, containing the primary keyword; keyword in first 100 words
- [ ] Primary keyword used 2–3× in body — no more (stuffing check: read headings aloud; if they sound robotic, rewrite)
- [ ] Named gap vs. top results is actually filled in the draft
- [ ] ≥1 first-hand example or clearly-marked placeholder for one; every statistic cited or removed; no invented experience or testimonials
- [ ] 3–5 internal link markers, 2–3 authoritative external link markers
- [ ] FAQ answers 40–60 words each
- [ ] Exactly one CTA
- [ ] Scannable: no paragraph >3 sentences, subhead every 200–300 words

## Integration

- `skills/marketing/seo-strategy` — feeds this skill the keyword, intent, cluster, and SERP notes; return the published-article slug so internal linking stays current.
- `skills/marketing/keyword-research` — alternative lighter-weight source of the target keyword.
- `skills/marketing/brand-voice` — supplies the voice guide applied in Step 3.
- `skills/marketing/direct-response-copy` — takes over for transactional-intent pages and CTA-heavy sections.
- `skills/marketing/content-atomizer` — consumes the finished article as seed content for social posts, threads, and newsletter items.
- `skills/marketing/newsletter` — the article is a natural feature item; pass the title, link, and one-sentence hook.

## References

- `references/article-templates.md` — full H1→conclusion skeletons for the How-To Guide, Listicle/Roundup, and Ultimate Guide formats, plus copy-paste FAQ and Article JSON-LD schema. Read it at Step 3, before drafting.
