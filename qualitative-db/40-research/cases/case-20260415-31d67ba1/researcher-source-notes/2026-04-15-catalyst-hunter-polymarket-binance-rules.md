---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-31d67ba1 | catalyst-hunter
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above 70,000 on April 17
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/catalyst-hunter.md
tags: [polymarket, binance, resolution, timing]
---

# Summary

This source defines the governing contract mechanics. The market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026, using the final close price, not any other exchange or pair.

## Key facts extracted

- Resolution is based on the Binance BTC/USDT market specifically.
- The relevant candle is the 1-minute candle labeled 12:00 in ET timezone on the date in the title.
- The market resolves Yes only if the final Close price is strictly higher than 70,000.
- Price precision is whatever Binance displays in the source.
- Other exchanges, BTC/USD references, or broader intraday highs do not govern settlement.

## Evidence directly stated by source

The rules text says the market resolves to Yes if the Binance 1-minute candle for BTC/USDT 12:00 in ET has a final Close above the threshold; otherwise No. It explicitly names Binance as the resolution source and warns that the question is not about other exchanges or trading pairs.

## What is uncertain

- The webpage itself does not expose the eventual historical candle in static fetch output.
- The rule text does not independently explain DST mechanics, though the contract wording says ET and the market close timestamp is noon ET on Apr 17.

## Why this source may matter

This is the primary source-of-truth for contract interpretation. It sharply narrows what counts: one exchange, one pair, one minute, one closing print.

## Possible impact on the question

Because the contract is narrow, the main catalysts are not just generic Bitcoin direction; they are any events that could materially move Binance BTC/USDT over the next roughly 45 hours while avoiding exchange-specific settlement noise.

## Reliability notes

High reliability for contract wording. Lower usefulness for live price context by itself, so it needs supplementation with Binance or independent market-price context.