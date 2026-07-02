---
name: content-atomizer
description: "Turn one piece of long-form content (blog post, video/podcast transcript, guide, talk) into a ready-to-post multi-platform content pack: LinkedIn posts, X/Twitter thread, newsletter item, short-video scripts, carousel outlines, quote pulls, and more — each natively adapted, not copy-pasted. Use when the user says 'repurpose this post', 'turn this into social content', 'atomize this', 'get more mileage out of my content', 'make LinkedIn posts from my article', or shares long-form content wanting distribution. Produces an idea inventory plus a per-platform atomization pack with a suggested posting order."
---

# Content Atomizer

Break one substantial piece of content into many platform-native pieces. **Prime directive: adapt, never excerpt** — each atomic piece must stand alone as if written for that platform on purpose, carrying the user's voice, while format and length obey the platform. The second rule: atomize ideas, not paragraphs — you extract the content's core ideas first, then re-express each idea per platform.

## When to use / when not to

- Use when there is existing long-form source content and the goal is distribution across channels.
- If the user needs the long-form piece written first, use `skills/marketing/seo-content` — then come back.
- If the user wants one great tweet/thread crafted and researched from scratch (not derived from source content), use `skills/marketing/tweet-writer` — it does niche research this skill skips.
- If the user wants a full newsletter issue (not just an item), hand the source to `skills/marketing/newsletter`.

## Intake

Ask in one batch, only what's missing:

1. **The seed content** — the actual text/transcript (or link). Verify it's substantial enough: multiple distinct ideas and a point of view. If it's thin (one idea, <~500 words), say so and offer a single-platform adaptation instead of a pack.
2. **Active platforms** — where does the user actually publish, and which 1–2 matter most?
3. **Goal** — reach/followers, traffic back to the source, or list growth? (This sets the CTAs.)
4. **Voice** — brand-voice guide or sample posts (use `skills/marketing/brand-voice` output if it exists).

Don't ask which formats they want — that's your job to propose in Step 3. If platforms are unknown, default to LinkedIn + X + newsletter item and say so. State assumptions and proceed — don't stall.

## Workflow

### 1. Extract the idea inventory

Read the seed content and pull 5–10 discrete ideas, each tagged by type — the type determines which formats it can power:

- **Core concept** — the piece's main argument
- **Framework/process** — anything with steps or named parts (best carousel/thread material)
- **Story/example** — narratives and cases (best LinkedIn/newsletter material)
- **Surprising insight or contrarian take** — the counterintuitive bits (best hook material)
- **Actionable tip** — standalone do-this-today advice (best short-video/single-post material)
- **Quotable line** — sentences that sting (quote graphics, thread closers)

If you can't find at least 4 distinct ideas, the content is too thin for a full pack — tell the user and scale scope down.

### 2. Select formats

Pick 5–7 formats, never all 15 — quality over coverage (heuristic: a strong pack on the user's 2 priority platforms beats a thin spray across 8). Decision rules:

- B2B / professional audience → weight LinkedIn posts + carousel; consumer/creator audience → weight short-video scripts + X.
- Goal = traffic/list growth → include the newsletter item and give posts link-out CTAs; goal = reach → engagement CTAs, links in replies/comments.
- Framework-type ideas present → include a carousel or thread; strong story present → include a story-post; no visual asset capacity → skip infographic/quote graphics, deliver text specs only.

Format spec table (length and structure per format):

| Format | Yield from one seed | Spec |
|---|---|---|
| LinkedIn posts | 3–5 | 100–200 words; hook line → story/insight → lesson → question or CTA; line breaks for scannability |
| X/Twitter thread | 1–2 | 5–10 tweets; hook tweet ≤250 chars; one idea per tweet; closer with CTA (full craft: `skills/marketing/tweet-writer`) |
| Single tweets | 3–5 | ≤110 chars preferred; sharpest standalone insights |
| Newsletter item | 1 | 300–500 words; hook → insight → lesson → link to full piece |
| Short-video scripts (TikTok/Reels/Shorts) | 2–3 | 30–60s; hook (≤3s) → problem → insight → CTA; write as spoken lines with [B-ROLL] notes |
| Carousel outline | 1–2 | 5–10 slides; slide 1 = hook, one point per slide, last slide = CTA; text per slide ≤25 words |
| Quote graphics (specs) | 3–5 | One pulled quote + attribution; supply exact text, no design |
| Instagram captions | 2–3 | 100–150 words; hook first line (feed truncates), story → lesson → CTA |
| Slide deck outline | 1 | 10–15 slides: title → problem → 3–5 content → conclusion → CTA |
| FAQ/explainer | 1 | 5–10 Q&As, 40–80 word answers (feeds SEO FAQ blocks) |
| Case study | 1 | 1,000–1,500 words; situation → action → result → lesson (only if seed contains a real result) |
| Webinar/talk outline | 1 | Timed outline: intro → problem → solution → examples → Q&A → CTA (only on request) |

### 3. Propose the pack, then generate

Show the user a one-screen plan first: idea inventory + chosen formats + which idea powers which piece. Get a quick confirm (or proceed if they said "just do it"). Then write **every piece in full** — no "you could write a post about X" stubs. While generating:

- Rewrite hooks natively per platform; never reuse the seed's opening line verbatim across pieces.
- Keep facts and claims within what the seed content supports — atomizing must not amplify a hedge into a certainty or invent numbers.
- Apply the one-CTA rule per piece, CTAs set by the goal from intake.

### 4. Sequence the distribution

Order the pieces for posting: lead with the strongest hook on the priority platform, don't post two derivatives of the same idea on the same platform back-to-back, thread/carousel mid-pack when early pieces have tested the angle. Present as a numbered posting order (the user maps it to their own dates/scheduler — no calendar prescriptions).

## Required output format

```
# Atomization Pack — [seed content title]

## Idea inventory
| # | Idea (one line) | Type | Powers |
| 1 | ... | framework | Carousel, LinkedIn #2 |
(5–10 rows)

## Pack plan
Formats chosen: [list] — [one-line rationale tied to platforms/goal]
Skipped: [notable exclusions + why]

## Pieces

### LinkedIn Post 1 — [idea #]
[Full post text, ready to paste]
CTA: [the one ask]

### X Thread — [idea #s]
1/ [tweet]
2/ [tweet]
...
(char count noted per tweet)

### [Every other piece, fully written, grouped by platform]

## Posting order
1. [Piece] — [platform] — [why first]
2. ...
(strongest hook first; same-idea derivatives spaced apart)

## Leftovers
[Ideas from the inventory not yet used — future seed material]
```

## Quality bar

Check every piece before delivering:

- [ ] Every piece is fully written and paste-ready — zero outlines-as-deliverables (except formats that *are* outlines: carousel, deck, webinar)
- [ ] No two pieces share an opening line; no piece is a copy-paste excerpt of the seed
- [ ] Each piece within its format's length spec (count characters for tweets: ≤110 single, ≤250 per thread tweet)
- [ ] Exactly one CTA per piece, aligned with the intake goal
- [ ] Every claim/number traceable to the seed content or the user — nothing invented in translation
- [ ] Voice consistent across all pieces — read three at random; they must sound like the same person
- [ ] 5–7 formats, not more; each chosen format justified by a platform the user actually uses
- [ ] Posting order spaces out same-idea derivatives

## Integration

- `skills/marketing/seo-content` — primary source of seed articles; atomize each published article as a standard follow-up.
- `skills/marketing/brand-voice` — supplies the voice guide every piece must pass.
- `skills/marketing/tweet-writer` — takes over when the X pieces deserve dedicated niche research and hook testing; hand it the idea inventory.
- `skills/marketing/newsletter` — consumes the newsletter item; strong issues flow back here as seeds.
- `skills/marketing/email-sequences` — value emails can be atomized into social pieces and vice versa.
