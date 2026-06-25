# Inline CSS Requirement — emmassleepadvice.com

## Why Inline CSS Is Required

The site at emmassleepadvice.com is hosted on Cloudflare + GitHub Pages. Unlike a traditional web server, this setup has limitations:

- **`/style.css` returns 404.** There is no external stylesheet file. All CSS is inlined in each page's `<style>` block inside `<head>`.
- **`/js/include.js` returns 404.** Nav and footer are NOT loaded from include scripts. Every page has the full nav `<header>` and `<footer>` HTML inline.

## How to Get the Correct CSS

When building a new page, NEVER add `<link rel="stylesheet" href="/style.css">`. Instead:

1. Clone the repo to /tmp/
2. Read an existing guide's `<style>` block (e.g. guides/does-white-noise-help-baby-sleep/index.html)
3. Copy the entire `<style>...</style>` block, including the Google Fonts import
4. Also copy the `<header class="header">...</header>` and `<footer>...</footer>` blocks
5. Add any guide-specific CSS needed (author-bio, cta-box, faq-item styles)
6. Insert them inline in the new page

## What the Inline CSS Contains

The full inline CSS includes:
- Variables (--primary: #5B4B8A, --accent: #E8758A)
- Container layout (.container, max-width 960px)
- Header and nav with dropdowns
- Guides hero section
- Guide cards grid (guide-cards, 2-column)
- Guide page content styles (h1, h2, h3, ul, ol, toc)
- Author bio
- CTA box
- FAQ items
- Affiliate disclosure
- Footer
- Mobile responsiveness (@media queries)

## Verification Checklist

Before pushing any new page:
- [ ] `<link rel="stylesheet" href="/style.css">` is NOT present
- [ ] `<script src="/js/include.js">` is NOT present
- [ ] `<style>...</style>` with full CSS IS present inside `<head>`
- [ ] `<header class="header">...</header>` IS present
- [ ] `<footer>...</footer>` IS present
- [ ] Use `curl -sI https://emmassleepadvice.com/style.css` to double-check: expect 404
