---
type: source_note
case_key: case-20260415-d63a2806
dispatch_id: dispatch-case-20260415-d63a2806-20260415T175526Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance noon ET close-above resolution mechanics for BTC/USDT > 72000 on April 17
question: Will the Binance BTC/USDT 1 minute candle for 12:00 ET on April 17, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page rules
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-d63a2806/researcher-analyses/2026-04-15/dispatch-case-20260415-d63a2806-20260415T175526Z/personas/risk-manager.md
tags: [source-note, polymarket, bitcoin, binance, resolution-rules, noon-close]
---

# Summary

Primary contract source defining what counts for resolution. This source matters because the market is not about spot BTC generally; it is specifically about the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17.

## Key facts extracted

- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final Close price higher than 72,000.
- The resolution source is Binance, with BTC/USDT selected and the 1m candle view.
- Other exchanges or trading pairs do not govern settlement.
- Precision is determined by the source display.
- The market page showed the 72,000 contract trading around 83% at capture time.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The public market page does not itself show the future qualifying candle; it only defines the settlement mechanism.
- The page does not resolve whether timezone display quirks on Binance UI could create interpretation friction, so the operative assumption is that Polymarket resolves from the relevant Binance 1-minute candle mapped to 12:00 ET.

## Why this source may matter

This is the governing source of truth for contract interpretation. It sharply reduces the relevance of non-Binance spot references and also means the event is a close-above contract, not a touch-above contract.

## Possible impact on the question

Because this is a single-minute close-above contract at a fixed future timestamp, path volatility before noon on April 17 matters less than where BTC/USDT is trading around that exact minute. That generally increases timing risk versus broader weekly touch markets.

## Reliability notes

High reliability for contract mechanics because it is the primary rule source. Lower utility for directional forecasting by itself because it does not provide current or expected price trajectory.
