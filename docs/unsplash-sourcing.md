# Sourcing Images from Unsplash (Desktop Agent)

When Kuya's desktop AI agent scrapes Unsplash for Emma's site images, use these guidelines.

## For "Where Should I Start?" Section Cards

Three cards, each needs a landscape crop. Image naming: `guide-start-{wake,wrap,buy}.webp`.

### Search Query Refinement

Unsplash returns NO results for specific product names like "white noise machine" or "baby monitor". Use broader, scene-based terms:

| Card | Bad Query | Good Query |
|---|---|---|
| "Baby wakes up" | `tired mother white noise monitor night` | `mother tired night baby nursery` |
| "Won't stay wrapped" | `swaddle wrap newborn baby sleeping` | `newborn sleeping swaddle` |
| "No idea what to buy" | `baby white noise swaddle monitor flatlay` | `baby nursery products flatlay white shelf` |

Key lesson: **use `flatlay` for product shots**, not individual product names. Scene terms (nursery, shelf, morning light) outperform product terms.

### Image Specs
- Orientation: landscape preferred (800x500 target ratio)
- Lighting: warm, natural, not studio
- No text/watermarks
- Portrait images are OK — we use CSS `object-fit:cover` with `aspect-ratio:800/500`

## Processing Pipeline

1. Desktop agent downloads images → Kuya sends to Hermes via Telegram
2. Hermes receives at `/opt/data/profiles/agentnyroh/image_cache/img_*.jpg`
3. Check dimensions with PIL (no vision model available)
4. Convert to 800px wide WebP, quality 75, target 10-30KB
5. Add to site with `<figure>` + `object-fit:cover` CSS
6. Push, verify live
