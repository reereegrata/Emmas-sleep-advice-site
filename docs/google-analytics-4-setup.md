# Google Analytics 4 Setup — emmassleepadvice.com

## Prerequisites

- Google account: farmer3tgf@gmail.com (same as GSC)
- Static GitHub Pages site (no server-side code)
- User creates the property in their browser (Google sign-in blocked on this server)

## Property Creation (User Handles This)

Send these instructions to Kuya or guide him step by step:

1. Go to https://analytics.google.com → sign in with farmer3tgf@gmail.com
2. Click "Start measuring"
3. **Property name:** Emma's Sleep Advice
4. **Reporting time zone:** Australia — Sydney (UTC+10)
5. **Currency:** Australian Dollar (AUD)
6. **Industry:** Shopping → Baby & Toddler (or Family & Parenting / Other)
7. **Business size:** Small / Individual
8. **Business objective:** "Understand web and/or app traffic" (1 selection enough)
9. **Platform:** Web
10. **Website URL:** https://emmassleepadvice.com
11. **Stream name:** Emma's Sleep Advice Web (auto-filled — keep default)
12. **Enhanced measurement:** ON (default — tracks scrolls, outbound clicks, site search)
13. Click "Create stream"
14. **Send the Measurement ID** (starts with G-)

## Data Sharing Settings

When prompted, recommend:
- **Google products & services:** ON (helps improve Google products, no ad personalization)
- **Modeling contributions & business insights:** OFF (no benefit for small site)
- **Technical support:** ON (needed for troubleshooting)
- **Recommendations for your business:** OFF (marketing emails, irrelevant)

## Tag Installation (Agent Handles This)

Once user sends the Measurement ID (e.g., G-L1KN4L71L9):

### 1. Add the snippet to all HTML files

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
```

Insert after `<head>` tag. Use Python string replacement:
```python
content.replace('<head>', '<head>\n' + GA_SNIPPET, 1)
```

### 2. Coverage

- Insert on ALL HTML files (homepage, about, contact, privacy policy, affiliate disclosure, all guides, all pillars, hub pages)
- **Skip** the GSC verification file (`googleeea9*.html`) — Google doesn't need analytics on it
- Typical Emma's site: 24 HTML files (verify with `find . -name '*.html' -not -path '*/.git/*'`)

### 3. Verification

```bash
# 1. Script tag balance — check ALL files
mismatch=0
while IFS= read -r f; do
  o=$(grep -c '<script' "$f"); c=$(grep -c '</script>' "$f")
  if [ "$o" -ne "$c" ]; then echo "MISMATCH: $f ($o open, $c close)"; mismatch=1; fi
done < <(find . -name '*.html' -not -path '*/.git/*' -not -name '*googleee*')
[ "$mismatch" -eq 0 ] && echo "All balanced"

# 2. Verify on live
curl -sL 'https://emmassleepadvice.com/' | grep -c 'G-XXXXXXXX'
# Should return 2+ (src reference + config call)

# 3. Check gtag.js is reachable
curl -sL -o /dev/null -w 'HTTP %{http_code}' 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX'
# Should return 200
```

### 4. Final Check

User visits the site in their browser → checks Google Analytics → Realtime → should show 1 active user.

## What to Tell the User

- The "Data collection isn't active for your website" warning is **normal** — GA4 takes 24-48 hours to show "Receiving data"
- Tell them to visit the site and check Realtime to confirm the tag fires
- Data starts appearing in Reports after 24-48 hours
- For a 2-3 week old site, don't expect much traffic yet — GA value grows as traffic grows

## Do NOT

- Use Google Tag Manager (overkill for static site)
- Add the snippet to the GSC verification file
- Expect immediate data
- Panic about the "Data collection isn't active" warning
