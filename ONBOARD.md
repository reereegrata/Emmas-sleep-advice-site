# Emma's Sleep Advice — Desktop Agent Onboarding

> **READ THIS FIRST.** This document is everything you need to understand and work on emmassleepadvice.com.
> After reading this, your next step is: clone the GitHub repo + read STATUS.md + read topical-map.md.

---

## 1. Site Identity

| Detail | Value |
|--------|-------|
| Domain | **emmassleepadvice.com** |
| Niche | Baby sleep advice — Australian audience |
| Brand | Emma (personal brand, Australian mum persona) |
| Monetization | Amazon AU Associates (not yet applied), display ads later |
| Colors | Purple #5B4B8A, Pink #E8758A |
| Font | Poppins |
| Tech | Static HTML/CSS (no WordPress, no frameworks) |
| Hosting | GitHub Pages + Cloudflare (CDN, SSL, DNS) |
| GitHub Repo | `reereegrata/Emmas-sleep-advice-site` (PUBLIC) |
| Clone URL | `git@github.com:reereegrata/Emmas-sleep-advice-site.git` (SSH) |
| | `https://github.com/reereegrata/Emmas-sleep-advice-site.git` (HTTPS, read-only) |

---

## 2. Current State (as of June 25, 2026)

- **25 pages indexed** (confirmed via GSC URL Inspection API)
- **Phase 0 complete** — topical mapping done, 27 gaps identified, 6 entities mapped
- **3 product pillars:** Baby Monitor, White Noise Machine, Baby Swaddle
- **15 informational guides** across 4 clusters
- **9 Tier 1+2 topics queued** in topical-map.md (ready to write)
- **June content pause** — no new pages until July 1 (let Google calibrate on 25 pages)
- **Amazon affiliate not yet applied** (Kuya handles this)
- **GEO Score: 69/100** (Good) — all pages in green zone
- **GSC permanent token active** — no expiry, weekly Monday reports via cron

---

## 3. Site Architecture (Silo Structure)

```
Homepage (/)
├── Best Picks Hub (/best-picks/)
│   ├── Best Baby Monitors AU (pillar) + 5 guides
│   ├── Best White Noise Machines AU (pillar) + 4 guides
│   └── Best Baby Swaddles AU (pillar) + 4 guides
├── Guides Hub (/guides/) — all 15 guides listed
├── About (/about/)
├── Contact (/contact/)
├── Privacy Policy (/privacy-policy/)
└── Affiliate Disclosure (/affiliate-disclosure/)
```

**4 Content Clusters:** Baby Monitor (6 pages), White Noise (5 pages), Swaddle (5 pages), General (2 pages)

---

## 4. July Content Schedule (Resume July 1)

From `topical-map.md` — 9 topics validated with Trends + Ahrefs + SERP data:

| Week | Priority | Topic | Score |
|:----:|:--------:|-------|:-----:|
| 1 | **#1** | Baby Sleep Schedule by Age (0-12mo) | 9.5/10 |
| 2 | **#2** | Teething & Baby Sleep | 7/10 |
| 3 | #3 | Baby Sleeping Bags Guide | 8/10 |
| 4 | #4 | Room Temperature + How to Dress Baby | 7.5/10 |
| 5 | #5 | Responsive Settling Techniques (AU) | 7/10 |
| 6-9 | #6-9 | Sleep Sacks, Safe Sleep, Cot Mattress, Toddler Sleep | 6-7.5/10 |

**Schedule rule:** 1 topic per week, 2 uploads max per week. Gather all data FIRST before writing.

---

## 5. Mandatory Rules (Do NOT Skip Any of These)

### 5.1 Always Read STATUS.md First
Before suggesting changes, continuing work, or touching ANY page — read `/repo-docs/STATUS.md`. It is the source of truth.

### 5.2 Heading Architecture Before Full Content
Before writing any article: present the heading structure (H1, H2s, FAQ schema questions) to Kuya for approval. He approves headings BEFORE you write the body. Never skip this step.

### 5.3 The 3-Skill Loading Rule (for SEO tasks)
Every SEO task requires loading these 3 skills in order:
1. `seo-mastery-workflow` — the process (stages, checklists)
2. `google-seo-docs-master` — Google's official rules and policies
3. `koray-topical-authority-framework` — Koray's topical authority structure (QDP/QDH/QDS, entity mapping)

These are complementary layers, not alternatives. If your Hermes Desktop has these skills, load them before any SEO work.

### 5.4 External Link Discipline
- **Red Nose Australia (rednose.org.au) ONLY** as external authoritative source
- Raising Children Network — text-only citations accepted
- Karitane is NOT authoritative (never link to it)
- Max 1-3 external links per guide
- Verify every external link with curl before publishing

### 5.5 Internal Link Philosophy
- 3-6 links per guide pointing TO the cluster pillar page
- Do NOT add homepage links just for link count
- Only link FROM pages with genuine topical connection to the target
- Relevance-first, minimalist approach

### 5.6 Content Workflow
```
Keyword Research → Data Gathering → Heading Architecture → Kuya Approves →
Full Content → QC Check → Kuya Approves Final → Publish + Push
```
- Kuya reviews and approves TWICE per article (headings + final content)
- Draft locally. Push ONLY when Kuya says "upload it" or "push"
- After pushing, verify with curl and a cache-busting query param before declaring live

### 5.7 AI-Optimized Content Structure
First 2 sentences = direct answer with number + source + date. Then expand. Use tables, FAQ schema, external citations, freshness dates. Works for Google + ChatGPT + Meta AI + Perplexity + Gemini simultaneously.

### 5.8 Optimization Trigger Rule
- **Wait 1 month** before touching underperforming new pages
- Low clicks at 15 days with positions 30-90 are NORMAL (Google calibrating)
- Only re-optimize with clear signal: stuck position, 0 CTR at visible positions, or >5 position drop per GSC

### 5.9 One Optimization Pass Per Page Per Month
Unless it's a critical bug (broken link, missing schema). Check STATUS.md Section 14 for rules.

---

## 6. Your Role as Desktop Agent

The Telegram agent (agentnyroh on Zeabur) handles: content planning, writing, GitHub pushes, GSC monitoring, cron jobs.

**You handle:**
- Google Trends data gathering (one keyword cluster per session, 2 keywords max, use region filter not keyword modifier)
- Ahrefs competitor research (manual via browser)
- SERP analysis (manual Chrome browsing)
- Image sourcing (Unsplash, stock sites)
- Manual browser-based tasks the VPS agent cannot do

**How we collaborate:**
- Kuya acts as bridge between you and the Telegram agent
- Telegram agent provides task prompts for you
- You execute in Chrome/Desktop and report results back via Kuya

---

## 7. Quick Setup (For Your Desktop Agent)

### Clone the Repo
```bash
# Clone (public repo — no auth needed for read)
git clone https://github.com/reereegrata/Emmas-sleep-advice-site.git

# OR with SSH for push access (private key included in this package):
# Copy .ssh/id_ed25519_emma to your ~/.ssh/
# chmod 600 ~/.ssh/id_ed25519_emma
# git clone git@github.com:reereegrata/Emmas-sleep-advice-site.git
```

### Use the SSH Deploy Key (for pushing changes)
The private key is at `.ssh/id_ed25519_emma` in this package. This key has WRITE access to the repo (registered in GitHub deploy keys).

```bash
GIT_SSH_COMMAND="ssh -i /path/to/id_ed25519_emma -o IdentitiesOnly=yes" git push origin main
```

**Security:** This is a sensitive credential. Keep it safe. It is repo-scoped (only works for reereegrata/Emmas-sleep-advice-site).

### GSC Access
The permanent GSC token is at `GSC/gsc_token.json` and credentials at `GSC/gsc_credentials.json`. These give read access to Google Search Console data for `https://emmassleepadvice.com/`. Use `GSC/gsc_pull.py` to pull performance data.

### Deploy Process
```bash
cd Emmas-sleep-advice-site
git add -A
git commit -m "description of changes"
GIT_SSH_COMMAND="ssh -i /path/to/id_ed25519_emma -o IdentitiesOnly=yes" git push origin main
# Site auto-deploys via GitHub Pages — no manual steps needed
```

---

## 8. Key Files Reference

| File | Location | What It Is |
|------|----------|------------|
| **STATUS.md** | `repo-docs/` or repo root | Source of truth — everything about the site |
| **topical-map.md** | `repo-docs/` or repo root | Content roadmap — 27 gaps, 9 queued topics |
| **topical-mapping-checklist.md** | `repo-docs/` or repo root | Step-by-step mapping process |
| **ahrefs-csv-inventory.md** | `repo-docs/` or repo root | Tracking of Ahrefs competitor data |
| **MEMORY-ARCHIVE.md** | `repo-docs/` or repo root | Full agent memory backup |
| **ONBOARD.md** | This file | You're reading it |

---

## 9. Critical Context (Don't Forget These)

- Site is only 1 month old (25 pages). Google is still calibrating. Do not over-optimize.
- Red Nose Australia is our primary external citation (Australian SIDS authority).
- No affiliate links are live yet — Kuya hasn't applied to Amazon AU Associates.
- June content pause is ACTIVE — no new pages until July 1.
- Brand colors and design: purple #5B4B8A, pink #E8758A, Poppins font, no emojis.
- The homepage has 8 sections (hero, age grid, editor's choice, meet Emma, FAQ, latest guides, newsletter, footer).
- All 25 pages have schema (Article, FAQPage, BreadcrumbList; pillar pages have Product + AggregateRating + Review).
- The `guides/` directory uses subdirectories: `/guides/guide-slug/index.html`.

---

## 10. Start Here (Your First Session)

When Kuya says "work on emmassleepadvice.com":

1. **Read this ONBOARD.md** (you're doing this now)
2. **Read repo-docs/STATUS.md** — understand current state
3. **Read repo-docs/topical-map.md** — understand the content plan
4. **Clone the GitHub repo** — `git clone https://github.com/reereegrata/Emmas-sleep-advice-site.git`
5. **Load the 3 SEO skills** if available: seo-mastery-workflow, google-seo-docs-master, koray-topical-authority-framework
6. **Do the task Kuya asked** — following the rules in Section 5

**When in doubt, check STATUS.md first. Never skip the heading-approval step.**
