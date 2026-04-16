---
type: source_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-74k-april-13-19
question: Will Bitcoin reach $74,000 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Coinbase BTC-USD ticker and candles; Binance/Kraken/CoinGecko spot cross-check; BLS CPI release schedule
source_type: mixed_primary_and_contextual
source_url: https://api.exchange.coinbase.com/products/BTC-USD/ticker
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
tags: [case-source-note, btc, spot-price, catalyst-calendar]
---

# Summary

This source cluster matters because the question is date-specific and threshold-based. The most important direct evidence is whether BTC is already trading above $74,000 on major venues during the relevant week; the most important contextual evidence is whether any scheduled macro catalyst still matters for repricing path between now and Apr. 19.

## Key facts extracted

- Coinbase BTC-USD ticker at approximately 2026-04-14T00:21:55Z showed price 74341.67 with bid/ask essentially the same.
- Binance BTCUSDT at the same verification pass showed 74303.56.
- Kraken XBTUSD showed last trade around 74320.2 and an intraday high of 74529.9.
- CoinGecko simple price endpoint showed bitcoin at 74403 USD.
- Coinbase daily candles showed a prior daily bar with high 74936.9, which is comfortably above 74000.
- BLS CPI release calendar shows March 2026 CPI was released Apr. 10, 2026, before this market week, so the major scheduled U.S. inflation catalyst was already behind the market by the time of this research pass.

## Evidence directly stated by source

- Direct threshold evidence: Kraken public ticker returned a 24h high above 74000 and live spot near 74320.
- Direct threshold evidence: CoinGecko and Coinbase both showed spot above 74000 during the verification pass.
- Contextual catalyst evidence: BLS schedule explicitly lists Mar. 2026 CPI release on Apr. 10, 2026 at 08:30 AM.

## What is uncertain

- The exact governing resolution source on Polymarket is not recoverable from the lightweight fetch output alone; the page fetch advises reading the Rules section but does not expose the rule text cleanly.
- Because the specific oracle/rule text was not machine-extracted, there remains minor ambiguity about whether resolution keys off an exchange-specific print, an index high, or another official source.
- I do not have a clean authoritative weekly catalyst calendar for all Fed speaker appearances during Apr. 13-19 from the fetched sources alone.

## Why this source may matter

- For a reach-threshold market, direct evidence that BTC is already above the threshold early in the week is the dominant causal fact.
- Once spot is already above 74000 on multiple major venues, the remaining catalysts matter mainly for whether there is any hidden source-of-truth trap, not for economic probability in the ordinary sense.

## Possible impact on the question

- This evidence strongly supports a very high probability that the market resolves Yes / above 74000 at some point during Apr. 13-19, assuming standard high-print threshold rules.
- The main residual risk is contract mechanics rather than market direction.

## Reliability notes

- Exchange API data are highly recent and directly relevant, but they are not guaranteed to be the contract's formal source of truth.
- Cross-exchange agreement materially reduces single-venue error risk.
- BLS is a strong primary source for the macro calendar and helps show that the biggest scheduled U.S. inflation catalyst had already occurred before the week in question.