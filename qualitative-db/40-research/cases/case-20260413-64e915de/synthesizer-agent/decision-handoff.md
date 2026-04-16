---
type: synthesis_decision_handoff
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
question: "Will Ethereum reach $2,400 April 13-19?"
source_syndicated_finding_path: qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/syndicated-finding.md
market_implied_probability: 0.905
syndicated_probability_low: 0.78
syndicated_probability_high: 0.84
syndicated_probability_midpoint: 0.81
relation_to_market: below_market
edge_quality: strong
edge_independent_verification_quality: medium
compressed_toward_market_due_to_verification: no
contract_ambiguity_level: none
contract_ambiguity_reason:
independently_verified_points: ["Polymarket page embeds explicit Binance ETH/USDT 1-minute High resolution rule", "Only Binance ETH/USDT highs count; other venues do not govern settlement", "Swarm consensus that event is favored but below market is faithful to raw findings", "The main unresolved risk is path conversion from near-touch to actual qualifying print, not contract meaning"]
verification_gap_summary: "The key remaining gap is fresh Binance path data proving whether the initial near-touch impulse will convert before Apr 19."
best_countercase_summary: "ETH was already within a few dollars of the threshold on day one, so a brief Binance wick above $2,400 may still deserve near-market odds."
main_reason_for_disagreement: "Remaining disagreement is mostly about how much residual failure risk to assign to a very-near threshold touch market."
resolution_mechanics_summary: "Resolves Yes if any Binance ETH/USDT 1-minute candle during Apr 13-19 ET has High >= 2400."
freshness_sensitive: yes
freshness_driver: "Binance ETH/USDT intraday path and any renewed retest of the 2390s before Apr 19 close"
decision_blockers: ["Fresh path dependence remains high in a short-dated threshold market", "No decisive synthesis-stage evidence that the remaining last-mile move is nearly automatic"]
blockers_require_new_research: no
disagreement_type: market_pricing
follow_up_needed: yes
---

# Decision summary

Post-synthesis view: ETH reaching $2,400 during Apr 13-19 is still more likely than not, but the swarm’s below-market stance remains the right synthesis posture after verification. The strongest reason is that the contract is explicitly a Binance ETH/USDT 1-minute high-touch market, and while ETH was already very close to the threshold on day one, the independent synthesis-stage check does not justify treating the last few dollars as nearly automatic. Final view stays below the market’s 90.5% and centers in the low-80s rather than near-certainty.

## Why this may matter now

Market-implied probability is 0.905. My syndicated range is 0.78 to 0.84. That leaves the edge as modestly below market, but not a huge contrarian call. The likely mispricing is the market compressing a very favorable setup into near-certainty even though the contract still requires one actual Binance 1-minute High >= 2400.

## Shift versus swarm baseline

This is close to the swarm-implied center rather than materially different from it. Synthesis-stage verification strengthened confidence in the contract interpretation by confirming the explicit Binance 1-minute High rule, but it did not uncover enough fresh evidence to justify moving materially upward toward the market. I trimmed the low end upward from the most bearish lane because the contract ambiguity was resolved more cleanly than several lanes thought, but I did not raise the top end because the edge still rests on path conversion rather than a completed hit.

## Edge verification status

Verification quality is medium. I independently checked the live Polymarket event page and confirmed the exact embedded rule text: the market resolves Yes if any Binance ETH/USDT 1-minute candle during the title window has High >= 2400, and only Binance ETH/USDT counts. That materially improves confidence in the contract mechanics and makes risk-manager the strongest lane on source-of-truth. What remains weaker is independent verification of the edge itself: I did not obtain decisive fresh evidence that ETH was already printing repeated 2390s or had crossed. So the below-market view is verified as plausible, but not with high confidence.

## Compression toward market

No. Verification did not force meaningful compression toward market; instead it mostly removed contract ambiguity. If anything, it supported keeping a disciplined below-market stance because the rule is narrow and venue-specific. I did not move closer to 0.905 because the missing piece is not rules clarity anymore; it is actual price conversion.

## Timing and catalyst posture

The next catalyst is simply price action, not a major scheduled Ethereum event. The most relevant checkpoint is whether Binance revisits the high-2390s soon. If that retest comes quickly, the edge versus market likely compresses or disappears fast. If ETH fades away from the threshold, the probability decays meaningfully because this is a short window.

## Key blockers

There is no major contract blocker now; the main blockers are operational and probabilistic. This is a short-dated, path-dependent threshold market with high staleness risk. The remaining question is whether the near-touch converts, not what counts.

## Best countercase

Best countercase: the market may simply be right that once ETH was within a few dollars of $2,400 on day one, several remaining days made a qualifying Binance wick overwhelmingly likely. Risk-manager and variant-view preserved this best even while staying below market, and catalyst-hunter acknowledged it directly through the same-day 2395 near-touch.

## What would change the view

A verified Binance ETH/USDT 1-minute High >= 2400 obviously falsifies the below-market stance immediately. Short of that, repeated strong retests into the 2390s with momentum would push the view upward toward market. Conversely, a meaningful rejection away from the threshold would move the estimate lower.

## Recommended next action

Wait for a catalyst / resolution checkpoint rather than rerunning the full swarm now. If revisited, do a narrow refresh on Binance ETH/USDT intraday highs and only rerun lanes if price meaningfully moves away from or through the threshold.

## Verification impact

Yes, synthesis-stage verification materially helped. It showed that some raw lanes understated how explicit the contract mechanics actually were. Cross-lane comparison made risk-manager look strongest on resolution/source-of-truth, while catalyst-hunter remained the most useful lower-confidence counterweight on path dependence. Extra verification did not materially change the directional call, but it did sharpen why the disagreement with market should be expressed as calibration rather than contract doubt.
