---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [catalyst-hunter finding]
tags: [polymarket, binance, resolution-rules, source-of-truth]
---

# Summary

This source defines the contract mechanics and the governing settlement source. It is the primary source for what counts, when it counts, and which venue matters.

## Key facts extracted

- The market resolves **Yes** if the **Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 16** has a final **Close** price **higher than 72,000**.
- The stated resolution source is Binance, specifically the BTC/USDT chart with **1m** candles selected.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges or pairs.
- Price precision is determined by the number of decimal places in the source.
- The market page showed the 72,000 line trading around **94%** at fetch time.

## Evidence directly stated by source

- Direct contract language makes clear that all of the following must hold for a Yes resolution:
  1. the relevant exchange is Binance,
  2. the relevant pair is BTC/USDT,
  3. the relevant candle is the 1-minute candle labeled 12:00 PM ET on April 16,
  4. the relevant field is the final Close price,
  5. that Close must be strictly greater than 72,000.

## What is uncertain

- The page does not independently verify whether Binance’s displayed ET labeling could create any edge-case confusion versus UTC timestamps, so a separate timestamp sanity check is still needed.
- The market page itself is not the data source for the closing price; Binance is.

## Why this source may matter

This is the governing rule set. For a narrow, date-specific crypto market, resolution mechanics matter almost as much as directional price view.

## Possible impact on the question

This source sharply narrows the relevant catalyst set: the only thing that truly matters is whether BTC/USDT on Binance stays above 72,000 at the exact noon ET minute-close on April 16. Broad bullish narratives matter only insofar as they affect that specific candle.

## Reliability notes

High reliability for contract wording and settlement logic. Lower utility for market direction beyond the market-implied probability snapshot.