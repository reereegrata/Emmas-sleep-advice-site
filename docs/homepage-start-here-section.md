# Homepage "Where Should I Start?" Section

## Context

In June 2026, we replaced the age-based grid (Newborn/Baby/Toddler → all pointing to the same /guides/ page) with a pain-point navigation section. This was an SEO architecture decision, not just a cosmetic change.

## Design

Three cards, each mapping a real search query to a specific money page:

| Card | Pain Point (H2) | Routes To | Link Path |
|---|---|---|---|
| Tired mother with baby | "Baby wakes up every hour" | White noise + monitor money page | `/best-baby-white-noise-machine-australia/` |
| Swaddled newborn | "Won't stay wrapped" | Swaddle money page | `/best-baby-swaddle-australia/` |
| Baby products flatlay | "No idea what to buy first" | Best Picks hub | `/best-picks/` |

## Why This Works

- **Matches real search intent** — parents search symptoms, not age groups
- **Direct link equity** — each card links to a money page, not the generic /guides/
- **No dilution** — doesn't create competing SILO paths (age vs topic)
- **Scalable** — 3 cards is the sweet spot; new products slot into Best Picks, not new cards

## CSS Classes Used

- `.start-grid` — 3-column grid (reused and renamed from `.age-grid`)
- `.start-card` — card with hover lift (reused from `.age-card`)
- `.start-card-icon` — 120px tall icon area with `object-fit:cover` images
- `.start-card-body` — content area with quote + heading + CTA

## Image Specs

Card icon images: 600px wide, WebP, quality 48-50, target 6-30KB. Use `object-fit:cover` on the `<img>` tag since the display area is only 120px tall.

## Nav Update

The dropdown nav was changed from age groups to topic links:

```
Before: Newborn (0-4m) | Baby (4-12m) | Toddler (12m+)
After:  Baby Monitors | Swaddles | White Noise
```

This affects ALL pages on the site (19 pages updated in the June 2026 batch).
