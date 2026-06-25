---
name: emmas-site-guide-building
description: "Build pages for Emma's Sleep Advice (emmassleepadvice.com) — both supporting guide pages AND 'Best X Australia' product-review pillar pages. Covers SEO workflow, HTML template, inline-CSS requirement, image optimization, card/nav consistency, HTTPS-PAT push, GA4 setup, Google Trends content discovery, deployment verification, and the pillar-page review/audit/publish pipeline."
version: 2.0.0
hermes:
  tags: [emma, html, seo, content, deployment, google-analytics, google-trends]
---

# Emma's Sleep Advice — Site Building Workflow

Complete workflow for building pages on emmassleepadvice.com. This skill is the
single umbrella for **all** Emma page building. The shared infrastructure below
(git auth, inline-CSS requirement, image pipeline, AU spelling, pre-push gates,
security scan, deployment verification, Google Trends discovery) applies to every
page type.

## Page Types — Route First

There are two page types. Read the shared infrastructure in this file first, then
follow the page-type-specific steps:

- **Guide pages** (informational how-to / what-is / signs-and-symptoms) — follow
  the numbered Workflow steps in this SKILL.md below.
- **Product-review pillar pages** ("Best X Australia 2026" — 6 product cards,
  comparison tables, Product+aggregateRating schema) — follow the dedicated
  pillar pipeline in **`references/pillar-page-workflow.md`** (7 phases: build →
  images → product verification → humanize/trim → audit → publish → post-publish
  cross-reference updates). Run **`scripts/pillar-audit-checklist.py DRAFT-<slug>.html`**
  before publishing any pillar, fixing issues until it scores 100/100.

Both page types share this file's git-auth, inline-CSS, image, spelling,
security, and deployment-verification sections — do not duplicate that logic.

## Prerequisites — Git Auth (CRITICAL: This Is The Most Common Blocker)

- Repo: `github.com/reereegrata/Emmas-sleep-advice-site` (PUBLIC — clone via HTTPS, no auth needed)
- **Git push requires authentication.** The repo remote defaults to SSH (`git@github.com:...`), but this server's SSH keys are NOT registered on GitHub. HTTPS PAT-based push is the only reliable method from this environment.
- **Two working push methods (from most to least reliable):**
  1. **HTTPS with PAT** (preferred — works immediately):
     ```bash
     git remote set-url origin https://reereegrata:<PAT>@github.com/reereegrata/Emmas-sleep-advice-site.git
     ```
     The PAT must be fine-grained with Contents:Write + Pages:Write permissions. Kuya provides this when the old one expires or is lost.
  2. **Deploy key** (`/opt/data/.ssh/id_ed25519_emma`):
     Not yet set up. Requires running `cat /opt/data/.ssh/id_ed25519_emma.pub` → adding as deploy key in GitHub repo settings → git remote stays SSH.

- **KNOWN BLOCKER:** Every push attempt that fails stalls the workflow. If `git push` returns `Permission denied (publickey)` or `Invalid username or token`, do NOT retry endlessly — tell Kuya and ask for a new PAT or help setting up the deploy key.

- **WARNING:** The `/root/.ssh/` directory on Zeabur gets wiped during Hermes version updates (git reset --hard on /opt/hermes destroys it). Do NOT store deploy keys there. Always use `/opt/data/.ssh/` instead.

- Site hosted on **Cloudflare + GitHub Pages** (not locally on a machine)

## Environments
- **`.nojekyll` file MUST exist at repo root.** GitHub Pages runs Jekyll by default and silently skips files with unknown extensions (like `.webp`). If `.nojekyll` is absent, new image files won't deploy even though they're in git. Check: `git ls-files .nojekyll`. If missing, `touch .nojekyll && git add .nojekyll && git commit -m "Add .nojekyll" && git push`. This is no longer optional — verify it before pushing any new image.
- Existing guide template: `guides/wifi-vs-non-wifi-baby-monitor/index.html` (copy for structure)
- Always check which environment you're in before assuming file paths exist. On Zeabur, clone fresh to /tmp/ each session.

## Workflow

### Step 1: Load ALL Relevant Skills (CRITICAL — Do Not Skip One)

Before writing ANY content, load BOTH skills:

1. **`seo-mastery-workflow`** — for the full SEO pipeline (intent classification, keyword mapping, SERP gap analysis)
2. **`emmas-site-guide-building`** (this skill!) — for Emma-specific: inline CSS, template structure, nav patterns, SSH deploy, image workflow, Google Trends workflow

**Do NOT rely on memory alone.** Load both explicitly with `skill_view()`. Kuya will call you out if you miss this step.

### Step 2: SEO Mastery Workflow (MANDATORY)

Run the full pipeline in order. Presenting heading architecture without having run intent classification and keyword mapping is a workflow violation.

1. **Keyword research** — use available data sources in order of reliability:
   - **SERP analysis from Desktop agent** (actual SERP results) → highest priority. Saved as reference files under this skill or seo-mastery-workflow.
   - **Google Trends via pytrends** (no account needed) → for demand validation, PAA extraction, seasonal patterns, related queries
   - **GSC data** → existing query signals from real users
   - **General knowledge** → LAST RESORT only. Flag it as unverified.
2. **SERP gap analysis** — for the target query, check all top 5-10 results for:
   - Are any .au domains ranking? If zero, that's the primary advantage.
   - Which topics appear 0-1 times across competitors? Those go in your headings (our differentiators).
   - Which topics appear 4-5 times? Those are table-stakes; cover briefly.
   - Unique angles: Red Nose Australia citations, AU products (Celsius temps, Love to Dream), internal links to existing Emma's guides (white noise, swaddle).
3. **Google Trends validation** — Before finalising headings, run pytrends queries (see `references/google-trends-workflow.md`). This is MANDATORY, not optional:
   - Compare keyword variants to pick the highest-demand primary keyword
   - Extract PAA questions from top related queries — these become FAQ schema targets
   - Check seasonal patterns (5-year monthly average) to time publication
   - Rising queries add as H2/H3 sections if demand is growing (value 50+)
   - **Combine SERP data + Trends data before writing:** Desktop agent SERP tells you competitor gaps; Google Trends tells you actual searcher questions. Use BOTH.
4. **Desktop agent SERP task** — After Trends identifies a promising topic (avg 20+), send a structured task to Kuya's Desktop agent using `templates/serp-task-prompt-template.md`. The SERP data is the primary input for the competition assessment and heading architecture.
5. **Competition assessment** — After receiving SERP data, evaluate whether the topic is worth pursuing:
   - **Skip if:** Top 5 are all authoritative .au domains (Red Nose, Raising Children Network, Ergopouch, Love to Dream). Domain authority gap is too large to overcome in the near term.
   - **Push if:** Zero or few .au domains in top 10. Competitors are non-AU (e.g. Healthline, Sleep Foundation, parent blogs). Wide open for AU targeting.
   - **Worth noting:** Even moderate Google Trends demand (avg 10-29) can be worth it if competition is weak. Conversely, strong demand (avg 30+) with heavy competition is usually not worth it for a young site.
6. **Intent classification** — run `intent_classifier.py` on all keywords
5. **Keyword-to-page mapping** — every keyword maps to exactly one page. Zero cannibalization.
6. **Heading architecture** based on PAA + competitor H2s + content gaps + Google Trends data + SERP gap analysis
7. **Self-critique the architecture** before presenting. Ask yourself:
   - Does every H2 trace back to a keyword from research (SERP, Trends, GSC)? Remove filler.
   - Is the AU differentiation clear in the headings themselves?
   - **Honest data sourcing check:** If any data point came from general knowledge rather than an actual tool, flag it as unverified.
   - What would Kuya spot as a weakness? Call it out first.
   - How many internal links to existing Emma's content? Target 3-4 (pillar + 2-3 companion guides).
8. **Present headings to user for approval** — never write content before approval

### Step 2a: Google Trends Content Idea Discovery

**PITFALL — Do NOT test multiple clusters in one session.** Testing Room Environment AND Sleep Schedules AND Sleep Training in the same Trends session will get the IP rate-limited (429) for 24-48 hours. Pick ONE cluster per session only. If Kuya asks for multiple options, test the first cluster, present results, get his feedback, THEN test the next cluster in a separate session (next day if needed).

When Kuya asks "what content should we add next?" or "what has demand?":

1. **Run multi-cluster keyword discovery** — test 4-6 keyword clusters covering related topic areas (sleep schedules, room environment, sleep training, toddler sleep, etc.)
2. **For each cluster**, get avg and peak demand scores for AU (`geo='AU'`)
3. **Prioritize topics** by avg demand score:
   - 30+ = high demand (strong content candidate)
   - 10-29 = moderate demand (worthwhile if seasonal alignment is good)
   - 0-9 = niche (only if fits existing cluster perfectly)
4. **For top candidates** (avg 20+), dig deeper with:
   - Related top queries → these become H2/H3 topics and FAQ questions
   - Rising queries with value 50+ → featured snippet opportunities
   - 5-year seasonal pattern → identify peak month for timing
5. **Present findings** as ranked table: Topic, Avg Demand, Peak, Seasonal Peak, Recommendation

See `references/google-trends-content-discovery.md` for the full pattern with pytrends rate-limit handling.

### Step 3: Build HTML — Critical: Inline CSS Required

**CRITICAL BUG — DO NOT reference external style.css or js/include.js:**
- This site does NOT serve `/style.css` (returns 404). All CSS must be **inline** in a `<style>` block in `<head>`.
- This site does NOT serve `/js/include.js` (returns 404). Nav and footer must be **inline HTML**, not loaded via include scripts.
- **How to get the working CSS:** Clone the repo and copy the `<style>` block from an existing guide page.
- **How to get nav/footer:** Copy `<header class="header">...</header>` and `<footer>...</footer>` from an existing guide page.
- **DO NOT** add `<link rel="stylesheet" href="/style.css">` — it will silently 404.
- **DO NOT** add `<script src="/js/include.js"></script>` — it will 404.

Copy template from `guides/wifi-vs-non-wifi-baby-monitor/index.html`. Required elements:
- Article + FAQ + Breadcrumb schema (mandatory)
- FAQ schema questions = PAA from SERP analysis
- Red Nose Australia citations
- 3-4 internal links (pillar page + 2-3 other guides)
- Author bio at end
- `<script>` tags MUST have matching `</script>` close tags
- Nav: "Best Baby White Noise 2026" (NOT "Best White Noise" — must include "Baby")

## H1 Decision Rule (For All Emma's Guides)

Kuya was asked: "should our H1 have 'Australia' or not?"

**Rule:** "Australia" is NOT required in the H1 for informational guides. The site is already geo-targeted via:
- Domain-level signals (Cloudflare + GitHub Pages serve AU traffic)
- URL structure independent of geo
- AU-specific body signals (Red Nose Australia, MCHN, GP, Celsius temps, AU$)
- Intro paragraph (mentions Australia)

**Prefer:** Direct, reader-focused H1s. E.g. "4-Month Sleep Regression — Your Survival Guide" over "4-Month Sleep Regression in Australia — Your Survival Guide"

**Exception:** If the primary search query explicitly includes "Australia" AND the keyword variant without geo has different intent (e.g. "best baby monitor" is generic vs "best baby monitor australia" is commercial-intent for AU shoppers), include it. For informational guides (how-to, what-is, signs-and-symptoms), the query intent is universal — skip the geo modifier.

### Step 4: Content Structure for ALL Search Engines — Google + AI (Meta AI, ChatGPT, Perplexity, Gemini)

**Key insight:** Google and AI engines want the same thing — clear answer, stats, sources, dates, tables. Optimizing for one optimizes for all. There's no trade-off.

**Content Structure Template (Guide Pages):**

```
H1: [Question/Keyword — e.g., "Safe White Noise Decibel Levels for Babies"]

📌 First 2 sentences = DIRECT ANSWER with number + source + date:
This is NOT keyword stuffing. It's giving the user what they searched for immediately.
Example: "Safe white noise for babies is ≤50 dB at crib level, 
measured from where baby sleeps. The AAP recommends keeping 
sound machines at least 1 metre from the cot. Updated June 2026."

Then expand (this satisfies Google's "answer the intent fully"):
- Why this number? (explain the research/context)
- Practical application (how to measure, steps to take)
- Table: Age → Max dB → Distance → Risk (scannable = more AI citations + featured snippets)
- Safety guidelines with citations to authoritative sources (gov/org/edu)
- FAQ section (5-7 questions from PAA data)
- Author bio with credentials
```

**Pillar Page Template — same plus:**
```
- Product comparison table at top (scannable)
- Individual product cards with pros/cons/price/specs
- Buyer's guide / how to choose section
- FAQ section
```

**Key rules:**
- First 2 sentences = direct answer. Then expand for depth. Both Google AND AI engines benefit.
- Tables get cited WAY more than paragraphs by all AI engines (and Google loves them for featured snippets)
- FAQ schema = 43% of AI citations come from FAQ content (Google also shows FAQ rich results)
- "Updated [Month Year]" or "Last tested: [Date]" on every page — freshness signal for all
- External links to authoritative sources (gov/org/edu) = +30-115% AI citation rate + E-E-A-T for Google
- Meta AI confirmed: same crawler standards as ChatGPT/Perplexity/Gemini. Allow Meta-ExternalAgent in robots.txt (already done).

### Step 4b: Content Writing Rules (from Kuya's feedback, updated June 2026)

**Search-intent-first rule:** Content length is determined by what the user needs to know, not a word target. Google's own docs say: no minimum or maximum word count. Write until the question is answered, then stop. No padding.

**Kuya's priority order for cuts when content is too long:**
1. Cut niche rules/tricks first — these are PAA curiosity, not search demand
2. Cut myth-debate deep-dives second
3. Cut any H2 that exists for novelty rather than actual search demand
4. Cut individual tip descriptions to 1 sentence each instead of 2-3
5. Cut sign/list descriptions to shorter bullet-style phrases

**Always keep (the differentiators no competitor has):**
- Red Nose Australia citations
- AU-specific details (Celsius temps, MCHN resources, AU product names)
- Internal links to existing Emma's guides (white noise pillar, swaddle pillar, decibel safety)
- FAQ schema (7 questions minimum from PAA)
- Author bio

### Step 5: HTML Quality Checks

After writing any HTML file, verify these BEFORE committing:
- [ ] No line-number artifacts (`1|...` or `...|` patterns) — run cleanup if found
- [ ] No double line-number artifacts from read_file offset views
- [ ] All `<script>` tags have matching `</script>` close tags
- [ ] Verify the file is valid HTML with `head -5` and `grep` for artifacts
- [ ] Count open vs close `<script>` tags

### Step 6: User Review

- User reviews draft content
- User provides feature image from Unsplash
- Process one guide at a time — build, review, push, then next

### Step 7: Australian English Spelling Verification

Before presenting any draft or pushing any page, scan for US English spellings in content (not CSS code):

```bash
grep -rnw --include='*.html' -iE '\b(mom|moms|favorite|colorful|apologize|realize|organize|recognize|neighbor|flavor|theater|diaper|stroller|aluminum)\b' .
```

Expected: zero content hits. CSS properties like `color`, `text-align: center`, `align-items: center` are code — not flagged.

**Fix pattern:** Replace US spellings:
- `mom` / `moms` → `mum` / `mums`
- `favorite` → `favourite`
- `center` → `centre`
- `organize` → `organise`
- `realize` → `realise`

**Why it matters:** Google uses consistent spelling as a geo-signal. Australian English + $AU prices + Red Nose Australia citations + Celsius temps = stronger AU targeting signal. Inconsistent spelling (mixing "mom" and "mum") weakens that signal.

### Step 8: Pre-Push Review Gate (MANDATORY — Do Not Skip)

**Kuya's rule (June 2026):** Before ANY `git push`, you MUST do a full review of the changes and present it to Kuya for approval. Do NOT push without his explicit "sige" or "push" command.

**Load these skills during review:**
- `seo-mastery-workflow` — for checklists (post-push-deployment-checklist, pillar-publishing-checklist, audit-findings-presentation)
- `emmas-site-guide-building` (this skill)
- `google-seo-docs-master` — for Google's own rules on meta tags, schemas, and indexing

Use their reference files and checklists. Do NOT rely on memory.

The review must include:

1. **Verify the live output** — curl the page/pages you changed and run checks programmatically on the LIVE deployed version (not just local files)
2. **For product pillar expansions specifically, the review must cover:**
   - All meta tags updated (title, description, OG title, OG description, Twitter) — check with `grep`
   - All schemas updated (Article headline + description + dateModified, Product reviewCount + reviews array, FAQPage if needed) — check with `python3` JSON parsing
   - Image files exist for EACH new product — `ls -la images/*.webp`, verify no placeholder references
   - Script tags balanced — `grep -c '<script'` vs `grep -c '</script'`
   - Budget tier prices cover the full range (cheapest → most expensive)
   - No dead links (`href="#"`)
   - Prices consistent across ALL locations (at-a-glance table, product card, full comparison, verdict table, Product schema)
   - Content scanned for US English spellings — zero hits expected
3. **Present findings** to Kuya in a structured format (table is best for comparisons)
4. **Wait for approval** — only push after Kuya explicitly says so

### Step 9: Pre-Push Security Check (Public Repo)

Since the Emma's repo is PUBLIC, add these checks to the pre-push routine:

1. **Credentials scan**:
   ```bash
   grep -rn -iE '(api[_-]?key|api[_-]?secret|access[_-]?key|secret[_-]?key|password|token|auth[_-]?key|client[_-]?secret|ghp_|gho_|github[_-]?token|sk-[a-zA-Z0-9]|AIza[0-9A-Za-z]|AKIA[0-9A-Z]{16})' --include='*.html' --include='*.js' --include='*.json' --include='*.yml' --include='*.yaml' --include='*.md' --include='*.sh' . 2>/dev/null | grep -v 'node_modules' | grep -v '\.git/'
   ```
   - Expect zero true-positive results. Article content mentioning "password" generically (e.g. WiFi password tips) is fine.
   - File paths to server-side credentials in STATUS.md are low risk (no SSH access = no exploit).

2. **`.gitignore` must exist** — if missing, create one with:
   ```
   # Credentials and secrets
   gsc_token.json
   gsc_credentials.json
   gsc_combined.json
   .env
   *.local
   # IDE
   .vscode/
   .idea/
   # OS
   .DS_Store
   Thumbs.db
   # Python cache
   __pycache__/
   *.pyc
   ```

### Step 10: Add Feature Image to Guide

Insert after breadcrumb + back-link, before first paragraph. Use Approach B (CSS object-fit:cover).

### Step 11: Update Guides Hub Card

Add new section card on `/guides/index.html`. Always check container nesting — cards must be inside `.guide-cards` divs inside `.container` div.

### Step 12: Update Sitemap

Add entry before the Utility Pages section.

### Step 13: Update STATUS.md

After any change (new guide, optimization, fix, push), update STATUS.md:
- Add entry to Section 12 (Optimization History) with date
- Update Section 13 (What's NOT Yet Done) — mark task as Done if applicable
- Update last updated date
- Push STATUS.md alongside the actual changes

### Step 14: Verify Deployment (CRITICAL — Do Not Skip)

After pushing, verify the live page is correct before telling Kuya it's done:
1. Check the page loads: `curl -sI https://emmassleepadvice.com/...` → expect `200 OK`
2. Check for remaining artifacts: `curl -s https://... | grep -c "[0-9]|"` — should be 0
3. Check styling works: inline `<style>` block should be embedded
4. Check nav/footer render
5. **Verify image serves (new images only):** Use `?v=1` to bypass Cloudflare stale 404 cache

**Common deploy failures:** HTTP 404 (wait 30-60s), Cloudflare cached 404 on new images (wait or rename file), no styling (missing inline CSS), line artifacts (run sed cleanup), old content (Cloudflare cache).
