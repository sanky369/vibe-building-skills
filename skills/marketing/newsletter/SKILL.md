---
name: newsletter
description: "Write a ready-to-send newsletter issue (and, when starting from zero, the recurring format and cadence to commit to): subject line options, preview text, body in one of six proven formats, and a single engagement CTA. Use when the user says 'write my newsletter', 'this week's issue', 'I want to start a newsletter', 'what should I send my list', 'help me email my subscribers regularly', or shares content to turn into an issue. Produces a complete issue draft with subject/preview variants — or a Newsletter Blueprint (format, cadence, section template) plus the first issue when setting one up."
---

# Newsletter

Write newsletter issues that subscribers open, read, and reply to. A newsletter is a recurring relationship, not a broadcast: it must be **consistent** (same format and cadence every time), **valuable** (useful before promotional), and **personal** (sounds like one human wrote it to one human). **Prime directive: the reader must finish the issue glad they opened it** — value first, promotion never more than a postscript.

## When to use / when not to

- Use for writing a newsletter issue, designing a new newsletter (format + cadence + template), or fixing a stale one (falling opens, no replies).
- If the user wants **automated emails triggered by behavior** (welcome series, launch, sales sequence), use `skills/marketing/email-sequences` — a newsletter is a recurring broadcast, not an automation.
- If the user has no list and no way to get subscribers, route to `skills/marketing/lead-magnet` first.
- If the source material is a blog post being adapted for many channels at once, use `skills/marketing/content-atomizer` (it can hand the newsletter item back here).

## Intake

Ask in one batch, only what's missing:

1. **Audience and list** — who subscribes, roughly how many, and what they signed up expecting.
2. **This issue's raw material** — a story, lesson, link roundup, data point, or recent piece of content. If nothing, ask for one recent professional observation or lesson; there is always one.
3. **Voice** — existing issues or a brand-voice guide to match (use `skills/marketing/brand-voice` output if it exists).
4. **Goal** — pure relationship-building, or is there something to softly promote?

If the user is starting a newsletter from scratch, also ask what they can sustain: writing capacity and how much source material their work naturally generates. Otherwise infer format and cadence from past issues. If enough is known, state assumptions and draft — don't stall.

## Workflow

### 1. If new: lock the format and cadence (the Blueprint)

Pick **one** primary format by decision rule — the user can guest-star other formats occasionally, but the flagship format is what subscribers learn to expect:

| If the user… | Format | Skeleton |
|---|---|---|
| Reads widely, low writing capacity | **Curated** | Personal opening note → 5–10 links, each with 1–2 sentences of *your take* (the commentary is the product) → sign-off |
| Has rich personal/client experiences | **Story-driven** | Hook → story → the lesson → how the reader applies it → sign-off |
| Sells expertise (consultant, coach, B2B) | **Educational** | Why this matters → the concept/framework → 2–3 real examples → how to apply → sign-off |
| Has network access to interesting people | **Interview** | Who + why them → 5–10 Q&As → your key takeaway → sign-off |
| Works with data or research | **Data-driven** | Surprising finding → the data → what it means → what to do with it → sign-off |
| Builds in public / personal brand | **Personal update** | Working on → learning → thinking about → one recommendation → sign-off |

Cadence by decision rule: weekly if their work generates material weekly and they'll actually sustain it; otherwise bi-weekly (the default recommendation — heuristic: a kept bi-weekly schedule beats a broken weekly one); monthly only if the format is heavyweight (interview, data-driven). Fix the send day/time and put it in the Blueprint.

### 2. Extract the issue's one idea

Every issue carries exactly **one** central idea (curated format: one theme unifying the links). From the raw material, pull the single most useful/surprising insight for *this* audience. If the material holds several strong ideas, list them, pick the best for now, and bank the rest as future issue seeds in the delivery notes.

### 3. Draft the issue

- **Subject line**: write 3 candidates, ≤45 characters each, specific and curiosity- or benefit-driven. No clickbait the body doesn't cash; no ALL CAPS; at most one punctuation flourish.
- **Preview text**: ≤90 characters that extends (not repeats) the subject.
- **Opening**: 1–3 sentences, personal and concrete — an observation, moment, or admission. Never "Welcome to another issue" or weather-report throat-clearing.
- **Body**: follow the format skeleton from Step 1. Short paragraphs (≤3 sentences), subheads or bold lead-ins if the issue runs past ~300 words, written to one reader ("you", never "you all"/"subscribers").
- **CTA**: exactly one, engagement-first — "Hit reply and tell me X" beats "click here" for relationship-building. If there's a promotion, it rides in the P.S., not the body, unless the user explicitly wants a promotional issue.
- **Sign-off**: first name + optional P.S. (the P.S. is prime real estate: a bonus link, question, or the soft promo).

Length target: 300–800 words for original-content formats; curated can run longer but each link blurb stays ≤2 sentences of commentary.

### 4. Self-review and deliver

Run the quality bar. Then deliver in the required output format, including next-issue seeds so the user never faces a blank page.

## Required output format

```
# Newsletter Issue — [working title]

## Subject line options
1. "…" (n chars)
2. "…" (n chars)
3. "…" (n chars)
Recommended: #_ — [one-line reason]

## Preview text
"…" (n chars)

## Body
[Full issue: opening → format-skeleton body → CTA → sign-off → P.S.]

## Send notes
- Format: [which of the six] · Cadence slot: [day/time]
- CTA: [the one action asked]
- Promo present: [none | P.S. only | promotional issue]

## Next-issue seeds
- [2–3 banked ideas pulled from this material or conversation]
```

When setting up a new newsletter, precede the issue with:

```
# Newsletter Blueprint — [name]

- Audience & promise: [who subscribes and what each issue gives them]
- Flagship format: [one of six] — [why, per decision rule]
- Cadence: [weekly/bi-weekly/monthly], sent [day/time]
- Section template: [the recurring skeleton, so every issue is structurally identical]
- Voice notes: [3–5 bullets]
- Metrics to watch: open rate trend, reply count, unsubscribe spikes per issue
```

## Quality bar

Check every item; fix before delivering:

- [ ] Every subject line ≤45 characters (count them) and honestly cashed by the body
- [ ] Preview text ≤90 characters and not a repeat of the subject
- [ ] Opening is personal/concrete — no "welcome to this week's issue" boilerplate
- [ ] Exactly one idea; exactly one CTA
- [ ] Promotion absent or confined to the P.S. (unless explicitly a promo issue)
- [ ] No paragraph over 3 sentences; issue scannable on a phone
- [ ] Sounds like the user, not like "a newsletter" — read it aloud; generic sentences get cut
- [ ] Every factual claim cited, attributable to the user's own experience, or cut; no invented anecdotes presented as the user's
- [ ] Curated format: every link has a stated reason it earned inclusion

## Integration

- `skills/marketing/brand-voice` — supplies the voice guide the issue must match; run it first if the user has no defined voice.
- `skills/marketing/lead-magnet` — builds the subscriber-acquisition offer; new subscribers flow through `skills/marketing/email-sequences` (welcome) before landing on this newsletter.
- `skills/marketing/email-sequences` — owns triggered/automated email; the newsletter is the ongoing touchpoint subscribers graduate into.
- `skills/marketing/content-atomizer` — turns blog/video content into newsletter items, and turns strong newsletter issues back into social posts.
- `skills/marketing/seo-content` — published articles are recurring issue material; pass title, link, and one-sentence hook.
