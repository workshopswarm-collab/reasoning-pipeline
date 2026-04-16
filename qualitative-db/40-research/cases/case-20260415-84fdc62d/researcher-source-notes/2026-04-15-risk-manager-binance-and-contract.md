---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules + Binance market data endpoints
source_type: market rules / exchange data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
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
downstream_uses: []
tags: [polymarket, binance, resolution-source, btc]
---

# Summary

This source note combines the governing contract text from the Polymarket market page with contemporaneous Binance BTC/USDT price data used for directional context. It matters because this is a narrow-resolution market whose source-of-truth and timing mechanics can dominate ordinary thesis arguments.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT **1-minute candle for 12:00 ET on Apr. 20** has a final **Close** price above 70,000.
- The governing venue is specifically **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- The assignment current price is 0.875, implying about **87.5%** market probability.
- Binance spot API data checked on 2026-04-15 shows BTCUSDT around **74,257.29**.
- Recent Binance daily closes from Apr. 7-15 were mostly above 70,000, with one close at **68,853.66** on Apr. 6 and all closes from Apr. 7 onward above 70,000.
- Recent realized daily range is still large enough that a several-thousand-dollar move over five days is plausible; Apr. 14 high/low was roughly **76,038 / 73,795**, and Apr. 13 high/low was roughly **74,900 / 70,567**.

## Evidence directly stated by source

- The contract source of truth is Binance and the relevant field is the final 1-minute candle close at 12:00 ET.
- Price precision is determined by Binance’s displayed decimal precision.
- Binance API outputs direct market prices and recent OHLC data for BTCUSDT.

## What is uncertain

- The live Binance trade page itself was not machine-readable via web_fetch, so the contract interpretation relies on Polymarket’s copied rule text plus Binance API market data rather than the rendered chart UI.
- The exact 12:00 ET candle on Apr. 20 is not yet knowable.
- Short-horizon macro or crypto-specific shocks could still move BTC several percent before resolution.

## Why this source may matter

This is the main source for both contract mechanics and the direct state variable that will settle the market. It bounds what actually counts and prevents over-weighting other exchanges, broader narratives, or non-noon prints.

## Possible impact on the question

The source supports a base case of Yes because spot BTCUSDT is already materially above 70,000 with several recent daily closes above that level. But it also highlights the main risk-manager objection: the contract is path-sensitive to one specific minute on one exchange, so a five-day selloff or a sharp intraday downdraft at noon ET could still flip the outcome.

## Reliability notes

- Polymarket market page is the authoritative contract/rules source for the prediction market.
- Binance API is a direct exchange-data source for BTCUSDT price context, though not itself the exact rendered chart UI named in the rule text.
- Independence between these sources is medium: Polymarket provides rules; Binance provides price data. They are complementary rather than fully independent.
