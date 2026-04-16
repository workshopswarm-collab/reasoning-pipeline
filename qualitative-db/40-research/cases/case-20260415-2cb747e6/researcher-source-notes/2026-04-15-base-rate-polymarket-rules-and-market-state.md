---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market primary / contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [base-rate finding]
tags: [polymarket, contract-rules, market-state, resolution-source]
---

# Summary

The Polymarket market page provides the live market-implied probability for the $72,000 threshold and the governing contract language. It states that resolution depends specifically on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, 2026, using the final close price, and that the outcome is Yes only if that close is strictly higher than 72,000.

## Key facts extracted

- The assigned market is the April 16 threshold ladder for Bitcoin.
- The $72,000 threshold was trading around 90% at fetch time, consistent with the assignment field `current_price: 0.895`.
- Resolution is tied to Binance BTC/USDT, not other exchanges or pairs.
- The relevant candle is the 12:00 ET 1-minute candle on April 16, 2026.
- The candle must have a final close price higher than 72,000; equality does not count.
- Price precision is determined by the source display.

## Evidence directly stated by source

- The market resolves to Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final close above the threshold.
- The market resolves to No otherwise.
- Binance is the explicit source of truth.

## What is uncertain

- The public market page is not itself the ultimate settlement source; it describes the source-of-truth process.
- The page does not by itself provide the future April 16 noon ET candle.
- It does not clarify whether Binance UI/API presentation differences could matter, so operational interpretation risk remains low but nonzero.

## Why this source may matter

This is the primary contract/rules source. It defines the exact condition set that all must hold: correct venue (Binance), correct pair (BTC/USDT), correct time (12:00 ET on April 16), correct interval (1 minute), and strict comparison (> 72,000).

## Possible impact on the question

This source frames the market as a narrow date-and-time threshold event rather than a general daily close or cross-exchange Bitcoin price question. That makes short-horizon price level persistence and timing risk more important than broad bullish sentiment alone.

## Reliability notes

Polymarket is authoritative for contract wording but not for the underlying future price. Reliability is high for the resolution mechanics and only medium for informational context around current price/odds.