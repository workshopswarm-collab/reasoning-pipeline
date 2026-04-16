---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: solana
entity: sol
topic: case-20260416-1f25d147 | risk-manager
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on April 19, 2026 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance SOLUSDT market data and Polymarket rules page
source_type: primary_market_data_plus_contract_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution-source, price-level]
---

# Summary

The governing source of truth is Binance SOL/USDT 1-minute candle data at 12:00 ET on April 19, 2026. As of the research run, Binance spot price was about 85.37 USDT and recent daily/hourly trading showed SOL consistently above 80 for several days, but the contract is not about spot at research time; it is specifically about the final close of the 12:00 ET 1-minute candle on the resolution date.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance SOL/USDT 1-minute candle for 12:00 ET on the specified date has a final close above the listed threshold.
- The rules explicitly exclude other exchanges and other trading pairs.
- Binance ticker endpoint showed SOLUSDT at 85.37 at fetch time.
- Binance daily candles over the prior week showed closes of roughly 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and 85.37, i.e. all above 80.
- The last ~72 hourly candles reviewed ranged mostly from low 82s to high 87s, showing SOL has recently traded with a several-dollar cushion above the 80 threshold.

## Evidence directly stated by source

- Direct contract mechanics: Yes requires the final Binance SOL/USDT 12:00 ET one-minute candle close on April 19 to be strictly greater than 80.
- Direct market condition: Binance spot price at research time was above the threshold.
- Direct contextual price history: recent Binance candles imply the threshold has not been especially close in the last several days.

## What is uncertain

- The source does not directly reveal where SOL will print at exactly 12:00 ET on April 19.
- It does not remove event risk from a broad crypto drawdown over the next ~3.5 days.
- Binance candle availability/UI interpretation could still create operational ambiguity for manual verification, though the contract wording is relatively specific.

## Why this source may matter

This is the closest thing to an authoritative source set for the market because it includes both the contract wording and the exact exchange/pair/source family used for resolution.

## Possible impact on the question

This source strongly supports a Yes-lean because the current spot and recent candle history are above 80, but from a risk-manager lens it mainly shows that the residual No path is concentrated in timing risk, crypto market drawdown risk, or last-minute exchange-specific price dislocation.

## Reliability notes

- Binance API data is highly relevant because Binance is the named resolution source.
- Polymarket page is authoritative for contract wording but not for the resolved price itself.
- This is a strong source set for source-of-truth interpretation, though still not sufficient by itself to eliminate forward-looking market risk.