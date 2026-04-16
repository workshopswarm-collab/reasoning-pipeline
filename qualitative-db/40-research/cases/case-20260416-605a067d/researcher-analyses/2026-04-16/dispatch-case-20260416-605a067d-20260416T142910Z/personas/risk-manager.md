---
type: agent_finding
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 462a53a5-a84b-4046-b50b-38278daf2730
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: daily-threshold-close
entity: ethereum
topic: "Binance ETH/USDT noon ET close above 2200 on April 17"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, 2026 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
stance: lean-yes
certainty: medium
importance: high
novelty: low
time_horizon: "< 24h"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-binance-spot-check.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/assumptions/risk-manager.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/evidence/risk-manager.md"]
downstream_uses: []
tags: ["agent-finding", "risk-manager", "ethereum", "polymarket", "binance", "noon-close"]
---

# Claim

Yes is still the better directional call, but the main risk-manager point is that this should not be treated like a near-lock just because ETH is currently above 2200. The contract only pays if **all** material conditions hold together: the instrument must be **Binance ETH/USDT**, the relevant candle must be the **1-minute candle labeled 12:00 ET on April 17**, and the **final close** for that exact minute must be **strictly higher than 2200**. My estimate is **83% Yes**.

## Market-implied baseline

The assignment price is **0.871**, implying about **87.1% Yes**.

I read that market price as embedding both a bullish directional view and fairly high confidence that the current cushion survives into tomorrow noon ET.

## Own probability estimate

**83% Yes**.

## Agreement or disagreement with market

I **roughly agree but am modestly more cautious** than the market.

Why: direct Binance market-state evidence is favorable, with ETH/USDT around **2298-2299** at check time and a 24-hour low of **2285.10**, both above 2200. That supports a high Yes probability.

The underpriced risk, in my view, is **exact-minute timing fragility**. This is not a touch market and not a daily average. A sharp move or Binance-specific deviation into the precise noon ET close minute is enough to flip the contract to No, even if ETH spends most of the next 24 hours above 2200.

## Implication for the question

This market should still lean Yes, but the relevant failure mode is path-dependent settlement risk rather than broad ETH weakness. The contract can resolve No from a short, badly timed downdraft even if the general market narrative remains constructive.

## Key sources used

Evidence floor compliance: **met with two meaningful sources plus an explicit extra verification pass**.

Primary / direct sources:
- `researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md` — primary contract-definition source establishing the governing source of truth, exact timing, timezone, pair, and close-above condition.
- `researcher-source-notes/2026-04-16-risk-manager-binance-spot-check.md` — direct Binance ETH/USDT market-state check using public Binance endpoints for current price, 24-hour range, and a target-minute existence check.

Supporting run artifacts:
- `.../assumptions/risk-manager.md`
- `.../evidence/risk-manager.md`

Direct vs contextual distinction:
- Direct evidence: Polymarket rules and Binance ETH/USDT data.
- Contextual evidence: the market-implied probability itself.

Governing source of truth:
- **Binance ETH/USDT 1-minute candle close for 12:00 ET on April 17, as displayed on the Binance chart surface referenced by the contract.**

## Supporting evidence

- Binance spot check showed ETH/USDT near **2298.16-2298.49**, giving roughly a **4.5% cushion** above 2200.
- Binance 24-hour stats showed a **low of 2285.10**, still above threshold.
- The contract condition is narrow but not especially hard if current levels hold: only the exact noon ET one-minute close must be above 2200.
- Additional verification pass: querying the exact future timestamp corresponding to **2026-04-17 12:00 ET = 2026-04-17 16:00 UTC** returned no candle yet, confirming the event is **not yet verified** rather than already observed negative.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: **crypto can move enough in 24 hours to erase the current cushion**, and this market cares about exactly one future minute on one exchange.

That is the key tail risk. A selloff of roughly 4-5% by settlement, or a Binance-specific downward deviation near noon ET, would be enough for No. The current 24-hour range itself shows the market is capable of large swings.

## Resolution or source-of-truth interpretation

This is the most important mechanism check for the case.

Material conditions that all must hold for a Yes resolution:
1. The relevant market is **Binance**, not Coinbase, Kraken, or an aggregate index.
2. The relevant pair is **ETH/USDT**, not ETH/USD.
3. The relevant bar is the **1-minute candle corresponding to 12:00 ET on April 17, 2026**.
4. The value that matters is the candle's **final Close**, not high, low, open, VWAP, or average price.
5. The close must be **higher than 2200**; equality would not satisfy "above."

Explicit date / deadline / timezone check:
- The contract specifies **12:00 ET (noon)** on April 17.
- On this date ET is in daylight time, so the target minute corresponds to **16:00 UTC**.

Explicit governing-source proof state:
- I verified the rules directly.
- I checked Binance data directly.
- I checked the exact future target-minute API query and got an empty result.
- Therefore the governing event is **not yet verified because it has not yet occurred**, not merely missing from my retrieval.

## Key assumptions

- Current Binance cushion above 2200 persists into the settlement window.
- Binance API values are a good practical proxy for the chart-based settlement surface named in the rules.
- No operational anomaly on Binance produces an exchange-specific close below 2200 despite broader ETH strength.

## Why this is decision-relevant

The market is priced at an extreme **87.1% Yes**, so the main question is not direction alone but whether residual uncertainty is being underpriced. My answer is: only slightly. The market is mostly right to lean strongly Yes, but I would still discount a few points for exact-minute settlement risk and exchange-specific dependency.

## What would falsify this interpretation / change your mind

What would most quickly invalidate the current working view:
- ETH/USDT on Binance trading down toward or below **2200** before the April 17 noon ET minute.
- Evidence that Binance is showing materially weaker prints than other ETH venues near settlement.
- Any Binance data integrity or chart-surface issue affecting the governing minute.

What could still change my mind:
- A fresh Binance check much closer to settlement that still shows a wide cushion would move me closer to the market or above it.
- A sharp overnight crypto drawdown would move me materially below the market.

## Source-quality assessment

- Primary source used: Polymarket rules page naming Binance ETH/USDT 1-minute close at 12:00 ET as the governing source.
- Most important secondary/contextual source: direct Binance ETH/USDT public data endpoints for current spot, 24-hour range, and target-minute timestamp check.
- Evidence independence: **medium**. The rule source and Binance market data are distinct source classes, but both ultimately point to the same exchange-specific mechanism.
- Source-of-truth ambiguity: **low to medium**. The contract is explicit, but there remains a small practical gap between chart-interface settlement wording and API-based pre-resolution checking.

## Verification impact

- Additional verification pass performed: **yes**.
- I directly rechecked Binance current data and queried the exact future timestamp for the governing minute.
- Material change from extra verification: **no major directional change**, but it improved mechanism confidence by cleanly separating **not yet verified** from **not yet occurred** and reinforced that this is a timing-risk case, not a contract-ambiguity case.

## Reusable lesson signals

- Possible durable lesson: in crypto close-above markets, a healthy current cushion can still deserve a discount if settlement depends on one exact minute rather than a broader interval.
- Possible missing or underbuilt driver: none clearly established from this single run.
- Possible source-quality lesson: explicit target-minute existence checks are useful for distinguishing future-event uncertainty from missing-proof uncertainty.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **no follow-up suggested**.
- Reason: the mechanism is clear and case-specific; current work mainly reinforces an already-active verification discipline rather than surfacing a new stable-layer gap.

## Recommended follow-up

If this case is revisited closer to settlement, the highest-value next step is a fresh direct Binance ETH/USDT check in the hour before **12:00 ET** with explicit capture of the governing minute close once available.