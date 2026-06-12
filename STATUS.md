# emmassleepadvice.com — Site Status & Optimization Log

> Central reference for everything on the site.
> Check this FIRST before suggesting changes, adding content, or running optimizations.
> Last updated: 2026-06-11

## 0. Google Knowledge Base — Saved Reference

All Google Search docs knowledge consolidated into skill `google-seo-docs-master` (replaces 3 old skills).

**What's inside that skill:**
- How Search Works + SEO Fundamentals + AI Content Policy
- Crawling & Indexing (sitemaps, robots.txt, noindex, canonical, recrawl)
- Search Appearance (titles, meta descriptions, images, video, structured data)
- Ranking Updates History (all core updates 2023-2026)
- Debugging Traffic Drops (step-by-step)
- GSC Guide + E-E-A-T + Penalties
- Reference file: `references/ranking-updates-timeline.md`

**Next expected core update:** August-September 2026 (~3 month cycle). Target: have all pages optimized before then.

**If traffic drops:** check https://status.search.google.com/ FIRST before changing anything on the site.

---

## 1. Site Overview

| Detail | Value |
|--------|-------|
| Domain | emmassleepadvice.com |
| Hosting | GitHub Pages + Cloudflare (CDN, SSL, DNS) |
| Repo | github.com/reereegrata/Emmas-sleep-advice-site |
| Deploy key | /opt/data/.ssh/id_ed25519_emma |
| Tech | Static HTML/CSS (no frameworks, no CMS) |
| Niche | Baby sleep advice — Australian audience |
| Brand | Emma (personal brand, Australian mum) |
| Colors | Purple #5B4B8A, Pink #E8758A |
| Font | Poppins |
| Affiliate | Amazon AU (not yet applied), direct AU brands later |

### Hermes Setup (for this server)

| Detail | Value |
|--------|-------|
| Profile | agentnyroh |
| Hermes home | /opt/data/profiles/agentnyroh/ |
| GSC credentials | /opt/data/profiles/agentnyroh/scripts/gsc_credentials.json (new Web app client) |
| GSC venv | /opt/data/profiles/agentnyroh/scripts/gsc_venv/ |
| GSC token | /opt/data/profiles/agentnyroh/scripts/gsc_token.json (PERMANENT — no expiry) |
| GSC connected sites | https://emmassleepadvice.com/ ONLY (bookshelfmemories removed) |

### Deploy Process

```bash
cd /tmp/Emmas-sleep-advice-site
git add -A
git commit -m "description of changes"
GIT_SSH_COMMAND="ssh -i /opt/data/.ssh/id_ed25519_emma -o IdentitiesOnly=yes" git push origin main
```

- Clone via HTTPS: `git clone https://github.com/reereegrata/Emmas-sleep-advice-site.git /tmp/Emmas-sleep-advice-site`
- Push via SSH deploy key (registered in GitHub repo settings)
- Site auto-deploys via GitHub Pages — no manual steps needed

### Cron Jobs

| Job | Schedule | Status |
|-----|----------|--------|
| Weekly GSC report | Every Monday 9am | ✅ Active (set up via cronjob tool) |

---

## 2. Site Architecture (Silo Structure)

```
Homepage (/)
├── Best Picks Hub (/best-picks/)
│   ├── 🏆 Best Baby Monitors AU (pillar)
│   │   ├── How to Choose a Baby Monitor (guide)
│   │   └── WiFi vs Non-WiFi Baby Monitor (guide)
│   ├── 🏆 Best White Noise Machines AU (pillar)
│   │   ├── Noise Comparison: Brown vs White vs Pink (guide)
│   │   ├── Does White Noise Help Baby Sleep (guide)
│   │   ├── White Noise Decibel Safety (guide)
│   │   └── How to Wean Off White Noise (guide)
│   └── 🏆 Best Baby Swaddles AU (pillar — NOT YET BUILT)
│       ├── Swaddle vs Sleep Sack (guide)
│       └── When to Stop Swaddling (guide)
├── Guides Hub (/guides/)
│   ├── All guides listed above
│   └── More coming soon...
├── About (/about.html)
└── Contact (/contact.html)
```

### Content Clusters

| Cluster | Pillar Page | Guides | Status |
|---------|-------------|--------|--------|
| Baby Monitor | /best-baby-monitor-australia/ | 2 guides | ✅ Complete |
| White Noise | /best-baby-white-noise-machine-australia/ | 4 guides | ✅ Complete |
| Swaddle | /best-baby-swaddle-australia/ | 4 guides | ✅ Complete |

---

## 3. All Pages

### Product Pillars (3)

| Page | Path | Status |
|------|------|--------|
| Best Baby Monitors | /best-baby-monitor-australia/ | ✅ Live |
| Best White Noise Machines | /best-baby-white-noise-machine-australia/ | ✅ Live |
| Best Baby Swaddles | /best-baby-swaddle-australia/ | ✅ Live |

### Informational Guides (12)

| Page | Path | Cluster | Status |
|------|------|---------|--------|
| How to Choose a Baby Monitor | /guides/how-to-choose-baby-monitor/ | Baby Monitor | ✅ Live |
| WiFi vs Non-WiFi Baby Monitor | /guides/wifi-vs-non-wifi-baby-monitor/ | Baby Monitor | ✅ Live |
| Noise Comparison (Brown vs White vs Pink) | /guides/white-noise-vs-pink-noise-vs-brown-noise/ | White Noise | ✅ Live |
| Does White Noise Help Baby Sleep | /guides/does-white-noise-help-baby-sleep/ | White Noise | ✅ Live |
| White Noise Decibel Safety | /guides/white-noise-decibel-safety-babies/ | White Noise | ✅ Live |
| How to Wean Off White Noise | /guides/how-to-wean-off-white-noise/ | White Noise | ✅ Live |
| How to Swaddle a Baby | /guides/how-to-swaddle-a-baby/ | Swaddle | ✅ Live |
| Swaddle vs Sleep Sack | /guides/swaddle-vs-sleep-sack/ | Swaddle | ✅ Live |
| When to Stop Swaddling | /guides/when-to-stop-swaddling-transition/ | Swaddle | ✅ Live |
| TOG & Temperature Guide | /guides/swaddle-tog-temperature-guide/ | Swaddle | ✅ Live |

### Hub Pages (2)

| Page | Path | Status |
|------|------|--------|
| Best Picks Hub | /best-picks/ | ✅ Live — content expanded (3 cards + intro) |
| Guides Hub | /guides/ | ✅ Live |

### Site Pages (5)

| Page | Path | Status |
|------|------|--------|
| Homepage | / | ✅ Live |
| About | /about/ | ✅ Live |
| Contact | /contact/ | ✅ Live |
| Privacy Policy | /privacy-policy/ | ✅ Live |
| Affiliate Disclosure | /affiliate-disclosure/ | ✅ Live |

---

### Full Page Inventory (24 HTML files)

**3 Product Pillars:** Best Baby Monitor (1,855w), Best Baby Swaddle (2,331w), Best White Noise Machine (2,357w)
**12 Informational Guides:** 5 Monitor cluster, 4 White Noise cluster, 4 Swaddle cluster
**2 Hub Pages:** /guides/ (517w), /best-picks/ (285w)
**5 Site Pages:** Homepage (1,584w), About (430w), Contact (224w), Privacy Policy (619w), Affiliate Disclosure (505w)
**1 Utility:** Google Search Console verification file
**23 public-facing pages** total

---

## 4. Internal Link Matrix

Shows how many links each guide sends TO the pillar page:

### Baby Monitor Cluster

| Guide | Links to Pillar | Notes |
|-------|:---------------:|-------|
| How to Choose a Baby Monitor | 4 | ✅ Within 3-6 range |
| WiFi vs Non-WiFi | 4 | ✅ Within 3-6 range (was 9, optimized down) |

### White Noise Cluster

| Guide | Links to Pillar | Notes |
|-------|:---------------:|-------|
| Noise Comparison | 6 | ✅ Within 3-6 range |
| Does White Noise Help | 5 | ✅ |
| Decibel Safety | 5 | ✅ |
| How to Wean | 5 | ✅ |

### Swaddle Cluster

| Guide | Links to Pillar | Notes |
|-------|:---------------:|-------|
| How to Swaddle a Baby | 2 | ✅ Linked from nav + CTA section |
| Swaddle vs Sleep Sack | 3 | ✅ Linked from nav, body, and CTA section |
| When to Stop Swaddling | 2 | ✅ Linked from nav + CTA section |
| TOG & Temperature Guide | 3 | ✅ Linked from nav, body, and CTA section |

**Rule:** All guides within a cluster must link to their pillar page 3-6 times. Swaddle guides are linked from nav (global — 2 links per page) + body/CTA sections.

---

## 5. Schema Inventory (Per Page)

| Page | Article | FAQPage | Product | AggregateRating | Review | BreadcrumbList | WebPage |
|------|:-------:|:-------:|:-------:|:---------------:|:-----:|:--------------:|:-------:|
| Homepage | — | — | — | — | — | — | ✅ |
| About | — | — | — | — | — | — | ✅ |
| Contact | — | — | — | — | — | — | ✅ |
| Best Picks Hub | — | — | — | — | — | ✅ | ✅ |
| Guides Hub | — | — | — | — | — | ✅ | ✅ |
| Monitor Pillar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| How to Choose Monitor | ✅ | ✅ | — | — | — | ✅ | ✅ |
| WiFi vs Non-WiFi | ✅ | ✅ | — | — | — | ✅ | ✅ |
| White Noise Pillar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Noise Comparison | ✅ | ✅ | — | — | — | ✅ | ✅ |
| Does White Noise Help | ✅ | ✅ | — | — | — | ✅ | ✅ |
| Decibel Safety | ✅ | ✅ | — | — | — | ✅ | ✅ |
| How to Wean | ✅ | ✅ | — | — | — | ✅ | ✅ |
| Swaddle Pillar | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| How to Swaddle | ✅ | ✅ | — | — | — | ✅ | ✅ |
| Swaddle vs Sleep Sack | ✅ | ✅ | — | — | — | ✅ | ✅ |
| When to Stop Swaddling | ✅ | ✅ | — | — | — | ✅ | ✅ |
| TOG & Temperature Guide | ✅ | ✅ | — | — | — | ✅ | ✅ |

---

## 6. Image Inventory

| Image | Page | Width | Format | Size | Alt Text |
|-------|------|:-----:|:------:|:----:|----------|
| whitenoise-hatch-rest2.webp | White Noise Pillar | 800 | WebP | — | Hatch Rest 2 — smart white noise machine |
| whitenoise-dreamegg-d1.webp | White Noise Pillar | 800 | WebP | — | Dreamegg D1 Classic — white noise machine |
| whitenoise-welcare-sleeptight.webp | White Noise Pillar | 800 | WebP | — | Welcare Sleep-Tight — portable white noise |
| whitenoise-ergopouch-driftaway.webp | White Noise Pillar | 800 | WebP | — | ergoPouch Drift Away — portable white noise |
| whitenoise-kyro.webp | White Noise Pillar | 800 | WebP | — | Kyro — white noise machine |
| whitenoise-nooie-sound.webp | White Noise Pillar | 800 | WebP | — | Nooie Sound — white noise machine |
| guide-noise-colors.webp | Noise Comparison | 800×450 | WebP | — | Brown vs white vs pink noise comparison |
| guide-does-it-help.webp | Does White Noise Help | 800×500 | WebP | — | Peaceful sleeping baby — does white noise help |
| guide-decibel-safety.webp | Decibel Safety | 800×600 | WebP | — | Safe nursery setup — decibel safety guide |
| guide-wean-white-noise.webp | How to Wean | 800×501 | WebP | — | Baby sleeping peacefully — weaning off white noise |
| emma-avatar.webp | All content pages | 400×400 | WebP | 11.7 KB | Emma — founder of Emma's Sleep Advice |
| logo-header.svg | All pages | — | SVG | — | Emma's Sleep Advice |

**Total image weight:** ~160 KB across all pages (estimated).

---

## 7. GSC Performance (90 days: Mar 11 — Jun 9)

| Page | Impressions | Clicks | Avg Position |
|------|:-----------:|:------:|:------------:|
| Homepage | 26 | 4 | 1.0 |
| Best Baby Monitor pillar | 40 | 3 | 25.0 |
| Guides Hub | 25 | 2 | 2.0 |
| White Noise pillar | 17 | 2 | 11.4 |
| How to Wean | 18 | 0 | 8.7 |
| Does White Noise Help | 15 | 0 | 11.9 |
| White Noise vs Pink vs Brown | 13 | 0 | 20.8 |
| Swaddle vs Sleep Sack | 10 | 1 | 5.1 |
| How to Choose Baby Monitor | 7 | 1 | 7.3 |
| How to Swaddle | 5 | 0 | 9.6 |
| How to Set Up Baby Monitor | 5 | 0 | 12.0 |
| Are Baby Monitors Worth It | 5 | 0 | 7.0 |
| When to Stop Swaddling | 5 | 0 | 7.6 |
| WiFi vs Non-WiFi | 5 | 0 | 18.2 |
| When to Stop Using Baby Monitor | 4 | 0 | 22.8 |
| Best Baby Swaddle pillar | 5 | 1 | 3.0 |
| Swaddle TOG Guide | 6 | 0 | 4.8 |
| Decibel Safety | 0 | 0 | — ❌ (not discovered yet) |

**Total (from search analytics): 17 pages with data, 0 queries with clicks** (90d view changed since last pull).

**5 pages are in Google index** (shown in site: search) — /guides/are-baby-monitors-worth-it/, /guides/how-to-choose-baby-monitor/, /guides/how-to-set-up-baby-monitor/, /guides/when-to-stop-using-baby-monitor/, /guides/wifi-vs-non-wifi-baby-monitor/ — but GSC dashboard still lists them as "Discovered - currently not indexed" (reporting delay).

---

## 8. Technical Status

| Item | Status | Notes |
|------|--------|-------|
| robots.txt | ✅ | Allow all + Sitemap link |
| sitemap.xml | ✅ | All pages listed with priorities |
| llms.txt | ✅ | For GEO/AI search visibility |
| SSL/HTTPS | ✅ | Cloudflare Full mode |
| Mobile responsive | ✅ | Hamburger menu, breakpoints |
| Canonical tags | ✅ | Self-referencing on all pages |
| Navigation: crawlable | ✅ | CSS-only hover dropdown |
| Image alt text | ✅ | All images descriptive |
| Images: WebP format | ✅ | All images converted |
| Author bio (E-E-A-T) | ✅ | Emma on all content pages |
| Red Nose Australia links | ✅ | All guides link to rednose.org.au |
| OG tags | ✅ | All present, no duplicates |
| Twitter cards | ✅ | summary_large_image on all pages |

---

## 9. Design System Reference

| Element | Value |
|---------|-------|
| Primary color | Purple #5B4B8A |
| Accent color | Pink #E8758A |
| Font | Poppins (all weights) |
| Max content width | 1200px |
| Card border-radius | 12px |
| Button border-radius | 25px (pill shape) |
| Feature image | 800px wide, WebP, max-height:400px, object-fit:contain |
| Guide image | 800px wide, WebP, q60-80 |
| Avatar | 400×400, circular, WebP, 11.7 KB |
| Navigation | Sticky, CSS-only hover dropdown |
| No emojis/icons in content | Clean text only |
| No "coming soon" visible | Don't link to non-existent pages |

---

## 10. Affiliate Programs Status

| Program | Status | Notes |
|---------|--------|-------|
| Amazon AU Associates | ❌ Not yet applied | Need to register — highest priority for monetization |
| Baby Bunting | ❌ Not yet applied | Via Partnerize network |
| Love to Dream | ❌ Not yet applied | Direct affiliate program |
| Chemist Warehouse | ❌ Not yet applied | Via Commission Factory |

**Note:** No affiliate links are active on the site yet. All product mentions are currently generic recommendations.

---

## 11. Content Ideas Backlog

Proposed future content, not yet prioritized:

| Topic | Type | Cluster | Notes |
|-------|------|---------|-------|
| Best Baby Swaddle Australia | Pillar page | Swaddle | **Highest priority** — 2 guides exist but need pillar to link to |
| Room Temperature for Baby Sleep | Guide | General | TOG ratings, Australian seasons |
| 4-Month Sleep Regression Guide | Guide | General | Existing draft may need refresh |
| Baby Nap Schedules by Age | Guide | General | Newborn → 12 months |
| Best Baby Sleep Sacks Australia | Pillar page | Swaddle/Sleep Sack | Could complement swaddle cluster |
| How to Set Up Baby Monitor | Guide | Baby Monitor | Informational, fills out monitor cluster |
| When to Stop Using Baby Monitor | Guide | Baby Monitor | Another monitor cluster fill |
| Are Baby Monitors Worth It | Guide | Baby Monitor | Informational/commercial hybrid |

---

## 12. Optimization History

### 2026-06-09 — New Guide: 4-Month Sleep Regression Australia 🆕

New informational guide with no feature image yet (waiting for Kuya's desktop agent for Unsplash sourcing).

| Detail | Value |
|--------|-------|
| URL | `/guides/4-month-sleep-regression-australia/` |
| Body words | ~1,480 |
| H2 sections | 7 (What Is It, Signs, Duration, Why It Happens, Survival Tips, Safe Sleep, When to See GP) |
| FAQ Schema | 5 questions (duration, signs, when it starts, do all babies, when to see GP) |
| Internal links | 1 back-link to White Noise pillar (CTA + bottom) + nav link |
| Red Nose citations | 3 (safe sleep section, tip box, links to rednose.org.au) |
| Unique angle | Red Nose Australia safe sleep guidelines during regression — zero competitors cover this |
| Guides hub | Added "Sleep Regression" section with card |
| Sitemap | Added with priority 0.7 |
| SERP data source | Desktop agent SERP analysis (sleep-regression-serps.md reference) |
| Google Trends validation | "4 month sleep regression" avg 62/100 AU, June-August peak demand |

### 2026-06-11 — New Guide: Sleep Training Methods (Australia)

New informational guide targeting "sleep training methods australia" keyword — fills the biggest Koray entity gap in Sleep Techniques.

| Detail | Value |
|--------|-------|
| URL | `/guides/sleep-training-methods-australia/` |
| Body words | ~1,480 |
| H2 sections | 8 (What Is It, Ferber, Chair Method, Pick-Up-Put-Down, Fading, No-Cry, How to Choose, FAQs) |
| Unique angle | Australian GP sleep training recommendations + Red Nose safe sleep |
| FAQ Schema | 6 questions (age to start, Ferber vs chair method, fading overview, most effective, hours to check, starting older babies) |
| Guides hub | Added "Sleep Training" section |
| Sitemap | Added with priority 0.7 |
| Koray framework gap | Sleep Techniques — Entity 3 (was ❌ Not covered, now ✅ Covered) |

### 2026-06-12 — Full Topical Mapping Phase 0 Complete

Completed Phase 0 data gathering for entire site. 27 content gaps identified, organized by entity, validated with 3 skills (Mastery Workflow + Google SEO Docs + Koray Framework).

**Data sources used:**
- Ahrefs CSVs: 8 competitors (raisingchildren, rednose, pregnancybirthbaby, tresillian, betterhealth, karitane, ngala, thesleepteacher)
- Desktop agent: Manual audit, Google Trends, SERP checks
- Koray entity-attribute framework: 6 entities, QDP/QDH/QDS classification
- Google SEO Docs: Technical compliance check

**Key outputs:**
- `topical-map.md` — complete source of truth with all tiers, entities, schedule
- `topical-mapping-checklist.md` — step-by-step process
- Tier 1 (4 topics) + Tier 2 (3 topics) = **7 content ready to write** — all validated
- Tier 3 (3 topics) needed Trends tests → Cot Mattress ✅ promoted to Tier 2, Toddler Sleep + Nap Transitions pending
- Tier 4 (13 side quests) — low-effort QDH/QDS to add as sections
- 6-month sleep regression: validated Trends avg 6 → **QDH** (add to 4-month regression guide, not standalone)
- Baby sleeping bags guide: SERP showed 50% camping intent → refined keyword to "baby sleeping bags australia"
- All topics passed: entity check ✅, QDP classification ✅, siteFocusScore ✅, template match ✅, Google rules ✅

**Repo files added:**
- `topical-map.md` — source of truth (v2, 18592c7)
- `topical-mapping-checklist.md` — step-by-step checklist

Expanded from 6 to 9 products based on Amazon AU Best Seller + Baby Bunting research (via Desktop agent). Filled 2 key gaps: budget under $40 and plush toy category.

| New Product | Price | Where | Gap Filled |
|-------------|:-----:|-------|------------|
| Fisher-Price Soothe & Snuggle Otter | AU$36.79 | Baby Bunting | Plush toy, budget under $40 |
| My Baby Sound Spa On The Go | AU$29.95 | Baby Bunting | Cheapest option, portable clip-on |
| Taf Toys Portable Sound Machine | AU$45-55 | Amazon AU | Cry sensor (unique feature) |

**Updated:** H1 (6→9), At-a-Glance table, Full Comparison Table (3 new columns), Budget Tiers (new "Under $40" tier + adjusted pricing), Final Verdict table.
**Updated (2nd pass):** Meta title, meta description, OG title, OG description, Twitter title, Twitter description, Article schema (headline, description, dateModified), Product schema (description, reviewCount→9, +3 new reviews). All now reflect 9 products.

**Search intent check:** Does the page cover all budgets now? ✅ Yes — from AU$29.95 to AU$130. Does it answer "which one should I buy?" ✅ Yes — 9 options across budget/portable/premium with clear verdicts.

Major milestone. All 23 pages confirmed "Submitted and indexed" via GSC URL Inspection API (June 9, 2026). Confirmed via `site:emmassleepadvice.com` search.

Previously unindexed pages that are now indexed:
- `/about/`, `/contact/`, `/privacy-policy/`, `/affiliate-disclosure/`, `/best-picks/`, `/guides/white-noise-decibel-safety-babies/`
- 5 baby monitor guides that showed "Discovered - currently not indexed" are also indexed

**Note:** GSC dashboard may still show "Discovered - currently not indexed" for up to 48h — this is a reporting delay. URL Inspection API is the authoritative real-time source.

### 2026-06-09 — Content Added to /best-picks/

| Page | Fix |
|------|-----|
| /best-picks/ | Replaced thin intro with substantial section: personal testing process, Red Nose safety guidelines, Australian availability, no-sponsor policy. Body text 258w → 285w. Goal: make page indexable. |

### 2026-06-09 — Navigation Standardization (4 Pages)

| Page | Fix |
|------|-----|
| /about/ | Replaced old flat nav with proper dropdown header (Best Picks + Guides dropdowns), removed emoji from nav |
| /contact/ | Replaced entire page nav CSS + HTML with standardized header, updated footer to match site |
| /privacy-policy/ | Same as contact — new nav, new footer, removed emojis |
| /affiliate-disclosure/ | Same as above — new nav, new footer, no emojis |

### 2026-06-08 — Stage 4 On-Page Fixes

| Page | Fix |
|------|-----|
| White Noise pillar | Title trimmed (78→71 chars), OG image added |
| Does White Noise Help | Title trimmed (72→62 chars), duplicate OG tags removed |
| How to Wean | Duplicate OG tags removed |

### 2026-06-04 — White Noise Cluster Initial Optimizations

| Page | Fix |
|------|-----|
| White Noise pillar | Full schema (Product, AggregateRating, Review, FAQ, BreadcrumbList) |
| White Noise pillar | Internal links from 4 guides (5-6 each) |
| Noise Comparison | Full expansion: brown noise section, Red Nose H2, FAQ 3→5, table to top |
| Noise Comparison | Title/meta trimmed, schema added |
| Does White Noise Help | Schema + Red Nose external links |
| Decibel Safety | Schema + 3x Red Nose external links |
| How to Wean | Schema + H1 + Red Nose external links |

### 2026-06-03 — Site-Wide Technical Setup

- robots.txt, llms.txt, sitemap.xml created
- Canonical tags, H1 tags, image alt text, author bio implemented
- Internal link structure set: guides→pillar at 3-6 links per guide

### 2026-05-31 to 2026-06-02 — Baby Monitor Cluster

| Page | Fix |
|------|-----|
| Best Baby Monitor pillar | Full schema + comparison table + 6 products |
| How to Choose guide | Internal links optimized 7→4 |
| WiFi vs Non-WiFi guide | Internal links optimized 9→4 |
| Guides Hub | Created with category cards |
| Best Picks Hub | Created with category cards |
| Navigation | CSS-only dropdown (crawlable) |
| All pages | OG tags + Twitter cards + BreadcrumbList |

### 2026-06-08 — Baby Monitor Cluster Audit

| Page | Cross-links to other guides | Note |
|------|:--------------------------:|------|
| Best Baby Monitor pillar | N/A (pillar) | Has FAQPage + Product + AggregateRating schemas |
| How to Choose | ✅ → WiFi vs Non-WiFi, How to Set Up, Are Monitors Worth It, When to Stop | Complete — 4 other guides linked |
| WiFi vs Non-WiFi | ✅ → How to Choose | Links to 1 other guide |
| When to Stop | ✅ → Are Monitors Worth It, How to Choose | Links to 2 other guides |
| Are Monitors Worth It | ✅ → When to Stop, How to Choose, WiFi vs Non-WiFi | Most connected — 3 other guides linked |
| How to Set Up | ✅ → WiFi vs Non-WiFi, How to Choose, When to Stop | Links to 3 other guides |

**No technical issues found:** All pages have Article schema, FAQPage schema (3 Qs each), OG tags, Twitter cards, canonicals, Red Nose citations, BreadcrumbList. No duplicate tags, no broken links.

**No optimization needed** — cluster is technically complete. Possible future: expand FAQs 3→5 per guide, add Red Nose external links (same pattern as white noise).

### 2026-06-08 — GSC Permanent Auth

- OAuth app published to **Production** (no more 7-day token expiry)
- New Web application client created (replaced Desktop type)
- Redirect URI: `https://emmassleepadvice.com/gsc-callback`
- Client ID: `37241543550-bcv6uifi37cjv009ks4b46nvkh755hlh.apps.googleusercontent.com`
- **Permanent refresh token** — no expiration!
- Connected via URL property: `https://emmassleepadvice.com/` (sc-domain not available for this property)
- Credentials saved at: `/opt/data/profiles/agentnyroh/scripts/gsc_credentials.json` + `gsc_token.json`

### 2026-06-08 — GSC First Full Data Pull

- **90-day data** pulled: Mar 10 → Jun 8, 2026
- **10 unique queries**, **9 pages with data**, **11 total clicks**
- Pages with clicks: Homepage (4), Monitor Pillar (3), Guides Hub (2), White Noise Pillar (1), Swaddle vs Sleep Sack (1)
- Top query: "best baby monitor australia" — 4 imps, pos 73.0
- **Bookshelfmemories.com removed** from GSC — wala kaming access
- GSC script hardcoded to `https://emmassleepadvice.com/` only

- Homepage design: purple/pink palette, sticky nav, age grid, Editor's Choice, FAQ accordion
- About page, Contact page
- Images: all WebP, descriptive alt text, lazy loading
- Mobile responsive: hamburger menu, breakpoints

---

## 13. What's NOT Yet Done

| Task | Priority | Notes |
|------|:--------:|-------|
| Amazon AU affiliate account | **High** | Need to apply — no affiliate links active yet |
| All 23 pages indexed | **Done** | Confirmed via API + site:search June 9. See section 12. |
| Google Analytics | **Done** | GA4 set up Jun 9 — G-L1KN4L71L9 on all 24 pages |
| Content: Sleep Regression Guide | **Done** | Published June 9, 2026. See section 12. |
| Content: White Noise Pillar Expansion | **Done** | Expanded 6→9 products June 9. See section 12. |
| Content: Room Temperature Guide | **Medium** | Google Trends avg 4, peak 100 — AU winter NOW (Jun-Aug) |
| Content: Baby Sleep Training Guide | **Done** | Published June 11, 2026. See section 12. |
| Content: Baby Teething & Sleep Guide | **Medium** | Google Trends avg 79, peak 100 — year-round, July peak |
| Content: Witching Hour Guide | Low | Trends avg 17, peak 85 — "what is witching hour" rising |
| Content: Dream Feeding Guide | Low | Trends avg 2, peak 100 — niche but real spikes |
| Content: Nap Schedules Guide | Low | New content idea |
| Stage 5: Off-Page SEO | Low | Too early for link building (site is new) |

---

## 14. Optimization Rules (Over-Optimization Prevention)

| 1. **One optimization pass per page per month** — unless critical bug (broken link, missing schema)
2. **Meta title:** Only trim if over 71 chars. Do NOT change content/topic.
3. **OG tags:** Only fix if duplicate or missing. Do NOT change content.
4. **Internal links:** Already 3-6 per guide. Do NOT add more.
5. **External links:** All guides have Red Nose. Do NOT add more.
6. **Schema:** Present on all pages. Do NOT add more types unless for new content.
7. **Content text:** Do NOT re-optimize unless GSC shows >5 position drop.
8. **Check this file FIRST** before any optimization suggestion.

## 15. Agent Memory Archive

Full Hermes agent memory + user profile backup saved to [MEMORY-ARCHIVE.md](./MEMORY-ARCHIVE.md) (June 11, 2026). Memory was cleared to free up space — this is the permanent reference.

## 16. Tier 3 Progress

Last updated: 2026-06-12

| Topic | Type | Trends | SERP | Status |
|:------|:----:|:------:|:----:|:------:|
| Best Baby Cot Mattress AU | QDP | avg 80 ✅ | 2/10 AU, vacuum ✅ | **Promoted to Tier 2 (#8)** |
| Toddler Sleep Guide | QDP (likely) | ❌ Pending | ❌ Pending | Waiting for Desktop agent Trends test |
| Nap Transitions Guide | QDH (likely) | ❌ Pending | ❌ Pending | Waiting for Toddler Sleep results first |

**Next action:** kuya relays Toddler Sleep Trends task to Desktop agent. 1 cluster (toddler sleep + toddler bedtime AU). If passes (avg 10+), SERP check next. Nap Transitions follows in separate session.

## 17. Required Skills for Every SEO Task

**Mandatory loading order for every SEO task (content, optimization, audit, etc.):**
1. `seo-mastery-workflow` — base SEO workflow (stages, checklists, audit format)
2. `google-seo-docs-master` — Google's official Search docs (rules, policies, technical)
3. `koray-topical-authority-framework` — Koray's Topical Authority framework (QDP/QDH/QDS, entity mapping, siteFocusScore)

These three are complementary layers, not alternatives:
- Mastery Workflow = **the how** (process)
- Google Docs = **the rules** (official policies)
- Koray Framework = **the what and why** (content structure for topical authority)
