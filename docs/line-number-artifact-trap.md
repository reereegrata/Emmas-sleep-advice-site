# Line-Number Artifact Trap in HTML Files

## What Happens

When any tool in the Hermes ecosystem outputs text with line-number prefixes (like `1|<!DOCTYPE html>\n2|<html...>`), and that output gets written back to a file — even through an intermediate step — the line numbers get **baked into the file bytes**. They render as visible text on the live web page (e.g. `279|Some FAQ answer text`).

## Root Cause

- `read_file` displays content as `LINE_NUMBER|CONTENT` (e.g. `244|  <p>Most babies adjust...</p>`)
- If you read a file with `read_file`, then write the output directly (or through `patch`, `execute_code`, or any intermediate), the `244|` prefix is in the string data
- `write_file` writes exactly what it receives — it does NOT strip line numbers
- `patch` can also introduce these if the old_string or new_string came from a read_file output
- Even saving to `/opt/data/profiles/agentnyroh/output/` and then copying to the site repo carries the contamination forward

## How to Detect

Before committing any HTML file, run:
```bash
# Check for leading number| patterns (byte-level — won't miss them)
grep -oP '^\d+\|' path/to/file.html | wc -l

# Check for stray | at line start
grep -c '^|' path/to/file.html

# Byte-level check with od
od -c path/to/file.html | head -5
# If output starts with "1|" (e.g. "0000000   1   |   <   !   D   O") then it's contaminated
# If output starts with "<" (e.g. "0000000   <   !   D   O") then it's clean
```

## How to Fix

```bash
# Strip leading number| patterns
sed -i 's/^[0-9]*|//g' path/to/file.html
# Strip leading pipe artifacts
sed -i 's/^|//g' path/to/file.html
# Verify
grep -oP '^\d+\|' path/to/file.html | wc -l  # should be 0
```

## How to Prevent

**NEVER pipe read_file output into write_file.** Always use one of these clean paths instead:

1. **Copy from a clean template** — use `cp` from an existing working page, then modify with `sed` or `patch` using clean strings
2. **Build from scratch with string literals in code** — use `execute_code` with Python f-strings or triple-quoted strings (no `read_file` involved)
3. **If you must use existing content**, extract it via `terminal(cat path/to/file)` not `read_file(path)`, since `cat` doesn't add line numbers
4. **After any edit**, verify byte-clean with `od -c` before committing

## Commands That Are Safe vs Unsafe for HTML Editing

| Tool | Safe? | Notes |
|---|---|---|
| `write_file` | ⚠️ CONDITIONAL | Safe ONLY if content string is clean (not from read_file output) |
| `patch` | ⚠️ CONDITIONAL | Safe ONLY if old_string/new_string are hand-typed clean strings |
| `terminal(cp)` | ✅ SAFE | Direct file copy, no intermediate processing |
| `terminal(sed)` | ✅ SAFE | In-place edit on the actual file |
| `terminal(cat)` | ✅ SAFE for reading | Output is clean, no line numbers |
| `read_file` | ❌ DANGEROUS for write-back | Always adds LINE_NUMBER| prefix |
| `execute_code(read_file)` | ❌ DANGEROUS | Contaminates the data in memory |
