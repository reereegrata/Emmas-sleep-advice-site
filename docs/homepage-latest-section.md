# Homepage "Latest from Emma" Section: Rotation Policy

Section: `<section id="latest-guides">` in `index.html` (h2 "Latest from Emma").
Status: **CURRENT POLICY, set 2026-09-15.**

## The policy (2026-09-15 onward)

The section shows the **4 newest published posts by `datePublished`**, newest first,
in ONE `.guide-grid` inside `.container`.

- Card count is fixed at **4**. This is a freshness shelf, not a full index: the hub
  (`/guides/`) and the category hubs carry the long list.
- Order is strictly newest `datePublished` first (read from each page's JSON-LD).
- Cards use the page's existing title, description, image and alt. Never write new
  card copy for a rotation.
- `.view-all-wrap` / `.view-all-btn` ("View All Guides ->" to `/guides/`) is a direct
  child of `.container`, NOT of the grid. Do not move it into the grid.
- Rotation happens **inside content-publish tasks**: when a new guide ships, the
  publishing task swaps it in and drops the oldest visible card. There is **no
  automation, no script, no cron** for this. Do not build one.

### Tie-break order for future trims

`datePublished` collisions are common on this site (content was published in batches).
When more posts share the cut-off date than there are slots, break the tie in this order:

1. **Intent / cluster spread across the 4 visible cards.** Prefer the mix that shows
   different clusters (regression, schedule, safety, product) over four cards from one
   cluster. A shelf of four sleep-schedule cards wastes the surface.
2. **Prefer candidates with the fewest inbound internal links.** A card on the homepage
   is an internal link; give it to the page that is not already well linked, not to the
   page every hub already links to.
3. **Most recent sitemap `<lastmod>`.** Only when 1 and 2 do not separate the candidates.

Record the tie and the reasoning in the commit message when a tie is broken.

## Current state after the 2026-09-15 trim

**22 cards -> 4 cards.** Two changes in one edit:

1. **Trim.** The shelf now shows the 4 newest posts by `datePublished`.
2. **Nesting fix.** The grid was mis-nested: `.guide-grid` closed after card 11, and
   cards 12 to 22 were stray siblings of the grid inside `.container`, so they got no
   two-column layout and rendered stacked full width. The section is now
   `.container > [.text-center, .guide-grid (4 cards), .view-all-wrap]`.

Cards kept (newest first, verified against each page's JSON-LD on 2026-09-15):

| # | Card href | datePublished | Cluster |
|---|-----------|---------------|---------|
| 1 | `/guides/baby-sleep-regressions/` | 2026-08-11 | Sleep Regression |
| 2 | `/guides/6-month-sleep-regression-australia/` | 2026-08-03 | Sleep Regression |
| 3 | `/guides/0-3-month-sleep-schedule/` | 2026-07-25 | Sleep Schedule |
| 4 | `/guides/7-9-month-sleep-schedule/` | 2026-07-25 | Sleep Schedule |

Tie at the cut-off: **five** pages carry `datePublished` 2026-07-25
(`0-3-month-sleep-schedule`, `4-6-month-sleep-schedule`, `7-9-month-sleep-schedule`,
`10-12-month-sleep-schedule`, `toddler-sleep`). Rule 1 above picked 0-3 and 7-9:
they are the two ends of the schedule cluster that are not already linked from every
sibling schedule page, which keeps the visible shelf spread across age ranges rather
than stacking 4-6 and 10-12 next to each other.

Verified `datePublished` for every card that was on the shelf before the trim (pull
2026-09-15, `grep` of each page's JSON-LD):

```text
2026-08-11  guides/baby-sleep-regressions
2026-08-03  guides/6-month-sleep-regression-australia
2026-07-25  guides/toddler-sleep
2026-07-25  guides/7-9-month-sleep-schedule
2026-07-25  guides/4-6-month-sleep-schedule
2026-07-25  guides/10-12-month-sleep-schedule
2026-07-25  guides/0-3-month-sleep-schedule
2026-07-12  guides/safe-sleep-sids-prevention-australia
2026-07-12  guides/room-temperature-baby-sleep-australia
2026-07-12  guides/responsive-settling-techniques-australia
2026-07-12  guides/baby-sleeping-bags-australia
2026-06-02  guides/when-to-stop-swaddling-transition
2026-06-02  guides/swaddle-vs-sleep-sack
2026-06-02  guides/swaddle-tog-temperature-guide
2026-06-02  guides/how-to-swaddle-a-baby
2026-06-02  best-baby-swaddle-australia
2026-06-01  guides/wifi-vs-non-wifi-baby-monitor
2026-06-01  guides/when-to-stop-using-baby-monitor
2026-06-01  guides/how-to-set-up-baby-monitor
2026-06-01  guides/how-to-choose-baby-monitor
2026-06-01  guides/are-baby-monitors-worth-it
2026-05-01  best-baby-monitor-australia
```

Note: `datePublished` and sitemap `<lastmod>` disagree on some pages (sitemap lastmod
tracks edits, not publication). Use `datePublished` for the shelf order.

### Dead CSS removed in the same edit

Four rule groups in the inline `<style>` of `index.html` supported the old
"grid clips at 540px, reveals on hover/target" behaviour. They are gone:

- the second `.guide-grid{...;max-height:540px;overflow:hidden;position:relative}` rule
- `.guide-grid::after{content:'View All Guides ->';...}`
- `.guide-grid:target,.guide-grid:hover{max-height:none;overflow:visible}`
- `.guide-grid:target::after,.guide-grid:hover::after{display:none}`

Kept: the base `.guide-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}`
plus both mobile 1-column overrides (`max-width:900px`, `max-width:640px`).

Why they went: the `::after` rule injected a fake, non-focusable "View All Guides"
link that duplicated the real `.view-all-btn` below the grid, and the `:target`/`:hover`
reveal needed a `#latest-guides` fragment URL that no page links to. Removing them
restores one real link and a grid that always shows all 4 cards.

### Trade-off accepted (2026-09-15)

18 pages lost their homepage card and keep hub links only. Approved by Kuya
2026-09-15: no replacement block, no extra cross-links added, no sitemap `lastmod`
bump for the trimmed pages. Revisit only if GSC shows a trimmed page losing its
only internal link.

## How to rotate (do this inside a content-publish task)

1. Read the current 4 card hrefs in `index.html` (`#latest-guides`).
2. New page's `datePublished` goes to the top; drop the oldest visible card.
3. Copy an existing card block verbatim (9 lines: `<a>` through `</a>`) and swap the
   `href`, image `src`, `alt`, cat-tag, `h3` and description. Keep the card block
   structure and class names exactly.
4. Keep exactly 4 cards and exactly one `.guide-grid`.
5. Re-run the structural check before committing: the section must be
   `.container > [.text-center, .guide-grid, .view-all-wrap]` with no `.article-card`
   outside the grid.
6. Update the "Cards kept" table above with the new date and pull in the commit.

```html
<a href="/guides/PAGE-SLUG/" class="article-card">
<div class="card-img guides-bg"><img src="/images/IMAGE.webp" alt="..." loading="lazy" style="width:100%;height:100%;object-fit:contain" width="800" height="500"></div>
<div class="card-body">
<div class="cat-tag guides">Category</div>
<h3>Page Title</h3>
<p>Short description.</p>
<div class="card-footer">Read Guide -></div>
</div>
</a>
```

## SUPERSEDED: June 2026 policy (do not follow)

The original version of this doc (June 2026) said:

- the section shows **9 cards** (5 monitor guides + 1 monitor pillar + 3 swaddle
  guides + 1 swaddle pillar), and
- rotation should be driven by **GSC clicks first**, then impressions, then freshness,
  and
- rotate only "after GSC shows clicks, otherwise leave as is".

That is superseded. Reasons: the shelf later grew to 22 cards and stopped being a
freshness signal at all; click data on a site with 1 click per 28 days cannot order 22
cards; and the "leave as is" rule produced the mis-nesting and the dead 540px CSS that
this edit removes. The section is a **freshness shelf of 4 by `datePublished`** now.
GSC performance is a valid input for what to *publish* or *refresh*, not for ordering
this shelf.

## Related

- `docs/container-nesting-bug.md`: the same class of nesting defect elsewhere.
- `docs/status-md-pattern.md`: how STATUS.md entries are written.
- `STATUS.md`: dated log of every change to this section.
