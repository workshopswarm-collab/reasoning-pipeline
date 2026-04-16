---
type: assumption_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
research_run_id: 283687c8-f7b4-4ad3-b5c1-16bfeefe0ee1
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: april-13-19-bitcoin-price-thresholds
question: "Will Bitcoin reach $76,000 April 13-19?"
driver:
date_created: 2026-04-14
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: "2026-04-13 to 2026-04-19"
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["threshold-touch-resolution-method"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/personas/risk-manager.md"]
tags: ["assumption-note", "resolution", "bitcoin", "threshold-market"]
---

# Assumption

The practical working assumption is that a broad, liquid spot-market print near or above $76,000 during Apr 13-19 will correlate closely enough with the contract’s governing source of truth that analyzing mainstream spot price action is directionally informative.

## Why this assumption matters

The probability estimate depends on using observable market prices as a proxy for what the contract is likely to count. If that linkage is weak, then proximity on major venues could be misleading.

## What this assumption supports

- A moderate Yes probability despite no confirmed governing-source threshold hit yet.
- Use of Binance and CoinGecko as decision-useful evidence rather than noise.
- The view that path risk is more important than end-of-week closing level.

## Evidence or logic behind the assumption

- Bitcoin is highly liquid across venues, so large price threshold moves often propagate broadly.
- The market is framed as a price-hit question, making intraperiod touch dynamics more relevant than weekly close.
- Major liquid spot sources are usually directionally informative even when they are not the exact settlement source.

## What would falsify it

- Explicit contract rules showing settlement is based on a narrow venue, specific index, or methodology that can diverge materially from broad spot prints.
- Evidence that BTC printed 76k on one watched venue but not on the settlement source in analogous Polymarket resolution practice.

## Early warning signs

- Ambiguous or inaccessible rule text about source-of-truth.
- Large cross-venue dispersion around the threshold.
- A fast rejection from the 75k area suggesting momentum is weaker than proximity alone implies.

## What changes if this assumption fails

Confidence in the Yes case should fall because observed near-threshold price action would no longer map cleanly to settlement odds. The market could then be overpricing a simple spot-proximity narrative.

## Notes that depend on this assumption

- Main risk-manager finding for this dispatch.
- Evidence map for support-versus-fragility netting.