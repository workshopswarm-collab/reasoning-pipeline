---
type: agent_finding
case_key: case-20260416-33b4e3b5
dispatch_id: dispatch-case-20260416-33b4e3b5-20260416T021538Z
research_run_id: 67c7c895-78bf-4dd2-bcde-7d6858f9f131
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 1-minute candle for 12:00 ET on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
stance: lean-yes-below-market
certainty: medium
importance: high
novelty: medium
time_horizon: "2026-04-19 12:00 ET"
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "risk-manager", "crypto", "settlement-risk", "timing-risk"]
---

# Claim

SOL is more likely than not to resolve **Yes** on this contract, but the market looks somewhat overconfident. My working view is that the Binance SOL/USDT noon-ET 1-minute close on Apr 19 finishes above 80, yet the path-dependent settlement mechanics justify a noticeable haircut versus the market price.

**Evidence-floor compliance:** met with (1) a direct governing-source-of-truth check of the Polymarket rules page and (2) a direct Binance verification pass using live SOLUSDT spot and recent 1-minute kline data. This is above the stated floor for a medium-difficulty, date-specific market and includes the required extra verification for an extreme market probability.

## Market-implied baseline

Current market-implied probability from `current_price = 0.895` is **89.5% Yes**.

That price also implies high confidence that the current SOL buffer above 80 survives until the exact settlement minute. As a confidence object, the market seems to be treating timing/path risk as fairly minor.

## Own probability estimate

**78% Yes.**

## Agreement or disagreement with market

**Moderate disagreement.** I agree with the direction — Yes is more likely than No — but I think the market is too confident by roughly 11.5 percentage points.

Why I am below market:
- Binance spot checked around research time was **84.91**, so SOL is clearly above the threshold now.
- Recent Binance 1-minute closes clustered around **84.76-84.94**, so this is not a knife-edge trade at the moment.
- But the contract resolves on **one exact Binance 1-minute close at 12:00 ET on Apr 19**, not on an average price, not on a daily close, and not on a multi-exchange composite.
- A roughly 6% downside move over several days is very plausible for a high-beta crypto asset, especially if broader crypto turns risk-off or if weekend volatility hits.
- Because the market is already above 85%, I think the right question is not “is SOL above 80 now?” but “how often does a currently 84-85 SOL still fail a single-minute venue-specific close three days later?” That tail is not huge, but it is larger than the market price suggests.

## Implication for the question

The base case is still Yes, but this should be interpreted as a **fragile Yes**, not an effectively settled Yes. Anyone using this market for decision support should respect that the only thing that matters is the Binance SOL/USDT **12:00 ET** 1-minute candle close on **Apr 19, 2026** and that **all** of the following material conditions must hold for Yes:

1. The relevant venue is **Binance**, not another exchange.
2. The relevant pair is **SOL/USDT**, not SOL/USD or another instrument.
3. The relevant timestamp is the **12:00 ET (noon) 1-minute candle** on Apr 19, 2026.
4. The relevant field is the final **Close** price of that candle.
5. That Close must be **strictly higher than 80**.

If any of those conditions fail, or if the Binance close is 80.0 or below at the designated minute, the market resolves No.

## Key sources used

**Primary / authoritative for resolution mechanics**
- Polymarket market page and rules for `solana-above-on-april-19` (governing source-of-truth for contract wording and settlement mechanics).

**Primary / direct for current underlying price context and verification**
- Binance public API `ticker/price` for `SOLUSDT`.
- Binance public API `klines` for `SOLUSDT`, `interval=1m`, recent candles.

**Vault context / canonical mapping check**
- `qualitative-db/20-entities/tokens/sol.md`
- `qualitative-db/20-entities/protocols/solana.md`
- `qualitative-db/30-drivers/reliability.md`
- `qualitative-db/30-drivers/operational-risk.md`

**Supporting provenance artifact**
- `qualitative-db/40-research/cases/case-20260416-33b4e3b5/researcher-source-notes/2026-04-16-risk-manager-binance-polymarket-resolution-check.md`

Direct vs contextual distinction:
- Direct evidence: Polymarket rules; Binance spot and kline data.
- Contextual evidence: the risk interpretation that a ~6% move in SOL over several days is plausible for a high-beta crypto asset.

## Supporting evidence

- Direct Binance check showed **SOLUSDT = 84.91**, already materially above 80.
- Recent Binance 1-minute closes around the research window were **84.76, 84.81, 84.86, 84.87, 84.94**, confirming a live trading range several dollars above the threshold.
- Only a short period remains until settlement, which limits the time available for a large bearish repricing to develop.

## Counterpoints / strongest disconfirming evidence

**Strongest disconfirming consideration:** this contract is path-fragile because it resolves off **one exact venue-specific minute close**. A single adverse move, wick, or localized Binance dislocation at noon ET on Apr 19 can still produce No even if SOL spends most of the next three days above 80.

Other disconfirming considerations:
- SOL is a volatile high-beta crypto asset; a ~6% drawdown before settlement is not exotic.
- Weekend or macro-led crypto weakness could compress SOL toward or through 80.
- Exchange-specific print or operational issues matter more here than in a broader index-based contract.

## Resolution or source-of-truth interpretation

The governing source of truth is **Binance SOL/USDT**, specifically the **1-minute candle** for **12:00 ET** on **Apr 19, 2026**, and the decisive value is that candle’s final **Close** price.

I explicitly verified the contract wording from the Polymarket rules page. I also explicitly verified date/timing handling by converting recent Binance kline timestamps, which mapped correctly between UTC and ET. For this market, the important timing consequence is that the settlement window is **not** “any time on Apr 19” and **not** “end of day”; it is one exact noon-ET minute.

Source-of-truth ambiguity is low on wording, though the Binance front-end chart itself was not directly rendered via web fetch; the Binance public API provided the practical direct verification surface for current price and 1-minute candles.

## Key assumptions

- The current several-dollar cushion above 80 persists through ordinary volatility into Apr 19 noon ET.
- Binance remains a usable and representative settlement venue at the designated minute.
- There is no abrupt broad-crypto selloff large enough to push SOL below the threshold by settlement.

Key hidden market assumption: traders appear to be assuming that “currently above 80 by several dollars” translates into “nearly locked to finish above 80 at the exact settlement minute.” I think that assumption is directionally reasonable but too strong.

## Why this is decision-relevant

This is the core risk-management distinction: the market is not just pricing SOL direction, it is pricing **confidence in a narrow settlement mechanic**. When market odds are already extreme, the main failure is often not thesis reversal but underpriced path/timing fragility. That matters for whether to trust an 89.5% reading as near-settled versus merely favorable.

## What would falsify this interpretation / change your mind

What would most quickly invalidate the current lean-Yes view:
- Binance SOLUSDT trading down toward **80-82** ahead of Apr 19, showing the current buffer is eroding.
- Repeated 1-minute prints near or below 80 before settlement.
- Evidence of Binance-specific disruption, abnormal pricing behavior, or candle-quality issues near the settlement window.

What would move me **toward** the market:
- Additional direct Binance checks closer to settlement still showing SOL comfortably above 80, especially with a wider cushion.

What would move me **further away** from the market:
- Broad crypto weakness, especially if BTC/ETH roll over and SOL remains a higher-beta laggard.
- Any sign that Binance-specific microstructure could matter at the noon ET print.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for contract mechanics, plus Binance public API for current SOLUSDT spot and 1-minute candle verification.
- **Most important secondary/contextual source used:** none materially beyond the direct source set; the main contextual inference is volatility/timing risk from the market structure itself.
- **Evidence independence:** medium. The sources are not independent confirmations of the same fact; rather, one defines settlement mechanics and the other gives the direct underlying price venue. For this case, that is adequate.
- **Source-of-truth ambiguity:** low. Contract wording is explicit. Practical chart-surface verification was done via Binance API rather than rendered chart UI, which is a minor implementation caveat but not a major ambiguity.

## Verification impact

- **Additional verification pass performed:** yes.
- **What was checked:** direct Binance spot price, recent 1-minute klines, and timestamp conversion sanity check alongside the Polymarket rule text.
- **Did it materially change the view?** No material directional change. It reinforced that Yes is the base case, but it also reinforced that this is a narrow-minute settlement and therefore not as safe as the market price implies.

## Reusable lesson signals

- **Possible durable lesson:** single-minute exchange-specific crypto resolution markets deserve a meaningful confidence haircut versus simple “current price above threshold” reasoning.
- **Possible missing or underbuilt driver:** none clearly missing; `operational-risk` and `reliability` cover most of the fragility lens here.
- **Possible source-quality lesson:** for Binance-settled markets, public API endpoints can be a practical verification surface when chart rendering is inaccessible.
- **Confidence reusable:** medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** no.
- **Review later for driver candidate:** no.
- **Review later for canon or linkage issue:** no.
- **Reason:** canonical mapping was clean (`sol`, `solana`, `operational-risk`, `reliability`) and the lesson is useful but not yet broad enough from one case to justify promotion.

## Recommended follow-up

If this case is revisited closer to Apr 19, the highest-value follow-up is a fresh direct Binance check on the morning of settlement day with explicit attention to the remaining cushion above 80 and any venue-specific anomalies around noon ET.