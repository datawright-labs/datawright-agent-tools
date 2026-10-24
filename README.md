# Datawright web tools for AI agents

Give your agent (Grok Bot, Cursor, Hermes, OpenClaw, Claude, ChatGPT/dots, Muse) eleven web-data tools through [Apify's MCP server](https://mcp.apify.com). Each tool is an Apify Actor by Datawright Labs; you pay per result on your own Apify account (free accounts work, from $1 per 1,000 results).

| Tool | Use it to |
|---|---|
| [email-domain-dns-checker](https://apify.com/datawright-labs/email-domain-dns-checker) | Check SPF, DMARC, DKIM and MX for a list of domains |
| [whois-rdap-domain-lookup](https://apify.com/datawright-labs/whois-rdap-domain-lookup) | Bulk WHOIS/RDAP: registrar, domain age, expiry, availability |
| [ssl-certificate-checker](https://apify.com/datawright-labs/ssl-certificate-checker) | Bulk SSL certificate and domain expiry |
| [security-headers-checker](https://apify.com/datawright-labs/security-headers-checker) | HTTP security headers (HSTS, CSP, X-Frame-Options, cookies, HTTPS redirect), A-F grade per URL |
| [broken-link-checker](https://apify.com/datawright-labs/broken-link-checker) | Find 404s and dead links, grouped by page |
| [pagespeed-auditor](https://apify.com/datawright-labs/pagespeed-auditor) | Core Web Vitals / Lighthouse for many URLs |
| [website-screenshot](https://apify.com/datawright-labs/website-screenshot) | Full-page, mobile screenshots and URL to PDF |
| [sitemap-url-extractor](https://apify.com/datawright-labs/sitemap-url-extractor) | Every URL from a site's sitemaps |
| [autocomplete-keyword-scraper](https://apify.com/datawright-labs/autocomplete-keyword-scraper) | Google, YouTube and Bing keyword suggestions |
| [app-store-top-charts](https://apify.com/datawright-labs/app-store-top-charts) | iOS App Store top charts by country and genre |
| [ats-jobs-scraper](https://apify.com/datawright-labs/ats-jobs-scraper) | Jobs from Greenhouse, Lever and Ashby boards |

## Connect (any MCP client)
URL: see `mcp.json` (Streamable HTTP). Header: `Authorization: Bearer <your APIFY_TOKEN>`.
Each tool call returns a run summary; fetch rows with the `get-dataset-items` tool.

- **Hermes** (tested): `pip install "hermes-agent[mcp]"`, add the server under `mcp_servers:` in `~/.hermes/config.yaml` with `url` and `headers`, then `hermes mcp test datawright`.
- **OpenClaw** (tested): `openclaw mcp add datawright --no-probe --url "<url>" --transport streamable-http --header 'Authorization=Bearer ${APIFY_TOKEN}'`, then `openclaw mcp probe datawright`.
- **Muse**: install the skill in `skills/datawright-web-tools` (calls Apify's REST API directly).

## Try it
"Check SPF, DMARC and DKIM for example.com and github.com." "Find broken links on https://crawlee.dev, max 20 pages." "When do github.com and bbc.co.uk expire, and who is the registrar?" "Grade the security headers of apify.com and example.com and tell me what to fix."

Made by Datawright Labs. MIT license.
