#!/usr/bin/env python3
"""Datawright Labs web tools for AI agents: runs a Datawright Labs Actor on Apify and prints results as JSON.
Needs APIFY_TOKEN in the environment (collected through the agent's secure credential flow). Stdlib only."""
import argparse, json, os, sys, urllib.request, urllib.error

TOOLS = {
    "dns":         ("email-domain-dns-checker", "SPF, DMARC, DKIM, MX, MTA-STS for domains", "domains"),
    "ssl":         ("ssl-certificate-checker", "SSL certificate expiry, issuer, chain, domain expiry", "domains"),
    "whois":       ("whois-rdap-domain-lookup", "WHOIS/RDAP: registrar, domain age, expiry, availability", "domains"),
    "headers":     ("security-headers-checker", "HTTP security headers, HTTPS redirect, cookies, A-F grade", "urls"),
    "redirects":   ("redirect-checker", "Redirect chains, final status, migration old->new checks", "urls"),
    "links":       ("broken-link-checker", "Crawl sites and report broken links", "startUrls"),
    "pagespeed":   ("pagespeed-auditor", "Lighthouse / Core Web Vitals scores for URLs", "urls"),
    "screenshot":  ("website-screenshot", "Full-page screenshots of URLs", "urls"),
    "sitemap":     ("sitemap-url-extractor", "All URLs from a site's sitemaps", "startUrls"),
    "autocomplete":("autocomplete-keyword-scraper", "Google/YouTube/Amazon autocomplete keyword ideas", "keywords"),
    "appcharts":   ("app-store-top-charts", "Apple App Store top charts", None),
    "jobs":        ("ats-jobs-scraper", "Jobs from Greenhouse, Lever, Ashby boards", None),
}

def call(actor, payload, timeout):
    tok = os.environ.get("APIFY_TOKEN")
    if not tok:
        sys.exit(json.dumps({"ok": False, "error": "APIFY_TOKEN not set"}))
    url = f"https://api.apify.com/v2/acts/datawright-labs~{actor}/run-sync-get-dataset-items?timeout={timeout}&format=json"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST",
                                 headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout + 30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(json.dumps({"ok": False, "status": e.code, "error": e.read().decode()[:500]}))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth"); sub.add_parser("tools")
    r = sub.add_parser("run"); r.add_argument("tool", choices=TOOLS)
    r.add_argument("targets", nargs="*", help="domains, URLs or keywords")
    r.add_argument("--input", help="full Actor input as JSON (overrides targets)")
    r.add_argument("--timeout", type=int, default=240)
    a = p.parse_args()
    if a.cmd == "tools":
        print(json.dumps({k: {"actor": "datawright-labs/" + v[0], "does": v[1]} for k, v in TOOLS.items()}, indent=2)); return
    if a.cmd == "auth":
        tok = os.environ.get("APIFY_TOKEN", "")
        req = urllib.request.Request("https://api.apify.com/v2/users/me", headers={"Authorization": "Bearer " + tok})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=20))["data"]
            print(json.dumps({"ok": True, "username": d.get("username")}))
        except Exception as e:
            print(json.dumps({"ok": False, "error": str(e)[:200]}))
        return
    actor, _, field = TOOLS[a.tool]
    if a.input:
        payload = json.loads(a.input)
    elif field and a.targets:
        payload = {field: a.targets}
    else:
        sys.exit(json.dumps({"ok": False, "error": "pass targets or --input"}))
    print(json.dumps(call(actor, payload, a.timeout), indent=2))

if __name__ == "__main__":
    main()
