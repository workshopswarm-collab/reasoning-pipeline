---
type: agent_finding
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 50fa720d-a864-40e4-8184-6a9f5b56bbba
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "bitcoin above 72000 on April 17 noon ET"
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 72000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
stance: yes-lean
certainty: medium
importance: high
novelty: low
time_horizon: "2026-04-17 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-base-rate-binance-polymarket-resolution-and-price.md", "qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/assumptions/base-rate.md", "qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/evidence/base-rate.md"]
downstream_uses: []
tags: ["agent-finding", "base-rate", "btc", "polymarket", "threshold-close"]
---

# Claim

Base-rate view: **Yes is more likely than not and still favored even after accounting for close-specific fragility, but 87% looks somewhat rich for a contract that settles on one exact Binance one-minute close rather than a touch.** My estimate is **81%**.

**Evidence-floor / compliance label:** medium-difficulty case met with (1) direct governing rules verification on the Polymarket market page, (2) direct Binance price/context verification via Binance API, and (3) an explicit additional verification pass because market-implied probability is extreme (>85%).

## Market-implied baseline

The assignment gives `current_price: 0.87`, so the market-implied probability is **87%** for Yes.

## Own probability estimate

**81% Yes.**

## Agreement or disagreement with market

I **roughly agree on direction** but **modestly disagree on magnitude**. BTC is already around **74.6k** on Binance, so the outside view should start with persistence above a nearby threshold over a short horizon, not with a fresh attempt to rally through 72k. That strongly favors Yes.

But this is **not** a touch/high market. All of the following must hold for Yes:
1. the relevant source must be **Binance BTC/USDT**,
2. the relevant candle must be the **12:00 ET one-minute candle on April 17**,
3. the relevant field is the candle's **final Close**,
4. that Close must be **strictly higher than 72,000**.

That last-mile contract precision is the reason I sit below the market rather than matching 87% or higher.

## Implication for the question

The market should still be interpreted as a clear Yes-leaning setup because BTC is already safely above the strike. The real question is not whether BTC can ever print above 72k before April 17; it is whether BTC remains above 72k **at the exact governing minute close**. That distinction makes No less likely, but not negligible.

## Key sources used

- **Primary governing source / contract-mechanics source:** Polymarket event page rules for `bitcoin-above-on-april-17`, which explicitly define settlement from the Binance BTC/USDT 12:00 ET 1-minute candle close.
- **Primary direct contextual market source:** Binance API direct checks on 2026-04-15:
  - `ticker/price` for BTCUSDT = **74,659.41**
  - `avgPrice` for BTCUSDT = **74,631.98**
- **Additional direct contextual verification:** Binance daily klines for recent sessions showing BTC trading above 72k repeatedly and recent highs up to roughly **76,038**.
- **Case source note:** `qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-base-rate-binance-polymarket-resolution-and-price.md`

Direct vs contextual:
- **Direct settlement evidence:** only the Polymarket rules describing the governing source; the event itself is **not yet verified** because the governing 12:00 ET April 17 candle has **not yet occurred**.
- **Direct current-state evidence:** Binance API price surfaces.
- **Contextual evidence:** recent daily Binance klines showing persistence above the threshold.

## Supporting evidence

- BTC is already trading roughly **3.7% to 3.8% above 72,000** on Binance.
- Recent Binance data show that above-72k trading has not been a single fleeting spike; BTC has been trading and closing above that level repeatedly.
- With only about two days until settlement, the outside-view prior favors persistence when the asset is already clearly above the strike.
- The governing source is a highly liquid BTC/USDT market on Binance, reducing weird thin-market resolution risk.

## Counterpoints / strongest disconfirming evidence

The **strongest disconfirming consideration** is that BTC can easily move several percent in two days, and the contract settles on **one exact minute close**, not on a touch, high, daily close, or multi-minute average. A short, sharp downside move into April 17 noon ET could still produce No even if BTC spends most of the next two days above 72k.

## Resolution or source-of-truth interpretation

**Primary governing source:** Binance BTC/USDT, specifically the 1-minute candle for **12:00 ET on April 17, 2026**, using the candle's **final Close** value.

Mechanism-specific checks completed:
- **Verified primary resolution source:** yes, from Polymarket rules page.
- **Verified date / deadline / timezone:** yes, April 17 at **12:00 ET**.
- **Verified multi-condition contract mechanics:** yes; exchange, pair, interval, timestamp, and field all matter.
- **Captured governing-source proof when near-complete:** not yet possible, because the resolving candle has not yet occurred.
- **Distinguished not-yet-verified from not-yet-occurred:** yes. Here the event is **not yet occurred**, not merely unverified.

## Key assumptions

- BTC remains broadly in its current trading regime through April 17.
- No major downside macro or crypto-specific shock hits before the governing minute.
- Binance remains the operative and accessible resolution surface without material data ambiguity.

## Why this is decision-relevant

This case is a good reminder that short-dated threshold-close markets should be priced from the current state outward. Because BTC is already above the threshold, the base rate favors persistence. But contract precision still matters enough to justify a discount from a near-certainty view.

## What would falsify this interpretation / change your mind

What could still change my mind:
- A material BTC breakdown back **below 72k** on Binance before April 17.
- A sharp risk-off move in crypto or macro markets that compresses BTC into the settlement window.
- Fresh direct Binance checks late on April 16 / early April 17 showing BTC much closer to the threshold than it is now.
- Any newly discovered ambiguity in how Polymarket maps ET noon to the Binance candle display, though the current rule wording looks straightforward.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for the exact market; strong for settlement mechanics.
- **Most important secondary/contextual source:** Binance API direct market data; strong for current state, though not itself the exact chart UI named in the rule text.
- **Evidence independence:** **medium-low**. Both the contract and contextual price state ultimately anchor to Binance.
- **Source-of-truth ambiguity:** **low**. The contract wording is unusually explicit about exchange, pair, interval, timezone, and field.

## Verification impact

- **Additional verification pass performed:** yes.
- I did a second direct Binance pass using live ticker/average-price endpoints and recent daily klines after first reading the Polymarket rules.
- **Material change from extra verification:** no major directional change. It reinforced the Yes lean and narrowed the main residual risk to close-specific volatility rather than source ambiguity.

## Reusable lesson signals

- Possible durable lesson: close-specific crypto threshold markets deserve a discount versus touch-style markets even when current spot is already above threshold.
- Possible missing or underbuilt driver: none clearly required from this single case.
- Possible source-quality lesson: when Binance UI extraction is awkward, direct Binance API checks are useful contextual verification, but should still be labeled as contextual rather than settlement proof.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **no**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: this looks like a routine application of explicit settlement mechanics plus short-horizon BTC persistence, not a new recurring canon problem.

## Recommended follow-up

If this case is revisited close to settlement, do one last direct Binance check shortly before April 17 noon ET and explicitly record whether BTC is still comfortably above 72k versus merely hovering near the threshold.