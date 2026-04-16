---
type: evidence_map
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
research_run_id: 2d0e1712-4bcf-4772-9a2a-1b4309a6898b
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
tags: ["evidence-map", "market-implied", "binance", "settlement-check"]
---

# Net assessment

The market's 0.93 Yes price is directionally justified by the large current cushion above 72,000 and by the simple settlement mechanic of a single Binance 1-minute close at noon ET. The main residual risk is short-horizon BTC volatility rather than uncertainty about the governing source.

## Evidence for the market view

- Direct Binance ticker read during research: BTCUSDT 75080.70.
- Direct Binance recent 1-minute candle closes during research: 75025.25, 75048.63, 75077.99.
- Polymarket contract wording is straightforward: Yes if the 12:00 ET Binance BTC/USDT 1-minute candle close is strictly above 72,000.
- Because spot was already about 4.3% above threshold during research, the market does not need an additional rally; it mainly needs BTC not to suffer a substantial drawdown before noon ET.

## Evidence against the market view

- The market resolves at a specific minute, not on a broad average or end-of-day range, so intraday timing risk matters.
- BTC can move several percent in less than a day, so a 4% cushion is meaningful but not ironclad.
- The explicit source-of-truth is the Binance UI candle view rather than a generalized reference index, leaving some exchange-specific operational or display risk at the margin.

## Conflict or netting logic

There is no major source conflict here. The real netting problem is between current distance-to-threshold, which strongly favors Yes, and short-horizon crypto volatility, which keeps No from being trivial.

## Auditability notes

- Governing rule source checked directly on Polymarket event page.
- Direct exchange data checked from Binance public API because the Binance web page itself served a challenge response in this environment.
- Time conversion checked explicitly: observed Binance candle timestamps around 2026-04-16 02:38-02:40 UTC correspond to 2026-04-15 22:38-22:40 ET, confirming the remaining time-to-settlement is about 13 hours rather than a same-minute settlement.

## Bottom line

A high Yes price is reasonable and not obviously stale. My slight discount versus the market comes from residual overnight-to-noon volatility and exchange-specific settlement mechanics, not from a fundamentally bearish BTC view.