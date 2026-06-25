# Emma Site Pillar Page Workflow (Product Reviews)

> Absorbed from the former standalone `emma-pillar-workflow` skill. This is the
> PILLAR-PAGE variant of the Emma site-building workflow. The shared
> infrastructure (git auth, inline-CSS requirement, image pipeline, deployment
> verification, US/AU spelling, pre-push gates, security scan) lives in the main
> `emmas-site-guide-building` SKILL.md — read that first, then use this for the
> pillar-specific phases.

End-to-end workflow for creating "Best X Australia 2026" product review pillar
pages on emmassleepadvice.com.

## Prerequisites

- Existing pillar page template (copy from `/best-baby-swaddle-australia/index.html`)
- Product research completed (keyword research, competitor H2s, intent classification)
- 6 products selected with AU pricing data
- **Target word count: 1,500–2,500 body words** (Kuya's sweet spot for product review pillars). Initially aim for ~6,000 words of raw content, then trim aggressively in Phase 4. Product cards should be ~180 words each — not 400+. Cut feature lists that already appear in the comparison table. Safety section ~200 words, FAQ ~200 words.

## Phase 1: Build Draft

1. Copy the swaddle page template — identical CSS, header, nav, footer
2. Customize: hero badge emoji, H1 title, meta tags, schema
3. Write 6 product cards following the exact template structure:
   - `<div class="product-card">` with figure, H3, price-tag, product-desc
   - `pros-cons` grid (pros h4 in sage, cons h4 in accent)
   - `who-for` div at bottom
4. Add comparison tables (at-a-glance + full feature matrix)
5. Add Red Nose Australia safety section
6. Add FAQ (5 questions, `<details>` elements with `faq-item` class)
7. Add verdict table, disclaimer box, author bio, related guides
8. Schema: 3 blocks — Article, FAQPage, Product with aggregateRating (4.7★) + 6 Review items each with `"author": {"@type": "Person", "name": "Emma"}`
9. Save as `DRAFT-<slug>.html` at repo root — DO NOT push live yet

## Phase 2: Images

- 6 product images needed, one per product
- User provides images (usually as Telegram uploads)
- Process each: convert to webp (quality 85), resize to max 800px wide (maintain ratio)
- Save to `/images/whitenoise-<product-slug>.webp`
- Image slots in HTML: `<img src="/images/whitenoise-*.webp" ... loading="lazy">`
- All product images need alt text, lazy loading, width/height attrs

## Phase 3: Product Verification

Ask user for each product — three things only:
1. **Price (AU$)** — confirmed current AU retail price range
2. **Brand / Model** — correct brand name and model identifier
3. **Features** — sounds count, battery type, extras (night light, humidifier, app, timer, etc.)

User provides verification data. Update EVERY reference across:
- Product card (H3, price-tag, product-desc, pros, cons, who-for)
- At-a-glance table
- Full comparison table (every row)
- Verdict table
- Budget tier picks
- FAQPage schema
- Product schema reviews
- FAQ HTML answers
- Image alt text
- Any body copy mentioning that product

**Verify no stale references remain** — grep for old prices, wrong feature counts, old model names.

## Phase 4: Humanize + Trim + Design

1. **Word count trim** — the raw draft will be ~5,000-6,500 words. Cut aggressively to 1,500-2,500 body words:
   - Product descriptions: cut redundant feature lists (they're in the comparison table). Target ~180 words each.
   - Safety section: tighten bullet points. Keep study citations but cut exposition.
   - FAQ: shorter answers, one paragraph each max.
   - Intro: one paragraph, straight to the point.
   - Budget tiers: one sentence per tier.
   - After trimming, verify with `article_body_wc()` script.
2. **Humanizer pass** — scan for AI patterns (filler phrases, promotional hype, clichés, overused metaphors, generic positive conclusions). Fix with targeted patches.
3. **Claude-design pass** — refine visuals (budget tier color coding, hover effects, mobile breakpoint verification). Keep it subtle — template CSS is already solid.
4. **Quality check** — re-read trimmed content. Does Emma's voice still come through? Are product differentiators clear? Did any key features get cut?

## Phase 5: Audit (target: 100/100)

Run full audit before considering publication:

### Meta Tags
- Title: 50-65 chars, keyword near front, brand at end
- Meta description: 145-160 chars, natural keyword inclusion
- Canonical URL matching live path
- OG tags (title, description, type, url, site_name)
- Twitter card (summary_large_image, title, description)
- lang="en-AU", charset, viewport

### Schema
- 3 blocks: Article + FAQPage + Product
- Product: aggregateRating (ratingValue, reviewCount), category
- Each Review: author (Person, name: "Emma"), reviewBody
- FAQ: 5 questions with substantive answers

### Content
- 1 H1, ≥5 H2s
- All 6 images have alt text + lazy loading + dimensions
- AU$ refs ≥40, bare $ refs = 0
- Australia mentions ≥15, Red Nose ≥5, Emma ≥5
- Guide cross-links ≥3

### Technical
- Script tags balanced (open = close)
- HTML tags balanced
- Media queries ≥1 (mobile responsive)
- Google Fonts preconnect present

### Audit Script
Use `scripts/pillar-audit-checklist.py` (in this skill) as a starting point. Run it
against your `DRAFT-<slug>.html`, fix all issues, re-run until 100/100.

## Phase 6: Publish

**DO NOT push live without Kuya saying "go."** When approved:
1. Copy draft to `/best-<slug>-australia/index.html`
2. Update sitemap.xml (priority 0.9)
3. Update llms.txt (Best Picks section + new guide links)
4. Git add, commit, push (use the HTTPS-PAT push method from the main SKILL.md git-auth section)
5. Verify 200 on live URL
6. Remove DRAFT file

## Phase 7: Post-Publish Site Updates

After the pillar is live, update ALL cross-references across the site (Kuya expects these immediately):

### Homepage (`/index.html`)
- **Nav dropdown**: change `<a href="#">` placeholder to real pillar URL
- **Editor's Choice card**: change from `<div class="editor-card">` to `<a href="...">`, update badge (e.g., "Top Rated"), add real product names in verdict text
- **Comparison table**: replace placeholder brands (Kipcush/eSynic/SURFOU) with 3 real products from the pillar — typically Hatch Rest 2, Dreamegg D1, ergoPouch Drift Away
- **Shop by Category**: change `<a href="#">` on the relevant category card to the pillar URL
- **Footer**: change `<a href="#">Best White Noise</a>` to real URL
- **FAQ**: if homepage FAQ references the category, update "coming soon" text to link to the pillar

### Best Picks Hub (`/best-picks/`)
- **Nav dropdown**: same fix as homepage
- **Product card**: change from `<div class="pick-card coming">` to `<a href="..." class="pick-card">`, change badge from "Coming Soon" to "Editor's Pick", replace "In Progress" tag with "Read Full Review →" CTA
- Add real product names in the description paragraph

### Verification after Phase 7
- Homepage: grep for "Kipcush" and "eSynic" — should be 0
- Homepage: grep for real product names — should find them
- Best Picks: grep for "Coming Soon" — should be 0
- Best Picks: grep for "Editor" — should find the badge
- All nav dropdowns across all pages should link to the pillar
- Sitemap and llms.txt should contain the pillar URL

**Common pitfall**: if you used `write_file` in execute_code during earlier phases, the homepage and best-picks files may have line-number artifacts. Strip them with sed before pushing: `sed -i 's/^|*//' index.html` then re-apply the Phase 7 changes.

## Pitfalls

- **File corruption from read_file/write_file cycle**: reading with `read_file` and writing with `write_file` in execute_code embeds line-number pipe artifacts (`1|     1|     content`) into the file. After multiple cycles, the file accumulates multiple layers of these artifacts and becomes unreadable. **Always read raw files with `open()` in terminal Python scripts, never through execute_code's read_file/write_file.** If corruption occurs, clean with: `re.sub(r'^(\d+\|\s*)+', '', line)` on each line. For homepage/best-picks files that get corrupted during Phase 7 updates, quick fix with sed: `sed -i 's/^|*//' index.html` then re-apply changes. **Always verify with `head -1 index.html` — should show `<!DOCTYPE html>`, not `|1|...` or `1|<!DOCTYPE`.**
- Never fabricate product features — wait for user verification
- Check for "made up" features (e.g., night light on a product that doesn't have one)
- The Glow Sleep Easy doesn't play white noise — only pink/brown/rain/waterfall. Flag non-white-noise products honestly
- Product positioning may shift after verification (e.g., "portable" → "nursery" if battery turns out to be mains-only)
- Always confirm model names — "Glow Dreaming" is the brand, "Glow Sleep Easy" is the model
- Budget tier headings with bare $ (like "Under $60") are acceptable as category labels, not product prices
- **Kuya's #1 rule: DO NOT push live without explicit approval.** Draft first, verify everything, then push only when told.
