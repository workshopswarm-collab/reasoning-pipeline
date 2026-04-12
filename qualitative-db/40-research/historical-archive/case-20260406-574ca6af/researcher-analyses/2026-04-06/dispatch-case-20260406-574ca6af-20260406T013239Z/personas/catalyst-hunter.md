---
type: agent_finding
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 98f19f60-9ceb-4985-a375-2f6fdff8e994
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: crypto
subdomain: ethereum
entity: ethereum
topic: "ethereum 2200 threshold outcome under Binance-only settlement mechanics"
question: "Will Ethereum reach $2,200 March 30-April 5?"
driver:
date_created: 2026-04-06T01:39:00Z
agent: catalyst-hunter
stance: bearish_vs_market
certainty: high
importance: high
novelty: medium
time_horizon: immediate
related_entities: ["ethereum", "binance", "polymarket", "kraken"]
related_drivers: []
proposed_entities: ["CoinGecko"]
proposed_drivers: ["exchange-specific settlement mechanics", "resolution mechanics", "expiry timing", "cross-venue basis"]
upstream_inputs: []
downstream_uses: []
tags: ["eth", "polymarket", "binance", "resolution-source", "threshold-market", "catalyst-hunter"]
---

# Claim

This market should be viewed as effectively a **No** under the governing source-of-truth mechanics: Polymarket specifies Binance ETH/USDT 1-minute candle highs only, and a direct pull of Binance 1-minute data across the full Mar 30-Apr 5 ET window showed a maximum high of **2167.85**, below **2200**. For this case, the usual narrative catalysts matter far less than the venue-specific settlement rule.

**Evidence-floor compliance:** exceeded the stated floor. I verified one authoritative/direct settlement surface (Polymarket rule text naming Binance ETH/USDT 1m highs) and added a contextual verification pass (Binance current ticker, Kraken ticker, CoinGecko market data) because the contract mechanics were explicitly flagged as nontrivial. I also addressed all three case-specific checks: CEX vs DEX price relevance, market-maker attribution rule check, and settlement source hierarchy.

## Market-implied baseline

Current price is **0.74**, implying roughly **74% Yes**.

## Own probability estimate

**3% Yes / 97% No.**

Residual Yes probability is not zero only because of small implementation/interpretation risk around settlement handling or the possibility of a late unseen clarification; on the direct observed mechanism, the threshold was not reached.

## Agreement or disagreement with market

I **strongly disagree** with the market-implied baseline.

Why:
- The market appears too high relative to the actual source-of-truth mechanics.
- The contract is not asking whether ETH broadly traded near or above 2200 on any venue, index, or DEX; it asks whether **Binance ETH/USDT 1-minute Highs** hit 2200 in the specified ET window.
- Direct verification showed the highest relevant 1-minute high was **2167.85**, so the key catalyst path needed for Yes never materialized on the governing venue.

## Implication for the question

The decisive interpretation is that this was a **mechanical threshold-touch market on one named exchange pair**, not a broad market-narrative question. Once the Binance-only settlement rule is confirmed and the full 1-minute history is checked, the outcome is largely determined. Any remaining catalyst would have needed to force an actual Binance ETH/USDT 1-minute print through 2200 before expiry; that did not occur in the checked window.

## Key sources used

- **Primary / direct settlement source:** Polymarket market page for this market, which explicitly states the rule: Yes only if any **Binance ETH/USDT 1-minute candle** in the title window has a final **High >= 2200**.
- **Primary / direct price source:** Binance API ETHUSDT 1-minute klines over the ET window Mar 30 00:00 to Apr 5 23:59; observed maximum high **2167.85** at **2026-04-01 13:03 ET**. See case source note: `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-source-notes/2026-04-06-catalyst-hunter-binance-polymarket-resolution-and-price-check.md`
- **Secondary / contextual verification sources:**
  - Binance 24h ticker API (high 2135.39 at verification)
  - Kraken XETHZUSD ticker (high 2134.00 in the observed 24h set)
  - CoinGecko ETH market endpoint (high_24h 2127.49 at verification)

Direct vs contextual distinction matters here: only the Polymarket rule text plus Binance ETH/USDT 1m highs are governing; Kraken and CoinGecko are contextual only.

## Supporting evidence

Strongest evidence for No:
- Polymarket’s own market page says the market resolves from **Binance ETH/USDT 1-minute Highs**, not from DEX, other CEXs, spot composites, or indexes.
- The same page explicitly excludes other exchanges, pairs, and spot markets.
- Direct Binance 1-minute kline history across the whole ET window showed **max high 2167.85**, which is **32.15 below** the threshold.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **implementation risk**, not market direction:
- If Polymarket were to apply an unseen clarification, alternate chart source, or non-API interpretation of Binance “final High,” the direct API check could in theory miss a settlement nuance.
- More generally, ETH did trade high enough during the week that a late squeeze was not absurd ex ante; this helps explain why the market might have been elevated before direct full-window verification.

I do **not** see strong disconfirming factual evidence on the governing source itself once the full Binance 1m history is checked.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Binance ETH/USDT **1-minute candle Highs** during **Mar 30 00:00 ET through Apr 5 23:59 ET**, as stated on the Polymarket market page.

Explicit case-specific checks:
- **Verify CEX spot price vs DEX price:** DEX prices are irrelevant to settlement here. Even if a DEX wick had crossed 2200, it would not count unless Binance ETH/USDT 1-minute High also did.
- **Check for specific market maker attribution rules:** I found no indication on the market page that a specific market maker, index publisher, or third-party attribution rule supersedes Binance. The named resolution source is Binance itself.
- **Confirm settlement source hierarchy (CEX vs DEX vs index):** Hierarchy is explicit and narrow: Binance ETH/USDT 1m highs control; other exchanges, other pairs, and spot markets are excluded. So this is **CEX-specific**, not DEX-based and not index-based.

## Key assumptions

- Polymarket’s published Binance-only wording is the operative settlement rule without hidden override.
- Binance API historical 1-minute klines faithfully reflect the finalized 1-minute highs referenced by the chart/UI.
- The ET window was translated correctly when querying start and end times.

## Why this is decision-relevant

This case is a clean example of why crypto threshold markets need explicit source-of-truth auditing. A trader or synthesizer focusing on broad ETH price action could overestimate Yes odds if they fail to notice that only one exchange pair and one candle granularity count. The market’s 74% implied Yes looks too high once that mechanics check is done.

## What would falsify this interpretation / change your mind

What could still change my mind:
- a formal Polymarket clarification broadening or altering the settlement source,
- evidence that Binance charted 1-minute highs differ materially from the API historical klines for the relevant window,
- a verified overlooked Binance 1-minute candle at or above 2200 inside the ET date range.

Absent one of those, I would not move materially.

## Source-quality assessment

- **Primary source used:** Polymarket market page rule text naming Binance ETH/USDT 1-minute highs.
- **Most important secondary/contextual source:** Binance direct API kline history for the full window; contextual checks from Kraken and CoinGecko only support sanity-checking, not settlement.
- **Evidence independence:** **Medium.** The core evidence is intentionally not independent because Polymarket delegates to Binance. Contextual venue checks are independent but non-governing.
- **Source-of-truth ambiguity:** **Low after verification.** It starts high from the assignment prompt, but the market page wording resolves the ambiguity cleanly.

## Verification impact

- **Additional verification pass performed:** Yes.
- **Did it materially change the view?** Yes.
- **How:** The extra pass converted this from a potentially catalyst-driven threshold case into a mostly mechanical settlement case. Cross-venue/contextual checks reinforced that no nearby hidden threshold touch was being missed, but the main material change came from confirming Binance-only settlement and the actual full-window max high.

## Reusable lesson signals

- **Possible durable lesson:** In crypto threshold markets, always inspect whether resolution is tied to one exchange pair plus candle interval before reasoning from broad “did price touch X?” narratives.
- **Possible missing or underbuilt driver:** Exchange-specific settlement mechanics / venue basis risk may deserve more explicit treatment as a reusable driver for crypto event markets.
- **Possible source-quality lesson:** When Polymarket explicitly names a venue and candle interval, direct API verification can be more decision-useful than multiple broad market-data summaries.
- **Confidence that reusable lesson is reusable:** **High.**

## Orchestrator review suggestions

- **Review later for durable lesson:** yes
- **Review later for driver candidate:** yes
- **Review later for canon or linkage issue:** no
- **One-sentence reason:** This case strongly suggests a reusable lesson/driver around venue-specific settlement mechanics in crypto threshold markets, but it does not obviously require canonical entity or linkage repair.

## Recommended follow-up

- If a controller or synthesizer is still treating this as a generic ETH momentum/catalyst question, reframe it as a Binance-only threshold-resolution case.
- If post-resolution audit is desired, compare Binance UI historical 1m chart highs against the API query used here, mainly as a process-quality check rather than because the base conclusion looks fragile.
