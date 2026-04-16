---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1m candle close on 2026-04-15 be above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance spot API and Polymarket market rules
source_type: primary_plus_resolution_context
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-source, timing-risk]
---

# Summary

This note captures the main direct evidence used for the April 15 BTC > 70,000 market: Polymarket's explicit resolution rule and Binance spot market data from the public API as a verification/context pass.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET (noon)** on the specified date, using the candle's final **Close** price.
- The contract is specifically about **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- The assigned market's current displayed price was 0.945, implying about **94.5%** Yes.
- Binance public API spot data fetched during this run showed BTC/USDT trading around **74.2k** on 2026-04-13 at roughly 22:26 UTC / 18:26 ET.
- A timezone check confirms the relevant settlement timestamp is **2026-04-15 16:00:00 UTC**, corresponding to **2026-04-15 12:00:00 ET**.
- Binance 24h ticker data during this run showed:
  - last price about **74,230**
  - 24h weighted average price about **72,005**
  - 24h low about **70,505.88**
  - 24h high about **74,465**

## Evidence directly stated by source

From Polymarket rules page:
- Yes iff the Binance BTC/USDT 1m candle for 12:00 ET on Apr 15 has a final close above 70,000.
- Resolution source is Binance trade page candle display.
- Price precision is determined by the number of decimals in the source.

From Binance API outputs observed during this run:
- Latest BTC/USDT prints were materially above 70,000.
- Even the 24h low remained above 70,000, though only by roughly 506 dollars.

## What is uncertain

- These observations do not settle the market yet because the relevant candle is still about 42 hours away.
- Binance API data is a strong contextual verification surface, but Polymarket names the website candle display as the official settlement surface.
- BTC is volatile enough that a move from ~74.2k to below 70k by the resolution minute is plausible even if not base-case.

## Why this source may matter

This is the key direct evidence pair for the case: one source defines exactly what counts for resolution, and the other verifies the current price level and how much downside room exists before the threshold fails.

## Possible impact on the question

The evidence strongly supports a Yes lean because spot BTC/USDT is currently well above 70,000. The main residual risk is timing/path risk into the specific noon ET minute rather than uncertainty about what source governs the market.

## Reliability notes

- Polymarket rules are high-value for contract interpretation but are still a platform text surface rather than the final observed Apr 15 candle itself.
- Binance API is highly relevant and near-direct for price context, but the named authoritative settlement surface is Binance's own BTC/USDT candle display.
- Independence between these two is only medium because both ultimately point back to Binance for market data mechanics.