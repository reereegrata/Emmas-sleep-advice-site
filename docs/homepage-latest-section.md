# Homepage "Latest from Emma" Section — Rotation Guide

The homepage (`/index.html`, line ~774) has a "Latest from Emma" section currently displaying 9 guide cards in a static grid. Kuya flagged that this should be periodically rotated to feature content with actual GSC traction instead of always showing all guides.

## Current State (June 2026)

- **9 cards** currently displayed: 5 monitor guides + 1 monitor pillar + 3 swaddle guides + 1 swaddle pillar
- **No dynamic rotation** — same cards always shown
- **Section:** `<h2 class="section-title">Latest from Emma</h2>` followed by `<div class="guide-grid">` containing `<a href="..." class="article-card">` elements

## When to Rotate

- After GSC data shows a guide getting **clicks** (currently only Swaddle vs Sleep Sack has 1 click among guides)
- After a new content piece is published (add it, remove the oldest/lowest-performer)
- When Kuya explicitly asks to feature something specific

## What to Feature

Priority order:
1. Pages with **actual GSC clicks** — even 1 click means real user engagement
2. Pages with **highest impressions** among guides (currently: How to Wean = 10, Does White Noise Help = 9)
3. Newly published or optimized content (freshness signal)
4. Mix across clusters — don't show 4 guides from same cluster

## How to Rotate

```html
<!-- In index.html, replace the guide-grid content -->
<a href="/guides/PAGE-SLUG/" class="article-card">
  <div class="card-img guides-bg">
    <img src="/images/guide-IMAGE.webp" alt="..." loading="lazy" width="800" height="500">
  </div>
  <div class="card-body">
    <div class="cat-tag guides">Category</div>
    <h3>Page Title</h3>
    <p>Short description.</p>
    <div class="card-footer">Read Guide →</div>
  </div>
</a>
```

## When NOT to Rotate

- If no guides have clicks yet — Kuya decided to "leave as is" until GSC shows traction
- If only 1-2 guides have clicks — better to wait for broader data
- Before checking STATUS.md for the current optimization state of the featured pages
