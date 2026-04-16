---
type: assumption_note
case_key: case-20260416-969f7c01
research_run_id: 810c1ece-82f1-479d-9fb3-d4c2b39fb0eb
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price-threshold-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<48h"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "binance", "timing", "crypto"]
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
---

# Assumption

The relevant Binance ETH/USDT market remains normally functioning through the Apr 17 noon ET resolution window and the visible 12:00 ET one-minute candle maps cleanly to the contract language.

## Why this assumption matters

The market is settled on a narrow operational observation, not on a daily close or a multi-exchange average. If Binance data presentation, candle timing, or market functioning behaves abnormally, interpretation risk rises even if broad ETH spot remains above 2200.

## What this assumption supports

- A high-probability Yes view based mostly on spot cushion above the strike.
- The judgment that ordinary price volatility, rather than settlement mechanics, is the main residual risk.
- Treating external ETH/USDT context as relevant directional evidence for the contract.

## Evidence or logic behind the assumption

- Polymarket explicitly names Binance ETH/USDT 1-minute candles as source of truth, implying the venue and chart convention are usually stable enough to use operationally.
- There is no assignment-specific evidence of an outage, delisting, or special contract ambiguity.
- For liquid major crypto pairs, the default base rate is ordinary continuity rather than a venue-level failure exactly at settlement.

## What would falsify it

- Binance outage, charting failure, or symbol disruption near the resolution minute.
- Evidence that the contract's 12:00 ET label maps differently than expected to Binance's displayed candle timestamps.
- A rule clarification indicating a different data surface or treatment of incomplete/finalized candles.

## Early warning signs

- Reports of Binance execution or chart issues near Apr 17.
- Visible discrepancies between Binance and reputable aggregators around the resolution window.
- Community confusion or moderator clarification requests about which minute counts.

## What changes if this assumption fails

Confidence in a simple price-level inference should drop. The question would become partly operational and interpretive rather than mostly a spot-price threshold judgment.

## Notes that depend on this assumption

- The main base-rate finding for this dispatch.
- The evidence map for this dispatch.
