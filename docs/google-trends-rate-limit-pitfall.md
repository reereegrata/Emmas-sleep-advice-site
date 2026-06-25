# Google Trends Rate Limit Pitfall

## The Trap

Google Trends (via pytrends) rate-limits aggressively when you send too many requests in quick succession. Once hit with HTTP 429, the IP can be blocked for **hours to 24+ hours** — no workaround, no retry-after header.

## Root Cause

**Batching too many keywords OR sending multiple payloads too fast.** Even with `time.sleep(1.5)` between batches, sending 4+ payloads in 2-3 minutes can trigger the ban.

### Specific Pattern That Triggered a Ban (real example):

In one session, the agent sent **7 payloads** in ~3 minutes:
1. Room Environment cluster (4 keywords)
2. Variations (4 keywords)
3. Temperature + TOG (4 keywords)
4. Deep dive: related queries
5. Related topics (failed)
6. Extra combos (3 keywords)
7. Global comparison (2 keywords)

Result: 429 blocked for the rest of the session + next several hours.

## The Fix: One Keyword At A Time

**Golden rule: Start with ONE keyword only.**

```
Step 1: Test the primary keyword alone
  → If avg < 20, abandon the topic entirely (don't waste requests)
  → If avg 20+, proceed to Step 2

Step 2: Deep dive on that one keyword (related queries + seasonal)

Step 3: Only THEN test variations (1-2 keywords at a time)
```

### Why this matters to Kuya

Kuya called this out explicitly: "I told you to focus on 1 keywords mo na. Kay apala." Getting rate-limited means we lose the tool entirely for hours. Start small, get signal, expand only if warranted.

## Prevention Checklist ✓

- [ ] Test only 1 keyword in the first payload
- [ ] If avg < 20, STOP — don't test more variants
- [ ] Only add variants if the first keyword shows real demand (avg 20+)
- [ ] Between payloads: wait minimum 3 seconds (not 1.5)
- [ ] If you get 429: stop trying for the rest of the session
- [ ] Max 3 payloads per session across all topics — not per topic
