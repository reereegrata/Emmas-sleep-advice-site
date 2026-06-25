# Google Trends Workflow — pytrends for SEO Content Research

## Quick Install
```bash
uv pip install pytrends
```

## Basic Usage

```python
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-AU', tz=420)  # AU = Australia
pytrends.build_payload(['keyword1', 'keyword2'], cat=0, timeframe='today 12-m', geo='AU', gprop='')
interest = pytrends.interest_over_time()
if not interest.empty:
    interest = interest.drop(columns=['isPartial'], errors='ignore')
```

## Available Data

| Method | Returns | Use Case |
|--------|---------|----------|
| `interest_over_time()` | Weekly 0-100 score per keyword over N months | Compare keyword variants, check seasonal patterns |
| `related_queries()['kw']['top']` | Top queries people also search (sorted by volume) | PAA extraction, FAQ schema questions, H2 ideas |
| `related_queries()['kw']['rising']` | Fastest-growing related queries | Trending topics to cover, rising PAA targets |
| `interest_by_region()` | Geo breakdown | Validate AU-specific demand |

## Common Workflows

### Workflow A: Topic Demand Validation
Compare keyword variants to pick the primary keyword.
```python
kw_list = ['4 month sleep regression', 'baby sleep regression', '6 month sleep regression']
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='AU', gprop='')
interest = pytrends.interest_over_time()
print(interest.mean().sort_values(ascending=False))  # Highest = best primary keyword
```

### Workflow B: PAA / FAQ Extraction
```python
pytrends.build_payload(['4 month sleep regression'], cat=0, timeframe='today 12-m', geo='AU', gprop='')
rq = pytrends.related_queries()
top = rq['4 month sleep regression'].get('top')
top.head(10)  # These = FAQ schema questions + H2 ideas
```

### Workflow C: Brand/Product Comparison
```python
kw_list = ['hatch rest baby', 'dreamegg white noise', 'baby shusher']
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='AU', gprop='')
interest = pytrends.interest_over_time()
print(interest.mean().sort_values(ascending=False))  # Most-searched brand
```

### Workflow D: Seasonal Timing
5-year monthly average to find peak months.
```python
pytrends.build_payload(['4 month sleep regression'], cat=0, timeframe='today 5-y', geo='AU', gprop='')
seasonal = pytrends.interest_over_time()
seasonal = seasonal.drop(columns=['isPartial'], errors='ignore')
seasonal['month'] = seasonal.index.month
print(seasonal.groupby('month').mean().round(1))  # Higher = peak demand month
```

## Pitfalls

- **Rate limits:** Pytrends hits Google Trends like a browser. ~10 requests/minute is safe. If you get 400 errors, wait 30s and retry.
- **No exact search volume:** Trends returns relative scores (0-100), not exact numbers. Good for directional comparison only.
- **No keyword difficulty:** Trends alone can't tell you if a keyword is hard to rank for. Combine with SERP analysis.
- **Brand/product names fail:** Some product names trigger 400 errors because the query pattern is too specific. Prefer generic descriptive queries (e.g. "white noise machine baby" over specific brand names).
- **"Not enough data"** — queries with very low volume return empty DataFrames. This means the topic has minimal search demand. Skip it.
- **`timeframe` matters:** 'today 12-m' = last 12 months by week. 'today 5-y' = last 5 years by month. Use 5-year for seasonal patterns, 12-month for recent trends.
- **`geo='AU'` is critical** — without it, results are global/US-centric and irrelevant for Australian SEO.
