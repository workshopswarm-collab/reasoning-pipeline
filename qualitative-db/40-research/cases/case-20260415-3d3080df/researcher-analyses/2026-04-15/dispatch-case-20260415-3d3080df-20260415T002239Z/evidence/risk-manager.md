---
type: evidence_map
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
research_run_id: b603bf79-c092-47de-a55d-cd4ad0269efa
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold", "timing-risk"]
---

# Summary

Evidence nets to a Yes lean, but with more fragility than the 87.5% market price suggests, because the contract resolves off one exact Binance minute close rather than a broader daily condition.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20 close above 70,000?

## Current lean

Lean Yes, but less confidently than market.

## Prior / starting view

Starting view was that a market at 0.875 likely reflected a straightforward spot-above-threshold setup, but required rule verification because the market is date-sensitive, source-specific, and extremely priced.

## Evidence supporting the claim

- Polymarket rules specify a simple threshold test on Binance BTC/USDT at a single minute close; there are no extra conditions beyond source, pair, time, and threshold. Direct, high weight.
- Binance API verification showed BTCUSDT around 74,559, leaving a cushion of roughly 4,559 above the threshold. Direct for current state, medium-high weight.
- CoinGecko contextual cross-check showed bitcoin around 74,611 USD at about the same time, supporting the view that Binance was not obviously idiosyncratic at assignment time. Indirect/contextual, medium weight.

## Evidence against the claim

- The contract is narrow: one exact 12:00 ET one-minute candle close. A brief selloff exactly into that minute is enough to flip resolution even if BTC is above 70k most of the surrounding period. Direct contract fragility, high weight.
- The market is priced at an extreme probability despite several days remaining; multi-day BTC moves of more than 6% are not rare enough to ignore. Contextual/base-rate style evidence, medium-high weight.
- Binance-specific source risk matters because only Binance BTC/USDT counts, not a cross-exchange average. Direct contract/source dependence, medium weight.

## Ambiguous or mixed evidence

- Current spot being well above 70k is supportive, but crypto’s realized volatility means the current buffer can erode quickly.
- The same source specificity that makes settlement precise also creates operational/path fragility.

## Conflict between inputs

No major factual conflict between checked inputs. The disagreement is between current market confidence and the risk-manager weighting of timing/path fragility.

## Key assumptions

- BTC retains enough cushion over 70k into April 20 noon ET.
- Binance BTC/USDT remains a fair operational reflection of broader BTC spot at settlement time.
- No major macro, regulatory, or crypto-specific shock occurs before the relevant minute.

## Key uncertainties

- BTC volatility over the next five days.
- Potential weekend price swings before the Monday noon ET settlement.
- Whether the market is underpricing the single-minute close risk.

## Disconfirming signals to watch

- BTC falls toward 71k or below before settlement.
- Binance-specific pricing deviates from other major venues.
- New macro or crypto-specific adverse headlines emerge close to settlement.

## What would increase confidence

- BTC still trading comfortably above 72k-73k late on April 19 or early April 20.
- Continued absence of venue-specific operational issues on Binance BTC/USDT.

## Net update logic

Contract verification and current spot context were enough to support a Yes view, but the risk-manager adjustment comes from the gap between “currently above threshold” and “will settle above threshold on one exact minute close several days from now.” That fragility keeps my estimate below market.

## Suggested downstream use

Use as orchestrator synthesis input and decision-maker review material, especially for calibrating whether the extreme market confidence should be discounted for narrow timing risk.