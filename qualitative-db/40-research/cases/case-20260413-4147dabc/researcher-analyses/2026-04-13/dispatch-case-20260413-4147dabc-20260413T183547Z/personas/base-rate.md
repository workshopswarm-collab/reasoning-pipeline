---
type: agent_finding
case_key: case-20260413-4147dabc
dispatch_id: dispatch-case-20260413-4147dabc-20260413T183547Z
research_run_id: e87346ad-1125-4911-8780-4bee507beade
analysis_date: 2026-04-13
persona: base-rate
domain: wildlife
subdomain: bald-eagle-nesting
entity:
topic: first-eaglet-hatch-date-traverse-city-2026
question: "Will the first eaglet hatch on April 11, 2026?"
driver: operational-risk
date_created: 2026-04-13
agent: Orchestrator
stance: no
certainty: medium
importance: high
novelty: medium
time_horizon: days
related_entities: []
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["great-lakes-bald-eagle-cam", "polymark"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "base-rate", "wildlife", "hatch-date", "exact-date-market"]
---

# Claim
My base-rate view is **No on April 11**. An April 11 first hatch is clearly plausible, but the market’s 94.45% implied probability is too high for an **exact-date** outcome that depends on both species-level timing and livestream-visible emergence timing.

## Market-implied baseline
Current price is **0.9445**, implying about **94.45%** for April 11.

## Own probability estimate
My estimate is **68%** for April 11.

## Agreement or disagreement with market
I **disagree** with the market. The outside view says April 11 is likely in the relevant hatch window, but not close to certain.

Why:
- The best biological base rate I found is **34-36 days incubation** for bald eagles (Cornell), which already implies a small but real multi-day window even if laying dates were known exactly.
- The case prompt says there are **three incubating eggs**, which makes April 11 plausible, but it does not itself collapse uncertainty to a single day for the **first** fully emerged eaglet.
- The contract is narrow: a **pip or partial emergence does not count**. That makes exact-date timing slightly noisier than "first visible crack" timing.
- The contract also has a livestream-mechanics wrinkle: if both streams are down and later return showing a hatch occurred while they were offline, the market resolves to the **return date**, not necessarily the true hatch date. That is low-probability, but it is another reason not to round an exact-date market up toward certainty.

## Implication for the question
Outside-view, this looks like a market that may be directionally right about the modal date but is **overconfident on the exact day**. A disciplined prior should allow meaningful probability mass on adjacent dates and on contract-mechanics edge cases.

## Key sources used
1. **Primary / direct contract source:** Polymarket market page and contract text for the exact resolution wording and source-of-truth mechanics. This is authoritative for settlement rules.
2. **Primary-contextual / direct case source:** Great Lakes Bald Eagle Cam YouTube livecam page, including operator description and linked bulletin-board/log-book reference. See `qualitative-db/40-research/cases/case-20260413-4147dabc/researcher-source-notes/2026-04-13-base-rate-youtube-livecam-description.md`.
3. **Secondary / contextual independent source:** Cornell Lab of Ornithology All About Birds Bald Eagle life history for the species-level incubation base rate. See `qualitative-db/40-research/cases/case-20260413-4147dabc/researcher-source-notes/2026-04-13-base-rate-cornell-bald-eagle-life-history.md`.
4. **Additional verification pass:** U.S. Fish & Wildlife Service bald eagle species page for general species credibility/context, though it was less useful on the exact timing question than Cornell.

Evidence-floor compliance: **met**. I used one governing primary source plus one nest-specific contextual source plus one strong independent biological contextual source, and I performed an extra verification pass because the market was at an extreme probability.

## Supporting evidence
- Cornell gives a **34-36 day incubation period**, which is narrow enough that an April 11 hatch can easily be the modal outside-view date if first lay was around early March.
- The livecam operator description says the pair raised **three eaglets in 2024**, suggesting the nest is operationally real and recent successful hatching is not an outlandish path.
- The operator also frames **March-April** as the usual hatching window, which is broadly consistent with April 11 being in-range.

## Counterpoints / strongest disconfirming evidence
The strongest disconfirming consideration to my bearish-vs-market stance is that the market may already be informed by nest-specific lay-date tracking from the livecam/log-book community. If the first egg date is tightly known and points almost exactly to April 11, then a high probability on that date is more justified than a pure outside view would allow.

## Resolution or source-of-truth interpretation
Governing source of truth: **the Great Lakes Bald Eagle Cam livestream timestamps**, as specified by the Polymarket contract.

Material conditions for an April 11 "Yes":
1. At least one egg must produce the **first** eaglet.
2. The eaglet must be **visibly fully emerged from the shell** on **April 11, 2026 ET**.
3. A mere **pip** or partial emergence on April 11 is **not sufficient**.
4. The relevant timing is based on the **live timestamps** available on the designated livestreams.
5. If **both** livestreams are unavailable and later return showing the hatch occurred while offline, the contract resolves to the **calendar date when the livestream returns**, not necessarily the actual unseen hatch date.

Date / timezone verification: I explicitly used the contract’s **calendar date in ET** and the fallback deadline of **April 16, 2026 11:59 PM ET** for the no-hatch bucket. For this specific question, the key window is whether the first full emergence is visible on **April 11 ET**, not local Michigan civil time phrased vaguely elsewhere.

Canonical-mapping check:
- Clean canonical slug used: `polymark` and drivers `operational-risk`, `reliability`.
- Structurally important uncaptured entity: **Great Lakes Bald Eagle Cam** does not appear to have a clean canonical entity slug in the vault, so I recorded it under `proposed_entities` instead of forcing a weak fit.
- No additional driver gap clearly required; existing `operational-risk` and `reliability` are adequate for the stream-resolution wrinkle.

## Key assumptions
- The market is not mis-specified about the actual nest / eggs being monitored.
- The livecam community’s implied lay-date consensus, if any, is not so precise that April 11 should be treated as near-certain.
- No major outage or source-of-truth anomaly distorts the visible hatch date.
- Ordinary biological timing remains the dominant mechanism.

## Why this is decision-relevant
At 94%+, the main question is not whether April 11 is plausible; it is whether the residual uncertainty is being underpriced. Exact-date wildlife markets often deserve more humility than broader "within the normal window" markets because biological variance and observation-rule variance both matter.

## What would falsify this interpretation / change your mind
I would move materially toward the market if I saw a credible nest-specific log confirming the first egg was laid on a date that makes **April 11 the overwhelmingly likely day** under observed incubation norms, or if there were current livecam observations showing a near-imminent full hatch on April 11 ET rather than adjacent-date ambiguity.

## Source-quality assessment
- Primary source used: **Polymarket contract text** for the governing resolution mechanics.
- Most important secondary/contextual source: **Cornell All About Birds** for incubation timing; **Great Lakes Bald Eagle Cam description** for nest-specific context.
- Evidence independence: **medium**. Cornell is independent; the livecam/operator context is not independent of the governing observation surface.
- Source-of-truth ambiguity: **medium**. The contract is explicit, but the "visible fully emerged" threshold and outage-return rule create nontrivial date-label ambiguity around edge cases.

## Verification impact
- Additional verification pass performed: **yes**.
- Why: market implied probability was above the >85% threshold and the contract is date-sensitive and multi-condition.
- Impact on estimate: **not material**. Extra checking reinforced that April 11 is biologically plausible, but it did not justify moving from a high-likelihood exact-date call to near-certainty.

## Reusable lesson signals
- Possible durable lesson: exact-date biological-event markets can look overconfident when communities infer a modal date from incubation norms and lay-date chatter, especially when contract wording requires a stricter visible threshold than the underlying biological start of hatch.
- Possible missing or underbuilt driver: none clearly beyond existing operational-risk / reliability.
- Possible source-quality lesson: when public nest log books are linked from livestream operators but not machine-readable, preserving the link and noting the accessibility limitation is still useful provenance.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions
- Review later for durable lesson: **yes**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **yes**.
- Reason: this case suggests a reusable lesson on exact-date biological-event overconfidence, and the Great Lakes Bald Eagle Cam may merit a canonical entity if this family of markets recurs.

## Recommended follow-up
If higher precision is needed before synthesis, the best marginal next step is to obtain the nest-specific 2026 lay-date log from the operator bulletin board or visible archived stream notes. That is the one likely source that could move this estimate by more than ~5 points; absent that, the outside-view case is already good enough to write decisively.
