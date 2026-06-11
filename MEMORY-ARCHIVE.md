# Hermes Agent Memory Archive (Dumped: 2026-06-11)
> Memory was full. Dumped here to free up space. This is the complete agent memory + user profile backup.

## Workflow Rules
1. SEO Skills: Always load seo-mastery-workflow first. Prospecting = prospecting-bundle → Universal Engine + locked sub-agents (PRIMARY).
2. TLD filter: com/au/uk/co/net/com.au/nz/org/ca/us/io only.
3. Proposal rules: Never promise specific numbers ("15-25 links/month") — frame as process. Let audit reveal real targets. Commission-only = auto pass.
4. Client site audits: Even if different site type, still load seo-mastery-workflow first.

## Image Standards
- Article images: object-fit:contain, max-height:400px
- Guide images: 800px, WebP q60-80, ~10-15KB
- Homepage card images: 600px, q48, 10-30KB, CSS object-fit:cover
- Real photos from Unsplash via desktop agent — short broad queries
- Alt text user-approved

## HTML Golden Rule
Every `<script>` tag MUST have a matching `</script>`. Always count open vs close before finalizing edits. Missing `</script>` = blank white page.

## SEO Mastery Principles
- Stage 4 audit: present delta-only issues (skip optimized pages), state ranking impact per fix, include effort
- Over-optimization prevention: check STATUS.md > Optimization History; 1 pass/month per page
- Meta title: only if >71 chars; OG tags only if duplicate/missing
- Content unchanged unless >5 position drop
- After EVERY task: update STATUS.md and push to GitHub
- Word count: no sweet spot. Answer search intent fully, then stop. No padding.
- Google docs > SEO blogs

## Google Trends Rule
Test ONE keyword cluster per session. Multiple clusters = consecutive days, not same session.

## Repo Access
- Emmas-sleep-advice-site (reereegrata/Emmas-sleep-advice-site) — PRIVATE (changed June 11, 2026)
- SSH deploy key: /opt/data/.ssh/id_ed25519_emma
- Clone/push only via SSH. No HTTPS without auth.
- 23 public-facing pages + 1 GSC verification file = 24 HTML files

## GSC Setup
- Connected to emmassleepadvice.com only
- Credentials: scripts/gsc_credentials.json + scripts/gsc_combined.json
- Weekly cron: Mon 9am
- Bookshelf Memories: REMOVED — no access
- OAuth client (Web app): 37241543550-bcv6uifi37cjv009ks4b46nvkh755hlh.apps.googleusercontent.com
- Redirect URI: https://emmassleepadvice.com/gsc-callback
- Permanent refresh token (production publish)

## DeepSeek API
- deepseek-chat/reasoner deprecated July 24, 2026 (auto-map to v4-flash)
- v4 models: deepseek-v4-flash ($0.14/$0.28 per 1M), deepseek-v4-pro ($0.435/$0.87)
- Base URL: https://api.deepseek.com
- Cache hit ~90% cheaper

## Ranking Updates
- Next expected: August-September 2026

## Technical Lessons
- Nav fix on site pages: Must replace BOTH nav HTML AND CSS (header, dropdown, hamburger classes)
- Pre-push review: Load seo-mastery-workflow + google-seo-docs-master. Send to Kuya. Never push without approval.
- "Latest from Emma" (homepage line 774): Rotate periodically based on GSC traction
- Self-critique before presenting: "Is this the best version?" Call out weaknesses first.

---

## User Profile Archive

### Kuya Armss
- PH, Eastern Samar
- Emma's Sleep Advice (Amazon AU affiliate)
- Non-techy, Taglish OK

### Communication Preferences
- Direct, honest — no sugarcoat. Data-driven over haka-haka.
- Google docs > SEO blogs
- No emoji in chat responses
- One-thing-at-a-time testing
- Prefers straight answers on what moves rankings

### Corrections History
- Fix only what he said, don't over-fix
- Was frustrated by 7 Google Trends batches (1 per session rule)
- Insists on STATUS.md check before optimization suggestions
- Independently verifies claims via site:search
- Trusts GSC dashboard over API
- Corrects page count inaccuracies

### Proposal Style (for clients)
- Template: hook → pain → stages → question CTA
- No em dashes, fake link counts, generic intros, past-client proof
- Back claims with real Emma site examples
- Pitch the workflow, not yourself
- Include honest ceiling

### Content Rules
- Expert bios: only real, verifiable (Red Nose Australia, Raising Children Network)
- Backlinks: don't chase .gov/.edu for new sites. Content + Red Nose citations first.

### Other Ventures
- Next: other baby-niche sites + social media news aggregation (PH news)
- Wants realistic income assessments

### Pet Peeves
- "Forgetting" — wants STATUS.md documentation
- Bloated content / padding paragraphs
- Skipped steps / workflows
- Emojis in site text (only remove if he asks)
- Inaccurate page counts

### Praise Signal
"Your getting better. keep it up" = high praise

### Environment
- Desktop agent (DeepSeek V4 Pro w/ Chrome) handles SERP, Ahrefs, browser tasks
- Two agents coordinate through Kuya, not directly
- Cleanup preference: safe, targeted removal — no collateral damage
