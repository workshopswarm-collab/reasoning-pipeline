---
type: evidence_map
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
research_run_id: f49d769a-4acd-4f42-8e72-972d9bfbdf54
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["macro-calendar-gap"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalysts", "timing"]
---

# Summary

The evidence nets to a moderately strong Yes lean: the contract is narrow but clear, BTC currently has a multi-thousand-dollar cushion above the strike on the named venue, and one obvious scheduled macro catalyst (CPI) is already behind the market. The main residual risk is simply that crypto can still move fast enough over six days to make the exact noon ET one-minute close fall below 70k.

## Question being evaluated

Whether Binance BTC/USDT will have a final 12:00 ET one-minute candle close above 70,000 on Apr. 20, 2026.

## Current lean

Lean Yes.

## Prior / starting view

Starting view was that an 85% market-implied probability looked plausible but required explicit checking because the contract is date-sensitive, venue-specific, and extreme-priced.

## Evidence supporting the claim

- **Polymarket rules are narrow and explicit**  
  - Source: Polymarket rules source note.  
  - Why it matters: removes ambiguity about exchange, pair, and candle type.  
  - Direct or indirect: direct for contract interpretation.  
  - Weight: high.

- **Binance live BTCUSDT is already ~74.2k, well above 70k**  
  - Source: Binance API source note.  
  - Why it matters: current buffer is ~4k+, so the market does not need a fresh upside move; it mainly needs BTC not to suffer a significant drawdown by settlement.  
  - Direct or indirect: direct for current state, indirect for Apr. 20 outcome.  
  - Weight: high.

- **24h Binance range also remained above 70k**  
  - Source: Binance API source note.  
  - Why it matters: shows the threshold is not just barely met at one instant; recent realized range still clears it.  
  - Direct or indirect: indirect/contextual.  
  - Weight: medium-high.

- **No CPI release sits between now and settlement**  
  - Source: BLS CPI schedule note.  
  - Why it matters causally: removes one obvious scheduled macro repricing event that could have forced a large move before settlement.  
  - Direct or indirect: indirect/timing.  
  - Weight: medium.

## Evidence against the claim

- **Six days is long enough for BTC to move >5% to >6%**  
  - Source: inference from crypto volatility plus the contract’s exact-minute structure.  
  - Why it matters: a drop from ~74.2k to sub-70k is large but not extraordinary for BTC over multi-day windows.  
  - Direct or indirect: indirect.  
  - Weight: high.

- **Resolution is based on one exact minute, not a daily average**  
  - Source: Polymarket rules and Binance kline mechanics.  
  - Why it matters: timing noise, intraday volatility, or a brief selloff at noon ET can matter disproportionately.  
  - Direct or indirect: direct for mechanics.  
  - Weight: high.

- **Catalyst coverage outside CPI is incomplete**  
  - Source: verification limits during this run.  
  - Why it matters: Fed communication, ETF flow shocks, or geopolitical headlines could still create repricing.  
  - Direct or indirect: indirect.  
  - Weight: medium.

## Ambiguous or mixed evidence

- Bitcoin’s current distance above 70k supports Yes, but also means some bullish catalysts may already be priced, limiting further upside relevance.
- The market’s 85-86% pricing may be directionally right while still slightly underweighting contract path fragility around one specific minute.

## Conflict between inputs

There is no major factual conflict between sources. The main tension is weighting-based: how much comfort should the current spot cushion provide given that settlement depends on one exact future minute.

## Key assumptions

- No major new scheduled macro catalyst emerges before Apr. 20 noon ET.
- Binance venue mechanics remain stable and consistent with published kline behavior.
- The current >70k regime is not immediately broken by a fast crypto-specific risk-off move.

## Key uncertainties

- Whether any still-unidentified near-term catalyst can force a sharp drawdown.
- How much noon ET intraday timing risk matters relative to the multi-day spot cushion.

## Disconfirming signals to watch

- BTC loses the low-70k area before Apr. 20.
- A credible exchange, regulatory, or geopolitical shock hits crypto.
- Binance BTCUSDT begins trading near the threshold rather than comfortably above it.

## What would increase confidence

- Continued spot stability above ~72k into Apr. 18-19.
- Additional confirmation that no major scheduled macro or crypto-specific catalyst sits before settlement.
- Evidence of continued ETF or broad risk-asset support.

## Net update logic

The current view stayed close to the market but moved modestly lower than the raw 85-86% quote because the contract is narrower than a generic “BTC above 70k by next week” intuition. The exact-minute settlement and crypto’s drawdown capacity matter enough to prevent endorsing the full market optimism.

## Suggested downstream use

Use as an orchestrator synthesis input and forecast update input. Main takeaway: treat this as high-probability Yes, but not as near-certainty, because exact-minute timing and unscheduled crypto shocks remain the live disconfirmers.