---
type: source_note
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules plus Binance current spot / 1-minute market-data check
source_type: primary+contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-17 ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-3e035ad7/researcher-analyses/2026-04-16/dispatch-case-20260416-3e035ad7-20260416T043505Z/personas/catalyst-hunter.md]
tags: [binance, polymarket, catalyst, timing, source-note]
---

# Summary

This note isolates the only clearly material catalyst structure for the April 17 BTC-above-70000 market: the exact settlement timestamp itself. There is no identified scheduled event in the assignment materials more important than the noon ET Binance candle that directly determines resolution.

## Key facts extracted

- Polymarket resolves the market from the Binance BTC/USDT **1-minute candle for 12:00 ET on April 17, 2026**.
- The decisive field is that candle's final **Close** price.
- The threshold is strict: the close must be **higher than 70000**.
- The assigned market-implied probability is **99.15%**.
- Existing case source notes verified Binance BTCUSDT around **74975.57** on 2026-04-16 04:36 UTC, leaving roughly a **7.1% cushion** over the threshold about 31 hours before resolution.
- Existing case notes also verified Binance exchange timestamps in **UTC**, implying the relevant settlement minute is approximately **2026-04-17 16:00 UTC** because ET on that date is EDT (UTC-4).

## Evidence directly stated by source

- Polymarket states that Binance BTC/USDT 12:00 ET 1-minute candle close is the resolution source.
- Binance public market data confirms BTCUSDT is trading materially above the threshold and that 1-minute candle data exists.

## What is uncertain

- This note does not identify a single exogenous scheduled macro or policy catalyst that is more important than ordinary BTC volatility over the remaining window.
- The formal resolution surface is the Binance UI candle display, while the verification pass used Binance API data as an operational proxy.
- A sudden macro shock, liquidation cascade, or Binance-specific wick could still push the exact settlement minute below 70000.

## Why this source may matter

For a one-minute crypto threshold market already trading at an extreme implied probability, the main catalyst question is whether any event before noon ET on April 17 is more important than the settlement minute itself. The answer here appears to be no. The critical catalyst is the countdown to that exact candle, with the highest information value arriving in the final hours before noon ET.

## Possible impact on the question

This source set supports a catalyst view that is mostly pro-Yes but slightly less certain than the market: absent a discrete downside shock, the most plausible path is that BTC remains above 70000 into settlement, but the remaining No path is concentrated in a late selloff or exchange-specific one-minute dislocation near the final timestamp.

## Reliability notes

Reliability is high for contract mechanics and current price context because the evidence comes from the governing market page and the named exchange's direct market-data surfaces. Independence is only medium because both surfaces ultimately anchor to the same exchange market, but they answer different parts of the problem: contract definition versus current state.