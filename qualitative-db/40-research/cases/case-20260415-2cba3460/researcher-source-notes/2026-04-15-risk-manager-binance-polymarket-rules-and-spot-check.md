---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-market-structure
entity: btc
topic: case-20260415-2cba3460 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page plus Binance API spot/1m market data check
source_type: primary+direct
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: risk-manager
related_entities: [btc]
related_drivers: [operational-risk, liquidity, macro]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-rules, spot-price, direct-evidence]
---

# Summary

This source note combines the contract text from the Polymarket market page with a direct Binance API spot/1-minute data verification pass. It establishes the governing resolution mechanics and confirms that BTC/USDT was trading materially above 72,000 during the research run, while also clarifying that the market resolves on a very specific Binance 1-minute close at 12:00 ET on April 16 rather than on broader BTC price levels.

## Key facts extracted

- Polymarket rules state the market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16 has a final Close strictly higher than 72,000.
- The market is explicitly tied to Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by Binance source precision.
- During the research run, Binance API returned BTCUSDT spot around 74,194 to 74,196.
- Binance 24-hour ticker showed last price around 74,195.81, 24h high 76,038.00, and 24h low 73,514.00.
- Recent 1-minute klines sampled during the run all closed around 74,173 to 74,194, comfortably above 72,000.

## Evidence directly stated by source

From Polymarket rules page:
- Resolution source is Binance BTC/USDT.
- Required datapoint is the 12:00 ET 1-minute candle Close on April 16.
- Outcome is Yes only if that Close is higher than 72,000.

From Binance API responses observed during the run:
- ticker/price returned 74,194.00000000.
- ticker/24hr returned lastPrice 74,195.81000000 and lowPrice 73,514.00000000.
- recent 1-minute klines closed near 74,179, 74,173, 74,188, and 74,194.

## What is uncertain

- The decisive print is tomorrow's 12:00 ET candle close, not the current spot level.
- Short-horizon crypto volatility can move BTC by more than 2,000 in a day, so being above 72,000 now does not eliminate path risk.
- The market page is authoritative for contract wording, but the final settlement datapoint will come from Binance’s live/chart surface at the relevant time.

## Why this source may matter

This is the core direct-evidence bundle for the case. It defines exactly what has to happen and shows that the current market state is above the threshold by roughly 2.2k, which explains why the market is pricing a high probability. It also highlights the main fragility: the contract depends on one precisely timed Binance close, so short-term downside volatility or exchange-specific print differences can still defeat an otherwise bullish baseline.

## Possible impact on the question

The direct evidence supports a Yes lean because current Binance pricing is materially above 72,000. But it also supports a risk-manager discount versus a near-certainty framing because all material conditions must hold simultaneously: Binance must be the reference venue, the relevant candle must be the noon ET candle on April 16, and its final close must still print above 72,000.

## Reliability notes

- Polymarket rules page is the governing contract source for what counts.
- Binance API is a strong direct contextual verification surface for current BTC/USDT conditions, though not itself the final settlement observation yet.
- Evidence independence is only moderate because both sources concern the same contract/venue complex; this is enough for a medium-difficulty, date-specific market but still leaves timing risk.