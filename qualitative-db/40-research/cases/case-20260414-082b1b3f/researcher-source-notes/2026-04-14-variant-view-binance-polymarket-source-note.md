---
type: source_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: altcoins
entity: sol
topic: solana-above-80-on-april-17
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above $80 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance SOL/USDT API and Polymarket market rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=30
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/variant-view.md]
tags: [binance, polymarket, settlement-source, timing-check, price-path]
---

# Summary

This note combines the governing market rules from Polymarket with direct Binance market data needed to assess whether SOL is likely to remain above $80 at the settlement timestamp.

## Key facts extracted

- Polymarket says the market resolves from the Binance SOL/USDT 1-minute candle for 12:00 ET on April 17, 2026, using the final Close price.
- The contract is explicitly about Binance SOL/USDT, not other venues or pairs.
- Binance daily candles for the last ~30 sessions show SOL recently traded below $80 on April 1 (close 78.94), and had intraday lows below $80 on April 2 (78.85), April 6 (78.38), and April 7 (78.96).
- More recent daily closes recovered to the low/mid-80s: April 11 close 81.53, April 12 close 86.51, April 13 close 85.25.
- Binance 24h ticker at time of check showed last price about 85.25, 24h high 87.67, low 82.58.
- Hourly candles for April 14 show intraday trading mostly in the 85-87 range, not near the threshold but still within a few percent of it.

## Evidence directly stated by source

- Polymarket rule text directly states the governing source and timing condition.
- Binance API directly states recent price history and current trading range.

## What is uncertain

- The exact noon ET settlement print on April 17 is still ~2.5 days away.
- Crypto can move several percent quickly; recent realized volatility shows a move from 85 to below 80 is plausible even if not base case.
- The Binance public API is a strong direct data surface, but the contract text references the Binance trading UI candle specifically, so there remains a low-level display/API alignment risk.

## Why this source may matter

This is the cleanest combination of source-of-truth mechanics plus current market state. It makes the key neglected question visible: not whether $80 is generally “low” for SOL, but whether the market is overconfident about a specific 1-minute settlement print several days out.

## Possible impact on the question

The source package supports a bullish baseline because spot is currently above $80 by more than 6%, but it also supports a credible variant against extreme certainty because recent Binance trading shows sub-$80 prints are not remote history. The relevant risk is timing/path risk rather than a fundamental thesis collapse.

## Reliability notes

- Polymarket market page is the contextual but governing contract surface for resolution rules.
- Binance API is a direct and highly relevant data source for the underlying asset and likely aligns closely with the resolution venue.
- Evidence independence is only medium because both conclusions ultimately depend on Binance as the operative source.
- Source-of-truth ambiguity appears low-to-medium rather than zero because the contract points to the Binance UI candle, while this check used Binance API endpoints instead of the front-end chart widget directly.