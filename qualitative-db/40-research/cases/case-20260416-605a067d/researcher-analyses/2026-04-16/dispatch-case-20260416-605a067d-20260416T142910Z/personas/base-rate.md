---
type: agent_finding
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 0bea9a8d-3bf2-4b6a-9261-3cc4d510709b
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: short-dated-price-thresholds
entity: ethereum
topic: "Binance ETH/USDT noon ET close versus 2200 threshold"
question: "Will the Binance 1 minute candle for ETH/USDT at 12:00 ET on April 17 have a final close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
stance: yes-leaning
certainty: medium
importance: medium
novelty: low
time_horizon: "<48h"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-base-rate-binance-and-reference-prices.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/assumptions/base-rate.md"]
downstream_uses: []
tags: ["agent-finding", "base-rate", "crypto", "ethereum", "binance", "noon-close", "threshold-market"]
---

# Claim

Base-rate view: **Yes is more likely than not, but not as close to certain as the market price implies.** With ETH currently around 2295 on Binance and nearby major venues, the outside-view starting point favors staying above 2200 through tomorrow noon ET. But this is a **timed close-above** contract, not a touch market, so a one-day selloff remains the real risk.

**Evidence-floor / compliance label:** Met the medium-case evidence floor with (1) the primary governing source/rules surface from Polymarket naming Binance ETH/USDT 1-minute candle close at 12:00 ET, and (2) an additional verification pass using direct Binance market data plus independent contextual spot checks from Coinbase and Kraken. I also explicitly checked timing, source-of-truth, multi-condition mechanics, canonical mapping, and the near-complete verification distinction.

## Market-implied baseline

The assignment gives `current_price: 0.871`, implying roughly **87.1%** for Yes.

## Own probability estimate

My estimate is **82% Yes**.

## Agreement or disagreement with market

I **roughly agree on direction** but **disagree modestly on confidence**. The market is saying ETH is very likely to remain above 2200 at the exact noon ET close on Binance tomorrow. That is plausible given the current price buffer of about 95 dollars, but 87% looks somewhat rich for a major crypto asset over roughly one day when a ~4% move is still well within ordinary short-horizon possibility.

## Implication for the question

The most decision-relevant interpretation is: this looks like a favorable Yes setup, but not an already-settled one. The contract requires **all** of the following to hold for Yes:

1. the governing venue must be **Binance**,
2. the relevant pair must be **ETH/USDT**,
3. the relevant candle must be the **1-minute candle for 12:00 ET on April 17**,
4. the market uses the candle's **final Close** value,
5. that close must be **strictly higher than 2200**.

At research time, those conditions are **not yet verified**, because the decisive minute has not happened yet. That is different from saying the event is unlikely.

## Key sources used

- **Primary / authoritative contract source:** Polymarket market page and rules for `ethereum-above-on-april-17`, which explicitly state that resolution is based on the Binance ETH/USDT 1-minute candle at 12:00 ET and its final Close value.
- **Primary governing-market-state source:** Binance public market-data API (`ticker/price` and `klines`) showing ETH/USDT around 2295 and recent 1-minute closes in the high-2280s to mid-2290s.
- **Secondary / contextual independent checks:** Coinbase ETH-USD spot and Kraken ETH/USD ticker, both around 2295 at research time.
- **Contextual prior-learning source:** prior case review on a Binance ETH threshold market emphasizing the need to distinguish "not yet verified" from "not yet occurred" and to identify the governing source explicitly.

## Supporting evidence

- ETH is currently about **4.3% above** the 2200 threshold on the governing Binance venue.
- Coinbase and Kraken spot checks closely match Binance, so there is no obvious venue-specific distortion at the moment.
- For a liquid major asset already well above the line, the outside-view prior over the next ~day is favorable to remaining above the threshold unless a broad crypto selloff or asset-specific shock intervenes.
- The contract is mechanically straightforward once the governing source is identified: there is little interpretive ambiguity beyond the exact candle/timezone/close requirement.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: **crypto can move 4% in a day without extraordinary drama.** Because this market resolves on one exact minute close rather than an intraday touch or daily average, a late selloff below 2200 would be enough to flip the result to No even if ETH spends most of the next 24 hours above the threshold.

## Resolution or source-of-truth interpretation

**Primary governing source:** Binance, specifically the ETH/USDT market with `1m` candles.

**Governing-source proof captured:** The Polymarket rules explicitly say the market resolves to Yes if the Binance 1-minute candle for ETH/USDT at **12:00 in ET** on April 17 has a final **Close** price higher than 2200, and No otherwise.

**Date / deadline / timezone check:** The assignment lists both `closes_at` and `resolves_at` as `2026-04-17T12:00:00-04:00`, which is noon **America/New_York / ET** on April 17. That aligns with the market rules surfaced on Polymarket.

**Multi-condition check:** This is not "ETH above 2200 at any point on April 17" and not "ETH above 2200 on other exchanges." It is only the Binance ETH/USDT 1-minute candle at the specified noon ET timestamp, using the final close value.

**Verification-state separation:** The event has **not yet occurred** at the decisive resolution minute, so there is no governing-source outcome to verify yet. This is a cleaner case than a near-complete touch market where the event may already have occurred but not yet been verified.

## Key assumptions

- ETH will not experience a sustained downside move of roughly 4% or more before tomorrow noon ET.
- Binance price behavior will remain broadly aligned with other major venues.
- No material contract-interpretation wrinkle beyond the stated candle/timezone/close rule emerges.

## Why this is decision-relevant

The market is pricing Yes as highly likely. My outside-view says that is directionally right, but still somewhat overconfident because the remaining path is dominated by ordinary short-horizon crypto variance rather than by a nearly completed deterministic process.

## What would falsify this interpretation / change your mind

I would move materially lower if:
- ETH loses the mid-2200s and starts trading near or below 2230 across major venues,
- a macro or crypto-specific shock materially increases downside volatility into U.S. midday tomorrow,
- Binance begins showing relative weakness versus Coinbase/Kraken,
- new evidence suggests the noon ET candle mapping or displayed Binance source surface differs from the working interpretation.

I would move closer to the market if ETH remains comfortably above 2250-2275 into late morning ET tomorrow with stable cross-venue alignment.

## Source-quality assessment

- **Primary source used:** Polymarket rules plus Binance direct market data.
- **Most important secondary/contextual source:** Coinbase and Kraken spot references.
- **Evidence independence:** **Medium**. Coinbase and Kraken are separate venues, but all are observing the same broad ETH market regime.
- **Source-of-truth ambiguity:** **Low to medium**. The rule wording is fairly explicit, though the operative source is a Binance chart/UI surface, so exact minute mapping and final close remain the only meaningful mechanical sensitivities.

## Verification impact

- **Additional verification pass performed:** Yes.
- **What I checked:** I verified the explicit governing-source rule on the Polymarket page, then checked direct Binance market data and cross-venue spot alignment on Coinbase and Kraken.
- **Material change from verification:** No major directional change. It strengthened confidence that the current price buffer is real and that the main residual risk is ordinary one-day volatility, not source confusion.

## Reusable lesson signals

- Possible durable lesson: distinguish short-dated **close-above** markets from more permissive **touch** markets; current distance to threshold matters differently.
- Possible missing or underbuilt driver: none confidently identified from this single run.
- Possible source-quality lesson: for Binance-settled crypto markets, direct venue verification plus one or two cross-venue checks is a good medium-case standard.
- Reusable confidence: **medium-low**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**
- Review later for driver candidate: **no**
- Review later for canon or linkage issue: **yes**
- One-sentence reason: Binance is structurally important to these contracts, but I only had high confidence in a canonical `ethereum` slug; `binance` looked important yet the provided entity path was `binance-us`, so I kept `binance` in `proposed_entities` rather than forcing a weak canonical fit.

## Recommended follow-up

If this case is revisited closer to resolution, do one final direct check of Binance ETH/USDT behavior in the hour before noon ET and ensure the exact 12:00 ET candle mapping is being read correctly on the governing surface.