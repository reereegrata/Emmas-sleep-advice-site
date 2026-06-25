# Desktop Agent SERP Task Prompt Template

Use this template when asking Kuya's Desktop agent to collect SERP data. The Desktop agent has Chrome + can see actual Google results with PAA.

## Template

Copy-paste the block below for Kuya:

---

**Task: SERP Research — [TOPIC]**

Search Google for **"[primary keyword] australia"** and collect:

1. **Top 10 search results** — list URLs and page titles
2. **People Also Ask (PAA)** — all questions in the PAA box. Click each to expand sub-questions
3. **H2 headings** of the top 3-5 results (especially .au domains and authoritative sources like Red Nose Australia, Raising Children Network)
4. **Related searches** — the "Related searches" section at the bottom of the SERP
5. **Content gaps** — topics NOT covered by the top results that searchers might want

**Format output as:**

```
---
## Top 10 Results
1. [Title] - URL
2. [Title] - URL
...

## PAA Questions
- question 1
- question 2
...

## H2 Summary (per competitor page)
[Site Name]:
- H2
- H2
...

## Related Searches
- search 1
- search 2
...

## Potential Gaps
- gap 1
...
```

---

## When to Use This

- After Google Trends identifies a promising topic (avg 20+)
- Before writing any heading architecture — SERP data is the primary input
- When deciding whether a topic is worth pursuing (high competition = skip)

## What Comes Next

1. Desktop agent collects SERP → Kuya sends output back to Hermes
2. Hermes cross-references with Google Trends data
3. Hermes makes a recommendation: push (low competition + good demand) or skip (heavy competition)
4. If push: heading architecture based on PAA + gaps + competitor H2s
