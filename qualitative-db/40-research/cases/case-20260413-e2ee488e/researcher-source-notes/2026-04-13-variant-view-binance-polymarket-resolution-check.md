---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-15 close above 70000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market rules and Binance BTCUSDT spot API spot check
source_type: primary_plus_verification
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/variant-view.md]
tags: [source-note, polymarket, binance, resolution-check, btc]
---

# Summary

This note captures the direct resolution mechanics from Polymarket and a verification pass on Binance spot data surfaces relevant to the contract.

## Key facts extracted

- Polymarket states the market resolves **Yes** if the Binance **BTC/USDT 1 minute candle for 12:00 ET (noon) on April 15** has a final **Close** price higher than **70,000**.
- The market is explicitly about **Binance BTC/USDT**, not other exchanges or other pairs.
- Price precision is determined by the source display / source decimals.
- A live Binance API spot check on 2026-04-13 showed BTCUSDT around **74.27k**.
- A Binance 1-minute kline API check returned normal 1-minute OHLC rows with a close field, consistent with the contract’s operational reference to a 1-minute candle close.

## Evidence directly stated by source

From Polymarket rules page:
- Resolution depends on the Binance BTC/USDT 12:00 ET 1-minute candle close on the specified date.
- The relevant comparison is whether the final close is **higher than** 70,000.
- Exchange/pair substitution is not allowed.

From Binance API verification:
- `ticker/price?symbol=BTCUSDT` returned `74265.28000000` on this pass.
- Recent `klines?symbol=BTCUSDT&interval=1m&limit=5` returned standard OHLCV rows, including close values in the fifth position.

## What is uncertain

- The contract text references the Binance web chart UI as settlement source; API parity is likely but not explicitly guaranteed in the market text.
- Current price does not settle the market; only the specific 12:00 ET April 15 one-minute close matters.
- Intraday volatility between now and the settlement minute can still change the outcome materially.

## Why this source may matter

This is the governing source-of-truth surface for contract interpretation and establishes that the key risk is not generic Bitcoin direction but whether BTC/USDT remains above 70k at one specific noon ET snapshot.

## Possible impact on the question

The direct rules support a bullish base case because BTC is currently several thousand dollars above the threshold, but they also create a variant-view opening: even a broadly bullish BTC regime can still fail this contract if a sharp drawdown or noon-specific dip pushes the single minute close below 70k.

## Reliability notes

- Polymarket rules are the authoritative contract surface for how the market should resolve.
- Binance API checks are strong contextual verification of current price level and candle structure, but are still secondary to the exact Binance settlement surface named in the rules.
- Evidence independence is moderate: Polymarket rules define the contract, while Binance provides the underlying market data surface.