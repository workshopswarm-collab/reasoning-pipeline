---
type: assumption_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
research_run_id: 8830db06-dc60-4771-a35f-912f50967454
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-74k-april-13-19
question: "Will Bitcoin reach $74,000 April 13-19?"
driver: liquidity
date_created: 2026-04-14
agent: catalyst-hunter
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-19"
related_entities: ["bitcoin"]
related_drivers: ["liquidity", "macro"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption-note", "threshold-market", "source-of-truth"]
---

# Assumption

The contract resolves from a standard recognized BTC price source/high-print logic rather than from an idiosyncratic venue print that would exclude the already observed above-74000 trades.

## Why this assumption matters

My probability is extremely high mainly because multiple major spot references already show BTC above 74000 during the relevant week. If the contract uses a narrower or unusual oracle definition, that could create residual failure risk despite broad market evidence.

## What this assumption supports

- A probability estimate materially above the already-high market baseline.
- The conclusion that remaining risk is mostly rule mechanics rather than price-path economics.
- The claim that there is no major upcoming scheduled macro catalyst needed to get the market over the threshold, because the threshold appears already reached in ordinary spot terms.

## Evidence or logic behind the assumption

- Polymarket's fetched page indicates there is a Rules section specifying official data sources.
- Threshold crypto markets usually settle from a named exchange/index/oracle rather than requiring every venue to print the level.
- Multiple independent spot references already show levels at or above 74000, which makes a complete source-of-truth miss less likely unless the contract uses a very specific excluded source.

## What would falsify it

- Rule text showing that only a specific excluded venue or narrowly defined reference counts and that reference never touched 74000.
- An official settlement note indicating that observed spot prints on Coinbase/Kraken/Binance/CoinGecko are irrelevant to the contract.

## Early warning signs

- Inability to identify the contract's named resolution source.
- A visible Polymarket rule specifying a single source that is not among the spot references checked.
- Divergence between broad spot market prints and the named settlement oracle.

## What changes if this assumption fails

The estimate should fall materially, and the analysis should shift from 'already effectively hit' to 'needs direct oracle confirmation.' The main mechanism would become contract interpretation risk rather than market catalyst timing.

## Notes that depend on this assumption

- Main finding at personas/catalyst-hunter.md
- Source note 2026-04-14-catalyst-hunter-btc-spot-and-calendar.md