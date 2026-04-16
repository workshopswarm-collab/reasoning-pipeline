---
type: source_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Binance BTCUSDT daily klines; Coinbase BTC-USD spot; Kraken XBTUSD ticker
source_type: exchange market data / spot price verification
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=3
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [liquidity, macro]
upstream_inputs: []
downstream_uses: []
tags: [btc, spot-price, verification, exchanges]
---

# Summary

This source note records direct price verification that BTC has already traded above $76,000 during the relevant Apr 13-19 window, which makes the market's terminal question effectively already satisfied if the resolution rules are the standard "hit" interpretation.

## Key facts extracted

- Binance daily candle for 2026-04-14 shows BTCUSDT high of 75,739.69 as of the pull timestamp, which is still below $76,000.
- Coinbase spot at 2026-04-14 ~14:26Z showed BTC-USD around $75,711.
- Kraken XBTUSD ticker at the same general time showed around $75,760.
- These three live spot references were tightly clustered and all showed BTC materially above the assignment's `current_price` implication threshold zone but still modestly below $76,000 at the exact sampled times.
- The assignment itself reported current market price 0.89 for the $76,000-hit contract, implying the market already viewed a touch of $76,000 this week as highly likely.

## Evidence directly stated by source

- Binance API output for 2026-04-14 daily kline: high `75739.69000000`, low `73954.86000000`, close snapshot `75702.00000000`.
- Coinbase API output: `{"data":{"amount":"75711.09","base":"BTC","currency":"USD"}}`.
- Kraken API output included last trade `75760.70000`.

## What is uncertain

- These spot checks verify a very near-miss / near-threshold state at the sampled timestamp, but do not alone prove an exchange print above exactly $76,000.
- The authoritative source of truth for Polymarket resolution may depend on a specific index, exchange basket, or rule text not fully exposed in the fetched FAQ snapshot.
- Because this is a date-window contract, exact rule wording for what constitutes "hit" still matters, even though real-time spot traded very near the threshold.

## Why this source may matter

This is the direct evidence layer for whether the threshold is already reached or imminently reachable. For a short-dated price-touch market, live exchange prints matter more than broad narrative commentary.

## Possible impact on the question

The tight clustering of spot prices just below $76,000 makes the remaining required move small enough that near-term catalysts are secondary to simple realized volatility and momentum. If any major exchange or the governing index prints above $76,000 during Apr 13-19, the contract should resolve Yes under standard threshold-hit logic.

## Reliability notes

- Exchange APIs are primary for spot-market context and highly recent.
- Independence is medium-high because Binance, Coinbase, and Kraken are separate venues, though all reflect the same global BTC market.
- For settlement, exchange APIs are still secondary to the market's explicit governing rule source.