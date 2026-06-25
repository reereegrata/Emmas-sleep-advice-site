# STATUS.md Pattern — Over-Optimization Prevention

> The STATUS.md file at `/tmp/Emmas-sleep-advice-site/STATUS.md` is the single source of truth for what has been optimized on emmassleepadvice.com.
> Check it BEFORE every optimization suggestion.

## Why STATUS.md Instead of Honcho

| Solution | RAM | Speed | Accuracy | Auto-Learn |
|----------|:---:|:-----:|:--------:|:----------:|
| Honcho (self-hosted, AI disabled) | -500MB | Slow (API) | Low (no embeddings) | No |
| Raised file memory (10K chars) | 0 | Instant | Exact | No |
| **STATUS.md + search_files** | **0** | **0.2s** | **Exact match** | **No — but permanent** |

STATUS.md is a markdown file committed to the repo. It persists across server restarts, Hermes version updates, and device changes because it lives on GitHub. The agent can `grep` or `search_files` on it in under 1 second.

## What STATUS.md Contains

| Section | Purpose |
|---------|---------|
| Site Overview | Domain, hosting, brand, colors, Hermes setup, deploy process, cron jobs |
| Site Architecture | Visual silo diagram showing page hierarchy |
| All Pages | Complete page inventory with paths and clusters |
| Internal Link Matrix | Exact link counts per guide → pillar |
| Schema Inventory | Per-page table of schema.org types |
| Image Inventory | All images, sizes, formats, alt text |
| GSC Performance | Last 28 days: impressions, clicks, positions per page |
| Technical Status | robots.txt, sitemap, HTTPS, mobile, canonical, OG |
| Design System | Colors, fonts, image specs, border-radius |
| Affiliate Programs | Status of each affiliate program |
| Content Backlog | Ideas not yet prioritized |
| Optimization History | Date-by-date log of every optimization performed |
| What's NOT Yet Done | Prioritized list of remaining work |
| Optimization Rules | Rules to prevent over-optimization |

## Rules Enforced by STATUS.md

1. One optimization pass per page per month — unless critical bug
2. Meta title: only trim if over 71 chars. Do NOT change content/topic.
3. OG tags: only fix if duplicate or missing. Do NOT change content.
4. Internal links: already 3-6 per guide. Do NOT add more.
5. External links: all guides have Red Nose. Do NOT add more.
6. Schema: present on all pages. Do NOT add more types unless for new content.
7. Content text: do NOT re-optimize unless GSC shows >5 position drop.

## How I Use It

Before suggesting any optimization:
1. `search_files(path="/tmp/Emmas-sleep-advice-site", pattern="STATUS.md")` — or just remember it exists
2. `grep` for the specific page or optimization in STATUS.md
3. If found — SKIP. The optimization was already done.
4. If not found — check the "What's NOT Yet Done" section for priority context
5. After performing any optimization — update STATUS.md and push alongside the page changes

## How the User Can Verify

Kuya can open STATUS.md directly on GitHub at:
`https://github.com/reereegrata/Emmas-sleep-advice-site/blob/main/STATUS.md`

He can see exactly what has been done, when, and why — full transparency.
