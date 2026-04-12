---
type: agent_finding
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 53b2f3c6-cb4c-4c59-80a6-9924143d9ad2
analysis_date: 2026-04-06
persona: risk-manager
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | risk-manager
question: Will Ethereum reach $2,200 March 30-April 5?
driver: settlement source hierarchy and threshold reach
date_created: 2026-04-06T01:38:10Z
agent: Orchestrator
stance: no
certainty: medium-high
importance: high
novelty: medium
time_horizon: immediate resolution
related_entities: [ethereum, binance, polymarket]
related_drivers: [resolution mechanics, source-of-truth ambiguity, threshold path]
upstream_inputs: [case.md, source notes, assumption note, evidence map]
downstream_uses: [orchestrator synthesis]
tags: [risk-manager, crypto, polymarket, binance, cex, settlement]
---

# Claim

My directional view is that this market should resolve **No**. The main reason is contract mechanics, not macro ETH direction: the market is governed by **Binance ETH/USDT 1-minute candle highs only**, and a direct Binance kline check over the full ET window found a maximum high of **2167.85**, below the 2200 threshold.

**Compliance label:** Evidence floor met with (1) one authoritative/direct source-of-truth surface for settlement mechanics (Polymarket contract text) plus (2) one direct contextual verification source on the designated venue (Binance ETH/USDT 1m klines API). Additional verification was performed because the market-implied probability was elevated and the case was flagged for source-of-truth ambiguity.

## Market-implied baseline

Current price `0.74` implies roughly **74% Yes**.

That price also implies fairly high market confidence that either (a) Binance already printed 2200 during the window or (b) traders were comfortable treating broader ETH price action as sufficient. I think that confidence was too high relative to the actual contract wording.

## Own probability estimate

**8% Yes / 92% No**.

This is mostly a settlement-mechanics estimate rather than a live market-direction estimate. Given the checked Binance data, the remaining Yes probability is primarily residual contract/API/chart-surface risk, not a directional belief that ETH likely hit 2200 on the designated source.

## Agreement or disagreement with market

**Disagree with the market.**

The market price looked much too confident in Yes relative to the designated source hierarchy. Once the contract is read carefully, broad ETH strength, DEX prints, or highs on other exchanges become largely irrelevant. The key underpriced risk in the market view appears to be **rule confusion**: traders may have treated this like a general "did ETH touch 2200 anywhere" market rather than a **Binance ETH/USDT 1m candle-high** market.

## Implication for the question

If Polymarket applies the contract as written, this should resolve **No** unless there is some specific Binance chart-level print or settlement clarification that is not reflected in the API check.

## Key sources used

- **Primary / authoritative source-of-truth surface:** Polymarket market page contract text specifying Binance ETH/USDT 1m candle highs as the sole resolution basis. See `researcher-source-notes/2026-04-06-risk-manager-polymarket-contract-and-resolution.md`.
- **Direct verification source:** Binance ETH/USDT 1m kline data queried across the full Mar 30-Apr 5 ET window. See `researcher-source-notes/2026-04-06-risk-manager-binance-klines-window-check.md`.
- **Supporting artifact:** `researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/evidence/risk-manager.md`.
- **Assumption note:** `researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/assumptions/risk-manager.md`.

Direct vs contextual distinction matters here:
- Contract text is **direct/authoritative for mechanics**.
- Binance kline check is **direct empirical verification** on the designated venue, but slightly secondary to the exact chart UI named in the contract.
- Market price is only **contextual** and was downweighted.

## Supporting evidence

- The contract explicitly says the market resolves Yes only if **any Binance 1-minute candle for ETH/USDT** in the title window has a final **High >= 2200**.
- The contract explicitly says outcome depends **solely** on Binance ETH/USDT and that **other exchanges, other pairs, and other price references do not count**.
- Binance ETH/USDT 1m kline review over the full ET window produced a maximum observed high of **2167.85**, which is comfortably below 2200.
- This directly addresses the case-specific checks:
  - **verify CEX spot price vs DEX price:** CEX controls; DEX prices are not relevant to settlement.
  - **check for specific market maker attribution rules:** none found in the fetched contract text beyond designated-source mechanics; no special attribution carveout was identified.
  - **confirm settlement source hierarchy (CEX vs DEX vs index):** hierarchy is explicit; **Binance ETH/USDT 1m candles** govern, not DEX and not a blended index.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **implementation-level source mismatch risk**: the contract references the Binance chart UI, while my verification used Binance's public kline API. If the chart surface showed a qualifying wick that the API did not, or if Polymarket applied some hidden clarification or override, the No view could fail.

A secondary disconfirming consideration is the market's own 74% Yes price, which suggests many participants may have believed a qualifying print existed. I treat that as weak-to-moderate evidence because this is exactly the kind of contract-sensitive market where traders can anchor to the wrong source.

## Resolution or source-of-truth interpretation

The governing source of truth is **Polymarket's contract text**, which in turn designates **Binance ETH/USDT on 1-minute candles** as the operative settlement source.

My interpretation of the source hierarchy:
1. **Polymarket contract wording** governs what counts.
2. Within that wording, **Binance ETH/USDT 1m candle highs** are the designated empirical source.
3. **Other exchanges, DEXs, other pairs, and generalized ETH price references do not count**.

So this is not a "best ETH price anywhere" market. It is a narrow designated-source CEX market.

## Key assumptions

- Binance API kline data is materially consistent with the Binance chart surface named in the contract.
- The ET window conversion used for the API query correctly matches the contract window.
- No unseen Polymarket clarification superseded the fetched contract text.

## Why this is decision-relevant

The main edge here is not forecasting ETH direction; it is avoiding a costly category error about **what actually resolves the market**. A trader who treated DEX spikes, Coinbase highs, or broad ETH headlines as sufficient would likely overprice Yes.

## What would falsify this interpretation / change your mind

I would revise sharply toward Yes if any of the following appeared:
- a timestamped Binance 1m chart print in-window showing **High >= 2200**;
- a Polymarket clarification changing the designated source hierarchy;
- evidence of a real Binance chart/API discrepancy for this exact symbol and interval.

The fastest invalidating evidence would be a specific in-window Binance candle on the designated chart showing a 2200+ high.

## Source-quality assessment

- **Primary source used:** Polymarket contract text on the market page.
- **Most important secondary/contextual source used:** Binance ETH/USDT 1m kline API data over the full settlement window.
- **Evidence independence:** **Medium**. The two sources are independent enough for mechanics vs empirical check, but the empirical check still depends on the exchange named by the contract.
- **Source-of-truth ambiguity:** **Low-to-medium** after audit. The contract is fairly explicit, but there is still a small API-vs-chart implementation ambiguity.

## Verification impact

- **Additional verification pass performed:** Yes.
- **Did it materially change the view?** Yes.
- **How:** It moved the case from potentially ambiguous/high-Yes if one assumed broad ETH price evidence mattered to a strong No lean once the designated-source check showed a max high of only 2167.85.

## Reusable lesson signals

- Possible durable lesson: crypto threshold markets can be badly misread when traders import a "best price anywhere" heuristic into a designated-exchange contract.
- Possible missing or underbuilt driver: source-of-truth / venue-selection risk for crypto market resolution.
- Possible source-quality lesson: when contract text names a venue/interval explicitly, direct venue-specific data should dominate broad market narratives.
- Confidence reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- reason: this looks like a recurring class of resolution-risk error in crypto threshold markets where venue specificity is easy to underweight.

## Recommended follow-up

No immediate follow-up suggested beyond optional final reconciliation against the resolved Polymarket outcome or a direct Binance GUI spot-check if a settlement dispute emerges.