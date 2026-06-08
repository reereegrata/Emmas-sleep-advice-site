# emmassleepadvice.com — Site Status & Optimization Log

> Central reference for everything on the site.
> Check this FIRST before suggesting changes, adding content, or running optimizations.
> Last updated: 2026-06-08

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

---

## 2. All Pages (9 pages + 2 hubs)

### Product Pillars (2)

| Page | Path | Status |
|------|------|--------|
| Best Baby Monitors | /best-baby-monitor-australia/ | ✅ Live |
| Best White Noise Machines | /best-baby-white-noise-machine-australia/ | ✅ Live |

### Informational Guides (7)

| Page | Path | Cluster | Status |
|------|------|---------|--------|
| How to Choose a Baby Monitor | /guides/how-to-choose-baby-monitor/ | Baby Monitor | ✅ Live |
| WiFi vs Non-WiFi Baby Monitor | /guides/wifi-vs-non-wifi-baby-monitor/ | Baby Monitor | ✅ Live |
| Noise Comparison (Brown vs White vs Pink) | /guides/white-noise-vs-pink-noise-vs-brown-noise/ | White Noise | ✅ Live |
| Does White Noise Help Baby Sleep | /guides/does-white-noise-help-baby-sleep/ | White Noise | ✅ Live |
| White Noise Decibel Safety | /guides/white-noise-decibel-safety-babies/ | White Noise | ✅ Live |
| How to Wean Off White Noise | /guides/how-to-wean-off-white-noise/ | White Noise | ✅ Live |
| Swaddle vs Sleep Sack | /guides/swaddle-vs-sleep-sack/ | Swaddle | ✅ Live |
| When to Stop Swaddling | /guides/when-to-stop-swaddling-transition/ | Swaddle | ✅ Live |

### Hub Pages (2)

| Page | Path | Status |
|------|------|--------|
| Best Picks Hub | /best-picks/ | ✅ Live |
| Guides Hub | /guides/ | ✅ Live |

### Site Pages (4)

| Page | Path | Status |
|------|------|--------|
| Homepage | / | ✅ Live |
| About | /about.html | ✅ Live |
| Contact | /contact.html | ✅ Live |
| Best Picks Hub | /best-picks/ | ✅ Live |

---

## 3. GSC Performance (Last 28 Days: May 11 — Jun 8)

| Page | Impressions | Clicks | Avg Position |
|------|:-----------:|:------:|:------------:|
| Homepage | 19 | 4 | 1.1 |
| Best Baby Monitor pillar | 33 | 3 | 29.5 |
| Guides Hub | 18 | 2 | 2.0 |
| White Noise pillar | 7 | 1 | 5.1 |
| How to Wean | 10 | 0 | 7.0 |
| Does White Noise Help | 9 | 0 | 11.0 |
| Noise Comparison | 7 | 0 | 19.6 |
| Swaddle vs Sleep Sack | 3 | 1 | 4.0 |
| When to Stop Swaddling | 1 | 0 | 5.0 |
| Decibel Safety | 0 | 0 | — |

**Total: 107 impressions, 11 clicks across all pages.**

---

## 4. Technical Status

| Item | Status | Notes |
|------|--------|-------|
| robots.txt | ✅ | Allow all + Sitemap link |
| sitemap.xml | ✅ | All pages listed with priorities |
| llms.txt | ✅ | For GEO/AI search visibility |
| SSL/HTTPS | ✅ | Cloudflare Full mode |
| Mobile responsive | ✅ | Hamburger menu, breakpoints |
| Canonical tags | ✅ | Self-referencing on all pages |
| Schema: Article | ✅ | All content pages |
| Schema: FAQPage | ✅ | All guides with FAQs |
| Schema: Product | ✅ | Pillar pages |
| Schema: AggregateRating | ✅ | Pillar pages |
| Schema: BreadcrumbList | ✅ | All pages |
| Schema: WebPage | ✅ | All pages |
| Author bio (E-E-A-T) | ✅ | Emma on all content pages |
| Image alt text | ✅ | All images descriptive |
| Images: WebP format | ✅ | All images converted |
| Navigation: crawlable | ✅ | CSS-only hover dropdown |
| Red Nose external links | ✅ | All guides link to rednose.org.au |
| Internal links (guides→pillar) | ✅ | 3-6 per guide |
| OG tags | ✅ | All present, no duplicates |
| Twitter cards | ✅ | summary_large_image |

---

## 5. Optimization Log

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

### 2026-05-28 to 2026-05-30 — Homepage & Initial Setup

- Homepage design: purple/pink palette, sticky nav, age grid, Editor's Choice, FAQ accordion
- About page, Contact page
- Images: all WebP, descriptive alt text, lazy loading
- Mobile responsive: hamburger menu, breakpoints

---

## 6. What's NOT Yet Done

| Task | Priority | Notes |
|------|:--------:|-------|
| Amazon AU affiliate account | High | Need to apply — no affiliate links active yet |
| Google Search Console verified | ✅ Done | Connected via OAuth |
| Google Analytics | Medium | Not yet set up |
| New content clusters | Medium | Swaddle cluster has 2 guides, needs pillar page |
| Stage 5: Off-Page SEO | Low | Too early for link building (site is new) |
| Image: White Noise pillar | Medium | Missing feature image (OG image uses product photo instead) |

---

## 7. Optimization Rules (Over-Optimization Prevention)

1. **One optimization pass per page per month** — unless critical bug (broken link, missing schema)
2. **Meta title:** Only trim if over 71 chars. Do NOT change content/topic.
3. **OG tags:** Only fix if duplicate or missing. Do NOT change content.
4. **Internal links:** Already 3-6 per guide. Do NOT add more.
5. **External links:** All guides have Red Nose. Do NOT add more.
6. **Schema:** Present on all pages. Do NOT add more types unless for new content.
7. **Content text:** Do NOT re-optimize unless GSC shows >5 position drop.
8. **Check this file FIRST** before any optimization suggestion.
