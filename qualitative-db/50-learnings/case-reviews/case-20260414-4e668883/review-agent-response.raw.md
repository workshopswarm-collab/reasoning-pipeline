---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-4e668883
market_category: polymarket-discovery
domain: crypto
subdomain: threshold_touch_markets
entity: ethereum
topic: Binance 1-minute high touch resolution near round-number resistance
date_created: 2026-04-14
resolution_date: 2026-04-14T13:20:02-04:00
evaluation_scope: resolved_case
evaluation_target: pipeline_case
outcome_observed: 1.0
decision_taken: watch_only
error_pattern: underconfidence_on_nearby_touch_market
intervention_status: hold
related_entities: ["ethereum", "binance", "polymarket"]
related_drivers: ["threshold proximity", "touch-style settlement mechanics", "verification-surface caution"]
upstream_inputs:
  - qualitative-db/40-research/cases/case-20260414-4e668883/case.md
  - qualitative-db/40-research/cases/case-20260414-4e668883/decision-maker/artifacts/decision-maker-packet.json
  - qualitative-db/40-research/cases/case-20260414-4e668883/synthesizer-agent/syndicated-finding.runtime.json
  - qualitative-db/40-research/cases/case-20260414-4e668883/timeline.md
  - qualitative-db/40-research/cases/case-20260414-4e668883/researcher-swarm-current.md
downstream_uses: []
promotion_candidates: []
tags: ["learning/case_review", "platform/polymarket", "crypto/ethereum", "threshold-touch", "underconfidence"]
---

# Learning Note

## What was being evaluated

- Resolved-case review for `case-20260414-4e668883`: “Will Ethereum reach $2,400 April 13-19?”
- Platform/category: Polymarket / polymarket-discovery.
- Operational question: whether the pipeline correctly priced a short-dated, touch-style crypto threshold market whose governing resolution surface was a Binance 1-minute high during the Apr 13-19 window.
- This note evaluates both the focal case decision at 0.87 fair value and the broader forecast path on the same market, because the packet contains all four recorded forecasts tied to this contract.

## What the pipeline believed or did

- In the focal case, the decision-maker concluded **Yes**, with `trade_authorization: watch_only`, `position_policy: hold_only`, and target probability **0.87**.
- The stated crux was that ETH was trading within roughly half a percent of the threshold with several days left, so a qualifying touch was more likely than not, but the market price at **0.9235** was still judged too rich relative to bounded evidence.
- Persona-level probabilities were tightly clustered between **0.78** and **0.88**, with fair-value range **0.84-0.90** and midpoint **0.87**.
- Across the full market history in the packet, the pipeline moved progressively more bullish:
  - **0.71** on 2026-04-13 19:13 EDT
  - **0.81** on 2026-04-13 20:15 EDT
  - **0.87** on 2026-04-14 09:49 EDT
  - **0.9825** on 2026-04-14 13:50 EDT
- Observed workflow fact: the later **0.9825** forecast was recorded **after** the market had already resolved Yes at **2026-04-14 13:20:02 EDT**, and explicitly cited bundled evidence that the threshold had likely already been satisfied. That later forecast is useful for calibration accounting but should not be confused with ex ante foresight.

## What happened in reality

- The market resolved **Yes** with `resolved_value: 1.0`.
- Recorded resolution timestamp: **2026-04-14T13:20:02-04:00**.
- The packet does **not** include the full reconstructed path showing the exact qualifying Binance 1-minute high candle that triggered settlement; it only includes the final resolution state from the Polymarket/Gamma market surface.
- Observed fact: resolution happened well before the Apr 19/20 end of the contract window, so the remaining-time path risk that dominated earlier reasoning did not need to persist for several more days.

## Outcome and scoring evidence

- Focal case forecast: **0.87 Yes** against resolved value **1.0** → Brier component **0.0169**.
- Initial forecast: **0.71** → Brier component **0.0841**.
- Latest recorded forecast: **0.9825** → Brier component **0.00030625**.
- Packet summary:
  - total recorded forecasts: **4**
  - resolved forecasts: **4**
  - average forecast probability: **0.843125**
- Market-state evidence in packet:
  - market reference price at focal decision: **0.9235**
  - recent observed market prices ranged up to **0.96** in the packet snapshot history
  - snapshot summary min/max reference price: **0.815 / 0.96**
- Evaluation of the focal decision:
  - Directionally correct.
  - Mildly underconfident relative to the realized outcome.
  - Commercially, the “watch-only” posture was consistent with the pipeline’s internal pricing because fair value midpoint (**0.87**) sat below market (**0.9235**), so this is **not** an execution-discipline error inside the system’s own pricing framework.
- Important timing caveat:
  - The case’s 09:49 EDT decision and 0.87 fair value were ex ante.
  - The 13:50 EDT 0.9825 forecast was effectively post-resolution updating, so it should not be used as evidence that the earlier case had already solved the verification problem.

## Which inputs were high signal

- **Settlement mechanics framing was high signal.**
  - Multiple personas correctly treated the contract as a **touch/high-style** market rather than a close-above market.
  - The market-implied persona explicitly identified the key rule: Yes on any Binance 1-minute high `>= 2400` during Apr 13-19.
- **Threshold proximity was high signal.**
  - Multiple researchers observed ETH trading around **$2,387-$2,392**, only about **$8-$13** below the threshold.
  - Base-rate and catalyst-hunter both highlighted recent highs around **$2,394.71-$2,396.03**, meaning the contract was already in near-touch territory.
- **Time remaining in a 24/7 market was high signal.**
  - Several personas correctly recognized that multiple days remained in a continuously traded market, which materially raises touch-event probability versus a close-only framing.
- **Cross-venue spot checks were directionally useful.**
  - Binance, Coinbase, CoinGecko, and other contextual checks all pointed to ETH being very near the trigger, which supported the Yes direction even if they did not prove settlement.
- **Persona agreement was informative.**
  - The 0.78-0.88 cluster with no strong dissent suggests the research swarm had a coherent read on direction and mechanism.

## Which inputs were misleading

- **“Not yet verified on governing source” caution was somewhat overstretched in pricing, even if operationally sensible.**
  - It correctly prevented the pipeline from claiming the event had already happened without proof.
  - But in the focal case it appears to have pulled fair value down below the market despite a setup that, in hindsight, was extremely touch-favorable.
- **Repeated-rejection / round-number resistance concerns were real but overweighted relative to the short remaining distance and touch-style rules.**
  - The packet repeatedly notes the possibility of failing again just below $2,400.
  - In a touch market, that generic resistance concern mattered less than it would in a close-above or end-of-period market.
- **Lack of a specific catalyst was not very diagnostic here.**
  - Several notes observed there was no hard catalyst making the move “automatic.”
  - For a nearby threshold in a 24/7 crypto market, ordinary volatility appears to have mattered more than catalyst identification.
- **Some “source-of-truth wording incomplete” concern was probably too expensive relative to case difficulty.**
  - The packet shows medium concern about exact settlement wording visibility even though the usable rule understanding was already good enough to identify the decisive mechanism.

## What was missing

- **Missing in the packet:** a deterministic reconstruction of the exact qualifying Binance 1-minute high and timestamp that caused resolution.
  - Without that, the review can judge calibration and workflow stance, but cannot cleanly separate “correct caution before proof” from “avoidable delay in proof acquisition.”
- **Missing in the workflow:** stronger structured handling for “nearby threshold touch” cases where:
  - settlement is based on a permissive touch/high rule,
  - the asset is already within a fraction of a percent of the threshold,
  - and the remaining window is long relative to ordinary intraday volatility.
- **Missing in evaluator inputs:** a clear ex ante versus post-resolution labeling layer in the review packet to prevent later forecasts from visually blending with earlier decision quality.

## Error-pattern classification

- Primary classification: **underconfidence**.
- Secondary classification: **mild settlement-mechanics discount overweighting**.
- Not a wrong-direction call.
- Not an execution-policy failure under the pipeline’s stated economics, because the system judged the market overpriced and therefore appropriately stayed watch-only.
- Not yet supportable as a workflow failure, because the packet lacks the structured event-path evidence needed to prove that earlier decisive verification was feasible with existing tooling.

## Driver and mechanism takeaways

- In short-dated crypto **touch** markets, the combination of:
  - very small remaining price distance,
  - multi-day residual window,
  - and permissive “any qualifying high” mechanics
  can justify probabilities that are closer to the market than generic resistance narratives suggest.
- The decisive mechanism here was likely not a special catalyst but **ordinary volatility plus touch-friendly settlement rules**.
- A useful reusable driver candidate is:
  - **near-threshold touch markets with long residual window are closer to hazard-rate problems than thesis-quality problems**.
- Another takeaway: “not yet observed” should be split into two separate concepts:
  - **event not yet occurred**, versus
  - **event may already have occurred but has not been verified on the governing surface**.
  Those should not receive the same probability penalty.

## Source / input / workflow takeaways

- Source selection was broadly adequate for directional judgment:
  - direct contract/rules interpretation,
  - Binance contextual checks,
  - and cross-venue spot verification.
- The main limitation was not lack of sources but lack of **structured proof capture** for the governing event.
- The workflow appears strongest at bounding a fair-value range and preserving caution, but weaker at converting “almost certainly near the line” setups into an explicit high-probability touch model.
- The packet’s timeline also shows a review hazard:
  - the later 0.9825 forecast came after recorded resolution.
  - Evaluator artifacts should continue distinguishing ex ante decision quality from post-resolution assimilation quality.

## Proposed intervention or hold decision

- **Hold, not promote yet.**
- No prompt-level or policy-level intervention is clearly justified from this single case alone because:
  - the pipeline got direction right,
  - the focal forecast was reasonably high already,
  - and the watch-only decision was internally consistent with estimated fair value.
- Recommended follow-up instead:
  - monitor for recurrence of this pattern across similar crypto touch markets;
  - if repeated, test a calibration intervention that raises fair value in cases with:
    - touch-style settlement,
    - sub-1% distance to threshold,
    - and multiple remaining trading days.
- Separate workflow improvement candidate:
  - add structured capture of governing-source event proof so evaluator can tell whether “verification caution” was efficient or laggy.

## Promotion candidates for stable layers

- None yet for stable promotion.
- Candidate to monitor across more cases before promotion:
  - **In 24/7 crypto touch markets, when the threshold is already within roughly 0.5%-1.0% and several days remain, generic resistance and no-catalyst objections may deserve less weight than they receive in ordinary directional setups.**
- Candidate workflow lesson to monitor:
  - **Post-resolution forecast updates should be explicitly labeled as assimilation, not treated as comparable ex ante judgment.**

## How this should be reused later

- Reuse this note when reviewing future Polymarket crypto threshold-touch contracts, especially those tied to Binance intraperiod highs/lows.
- Use it as a comparison case for whether the pipeline systematically:
  - prices these markets below market despite correct direction,
  - over-penalizes missing direct proof,
  - or under-models hazard-style touch probability when distance-to-threshold is tiny.
- If similar cases accumulate, aggregate them into a cross-case calibration study rather than promoting this lesson from a single resolved example.