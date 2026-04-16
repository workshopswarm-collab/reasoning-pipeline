---
type: assumption_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
research_run_id: 1991a652-fda6-4b69-a906-a0d47582b3ca
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: intraworkweek
related_entities: ["bitcoin", "polymarket"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["crypto-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/variant-view.md"]
tags: ["assumption", "threshold-market", "source-of-truth"]
driver:
---

# Assumption

The market will resolve off a source/method that is economically close enough to broad spot pricing that a continued BTC rally into the mid-75k area gives a high, but not certain, chance of printing 76k during Apr 13-19.

## Why this assumption matters

Most of the bullish case comes from proximity to the threshold rather than from a direct already-settled print. If the governing source or exact threshold-touch mechanics differ from the broad spot feeds I checked, the probability could be lower than the market implies.

## What this assumption supports

- A moderately lower-than-market estimate rather than a sharp bearish call.
- Treating residual risk as microstructure / resolution risk rather than a macro directional BTC thesis.

## Evidence or logic behind the assumption

- Binance 24h data and Coingecko hourly data both place BTC in the high-75k neighborhood, close enough that an ordinary continuation move could hit 76k.
- The contract is a weekly hit-style market, so an intraperiod spike matters more than a final close.

## What would falsify it

- Clean rule text showing a governing source materially different from the spot references checked here.
- A reversal that pushes BTC well away from 76k and keeps it there through most of the window.
- A verified print above 76k on the governing source, which would make this residual-risk framing too conservative.

## Early warning signs

- Repeated inability of BTC to break the mid-75k range despite broad market strength.
- Evidence of venue-specific basis that leaves the governing source below 76k while contextual feeds approach it.
- Clarified rules indicating a narrower source-of-truth than assumed.

## What changes if this assumption fails

If the governing source is materially narrower or BTC momentum stalls, the probability should move down meaningfully. If a verified governing-source print above 76k appears, the probability should move toward near-certainty.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/variant-view.md
- qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-source-notes/2026-04-14-variant-view-btc-76k-verification.md