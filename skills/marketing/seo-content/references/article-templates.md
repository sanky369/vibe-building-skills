# SEO Article Templates & Schema Markup

Full skeletons for the three core article formats, plus copy-paste schema markup.
Pick the template that matches the keyword's search intent (see SKILL.md Step 1).

## Template 1: How-To Guide (informational intent)

```
H1: How to [Achieve Outcome] in [Year]: [Benefit]

[Hook: state the problem and promise the solution — answer the query in the first 2–3 sentences]

Table of Contents

H2: Why [Topic] Matters
[Context and stakes — keep short; readers came for the steps]

H2: Step 1: [First Action]
[Instructions + a real example]

H2: Step 2: [Second Action]
[Instructions + a real example]

[Continue for all steps]

H2: Common Mistakes to Avoid
[3–5 pitfalls with fixes]

H2: FAQ
[4–6 questions in exact-question format, 40–60 word answers]

H2: Conclusion
[3–5 bullet takeaways + one CTA]
```

## Template 2: Listicle / Roundup (commercial intent)

```
H1: [Number] Best [Category] for [Outcome] in [Year]

[Hook: why this matters + your selection criteria — criteria build trust]

Table of Contents

H2: Quick Comparison
[Summary table of all items: name, best-for, price, standout feature]

H2: 1. [Item Name] — Best for [Use Case]
[Overview, key features, pros/cons, who it's for]

[Continue for all items — every item gets a "best for" positioning]

H2: How to Choose the Right [Category]
[Decision framework mapped to reader situations]

H2: FAQ
[4–6 questions]

H2: Conclusion
[Top pick(s) by situation + one CTA]
```

## Template 3: Ultimate Guide (informational, competitive head terms)

```
H1: The Complete Guide to [Topic]: Everything You Need to Know

[Hook: scope of the guide + who it's for]

Table of Contents

H2: What is [Topic]?
[Definition + context]

H2: Why [Topic] Matters
[Benefits + stakes]

H2: How [Topic] Works
[Detailed explanation]

H2: [Major Subtopic 1]
  H3: [Aspect]
  H3: [Aspect]

[Continue for all subtopics — this is where you out-cover competitors]

H2: Best Practices
[5–10 actionable tips]

H2: Common Mistakes
[Pitfalls to avoid]

H2: Tools and Resources
[Recommended tools with one-line reasons]

H2: FAQ
[6–10 questions]

H2: Conclusion
[Key takeaways + one CTA]
```

## Schema markup

Include as JSON-LD in the article's metadata block. Use FAQ schema whenever the
article has an FAQ section; Article schema on everything else (they can coexist).

### FAQ schema (targets featured snippets / rich results)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Your question here?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Your answer here (40-60 words)."
    }
  }]
}
```

### Article schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "image": "https://yoursite.com/image.jpg"
}
```
