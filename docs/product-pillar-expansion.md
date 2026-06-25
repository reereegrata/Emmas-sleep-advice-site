# Product Pillar Expansion Workflow (from White Noise Pillar, June 2026)

## When to Use This

When Kuya says "expand [pillar page] — add more products." The goal is to fill real gaps in the page's product coverage so it better answers the user's search intent ("which product should I buy?").

## Step 1: Research via Desktop Agent

Write a task prompt for Kuya's Desktop agent. Include:

1. **Specific retailers to check** — tailor to AU: Amazon AU (Best Seller), Baby Bunting, Chemist Warehouse. These three cover online marketplace, dedicated baby store, and pharmacy chain.
2. **Products to exclude** — list the current products on the pillar page so Desktop doesn't report duplicates
3. **Gaps to look for** — based on what the current list is missing (budget options, plush toys, premium battery, unique features like cry sensor)
4. **Data format requested** — product name, price (AUD), key features, where available

**Example prompt for Desktop Agent:**
```
Task: Product Research for [Pillar Name] Expansion

Search these in Chrome:
1. Amazon AU → search "[category]" → sort by Best Seller → list top 8-10 results
2. Baby Bunting → search "[category]" → sort by Best Seller/Top Rated
3. Chemist Warehouse → search "[category]" if applicable

Skip these (already in our list):
[list current products]

For each NEW product found, tell me: product name, price (AUD), key features, and where it's available.

I'm looking for products that fill these gaps:
[list gaps - e.g. "budget options under AU$40", "plush toy / character designs"]
```

## Step 2: Analyze Gaps

Kuya returns a list. Identify:

- **Price gaps** — is there a price bracket missing? (Under $40, $40-80, $80+)
- **Category gaps** — missing a type? (plush toy, battery portable, app-controlled, fan-based)
- **Feature gaps** — unique features no current product has (cry sensor, heartbeat recording, breathing motion)
- **Store gaps** — are all products from one store? Products from multiple retailers = better reach

**Rule:** Only add products that fill a REAL gap for the user's search intent. If a product offers nothing new (same price, same features, same type as an existing product), skip it. The goal is completeness, not quantity.

## Step 3: Pick Products (3 Max Per Batch)

Limit to 3 products per expansion batch. Reasons:
- Keeps the task manageable in one deploy
- Each product needs a card, comparison table updates, budget tier updates, verdict updates
- Too many products dilute the page's focus

Selection criteria (in priority order):
1. **Fills a clear price gap** (e.g. no products under AU$40 → add budget option)
2. **Fills a clear category gap** (e.g. no plush toy → add Fisher-Price Otter)
3. **Has a unique feature** no existing product offers (e.g. cry sensor auto-activation)
4. **Available at a different retailer** than current products

## Step 4: Build Product Cards

Each new product card follows the existing template:

```html
<!-- ═══════ [N]. [PRODUCT NAME] ═══════ -->
<div class="product-card">
<figure style="margin:0 0 16px;text-align:center">
<img src="/images/whitenoise-PRODUCT.webp" alt="..." style="max-width:800px;width:100%;max-height:400px;object-fit:contain;border-radius:12px" loading="lazy">
</figure>
<h3>[N]. [Product Name] — [Best Feature] ✅ VERIFIED</h3>
<div class="price-tag">AU$XX–XX (Store Name)</div>
<p class="product-desc">[2-3 sentences. Include: what it is, key unique feature, why it matters. End with bold specs.]</p>
<div class="pros-cons">
<div class="pros"><strong class="pros-label">✅ Pros</strong><ul><li>[3-4 bullets]</li></ul></div>
<div class="cons"><strong class="cons-label">❌ Cons</strong><ul><li>[2-3 bullets, honest]</li></ul></div>
</div>
<div class="who-for"><strong>Who should buy this:</strong> [1-2 sentences. Who benefits most from this specific product.]</div>
</div>
```

## Step 5: Update All Sections

For each new product added, update ALL of these (do not skip any):

> **⚠️ CRITICAL — TWO-PASS RULE:** Updating the visible HTML (cards, tables) is only HALF the work. You MUST do a second pass to update the **meta tags and structured data**, which are often overlooked because they're in `<head>` and invisible. If you only update the body, the search snippet and rich results will still show the OLD count. Always do both passes.

### Pass 1 — HTML Content (visible)



1. **H1** — increment the number (e.g. "6 Best" → "9 Best")
2. **Intro paragraph** — same increment
3. **At-a-Glance H2** — same increment
4. **At-a-Glance table** — add a row per new product (Product, Price, Sounds, Power, Best For)
5. **Product cards** — place at end of existing list, after the last current product (before Budget Tiers)
6. **Budget Tiers section** — update pricing and picks. The existing tiers may need to shift (e.g. "Under $60" → "Under $40" when new cheaper products are added)
7. **Full Comparison Table H2** — update the count
8. **Full Comparison Table header row** — add a column per new product
9. **Full Comparison Table data rows** — add a column per new product for EVERY row (Price, Sounds, White Noise, Pink Noise, Shushing, Night Light, Humidifier, Battery, App, OK-to-Wake, Continuous, Best For)
10. **Final Verdict table** — add a row per new product with recommendation type + price
11. **Closing verdict paragraph** — optionally update if the new product changes the recommendation

### Pass 2 — Meta Tags & Schemas (invisible, often missed)

After Pass 1 is complete, do a SEPARATE pass targeting `<head>` only. Search the file for each of these:

**Meta Tags to update (6 total):**
| Tag | What to change |
|-----|---------------|
| `<title>` | Increment number (e.g. "6 Tested" → "9 Tested") |
| `<meta name="description">` | Update count + optionally add new product names (e.g. "My Baby Sound Spa, and more") |
| `<meta property="og:title">` | Same as title |
| `<meta property="og:description">` | Same as description |
| `<meta name="twitter:title">` | Same as title |
| `<meta name="twitter:description">` | Update count |

**Schema Tags to update (3 blocks to check):**

1. **Article schema** (first `<script type="application/ld+json">`):
   - `headline` — update count
   - `description` — update count + new products mentioned
   - `dateModified` — update to current date

2. **Product schema** (third `<script>` block, usually):
   - `description` — update count
   - `aggregateRating.reviewCount` — increment (e.g. `"6"` → `"9"`)
   - `review` array — add a new `{"@type": "Review", ...}` entry per new product

3. **FAQPage schema** (second `<script>` block):
   - Check if the "best white noise machine" FAQ answer mentions a count. Update if so. Usually safe — FAQ questions are evergreen.

**Verification:** After both passes, confirm:
- `grep -o '6'` on the file should return only legitimate "6" uses (dB safety, battery hours, etc.), NOT product count references
- Article schema `reviewCount` matches total products
- All `<script>` tags still balanced (every `<script>` has `</script>`)

## Step 5.5: Pre-Push Review — Present to Kuya for Approval

**HARD RULE (Kuya, June 2026):** After ALL changes are made (Pass 1 + Pass 2) but BEFORE `git push`, do a full review and send it to Kuya. Wait for his explicit "sige" or "push" before deploying.

The review must be structured — use the checklist below. Send the COMPLETE review as a single message to Kuya, not piecemeal.

### Review Checklist (Run Every Time)

**Load skills first:** `seo-mastery-workflow`, `emmas-site-guide-building`, `google-seo-docs-master`

**A. Verify via `curl` on the LIVE page** (if page is already live and you're updating it):
```bash
curl -sL "https://emmassleepadvice.com/PAGE-URL/" > /tmp/live-review.html
```

**B. Meta Tags (6 checks):**
```bash
grep -E '<title>|<meta name="description"|<meta property="og:(title|description)"|<meta name="twitter:(title|description)"' /tmp/live-review.html
```
- All counts match (e.g. ALL say "9", none say "6")
- New product names in description (optional but good)

**C. Schemas (3-4 JSON-LD blocks):**
```bash
python3 -c "
import re, json
with open('/tmp/live-review.html') as f:
    html = f.read()
blocks = re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
for i, b in enumerate(blocks):
    data = json.loads(b.strip())
    print(f'  [{i}] {data.get(\"@type\")}')
    if data.get('@type') == 'Product':
        revs = data.get('review', [])
        print(f'      reviewCount: {data.get(\"aggregateRating\",{}).get(\"reviewCount\")}, reviews: {len(revs)}')
        for r in revs:
            print(f'      - {r[\"name\"][:60]}')
"
```
- Article headline/description have correct count
- Product `reviewCount` matches total products
- Product `review` array has entries for ALL products (not just old ones)
- `dateModified` updated to current date

**D. Script Tag Balance:**
```bash
o=$(grep -c '<script' /tmp/live-review.html)
c=$(grep -c '</script>' /tmp/live-review.html)
echo "Open: $o, Close: $c"
# Must be equal
```

**E. No Dead Links (zero `href="#"`) in body:**
```bash
grep -n 'href="(?!https://|/)">' /tmp/live-review.html | grep -v 'onclick\|nav\|age-grid'
# Should return nothing
```

**F. Image Files Exist:**
```bash
ls -la /tmp/Emmas-sleep-advice-site/images/whitenoise-*.webp 2>&1 | grep -c "NEW-PRODUCT"
```
- Every product on the page has a corresponding .webp file in the images directory

**G. Budget Tier Prices Cover Full Range:**
```bash
grep -oP 'tier-price">[^<]+' /tmp/live-review.html
```
- The CHEAPEST product price appears in the most affordable tier
- The MOST EXPENSIVE appears in the premium tier
- No gaps where a product's price falls between tiers

**H. Prices Consistent Everywhere:**
Check ONE product's price appears the same in ALL these locations:
- At-a-glance table row
- Product card `price-tag`
- Full comparison table data row
- Final verdict table
- Product schema review body

### What to Send Kuya

Format the review as a clear summary:

```
**REVIEW: [Page Name] — [Description]**

**Technicals:**
- X JSON-LD blocks: [type] ✅ / [type] ✅ / ...
- Script tags: X open, X close ✅
- Canonical: correct ✅
- OG image: set ✅
- Dead links: none found ✅

**Meta Tags:**
- Title: "..." ✅
- Description: "..." ✅
- OG/Twitter: all consistent ✅

**Content Checks:**
- H1 says "[count] Best" ✅
- At-a-glance table: X rows ✅
- Product cards: X cards ✅
- Full comparison: X columns ✅
- Budget tiers: [list tiers + picks] ✅
- Verdict table: X rows ✅

**[If applicable:] Products & Pricing (verify consistency):**
| Product | Price in Card | Price in Schema | Match? |
|---------|:-----------:|:--------------:|:------:|
| ... | ... | ... | ✅ |

**[If new images added:] Images:**
- All X product images have WebP files ✅
- [List sizes KB]

**[If issues found:] Issues:**
1. [Issue] — [what needs fixing]
2. ...

**[Wait for approval] Sige Kuya, anong gusto mong gawin? 
1. Approve — ready to push
2. [Fix X first]
```

Do NOT push until Kuya replies with "push" or "sige" or "go".
