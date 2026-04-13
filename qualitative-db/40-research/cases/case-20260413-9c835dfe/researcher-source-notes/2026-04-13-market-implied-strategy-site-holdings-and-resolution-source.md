---
type: source_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: institutions
entity: strategy
topic: case-20260413-9c835dfe | market-implied
question: MicroStrategy announces >1000 BTC purchase April 7-13?
date_created: 2026-04-13
source_name: Strategy official site (MSTR metrics / purchases reference)
source_type: company website
source_url: https://www.strategy.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [strategy, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/market-implied.md]
tags: [official-source, resolution-source, holdings-page]
---

# Summary

Strategy's official website is the governing source family for this market because the contract says resolution is based on official information from MicroStrategy/Strategy or Michael Saylor. The live site currently exposes embedded page data showing BTC holdings and an `as_of_date` of 2026-04-13, plus a navigation reference to a `/purchases` page. That supports that Strategy is maintaining current holdings data on-site, but in this run I did not find a clearly attributable separate Apr 7-13 announcement text saying a >1000 BTC purchase was announced within the window.

## Key facts extracted

- The market contract explicitly references official information from MicroStrategy or Michael Saylor as the resolution source.
- Strategy's official site currently serves an analytics page with embedded data that includes `btc_holdings: 780897` and `as_of_date: 2026-04-13`.
- The site navigation includes a dedicated `Purchases` tab/path, indicating the company treats holdings/purchases as an official published surface.
- The simple fetch/readability path did not expose the purchases table content cleanly; direct HTML inspection showed the page framework and embedded data, but not a clear text statement of a new >1000 BTC purchase announcement within Apr 7-13 ET.

## Evidence directly stated by source

- Official site page metadata and embedded JSON indicate Strategy is publishing current BTC metrics dated 2026-04-13.
- The site contains a specific purchases surface, which matches the contract's reference link.

## What is uncertain

- Whether the `/purchases` page itself, if rendered fully in-browser, contains a qualifying dated announcement that should count for resolution.
- Whether a Michael Saylor social post inside the window exists and was simply not discoverable through the available lightweight search path.
- Whether same-day site metric updates are considered an "announcement" absent a separate press release/post.

## Why this source may matter

This is the strongest primary source because the contract itself points to official MicroStrategy/Strategy or Michael Saylor information, and specifically references Strategy's purchases page for holdings tracking.

## Possible impact on the question

If the purchases page or another official Strategy/Saylor post contains a dated Apr 7-13 statement of a >1000 BTC purchase, the market's 96% Yes price is justified. If not, then the current official-site evidence is weaker than the market price implies because updated holdings data alone may not cleanly prove a qualifying announcement in-window.

## Reliability notes

- High credibility as an official company source.
- Medium extractability in this run because the site is heavily client-rendered and the purchases content was not plainly exposed by lightweight fetch tooling.
- Strong for source-of-truth attribution, weaker for confirming the exact timing/wording of a qualifying announcement without a clearer dated post or table row.