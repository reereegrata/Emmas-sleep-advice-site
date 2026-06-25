# Image Workflow — Desktop Agent vs Telegram Agent

> Different agents, different tools. This doc explains who does what for images.

---

## Image Specs (Same for Both Agents)

| Spec | Value |
|------|-------|
| Format | WebP (lossy, q60-80) |
| Feature image (pillar) | 800×400px, landscape |
| Guide image | 800px wide, ~450-600px tall |
| Avatar | 400×400px, circular, 11.7KB max |
| Logo | SVG only |
| Alt text | Descriptive, product name included |
| Lazy loading | `loading="lazy"` on all images |
| Max file size per image | ~30KB (target) |

---

## Desktop Agent (Your Strengths)

You have BROWSER access. The Telegram agent does NOT. Use your advantage:

| Task | Tool | How |
|------|------|-----|
| Source new images | **Unsplash** | Search by keyword, download, crop to spec |
| Edit/resize images | **Canva** (free) | 800px wide, export as PNG → convert to WebP |
| Convert to WebP | **Squoosh.app** (browser) | Drag image, adjust quality to 60-80, download |
| Inspect competitor images | **Chrome DevTools** | Right-click → Inspect → check sizes/formats |
| Check existing images on site | **emmassleepadvice.com** | Browse live pages |

**Flow for a new guide image:**
1. Desktop agent searches Unsplash with keyword from Kuya
2. Downloads the best image
3. Crops to 800×450-600px in Canva
4. Converts to WebP via Squoosh (q60-80)
5. Names it `guide-<slug>.webp`
6. Places in `/images/` directory in repo
7. Adds `<img>` tag to guide HTML with `loading="lazy"` and descriptive alt text
8. Commits and pushes

---

## Telegram Agent (VPS Agent — Terminal Only)

**Cannot use browser tools.** Uses command-line alternatives:

| Task | Tool | Command |
|------|------|---------|
| Resize image | ImageMagick | `convert input.png -resize 800x -strip -quality 80 output.webp` |
| Convert to WebP | `cwebp` | `cwebp -q 75 input.png -o output.webp` |
| Check image size | `stat` | `stat -c '%s' file.webp` |
| Check image dimensions | `identify` | `identify file.webp` |

---

## Image Sources by Product

| Product Category | Best Source | Notes |
|-----------------|-------------|-------|
| White noise machines | Amazon AU product images | PPA (Primary Product Alternative — allowed under AU consumer law) |
| Baby monitors | Amazon AU / manufacturer site | Same PPA rule |
| Swaddles | Amazon AU / Love to Dream | Manufacturer images preferred |
| Generic baby/sleep | Unsplash | Free, high-quality, no attribution needed |

---

## Existing Images in Repo

All WebP images are in `/images/` directory. Before adding new images:
1. Check if a suitable image already exists: `ls images/ | grep <keyword>`
2. Reuse before creating new ones — saves bandwidth and load time
3. Full inventory in STATUS.md Section 6
