---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-11 close above 72000?
driver: operational-risk
date_created: 2026-04-11
source_name: Binance public market data API and trading pair reference
source_type: exchange API / exchange resolution source
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-11
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/variant-view.md]
tags: [binance, btcusdt, resolution-source, minute-candle]
---

# Summary

Binance public BTCUSDT data confirms the exact contract pair exists, that current spot is above 72,000 during the research window, and that recent 1-minute candle closes are also above 72,000. This matters because the market settles on Binance BTC/USDT specifically rather than broader BTC/USD composites.

## Key facts extracted

- Binance pair used by contract wording is explicitly `BTCUSDT` / `BTC_USDT`.
- Binance ticker price during research was about `72872.80` to `72872.81`.
- Binance 24h endpoint showed last price `72872.81000000`, 24h high `73434.00000000`, 24h low `71426.15000000`, and open `71886.22000000`.
- Recent 1-minute klines retrieved from Binance all closed above 72,000 in the sampled window.
- Example sampled closes from the last five minutes fetched during research: `72873.55`, `72863.15`, `72847.55`, `72861.31`, `72872.81`.

## Evidence directly stated by source

- `ticker/price` returned `{\"symbol\":\"BTCUSDT\",\"price\":\"72872.80000000\"}`.
- `ticker/24hr` returned last price `72872.81000000` and high/low/open fields.
- `klines` returned 1-minute candles for `symbol=BTCUSDT&interval=1m`, confirming the pair and candle format used by the contract are available directly from Binance infrastructure.

## What is uncertain

- The exact noon-ET resolution candle is still in the future at research time.
- Public API responses verify Binance market data mechanics, but the contract text points traders to the Binance web chart with `BTC_USDT`, 1m, candles selected; there is some interface-versus-API ambiguity even though both appear to reference the same underlying pair.
- This note does not independently prove how Polymarket handles any later Binance corrections or UI data revisions.

## Why this source may matter

This is the closest thing to the governing source of truth before the event itself. It directly addresses the case-specific checks around exact pair selection, candle mechanics, and whether BTC is currently trading above the threshold.

## Possible impact on the question

The direct Binance data supports a bullish base case for Yes because spot and sampled minute closes are already above 72,000. It also weakens any thesis that the market is underpricing a simple arithmetic condition. The remaining risk is mostly path and timing risk into the exact noon-ET minute close, not ambiguity about the pair being measured.

## Reliability notes

Binance is the named settlement source in the market rules, so credibility for contract interpretation is high. Independence is limited because all direct settlement evidence comes from the same source family. That makes a separate contextual source useful for sanity-checking price level and market framing, but not for replacing Binance as the governing source.