---
type: evidence_map
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
research_run_id: 97f53517-198b-4576-8cba-94e7b47b8f29
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-at-12-00-pm-et-on-2026-04-17-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70000?"
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
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["orchestrator synthesis input", "decision-maker review"]
tags: ["btc", "catalyst-analysis", "evidence-netting"]
---

# Summary

Net evidence favors **Yes**, but the key reason is not an identified bullish catalyst. It is that BTC already sits materially above 70k and no clearly superior near-term negative catalyst was found that is likely to erase that cushion before the exact resolution minute.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 70,000?

## Current lean

Lean **Yes** at roughly low-90s probability.

## Prior / starting view

Starting view was that the 92.5% market-implied probability was plausible because current BTC spot was reportedly in the mid-74k area, but the extreme pricing required an explicit timing and contract-mechanics audit.

## Evidence supporting the claim

- **Current Binance BTC/USDT is ~74.3k**
  - Source: Binance direct ticker and klines; catalyst-hunter verification note.
  - Why it matters causally: the market starts around 6% in-the-money versus the strike.
  - Direct or indirect: direct.
  - Weight: high.

- **Recent Binance daily closes and ranges are mostly above the strike neighborhood**
  - Source: Binance 1d klines; market-implied and catalyst-hunter source notes.
  - Why it matters causally: 70k is below the center of recent price action rather than a knife-edge threshold.
  - Direct or indirect: direct.
  - Weight: medium-high.

- **Polymarket strike ladder centers in the low-to-mid 74k range**
  - Source: Polymarket market page / rules note.
  - Why it matters causally: neighboring contract prices imply the crowd sees 70k as comfortably in-the-money, not barely so.
  - Direct or indirect: indirect for terminal truth, direct for market baseline.
  - Weight: medium.

- **Independent CoinGecko spot check broadly matches Binance level**
  - Source: catalyst-hunter verification note; risk-manager cross-check.
  - Why it matters causally: reduces concern that the mid-74k print is a one-source anomaly.
  - Direct or indirect: contextual.
  - Weight: low-medium.

## Evidence against the claim

- **The contract resolves on one exact Binance 1-minute close at noon ET**
  - Source: Polymarket rules note and case description.
  - Why it matters causally: a brief selloff or wick at the exact minute can decide the market even if BTC remains broadly strong.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

- **BTC can move >5% over a few days without a single obvious scheduled catalyst**
  - Source: recent Binance daily ranges.
  - Why it matters causally: the current 6% cushion is meaningful but not unbreakable in crypto.
  - Direct or indirect: contextual from recent volatility.
  - Weight: medium-high.

- **Extreme market pricing leaves limited room for ordinary path risk**
  - Source: market-implied price at 0.925.
  - Why it matters causally: even if Yes is more likely than No, the spread between 'likely' and '93% likely' matters.
  - Direct or indirect: indirect / valuation framing.
  - Weight: medium.

## Ambiguous or mixed evidence

- No standout scheduled catalyst was identified for the remaining window. That supports stability, but it also means the path is dominated by general market sentiment, which can turn quickly without warning.

## Conflict between inputs

There was little factual conflict across inputs. The main difference is weighting: direct venue data points to a strong Yes lean, while contract-mechanics and timing sensitivity argue against treating the trade as near-certain.

## Key assumptions

- No major negative catalyst hits before April 17 noon ET.
- Binance remains a clean and usable settlement source.
- Recent price structure remains broadly representative over the next three days.

## Key uncertainties

- Whether any macro or crypto-specific headline creates a fast repricing before settlement.
- Whether the precise noon ET candle prints materially away from surrounding spot levels.

## Disconfirming signals to watch

- BTC falling back toward 72k and then 70k before Friday.
- Large downside momentum into the April 17 morning session.
- Any Binance-specific disruption or settlement-minute ambiguity.

## What would increase confidence

- BTC holding above ~73k into late April 16 / early April 17.
- Additional confirmation that no major scheduled macro catalyst lands inside the settlement window.

## Net update logic

The evidence kept the view bullish but pulled it slightly below the market. The most important fact is that current price is well above the strike on the governing venue. What prevents a higher probability is the contract's narrow one-minute-close condition and the fact that crypto can still traverse a 6% gap in a few days without a bespoke catalyst.

## Suggested downstream use

Use as an orchestrator synthesis input emphasizing that the central issue is **timing/path risk versus cushion**, not disagreement about the current BTC level.