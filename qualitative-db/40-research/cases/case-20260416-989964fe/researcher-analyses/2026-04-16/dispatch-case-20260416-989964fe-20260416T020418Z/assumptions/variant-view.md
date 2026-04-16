---
type: assumption_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
research_run_id: ba2d7faa-1f0b-433c-a0b5-6267292e531a
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-market-context
entity: ethereum
topic: threshold-cushion-persistence
question: "Will ETH remain above 2200 at the exact Binance noon ET close on April 17?"
driver: reliability
date_created: 2026-04-15
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance exchange canonical slug appears malformed in current entity files"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/variant-view.md"]
tags: ["assumption", "crypto", "threshold", "timing-risk"]
---

# Assumption

ETH's roughly 7% cushion above 2200 on April 16 is large enough that ordinary sub-24-hour volatility is more likely than not to leave the Binance ETH/USDT 12:00 ET close on April 17 still above 2200.

## Why this assumption matters

The high-Yes case depends less on current spot level alone than on whether that cushion is likely to persist through one exact timestamp-based closing print.

## What this assumption supports

- A high but not near-certain Yes probability.
- A modest variant discount versus the market's 95.5% implied probability.
- The conclusion that the main residual risk is downside tail/timing risk rather than present-price uncertainty.

## Evidence or logic behind the assumption

- Multiple live price checks placed ETH near 2355, well above 2200.
- Binance and Coinbase were closely aligned, reducing concern that the cushion was a feed artifact.
- A 7% one-day drawdown is plausible but not the modal path absent a strong adverse catalyst.

## What would falsify it

- A sharp macro or crypto-specific selloff that takes ETH below 2200 before or by April 17 noon ET.
- Evidence that Binance-specific dislocation or an exchange incident makes its noon close diverge materially from broader spot conditions.
- New information showing extreme realized volatility or an imminent event likely to move ETH by more than the current cushion.

## Early warning signs

- ETH rapidly losing the 2300 level before the resolution window.
- Binance trading anomalies, outages, or unusual basis versus Coinbase.
- Broad crypto risk-off moves tied to macro data, regulatory headlines, or leverage unwinds.

## What changes if this assumption fails

The probability should fall materially and the core argument would shift from "large cushion probably survives" to "narrow timestamp risk is underpriced by the market."

## Notes that depend on this assumption

- Main finding at `.../personas/variant-view.md`.