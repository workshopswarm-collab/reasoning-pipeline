---
type: agent_finding
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 8adf7e65-044c-4c3f-b33c-1a3dccf75a17
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
stance: yes
certainty: high
importance: high
novelty: low
time_horizon: "<24h"
related_entities: ["ethereum", "binance"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["intraday-volatility"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-source-notes/2026-04-16-risk-manager-binance-polymarket-resolution-check.md", "qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/assumptions/risk-manager.md", "qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/evidence/risk-manager.md"]
downstream_uses: []
tags: ["agent-finding", "risk-manager", "eth", "binance", "polymarket", "resolution-risk"]
---

# Claim

ETH is likely to resolve **Yes** for this market, but the nonzero risk is concentrated in the contract’s narrow timestamp mechanic: Binance ETH/USDT must finish the **April 17 12:00 ET 1-minute candle** with a final close **strictly above 2200**, not merely trade above 2200 at other times.

## Market-implied baseline

The current market price is **0.975**, implying roughly **97.5%** probability of Yes.

## Own probability estimate

My estimate is **95%** Yes.

## Agreement or disagreement with market

I **roughly agree** with the market on direction, but I am slightly below it on confidence. The direct evidence strongly supports Yes because Binance ETH/USDT is currently around **2344**, roughly **144 points / ~6.5%** above the threshold, and the verified Binance 24h low is still **2285.10**, also above 2200. The gap versus market comes mostly from **uncertainty quality rather than directional disagreement**: a one-minute, timestamp-specific settlement condition can still be broken by a sharp overnight or late-morning selloff, or by a Binance-specific pricing anomaly.

## Implication for the question

The market should still be interpreted as overwhelmingly Yes-leaning, but not as risk-free. The main question is not whether ETH is broadly above 2200 today; it is whether Binance ETH/USDT stays above 2200 through the exact noon ET settlement minute tomorrow.

## Key sources used

- **Primary / direct / governing source-of-truth surface:** Binance ETH/USDT spot price and 1m kline API (`/api/v3/ticker/price`, `/api/v3/klines`, `/api/v3/ticker/24hr`) as the best direct proxy for the stated settlement source.
- **Primary / direct resolution-mechanics source:** Polymarket market rules page for this exact market, which specifies Binance ETH/USDT and the 12:00 ET 1-minute candle final close.
- **Secondary / contextual verification source:** Binance Spot API documentation confirming 1m klines and timezone handling.
- **Case source note:** `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-source-notes/2026-04-16-risk-manager-binance-polymarket-resolution-check.md`

## Supporting evidence

- Binance spot/API verification on 2026-04-16 around 15:02-15:03 ET showed ETH/USDT around **2343-2345**.
- Recent Binance 1m klines closed around **2343.10, 2343.37, 2343.36, 2343.55, 2343.42**, indicating the underlying is not hovering near the strike.
- Binance 24h ticker showed **lastPrice 2344.54**, **high 2385.61**, and **low 2285.10**; even the verified 24h low remained above 2200.
- Polymarket’s rule text is relatively clean: the relevant conditions are Binance, ETH/USDT, 1-minute candle, 12:00 ET, and final close strictly above 2200.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **single-candle timing risk**. This contract does **not** ask whether ETH is above 2200 on average, at any point during the day, or on other exchanges. It asks whether the **final close of one specific Binance 1-minute candle** at **12:00 ET on April 17** is above 2200. A sharp risk-off move, macro headline, crypto liquidation cascade, or Binance-specific dislocation could still flip the outcome despite the current cushion.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance ETH/USDT, specifically the 1-minute candle for **12:00 ET on April 17, 2026**, using the candle’s final **Close** price.

**Material conditions that all must hold for a Yes resolution:**
1. The relevant venue must be **Binance**, not another exchange.
2. The relevant pair must be **ETH/USDT**, not ETH/USD or another pair.
3. The relevant timestamp must be the **12:00 ET** 1-minute candle on **April 17, 2026**.
4. The relevant field is the candle’s **final Close** price.
5. That final close must be **strictly higher than 2200**.

**Date / deadline / timezone check:**
- Assignment metadata and market page both point to **Apr 17, 2026 at 12:00 PM ET** for closure/resolution.
- Binance API docs confirm 1m kline handling and timezone support; this reduces but does not fully eliminate implementation ambiguity versus manual website chart viewing.

**Compliance / evidence-floor note:**
- This case is medium difficulty and date-sensitive with multi-condition contract mechanics.
- I verified at least one authoritative/direct source-of-truth surface: **Binance spot/API**, which is the stated resolution venue.
- I also performed an **additional verification pass** via Binance API docs and explicit timezone checks because the market probability is extreme (>85%) and the contract is narrow/timestamped.

## Key assumptions

- ETH/USDT remains above 2200 through the specific noon ET settlement candle, not just before it.
- Binance spot remains orderly enough that its settlement-relevant print is not distorted by venue-specific operational issues.
- There is no overnight or late-morning shock large enough to erase a ~6.5% cushion.

## Why this is decision-relevant

At a 97.5% market-implied probability, the market is embedding both a directional view and a confidence judgment. The main risk-manager contribution is that the remaining risk is **not zero** and is concentrated in **timestamp/path dependency**. If someone is treating this as nearly deterministic simply because spot is far above the threshold, they may be underweighting the contract’s single-minute settlement fragility.

## What would falsify this interpretation / change your mind

The fastest way to invalidate the current view would be evidence that Binance ETH/USDT is **breaking down sharply toward 2200 during U.S. morning trading on April 17**, especially if price falls below the recent verified 24h low near **2285** and keeps compressing into noon ET. I would also cut confidence materially on any evidence of **Binance-specific outage, abnormal wick behavior, or exchange-specific dislocation**. Conversely, if ETH is still comfortably above ~2250-2300 on Binance close to settlement, I would move closer to market confidence.

## Source-quality assessment

- **Primary source used:** Binance ETH/USDT market data/API, which is also the named resolution source.
- **Most important secondary/contextual source used:** Polymarket’s own rules page, plus Binance API docs for kline/timezone interpretation.
- **Evidence independence:** **Medium**. The most important direct evidence necessarily centers on Binance because Binance is the settlement venue; contextual verification is somewhat independent but still structurally adjacent.
- **Source-of-truth ambiguity:** **Low to medium**. The rule text is fairly explicit, though there remains some practical ambiguity between website chart presentation and API-based reconstruction of the exact ET noon candle.

## Verification impact

Yes, an **additional verification pass** was performed. I checked:
- Polymarket’s exact rule text
- Binance live spot/API data
- Binance API documentation for 1m kline mechanics and timezone handling
- explicit UTC/ET timestamp conversion logic

This extra pass **did not materially change the directional view**; it mainly increased confidence that the key risk is **path/timing risk**, not contract ambiguity.

## Reusable lesson signals

- **Possible durable lesson:** Daily threshold crypto markets can look trivial but still carry meaningful risk if they resolve on a single venue-specific minute close.
- **Possible missing or underbuilt driver:** `intraday-volatility` may deserve later review as a proposed driver distinct from generic operational-risk/reliability when narrow timestamp settlement matters.
- **Possible source-quality lesson:** For exchange-settled markets, API verification plus explicit timezone handling is more reliable than relying on webpage/chart impressions alone.
- **Confidence that any lesson here is reusable:** **Medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: Narrow timestamp-settlement markets repeatedly create underappreciated path-risk and may justify a dedicated intraday-volatility / settlement-timing driver review.

## Recommended follow-up

No further research is necessary for this run unless a fresh verification is desired closer to settlement. If revisited tomorrow morning, the only thing that should matter is whether Binance ETH/USDT remains comfortably above the threshold into the final pre-noon ET window.