---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: spot-price-market
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance SOLUSDT API and Polymarket market rules page
source_type: primary-plus-market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT ; https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=14 ; https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-source, timing]
---

# Summary

This note captures the governing settlement mechanics and current spot-price regime for the SOL > $80 April 19 market.

## Key facts extracted

- Polymarket rules state the market resolves from the **Binance SOL/USDT 1-minute candle labeled 12:00 ET** on April 19, using the candle's final **Close** price.
- The market is specifically about **Binance spot SOL/USDT**, not another exchange or pair.
- Binance exchange info for SOLUSDT shows a **tick size of 0.01**, so practical settlement precision is to the cent.
- Binance ticker price on 2026-04-15 fetched at research time was about **84.87**.
- A direct Binance 1-minute kline query for **2026-04-15 12:00 ET** returned a close price of **83.94**, showing the contract mechanics can be mirrored via API and confirming that noon ET corresponds to **16:00 UTC** on the target date.
- Recent daily Binance closes were: Apr 12 **81.53**, Apr 13 **86.51**, Apr 14 **83.72**, Apr 15 **84.92**. Recent daily lows included sub-80 prints on Apr 12 (**81.27 low, still above 80**) and earlier sub-80 daily lows / closes on Apr 2, Apr 6, and Apr 7 intraday or close context.

## Evidence directly stated by source

- Polymarket directly states the settlement source and timing logic.
- Binance directly states the trading symbol metadata and provides live ticker / kline outputs.

## What is uncertain

- The exact April 19 noon ET close obviously remains unknown.
- Daily klines are contextual only; settlement depends on a single 1-minute close, which can differ materially from daily close or intraday trend.
- We do not have a strong independent explanatory source for what could move SOL between now and settlement; this note is mainly about mechanics and current regime.

## Why this source may matter

This is the main provenance bundle for whether the market is operationally understood correctly and whether current spot leaves enough cushion over the threshold to justify a 90%+ market probability.

## Possible impact on the question

The contract is narrower than a generic “SOL around April 19” view: all of these must hold for Yes — Binance spot SOL/USDT must still be trading, the relevant candle must be the one starting at 12:00 ET / 16:00 UTC, and the final close must be **strictly greater than 80.00**. Because current spot is only mid-80s and recent trading has revisited low-80s repeatedly, the setup looks favorable to Yes but not obviously 90% safe.

## Reliability notes

- Binance is the governing source of truth for settlement, so credibility for resolution mechanics is high.
- Polymarket is authoritative for contract wording but not for price truth.
- These two sources are not economically independent, but they are the correct pair for this case: one defines the contract, the other defines settlement data.