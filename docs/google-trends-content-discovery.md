# Google Trends Content Idea Discovery

Use when Kuya asks "what content should we add next?" — systematically test keyword clusters to find the highest-demand topic.

## The Multi-Cluster Pattern

Run 4-6 batches of keyword clusters, then dig deeper on winners.

### Cluster Ideas for Baby Sleep (AU)

| Cluster | Example Keywords | What It Tests |
|---------|-----------------|---------------|
| Sleep Schedules | newborn sleep schedule australia, baby sleep schedule 3 months, baby naps australia, newborn not sleeping, baby sleep cycles | General sleep problems |
| Room Environment | baby room temperature australia, best room temperature for baby sleep, baby cold at night australia, baby sleeping bag guide australia | Room setup / gear |
| Sleep Training | baby sleep training australia, how to settle baby australia, responsive settling, pick up put down method, cry it out australia | Behavioral methods |
| Toddler Sleep | toddler sleep problems australia, toddler bedtime routine, toddler night waking, 2 year old not sleeping | Older baby focus |
| Feeding & Sleep | dream feeding baby, when do babies sleep through night australia, baby sleep regression feeding | Connection topics |
| Broad Ideas | baby wake windows australia, witching hour baby, colic baby australia, baby teething sleep, daylight saving baby sleep | Novelty / seasonal |

### Execution (venv required, NOT execute_code sandbox)

```python
# Save as /tmp/trends_discovery.py, run via terminal with venv
from pytrends.request import TrendReq
import time

pytrends = TrendReq(hl='en-AU', tz=420)

kw1 = ['keyword1', 'keyword2', 'keyword3', 'keyword4']
pytrends.build_payload(kw1, cat=0, timeframe='today 12-m', geo='AU', gprop='')
r = pytrends.interest_over_time()
time.sleep(1.5)

for col in [c for c in r.columns if c != 'isPartial']:
    print(f"  {col}: avg {r[col].mean():.0f}, peak {r[col].max():.0f}")
```

### Interpreting Results

| Avg Demand | Meaning |
|:----------:|---------|
| 30+ | High demand. Strong content candidate. |
| 10-29 | Moderate. Worthwhile if seasonal alignment is good. |
| 0-9 | Niche. Only if fits existing cluster perfectly. |

### Deep-Dive on Winners (avg 20+)

1. **Related queries** — top queries become H2 topics and FAQ questions
2. **Rising queries** (value 50+) — featured snippet opportunities
3. **5-year seasonal** — identify peak month for timing

```python
# Get related queries
pytrends.build_payload(['keyword'], cat=0, timeframe='today 12-m', geo='AU')
related = pytrends.related_queries()
top = related['keyword'].get('top')
rise = related['keyword'].get('rising')

# 5-year seasonal pattern
pytrends.build_payload(['keyword'], cat=0, timeframe='today 5-y', geo='AU')
s = pytrends.interest_over_time()
s['month'] = s.index.month
monthly = s.groupby('month')['keyword'].mean()
print(f"Peak month: {monthly.idxmax()} ({monthly.max():.0f})")
```

### Rate Limit Handling — CRITICAL: Start With One Keyword

**Kuya's rule: ONE KEYWORD FIRST.** Do NOT test multiple clusters or batches in one session. Testing 4-6 clusters in one go will get the IP rate-limited and lose the tool for hours.

**Correct workflow:**
1. Pick ONE cluster
2. Test only the top 1-2 keywords from it
3. If avg < 20, abandon the cluster — don't test more
4. If avg 20+, deep dive on that keyword only
5. Max 3 payloads per session total

**Do NOT batch multiple clusters together.** Each batch = risk of 429.

See `references/google-trends-rate-limit-pitfall.md` in the parent skill for the full prevention guide.

- Batch 3-4 keywords per `build_payload()` (1 request)
- `time.sleep(1.5)` between separate batches
- If you get 429 (Too Many Requests), wait 30-60 seconds
- Split into smaller batches if you get 400 error (too many keywords)

### Pitfall: pytrends Only Works from Terminal + Venv

The `execute_code` tool runs in an isolated sandbox that does NOT see the system's virtualenv. Always:

```bash
cd /root && source .venv/bin/activate && python3 /tmp/your_trends_script.py
```

If no venv exists, create one:
```bash
uv venv --clear && source .venv/bin/activate && uv pip install pytrends
```
