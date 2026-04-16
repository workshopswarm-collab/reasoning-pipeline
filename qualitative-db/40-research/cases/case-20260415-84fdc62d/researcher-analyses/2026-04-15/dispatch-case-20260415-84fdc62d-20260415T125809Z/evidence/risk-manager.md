---
type: evidence_map
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
research_run_id: ddbe3337-0269-4228-bf0f-87f75752f460
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on 2026-04-20?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "btc", "timing-risk"]
---

# Summary

The evidence still leans Yes, but the contract’s narrow settlement mechanics make the market’s confidence look slightly too high relative to the remaining path risk.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle close above 70,000 for the 12:00 ET candle on Apr. 20, 2026?

## Current lean

Lean Yes, but with explicit caution against treating the outcome as nearly locked.

## Prior / starting view

Starting view was that the market’s 87.5% price was probably directionally right because spot BTC was already above 74k.

## Evidence supporting the claim

- Source note: `2026-04-15-risk-manager-binance-and-contract.md`
  - Direct evidence: Binance spot BTCUSDT around 74.3k on Apr. 15.
  - Why it matters: provides a material cushion above the 70k threshold.
  - Weight: high.
- Same source note
  - Direct evidence: recent Binance daily closes from Apr. 7 onward all above 70k.
  - Why it matters: suggests the threshold is not merely being touched intraday but has recently been sustained on a daily-closing basis.
  - Weight: medium-high.
- Polymarket rules in same source note
  - Direct evidence: source of truth is explicit, reducing ambiguity over what data series matters.
  - Why it matters: prevents dilution by off-exchange or cross-venue pricing.
  - Weight: medium.

## Evidence against the claim

- Source note: `2026-04-15-risk-manager-contextual-volatility.md`
  - Indirect/contextual evidence: current crypto commentary still flags bull-trap, correction, and overhead-resistance risk in the 70k-75k zone.
  - Why it matters: market narrative still recognizes that downside large enough to threaten 70k is plausible.
  - Weight: medium.
- Source note: `2026-04-15-risk-manager-binance-and-contract.md`
  - Direct contract-risk evidence: resolution depends on one specific minute on one specific exchange.
  - Why it matters: a temporary noon downdraft on Apr. 20 matters more than broader weekly strength.
  - Weight: high.
- Same source note
  - Direct price-history evidence: Binance daily ranges over recent days are several thousand dollars wide.
  - Why it matters: the remaining cushion is meaningful but not immune to ordinary crypto volatility.
  - Weight: medium.

## Ambiguous or mixed evidence

- Recent strength above 74k supports Yes, but because BTC is already well above threshold, some of the remaining uncertainty is mostly about short-horizon volatility rather than trend direction.
- Market price itself is informative, but the extreme probability may also signal overconfidence in a noisy short-term setup.

## Conflict between inputs

There is no hard factual conflict. The disagreement is mostly weighting-based: how much confidence should current spot and recent closes receive versus the remaining five-day volatility and single-minute settlement risk?

## Key assumptions

- The current >70k cushion persists through Apr. 20 noon ET.
- No adverse macro or crypto-specific shock breaks support before settlement.
- Binance’s settlement-relevant print will behave broadly in line with the recent spot regime rather than showing a transient isolated wick below threshold.

## Key uncertainties

- Whether BTC can hold the 72k-74k zone through the next five days.
- Whether a risk-off macro headline or crypto-specific liquidation event emerges before Apr. 20.
- Whether noon ET on the resolution day coincides with a sharp intraday move.

## Disconfirming signals to watch

- Binance spot trading back below 71k before Apr. 20.
- Daily closes deteriorating toward the threshold.
- New evidence of weak ETF/product flow or broader risk-off conditions hitting crypto.

## What would increase confidence

- Additional sessions with Binance daily closes above 72k.
- Stable spot action into Apr. 18-19 without testing 70k.
- Independent flow/context evidence showing downside catalysts have faded.

## Net update logic

The evidence did not flip the baseline Yes lean, but it reduced confidence relative to the market because the contract is narrower than a generic “BTC above 70k this week” thesis. The most important update was recognizing that the real risk is not whether Bitcoin is structurally bullish, but whether one exchange’s noon minute stays above threshold.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review
