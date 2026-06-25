# HTML Container Nesting — Guides Hub

## The Bug

When adding a new section of guide cards to `/guides/index.html`, placing them AFTER the closing `</div>` of `.container` causes the cards to render full-width instead of matching the existing grid.

## Root Cause

The guides hub structure is:
```html
<section class="guides-section">
  <div class="container">          ← max-width: 960px
    <h2>Buying Guides</h2>
    <div class="guide-cards">...</div>
    
    <h2>Sleep Guides</h2>
    <div class="guide-cards">...</div>
  </div>                           ← container closes HERE
</section>
```

New sections MUST go BEFORE the container closing `</div>`. If placed after, they inherit full viewport width with no max-width constraint.

## Fix

Restructure so the new section is inside the container:
```html
    <h2>Sleep Guides</h2>
    <div class="guide-cards">...</div>

    <h2>New Section</h2>          ← INSIDE container
    <div class="guide-cards">...</div>
  </div>                           ← container closes AFTER all sections
</section>
```

## Detection

Check rendered width — if new cards span the full viewport while existing cards are constrained to ~960px, the new section is outside the container.
