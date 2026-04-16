---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity:
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-15 be above 72000?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket event page and rules text
source_type: market_rules_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-395c5631/researcher-analyses/2026-04-13/dispatch-case-20260413-395c5631-20260413T221534Z/personas/variant-view.md]
tags: [polymarket, rules, market-state, source-note]
---

# Summary

Captured the market-implied probability and the operative contract language from the Polymarket event page.

## Key facts extracted

- The 72,000 line was trading around 73% Yes / 28% No at fetch time.
- The market resolves on the Binance BTC/USDT one-minute candle for `12:00` in ET on Apr. 15.
- Resolution depends on the final `Close` price of that one-minute candle being higher than 72,000.
- The rules explicitly say this is about Binance BTC/USDT, not other exchanges or trading pairs.
- Price precision is determined by the source display.

## Evidence directly stated by source

- Current market-implied probability for the 72k threshold is about 0.73.
- Governing source of truth is Binance BTC/USDT one-minute candles.
- All of the following conditions must hold for Yes: correct date, correct ET noon minute, correct venue/pair, and candle close strictly above 72,000.

## What is uncertain

- The page fetch is a rendered web extract rather than a signed rules archive.
- The event page does not itself provide the future settlement value.
- The page does not fully resolve edge-case questions such as temporary venue outage or post-publication data revision, though the venue source is clear.

## Why this source may matter

This source governs both market baseline and contract interpretation. For a date-sensitive, single-minute, single-venue market, the wording itself is materially important.

## Possible impact on the question

The rules make this narrower than a generic "BTC above 72k on Apr. 15" question. A trader can be directionally right on Bitcoin but still wrong on the exact noon ET Binance one-minute close.

## Reliability notes

- High relevance because this is the listed market/rules surface.
- Moderate-to-high credibility for contract text, though ideally paired with direct venue verification.
- Independence versus Binance is medium because Polymarket depends on Binance for settlement, but the source still separately establishes the market-implied baseline and explicit contract wording.