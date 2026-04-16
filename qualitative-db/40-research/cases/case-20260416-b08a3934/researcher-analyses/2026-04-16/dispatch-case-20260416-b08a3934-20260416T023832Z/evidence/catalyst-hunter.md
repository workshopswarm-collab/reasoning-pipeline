---
type: evidence_map
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
research_run_id: 34fd3e48-baa4-4b25-8c6a-521ce63966f9
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 72000?"
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
proposed_drivers: ["macro-event-timing"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-b08a3934/researcher-analyses/2026-04-16/dispatch-case-20260416-b08a3934-20260416T023832Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "btc", "settlement", "catalyst"]
---

# Summary

This evidence map nets a simple but timing-sensitive setup: the contract is mostly a short-window path question because BTC is currently well above the strike, but the exact noon ET Binance 1m close and any late downside catalyst still matter.

## Question being evaluated

Whether Binance BTC/USDT will have a final 12:00 ET one-minute candle close above 72,000 on April 17, 2026.

## Current lean

Lean Yes, high but not near-certainty.

## Prior / starting view

Starting view from market price was that Yes was highly likely at roughly 91% implied.

## Evidence supporting the claim

- **Current Binance spot materially above strike**
  - source: case source note on Polymarket rules + Binance API
  - why it matters causally: current distance from strike means a substantial downside move is required before settlement
  - direct or indirect: direct on current price, indirect on final settlement
  - weight: high

- **Settlement mechanics are straightforward once exact source is identified**
  - source: Polymarket rules page
  - why it matters causally: reduces ambiguity about what counts; one Binance 1m close decides the market
  - direct or indirect: direct
  - weight: high

- **No identified scheduled catalyst in this run that obviously forces repricing >4% lower before noon ET**
  - source: research process plus failed/limited contextual fetches
  - why it matters causally: absent a clear catalyst, persistence near current level is the default
  - direct or indirect: indirect
  - weight: medium

## Evidence against the claim

- **Short-dated BTC can move multiple percent on headlines or liquidation cascades**
  - source: contextual market knowledge, reflected as assumption/fragility rather than a single external note here
  - why it matters causally: path risk remains meaningful over 13+ hours
  - direct or indirect: indirect
  - weight: medium

- **Exact minute-close mechanics can punish a broadly right directional call**
  - source: Polymarket rules page
  - why it matters causally: a brief dip or settlement-window volatility matters more than daily close intuition
  - direct or indirect: direct
  - weight: medium

- **Binance UI inaccessible from runtime due to WAF challenge**
  - source: direct runtime verification
  - why it matters causally: introduces a small operational verification gap between named UI surface and accessible API surface
  - direct or indirect: direct
  - weight: low

## Ambiguous or mixed evidence

- Broader macro calendar risk exists in principle, but no single scheduled item was verified here as likely to dominate this exact window.
- CoinDesk contextual fetch provided little usable market detail, so it adds minimal independent weight.

## Conflict between inputs

No major factual conflict found. The main tension is between high current price distance above strike and residual short-window crypto volatility.

## Key assumptions

- No major adverse catalyst before settlement.
- Binance API path is a faithful proxy for the UI-based settlement surface.
- Noon ET timezone handling on the market page is literal and not subject to hidden conversion quirks.

## Key uncertainties

- Overnight headline risk.
- Exact realized volatility into US morning.
- Any edge-case mismatch between public API and the UI candle referenced in rules.

## Disconfirming signals to watch

- BTCUSDT losing 74k and then 73k before US morning.
- Sharp risk-off macro headlines.
- Evidence of Binance display/API inconsistency around candle closes.

## What would increase confidence

- BTC holding above 74.5k into US morning.
- Another direct Binance check closer to settlement.
- Confirmation that no major scheduled macro release lands in the final hours.

## Net update logic

The evidence keeps the starting high-Yes view intact but not at the market's full level. The main downweight versus the market is ordinary short-window crypto path risk plus a small operational verification gap around the exact Binance UI settlement surface.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, especially to frame the case as a timing-risk question rather than a broad directional Bitcoin thesis.
