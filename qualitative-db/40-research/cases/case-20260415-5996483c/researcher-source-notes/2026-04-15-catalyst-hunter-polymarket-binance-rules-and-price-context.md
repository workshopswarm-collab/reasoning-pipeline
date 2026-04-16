---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin-threshold-daily-close
entity: btc
topic: Polymarket April 20 BTC above 70000 contract mechanics and Binance context
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance public market data
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, btc, threshold-market]
---

# Summary

This source note captures the direct contract mechanics from Polymarket and the contemporaneous Binance market context used to evaluate the April 20 noon-ET threshold question.

## Key facts extracted

- Polymarket states the market resolves **Yes** if the **Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 20, 2026** has a final **Close** price **higher than 70,000**.
- The rules explicitly say the governing source is **Binance**, not other exchanges or trading pairs.
- Price precision is determined by the Binance source.
- The market page showed the **70,000** line trading around **92%** at fetch time.
- Binance public API spot price during this run was about **75,252 USDT**.
- Recent Binance daily candles showed BTC had closed above 70,000 for several consecutive days, with recent daily highs reaching about **76,038** and even the recent pullback day still closing around **70,741**.

## Evidence directly stated by source

From the Polymarket market page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

From Binance public market data gathered during the run:
- Spot price: about **75,251.99** BTC/USDT.
- Recent daily candles (UTC sessions) around Apr. 10-15 showed closes near **73,043**, **70,741**, **74,418**, **74,132**, and **75,260**.
- Recent realized range remained wide enough that a 5-day path back below 70,000 at the precise observation minute is possible but not the base case.

## What is uncertain

- The contract resolves on **one exact minute close** at **12:00 ET on Apr. 20**, not on current spot, daily high, or daily close.
- Binance website-display candles and Binance API representations should usually align, but the contract text points to the Binance trading interface as the named settlement surface.
- A large BTC move over the remaining window could still push the exact observation-minute close below 70,000 despite current trading well above the threshold.

## Why this source may matter

This is the governing market/rules source and the most direct available context for whether the threshold is already comfortably in the money versus still vulnerable to short-term volatility.

## Possible impact on the question

The direct rules make this a **single-minute close-above threshold** contract with clear source specificity. That materially lowers ambiguity versus a broader interpretive market, but it also means analysts must avoid overclaiming from non-Binance prices or from highs/touches. Current Binance levels around 75k make Yes favored, but the exact noon-ET close remains the operative event.

## Reliability notes

- **Primary-source strength:** high for resolution mechanics because the rules are explicit.
- **Contextual strength:** high for current price context because Binance public data is the same exchange family named in the rules, though the contract specifically references the trading interface candle surface.
- **Main caveat:** this is still a forward-looking price market, so current price context is informative rather than dispositive.