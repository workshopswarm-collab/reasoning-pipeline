---
type: evidence_map
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
research_run_id: 6c6dae63-899b-4d33-8486-50f3bb80d911
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-10
question: "Will the price of Bitcoin be above $68,000 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "binance", "btcusdt", "timing-risk"]
---

# Summary

The evidence leans strongly to Yes, with the remaining meaningful risk concentrated in timing interpretation and an unusually large intraday downside move rather than in ordinary directional uncertainty.

## Question being evaluated

Will Binance BTC/USDT 1-minute candle close above 68,000 for the 12:00 ET minute on 2026-04-10?

## Current lean

Strong Yes lean.

## Prior / starting view

Starting baseline was already bullish because the market was priced at 95.9% and BTC was likely near or above the low-70k range, but the key research need was stress-testing whether timezone mechanics or minute-label ambiguity could meaningfully erode that confidence.

## Evidence supporting the claim

- **Current Binance BTCUSDT spot around 72.3k**  
  - Source: live Binance `/api/v3/ticker/price` and recent 1m klines checked during the run.  
  - Why it matters causally: the threshold is 68k, so spot sits roughly 4.3k above strike with less than one day to go.  
  - Direct or indirect: direct contextual evidence from the governing venue.  
  - Weight: very high.

- **Binance is the governing source of truth and explicitly provides 1m klines**  
  - Source: Binance market-data docs; Polymarket rules.  
  - Why it matters causally: reduces venue mismatch risk and clarifies what instrument matters.  
  - Direct or indirect: direct for settlement mechanics.  
  - Weight: high.

- **Timezone verification supports noon ET = 16:00 UTC on April 10, 2026**  
  - Source: timezone conversion check plus Binance docs indicating `timeZone` handling.  
  - Why it matters causally: removes one of the most plausible operational failure modes.  
  - Direct or indirect: direct for mechanics.  
  - Weight: high.

## Evidence against the claim

- **Residual timing / interface ambiguity**  
  - Source: contract wording references Binance website candles while verification used docs plus API endpoint behavior.  
  - Why it matters causally: a bar-label mismatch or UI convention issue could create a false sense of certainty.  
  - Direct or indirect: indirect but highly decision-relevant.  
  - Weight: medium.

- **Large downside path risk over less than one day**  
  - Source: general BTC volatility regime inferred from live 1m price behavior and market structure.  
  - Why it matters causally: Bitcoin can move violently on macro or crypto-specific shocks, and a 4k+ move is not impossible even if it is unlikely over this horizon.  
  - Direct or indirect: contextual.  
  - Weight: medium.

## Ambiguous or mixed evidence

- Polymarket page scrape displayed 99% for the 68k threshold while assignment context listed current_price 0.959. This likely reflects scrape staleness or a different market snapshot rather than substantive disagreement, but it is a reminder that the runtime assignment field should be treated as the clean baseline input.

## Conflict between inputs

There is no major factual conflict on the mechanism. The only mild tension is between the assignment's 95.9% market-implied probability and the page scrape showing 99% on the visible web page. This appears timing-based rather than interpretive.

## Key assumptions

- Binance website and API candle timing conventions align for the relevant minute.
- No extraordinary BTC selloff of sufficient size occurs before settlement.
- The correct resolution bar is the 12:00 ET minute rather than a neighboring minute caused by timezone confusion.

## Key uncertainties

- Exact April 10 noon ET close is not yet known.
- Small residual uncertainty remains about website display versus API interpretation.

## Disconfirming signals to watch

- BTCUSDT falling toward or through 69k ahead of the settlement window.
- Evidence that Binance website labels the noon ET candle differently than expected.
- Any Polymarket clarification changing how the minute is interpreted.

## What would increase confidence

- Direct capture of Binance website candle display near settlement.
- Continued BTC price stability above 70k into April 10 morning ET.

## Net update logic

The investigation mostly converted an already-high prior into a cleaner, more audit-ready high-confidence Yes by reducing contract-mechanics uncertainty. The biggest remaining risk is not hidden fundamental weakness; it is a combined operational and path-risk tail where either the wrong minute is referenced or BTC experiences a rare but real sharp drawdown into the exact settlement bar.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, with attention to the small but nonzero operational/timing tail despite the very bullish price gap.