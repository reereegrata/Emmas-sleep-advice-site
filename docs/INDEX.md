# Emma's Sleep Advice — Documentation Index

> Start here. This tells you which file to read for which task.

---

## First-Time Setup (Read Once)

| Order | File | What It Is |
|:-----:|------|-------------|
| 1 | [../ONBOARD.md](../ONBOARD.md) | Full site identity, current state, mandatory rules, setup instructions |
| 2 | [../STATUS.md](../STATUS.md) | Source of truth — everything about the site right now |
| 3 | [emmas-site-guide-building.md](emmas-site-guide-building.md) | The 14-step workflow for building ANY page on Emma's site |

---

## By Task — Which Doc to Read

### Writing a New Informational Guide
1. [ai-optimized-content-structure.md](ai-optimized-content-structure.md) — Content template (first 2 sentences, tables, FAQ schema)
2. [google-trends-workflow.md](google-trends-workflow.md) — Validate demand with Google Trends before writing
3. [google-trends-content-discovery.md](google-trends-content-discovery.md) — Discover new topic ideas from Trends
4. [google-trends-rate-limit-pitfall.md](google-trends-rate-limit-pitfall.md) — Avoid getting blocked by Trends
5. [inline-css-requirement.md](inline-css-requirement.md) — CRITICAL: never reference external CSS/JS (they 404)
6. [line-number-artifact-trap.md](line-number-artifact-trap.md) — Avoid pipe artifacts in HTML files
7. [container-nesting-bug.md](container-nesting-bug.md) — Fix broken guide hub cards

### Writing a Product Review Pillar ("Best X Australia")
1. [pillar-page-workflow.md](pillar-page-workflow.md) — 7-phase pillar pipeline (build → images → verify → audit → publish)
2. [product-pillar-expansion.md](product-pillar-expansion.md) — Adding new products to existing pillars
3. [pillar-audit-checklist.py](pillar-audit-checklist.py) — Run before publishing (must score 100/100)
4. [ai-optimized-content-structure.md](ai-optimized-content-structure.md) — Same content template applies

### Sourcing Images
1. [unsplash-sourcing.md](unsplash-sourcing.md) — How Kuya's Desktop agent sources images from Unsplash

### Desktop Agent SERP Tasks
1. [serp-task-prompt-template.md](serp-task-prompt-template.md) — Template for sending structured SERP tasks to Kuya's Desktop agent

### Skills Setup & Image Workflow
1. [../SKILLS-SETUP.md](../SKILLS-SETUP.md) — Which Hermes skills to install + exact commands
2. [IMAGE-WORKFLOW.md](IMAGE-WORKFLOW.md) — Who handles images and how (Desktop vs Telegram agent tools)

### Homepage Updates
1. [homepage-latest-section.md](homepage-latest-section.md) — Updating the "Latest Guides" section
2. [homepage-start-here-section.md](homepage-start-here-section.md) — The "Start Here" section pattern

### Deployment & Git
1. [github-ssh.md](github-ssh.md) — Git auth setup (HTTPS PAT or SSH deploy key)
2. [../ONBOARD.md](../ONBOARD.md) Section 7 — Deploy process

### Analytics & GSC
1. [google-analytics-4-setup.md](google-analytics-4-setup.md) — GA4 tracking setup
2. [../GSC/README.md](../GSC/README.md) (in tar.gz) — GSC data pulling

### Post-Publish
1. [status-md-pattern.md](status-md-pattern.md) — How to update STATUS.md after changes
2. [sleep-regression-serps.md](sleep-regression-serps.md) — Reference: SERP analysis for the 4-month regression guide

---

## Critical Rules (Never Skip)

- **STATUS.md first** — before ANY change, read STATUS.md
- **Heading approval first** — present H1+H2s to Kuya, get approval, THEN write body
- **Inline CSS only** — never reference `/style.css` or `/js/include.js`
- **AU English** — mum (not mom), favourite (not favorite), centre (not center)
- **Red Nose Australia** — primary external citation, max 1-3 per guide
- **Internal links** — 3-6 per guide → pillar, relevance-first
- **Pre-push review** — verify with curl BEFORE telling Kuya it's live
- **One pass per page per month** — unless critical bug

---

## File List (All 19 docs)

| File | Purpose |
|------|---------|
| [emmas-site-guide-building.md](emmas-site-guide-building.md) | Complete 14-step site building workflow (the umbrella skill) |
| [pillar-page-workflow.md](pillar-page-workflow.md) | 7-phase pillar page pipeline |
| [product-pillar-expansion.md](product-pillar-expansion.md) | Adding products to existing pillars |
| [ai-optimized-content-structure.md](ai-optimized-content-structure.md) | Content template for Google + all AI engines |
| [inline-css-requirement.md](inline-css-requirement.md) | Why external CSS/JS is forbidden |
| [google-trends-workflow.md](google-trends-workflow.md) | Step-by-step Google Trends validation |
| [google-trends-content-discovery.md](google-trends-content-discovery.md) | Finding content ideas from Trends |
| [google-trends-rate-limit-pitfall.md](google-trends-rate-limit-pitfall.md) | Avoiding Trends IP bans |
| [google-analytics-4-setup.md](google-analytics-4-setup.md) | GA4 tracking implementation |
| [status-md-pattern.md](status-md-pattern.md) | How to update STATUS.md |
| [github-ssh.md](github-ssh.md) | Git authentication methods |
| [unsplash-sourcing.md](unsplash-sourcing.md) | Image sourcing workflow |
| [homepage-latest-section.md](homepage-latest-section.md) | Homepage updates |
| [homepage-start-here-section.md](homepage-start-here-section.md) | Homepage patterns |
| [sleep-regression-serps.md](sleep-regression-serps.md) | SERP analysis reference |
| [line-number-artifact-trap.md](line-number-artifact-trap.md) | Bug: pipe artifacts in HTML |
| [container-nesting-bug.md](container-nesting-bug.md) | Bug: broken guide hub cards |
| [serp-task-prompt-template.md](serp-task-prompt-template.md) | Desktop agent task template |
| [pillar-audit-checklist.py](pillar-audit-checklist.py) | Automated pillar audit (Python) |
