---
name: datawright-web-tools
description: Website and domain checks through Datawright Labs tools on Apify. SPF/DMARC/DKIM email-DNS audits, SSL certificate expiry, WHOIS/RDAP domain lookups (registrar, age, expiry, availability), HTTP security headers (HSTS, CSP, A-F grade), broken links, PageSpeed/Core Web Vitals, screenshots, sitemap URLs, autocomplete keyword ideas, App Store top charts, ATS job boards. Trigger phrases: check DMARC, SPF record, SSL expiry, whois lookup, domain age, domain expiry, is this domain available, security headers, check HSTS, CSP header, broken links, core web vitals, pagespeed, screenshot this site, sitemap URLs, keyword ideas, app store top charts, job listings from Greenhouse/Lever/Ashby.
tagline: Domain, website and SEO checks that return clean JSON.
catalog_auth: Apify API token
catalog_hosts: api.apify.com
version: 1.2.0
metadata:
  openclaw:
    primaryEnv: APIFY_TOKEN
    requires:
      env:
        - APIFY_TOKEN
      bins:
        - python3
    envVars:
      - name: APIFY_TOKEN
        required: true
        description: Apify API token (console.apify.com/settings/integrations); runs are billed pay-per-result to this Apify account.
    emoji: "🔎"
    homepage: https://apify.com/datawright-labs
---

## Purpose

Run a Datawright Labs Actor on Apify and return its results as JSON. Use when the user asks to audit a domain's email authentication, check SSL certificates, look up WHOIS/RDAP data (registrar, creation and expiry dates, availability), grade HTTP security headers, find broken links, score page speed, screenshot pages, list a site's URLs, get keyword ideas, pull App Store charts, or collect job postings from company career boards.

## Tooling

All commands go through `bin/datawright.py` (Python 3 standard library only):

```
bin/datawright.py auth                                  # verify the Apify token
bin/datawright.py tools                                 # list available tools
bin/datawright.py run dns example.com apify.com         # SPF, DMARC, DKIM, MX, MTA-STS
bin/datawright.py run ssl github.com example.com        # certificate + domain expiry
bin/datawright.py run whois github.com bbc.co.uk        # WHOIS/RDAP: registrar, age, expiry, availability
bin/datawright.py run headers apify.com example.com     # security headers, HTTPS redirect, cookies, A-F grade
bin/datawright.py run links https://example.com         # broken links (problems only)
bin/datawright.py run pagespeed https://example.com     # Lighthouse scores, Core Web Vitals
bin/datawright.py run screenshot https://example.com    # screenshot URLs
bin/datawright.py run sitemap https://example.com       # every URL in the sitemaps
bin/datawright.py run autocomplete "running shoes"      # autocomplete keyword ideas
bin/datawright.py run appcharts --input '{...}'         # full Actor input as JSON
bin/datawright.py run jobs --input '{...}'              # full Actor input as JSON
```

Each Actor's full input options are documented on its Apify Store page (apify.com/datawright-labs/<actor>).

## Auth

- Provider id: `apify` (credential collected as `custom.apify`, exposed to the CLI as `APIFY_TOKEN`)
- Collection: Apify API token via the secure credential flow; the user copies it from Apify Console, Settings, API & Integrations (free Apify account)
- Allowed hosts: `api.apify.com`
- Status check: `bin/datawright.py auth` (must return `"ok": true`)

## Operating Rules

1. Every run costs a small per-result fee on the user's Apify account (the price is on each Store page; Apify's free plan includes monthly credit). Tell the user before large batches (over ~100 domains or URLs, or big crawls).
2. All tools are read-only: they look at public websites and DNS, and never post or change anything.
3. Runs are synchronous with a 240 s default timeout; for big crawls pass `--timeout` or smaller batches.
4. Never print, log or transmit the token.

## Files

- SKILL.md
- bin/datawright.py

## Maturity

🧪 Beta: CLI live-tested against the Apify API on 2026-10-22 (auth, dns, ssl) and 2026-10-24 (whois, headers). Not yet run inside a Muse account.
