---
type: synthesis_decision_handoff
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
question: "Will the price of Bitcoin be above $74,000 on April 17?"
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/syndicated-finding.md
market_implied_probability: 0.605
syndicated_probability_low: 0.58
syndicated_probability_high: 0.62
syndicated_probability_midpoint: 0.6
relation_to_market: crosses_market
edge_quality: unclear
edge_independent_verification_quality: medium
compressed_toward_market_due_to_verification: yes
contract_ambiguity_level: minor
contract_ambiguity_reason: "Final authority is Binance UI 1m candle close while most checks used strong API proxies rather than the literal settlement screen."
independently_verified_points: ["Polymarket rules explicitly require Binance BTC/USDT 12:00 ET 1m candle final Close strictly above 74,000", "Current Binance BTCUSDT spot remained around 74.7k at synthesis time", "Binance 24h range still straddled 74k, confirming the strike sits inside normal recent volatility", "Polymarket visible 74k market was around mid-60s, directionally close to assignment baseline"]
verification_gap_summary: "The main unverified point is how much current above-strike spot should translate into the exact Apr 17 noon ET close probability."
best_countercase_summary: "A routine sub-1% to ~1% dip into the exact noon minute can still produce No even if BTC stays broadly firm."
main_reason_for_disagreement: "Different weighting of narrow one-minute timing risk versus current above-strike regime."
resolution_mechanics_summary: "Yes requires the Binance BTC/USDT Apr 17 12:00 ET 1-minute candle final Close to be strictly greater than 74,000."
freshness_sensitive: yes
freshness_driver: "BTC intraday price action into the Apr 17 late-morning ET settlement window."
decision_blockers: ["Thin cushion above strike relative to normal BTC short-horizon volatility", "Final settlement uses one exact Binance minute close rather than broader daily direction", "Literal settlement authority is the Binance UI candle surface, not just API proxies"]
blockers_require_new_research: no
disagreement_type: timing
follow_up_needed: yes
---

# Decision summary

Post-synthesis view: BTC is still modestly more likely than not to resolve Yes, but the case is a narrow threshold-maintenance bet rather than a broad bullish BTC call. I place the Apr 17 noon ET Binance BTC/USDT 1-minute close above 74,000 at 0.58 to 0.62, essentially near market with only a very small bullish lean because direct verification confirms the governing mechanics and current above-strike regime, while fresh checks also reinforce that the cushion is thin enough for ordinary volatility to erase it before the exact settlement minute.

## Why this may matter now

Market baseline was 0.605. My synthesized range is 0.58 to 0.62. That is marginal-to-unclear edge territory, not a clean actionable dislocation. The only plausible mispricing is that market participants may slightly over- or underweight exact-minute timing fragility relative to current above-74k spot, but fresh verification did not support a large deviation from market.

## Shift versus swarm baseline

The provisional swarm center was about 0.62. I moved slightly lower and tightened toward 0.60 because the synthesis-stage verification confirmed the strongest bullish premise already known to the swarm—BTC is above strike on Binance—but did not add new independent support strong enough to justify staying confidently above market. Fresh checks instead reinforced the risk-manager and variant-view caution that a thin cushion can easily be lost by the exact settlement minute.

## Edge verification status

Verification quality is medium. I independently rechecked Polymarket rules and confirmed the exact resolution mechanics: Binance BTC/USDT, 12:00 ET, 1-minute candle, final Close, strictly above 74,000. I also checked fresh Binance spot, 5-minute average, and 24h range, which confirmed BTC remained in the mid-74k regime and that 74k remained inside the recent realized range. I also checked the Polymarket event page and found the visible 74k price in the mid-60s. What remains weak is translation from current above-strike spot to the precise noon-close probability; no fresh conditional-distribution study or stronger intraday volatility model was added at synthesis.

## Compression toward market

Yes. The swarm's mild bullish lean was credible, but the extra truth-finding pass did not independently verify a meaningful positive edge over market. Because the gap versus market was small to begin with, the right compression was modest rather than dramatic: pull the final range toward market and avoid overstating a thin edge that depends on one exact minute.

## Timing and catalyst posture

The key catalyst is not a scheduled macro event identified in the bundle; it is simply price maintenance into the Apr 17 late-morning ET window. The edge, if any, is more likely to decay than widen if BTC drifts sideways near the threshold, because the market will keep updating on exact-minute fragility. Waiting closer to settlement would improve accuracy, but this also means the current view has high staleness risk.

## Key blockers

There are no major contract blockers, but there are practical blockers to high conviction: the strike is close to spot, the contract is one-minute specific, and the final authoritative surface is the Binance UI candle rather than generic spot prints. Those are reasons for caution rather than reasons the case cannot be judged.

## Best countercase

The best countercase, best represented by risk-manager and variant-view, is that the market still slightly overstates Yes because a roughly 1% cushion is small for BTC and the contract can fail on a routine fade at exactly the wrong minute even if the broader tape stays constructive.

## What would change the view

A sustained move materially above about 75.5k into the Apr 17 morning would push the view higher because the cushion would become meaningfully safer. A clean loss of 74k, or even sustained trade in the low-74k/high-73k area into late morning ET, would push the view lower quickly. Any evidence of Binance-specific settlement-surface irregularity would also change the view.

## Recommended next action

Wait for the Apr 17 late-morning checkpoint and refresh with a direct Binance-focused settlement-surface read. No rerun of the full swarm is needed unless price regime or venue-specific conditions change materially.

## Verification impact

Yes, additional synthesis-stage verification was used. It materially helped on contract mechanics and current same-venue price context, but it did not materially uncover a hidden edge. Cross-lane comparison also made clear that risk-manager and variant-view were not disagreeing on facts so much as on how heavily to discount current spot for exact-minute fragility. I did not find major raw-vs-sidecar distortions beyond variant-view being somewhat more compressed and hypothesis-forward.
