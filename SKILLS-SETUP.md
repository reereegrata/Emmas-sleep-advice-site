# Skills Setup — Desktop Agent

> Which Hermes skills to install and how. Your Desktop agent needs these to match the Telegram agent's workflow.

---

## Mandatory (Install First — Used on Every Task)

These 3 skills are loaded in order for EVERY SEO task. They are complementary layers:

```bash
hermes skills install seo-mastery-workflow
hermes skills install google-seo-docs-master
hermes skills install koray-topical-authority-framework
```

| Skill | What It Provides | Why Mandatory |
|-------|-----------------|---------------|
| **seo-mastery-workflow** | 7-stage SEO cycle, checklists, audit format, post-push deployment verification | The process (how to do SEO) |
| **google-seo-docs-master** | Complete Google Search documentation — crawling, indexing, ranking, penalties, E-E-A-T | The rules (Google's official policies) |
| **koray-topical-authority-framework** | Koray's Topical Authority framework — QDP/QDH/QDS, entity-attribute mapping, siteFocusScore, content structure for topical authority | The what and why (content structure) |

**Loading order (always):**
1. seo-mastery-workflow
2. google-seo-docs-master
3. koray-topical-authority-framework

These are on the Hermes skills hub. If `hermes skills install` can't find them, search first:
```bash
hermes skills search "seo mastery"
hermes skills search "google seo"
hermes skills search "koray"
```

---

## Useful (Install When Needed)

```bash
hermes skills install on-page-seo               # Meta tags, schema, on-page optimization
hermes skills install seo-site-audit-mastery    # Full 3-part SEO site audit
hermes skills install seo-keyword-research-mastery  # Keyword research pipeline
hermes skills install content-optimization      # Content optimization workflow
```

---

## Image Tools (Desktop Agent Advantage)

Your Desktop agent can do things the Telegram agent CANNOT:

- **Unsplash** — search and download images directly (browser)
- **Canva** — create/edit feature images with text overlays
- **Manual SERP browsing** — inspect competitor images and layouts

You DON'T need to install special Hermes skills for image work — use your browser.

See `docs/unsplash-sourcing.md` for the image sourcing workflow.

---

## Emma-Specific Skills (Already in Repo)

These are NOT installable from the hub — they're custom to Emma's site. You already have them in the `docs/` directory:

- **emmas-site-guide-building** — `docs/emmas-site-guide-building.md` (the main umbrella skill)
- **pillar-page-workflow** — `docs/pillar-page-workflow.md`
- **ai-optimized-content-structure** — `docs/ai-optimized-content-structure.md`

No install needed — just read the markdown files directly from the cloned repo.

---

## Verification

After installing all 3 mandatory skills, test:
```bash
hermes skills list | grep -E "seo-mastery|google-seo-docs|koray-topical"
```
Should show all 3 as installed.
