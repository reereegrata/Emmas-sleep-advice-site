# Emma Pillar Page Audit Script
# Run this against the draft HTML before publishing a "Best X Australia" product-review pillar.
# Usage: python3 pillar-audit-checklist.py DRAFT-<slug>.html

import re, sys

with open(sys.argv[1]) as f:
    html = f.read()

ok = "✅"
no = "❌"
score = 100
deductions = []

# Meta
title = re.search(r'<title>(.*?)</title>', html).group(1)
desc = re.search(r'<meta name="description" content="(.*?)"', html).group(1)
print(f"Title: {len(title)} chars {ok if 50<=len(title)<=70 else no}")
print(f"Desc: {len(desc)} chars {ok if 140<=len(desc)<=160 else no}")
print(f"OG tags: {ok if 'og:title' in html else no}")
print(f"Twitter: {ok if 'twitter:card' in html else no}")
print(f"Canonical: {ok if 'canonical' in html.lower() else no}")
print(f"lang=en-AU: {ok if 'lang=\"en-AU\"' in html else no}")
if not (50<=len(title)<=70): score -= 5; deductions.append("Title length")
if not (140<=len(desc)<=160): score -= 5; deductions.append("Desc length")
if 'og:title' not in html: score -= 3; deductions.append("OG tags")
if 'twitter:card' not in html: score -= 2; deductions.append("Twitter")

# Schema
has_agg = 'aggregateRating' in html
has_faq = 'FAQPage' in html
has_article = 'Article' in html
rv = html.count('"@type": "Review"')
au = html.count('"author":')
print(f"Schema blocks: Article={has_article} FAQ={has_faq} Product={True}")
print(f"aggregateRating: {ok if has_agg else no}")
print(f"Reviews: {rv} / Authors: {au} {ok if rv==6 and au>=6 else no}")
if not has_agg: score -= 10; deductions.append("aggregateRating")
if rv < 6 or au < rv: score -= 10; deductions.append("Review authors")

# Headings
h1s = len(re.findall(r'<h1[ >]', html))
h2s = len(re.findall(r'<h2[ >]', html))
print(f"H1: {h1s} {ok if h1s==1 else no}  H2: {h2s} {ok if h2s>=5 else no}")
if h1s != 1: score -= 15; deductions.append("H1 count")

# Images
imgs_alt = len(re.findall(r'<img[^>]*alt="[^"]', html))
print(f"Images with alt: {imgs_alt} {ok if imgs_alt>=6 else no}")
if imgs_alt < 6: score -= 5*(6-imgs_alt); deductions.append("Missing alt")

# Content
aud = html.count('AU$')
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\{[^}]*\}', '', text)
text = re.sub(r'\s+', ' ', text)
aust = text.lower().count('australia')
rn = text.lower().count('red nose')
print(f"AU$ refs: {aud} {ok if aud>=40 else no}")
print(f"Australia: {aust} {ok if aust>=15 else no}")
print(f"Red Nose: {rn} {ok if rn>=5 else no}")

# Technical
sc_open = html.count('<script')
sc_close = html.count('</script>')
print(f"Scripts: {sc_open}/{sc_close} {ok if sc_open==sc_close else no}")
print(f"Media queries: {ok if '@media' in html else no}")
print(f"Fonts: {ok if 'fonts.googleapis.com' in html else no}")
if sc_open != sc_close: score -= 50; deductions.append("Script mismatch")

# Cross-links
guides = len(set(re.findall(r'href="(/guides/[^"]*)"', html)))
print(f"Guide cross-links: {guides} {ok if guides>=3 else no}")
if guides < 3: score -= 5; deductions.append("Cross-links")

print(f"\nSCORE: {max(0,score)}/100")
if deductions:
    print(f"Deductions: {', '.join(deductions)}")
