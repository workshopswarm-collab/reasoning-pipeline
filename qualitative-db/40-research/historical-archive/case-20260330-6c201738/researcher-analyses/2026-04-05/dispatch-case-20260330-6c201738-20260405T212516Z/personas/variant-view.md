---
type: agent_finding
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: 47c44de8-8925-4cfd-9ae5-c4fa4eafa0f2
analysis_date: 2026-04-05
persona: variant-view
domain: trade-policy
subdomain: tariffs
entity: united-states-china-trade
topic: case-20260330-6c201738 | variant-view
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31?
driver: official-order-timing
date_created: 2026-04-05
agent: Orchestrator
stance: no
certainty: medium
importance: high
novelty: medium
time_horizon: through-2026-03-31
related_entities: [china, united-states, white-house]
related_drivers: [official-order-timing, tariff-stack-calculation, source-hierarchy, paused-vs-in-effect-orders]
upstream_inputs: []
downstream_uses: [orchestrator-synthesis]
tags: [variant-view, tariffs, china, polymarket, high-resolution-risk]
---

# Claim

The strongest credible variant view is not that **Yes** is currently more likely, but that the market may be **too confident** in No because the only realistic path into the 5–15% bracket is a future rollback/legal-status path that leaves only the universal 10% tariff in effect by noon ET on March 31, 2026. As of the official orders reviewed, however, the operative China tariff stack is well above 15%, so I still land **No**.

## Market-implied baseline

Current price is 0.959, implying roughly **95.9% No / 4.1% Yes** if interpreted as the No-side market context in the assignment. Put differently: the market is very close to certain that China will **not** be in the 5–15% band.

## Own probability estimate

**No: 88%**

Equivalent **Yes: 12%**.

## Agreement or disagreement with market

I **roughly agree on direction** with the market, but I think the market is somewhat **overconfident**.

Why I still agree on direction:
- Official Trump-administration orders show a China tariff stack far above the bracket.
- The contract says to count the general tariff on all imports plus any general tariff on Chinese imports.
- The contract excludes only item-specific exceptions/increases and paused or not-yet-effective tariffs.

Why I am less extreme than the market:
- This is a high-resolution-risk contract with material legal and administrative fragility.
- The only serious path to Yes is not current mismeasurement; it is that by March 31, 2026 the administration has rolled back, lost, or replaced the China-specific layers so that only a 10% broad tariff remains in effect.
- That path is not base case, but it is not absurdly small either.

## Implication for the question

If resolution were based on the official orders reviewed here and nothing materially changed before March 31, 2026, the answer should be **No** by a wide margin. The contract only gets into the 5–15% band if later official developments collapse the China-specific general tariff layers before the resolution timestamp.

## Key sources used

**Primary / authoritative source-of-truth set**
1. White House April 2, 2025 reciprocal tariff order: imposed a 10% all-country tariff effective April 5, 2025 and set country-specific reciprocal rates effective April 9, 2025.
2. White House April 9, 2025 modification order: suspended most countries’ higher reciprocal rates to 10% for 90 days **except China**, and raised the China reciprocal rate to 125% effective April 10, 2025.
3. White House March 3, 2025 China fentanyl order: raised the China-specific opioid-related tariff from 10% to 20%.
4. White House April 2025 fact sheet: plain-language confirmation of effective dates and 10% baseline structure.

**Secondary / contextual source**
5. Tax Foundation 2026 tariff summary: useful contextual check on later legal/policy fragility, including discussion of IEEPA tariffs being ruled unlawful and replacement Section 122 mechanics.

**Case provenance artifacts**
- Source note: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-source-notes/2026-04-05-variant-view-white-house-tariff-orders.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/evidence/variant-view.md`
- Assumption note: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/assumptions/variant-view.md`

## Supporting evidence

- **Verify in-effect timing:** the White House orders give explicit effective timestamps. The 10% universal tariff took effect April 5, 2025; the China reciprocal escalation took effect April 10, 2025; the China fentanyl tariff had already been raised to 20% on March 3, 2025.
- **Exclude paused announcements:** the April 9 order explicitly suspended higher country-specific reciprocal rates for many countries, but **not for China**. That exclusion matters more than headlines about a broad “pause.”
- **Confirm source hierarchy:** the contract says the primary resolution source is official Trump-administration information, with consensus reporting as fallback/context. White House orders therefore dominate the analysis unless later official guidance changes the picture.
- **Validate rate calculation logic:** the contract says to include both any general tariff on all imports and any general tariff imposed on Chinese imports. That strongly favors additive treatment of the universal 10% layer plus broad China-specific layers, while excluding item-specific exceptions or increases.

On this logic, even the narrower official stack of **10% universal + 20% China fentanyl = 30%** is already above the bracket. If the China reciprocal 125% layer remains operative, the answer is even more decisively No.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that the market resolves on **March 31, 2026**, not in April 2025. Later legal or policy developments could strip out the China-specific general layers while leaving only a 10% universal tariff in effect. The Tax Foundation 2026 summary is important because it points to exactly that kind of fragility: some IEEPA tariff layers may not survive intact and may be replaced by different authorities.

## Resolution or source-of-truth interpretation

**What counts:**
- broad tariffs in effect on imports into the U.S. from China at **March 31, 2026 12:00 PM ET**
- both all-country general tariffs and China-specific general tariffs
- official Trump-administration tariff orders and other official administration information as the primary source hierarchy

**What does not count:**
- item-specific exceptions or increases
- effective tariff burden from product-specific stacks
- tariffs that are announced but not yet effective
- tariffs that are paused at the resolution timestamp

**How contract wording affects the view:**
This contract is not asking for the weighted effective tariff rate, nor just the universal baseline. It asks for the “general tariff rate” and explicitly gives an additive example. That wording is the main reason the market is hard to get into the 5–15% bucket once China-specific general tariffs exist.

## Key assumptions

- The China fentanyl tariff and China reciprocal tariff qualify as broad China-specific tariffs rather than item-specific exceptions.
- A later legal ruling matters only if it changes what is actually “in effect” by the resolution timestamp under the contract’s source hierarchy.
- The additive reading of “general tariff rate” is the intended resolution method.

## Why this is decision-relevant

This is a good example of a market where the consensus direction may be right but the confidence can still be miscalibrated. The variant edge is not a present-tense Yes case; it is recognizing that the live residual risk comes from **future official rollback or legal-status collapse**, not from simplistic readings of today’s tariff headlines.

## What would falsify this interpretation / change your mind

I would move materially toward Yes if I saw any of the following closer to resolution:
- an official Trump-administration order or guidance removing China-specific general tariff layers and leaving only a 10% universal tariff,
- authoritative implementation material showing China’s operative general tariff is 10% at noon ET on March 31, 2026,
- credible consensus reporting near resolution, tied back to official sources, that the China-specific IEEPA layers are no longer in effect.

## Source-quality assessment

- **Primary source used:** White House executive orders / presidential actions and White House fact sheet.
- **Most important secondary/contextual source used:** Tax Foundation 2026 tariff summary.
- **Evidence independence:** **medium**. The primary evidence is highly authoritative but concentrated in one source family; the contextual verification source is independent.
- **Source-of-truth ambiguity:** **medium-high**. The contract names official administration information as primary, but the actual March 2026 answer could still depend on how official policy, legal status, and consensus reporting interact.

## Verification impact

- **Additional verification pass performed:** yes.
- **What I checked:** explicit effective dates, China’s treatment versus the 90-day reciprocal pause, source hierarchy, and whether additive rate logic was actually supported by contract wording.
- **Did it materially change the view?** It changed the mechanism emphasis more than the directional estimate. It made me more confident that current official policy is well above 15%, while reinforcing that the only serious Yes path is future rollback/legal-status change.

## Reusable lesson signals

- Possible durable lesson: extreme-probability tariff markets can still hide nontrivial resolution risk when “in effect” timing and additive tariff logic matter.
- Possible missing or underbuilt driver: a reusable driver around **policy stack survivability** or **official-policy vs operative-legal-status divergence**.
- Possible source-quality lesson: for tariff markets, primary orders plus explicit effective dates matter more than headline summaries about “pauses.”
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: this case suggests a recurring research pattern where markets hinge on stacked-policy arithmetic plus future survivability of the layers, not merely current headline rates.

## Recommended follow-up

Near the resolution date, do a narrow refresh focused only on:
1. latest official White House/USTR tariff orders,
2. operative HTSUS/implementation status for broad China tariffs,
3. whether any China-specific general layers have been paused, terminated, or legally displaced.

## Compliance with assignment checklist / evidence floor

- Market-implied probability stated: **yes**.
- Own probability estimate stated: **yes**.
- Strongest disconfirming evidence stated explicitly: **yes**.
- What could change my mind stated explicitly: **yes**.
- Governing source of truth explicitly identified: **yes**.
- Source-quality assessment included: **yes**.
- Verification impact included: **yes**.
- Reusable lesson signals included: **yes**.
- Orchestrator review suggestions included: **yes**.
- Evidence floor met with at least three meaningful sources: **yes**.
  - White House March 3, 2025 China tariff order
  - White House April 2, 2025 reciprocal tariff order
  - White House April 9, 2025 modification order
  - White House April 2025 fact sheet
  - Tax Foundation 2026 contextual verification source
- Provenance preserved via source note + evidence map + assumption note: **yes**.