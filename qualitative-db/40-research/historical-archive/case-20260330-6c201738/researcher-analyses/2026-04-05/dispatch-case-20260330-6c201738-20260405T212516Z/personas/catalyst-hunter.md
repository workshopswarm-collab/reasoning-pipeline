---
type: agent_finding
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: 70885244-3ed7-4285-ac14-ec9cb33f7e77
analysis_date: 2026-04-05
persona: catalyst-hunter
domain: trade-policy
subdomain: tariffs
entity: united-states-china-trade
topic: case-20260330-6c201738 | catalyst-hunter
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31?
driver: official-order-timing
date_created: 2026-04-05
agent: Orchestrator
stance: no
certainty: medium
importance: high
novelty: medium
time_horizon: through-2026-03-31
related_entities: [china, united-states, white-house, ustr]
related_drivers: [official-order-timing, paused-vs-in-effect-orders, tariff-stack-calculation, source-hierarchy]
upstream_inputs: []
downstream_uses: [orchestrator-synthesis]
tags: [catalyst-hunter, tariffs, china, timing, resolution-risk]
---

# Claim

My directional view is **No**. The most important catalyst insight is that the market likely does **not** get into the 5% to 15% bracket by default; it only gets there if a later concrete event removes or neutralizes one of the broad China-wide tariff layers before **March 31, 2026 12:00 PM ET**. As of the official action chain reviewed, the operative setup looks more like a stacked **10% + 10%** story than a simple single-10% story.

## Market-implied baseline

Current price is **0.959**, implying roughly **95.9% Yes** that the U.S. tariff rate on China will be between 5% and 15% on March 31, 2026.

## Own probability estimate

I estimate **15% Yes / 85% No**.

## Agreement or disagreement with market

I **disagree** with the market on direction, though not because I think the market is irrational to care about future de-escalation. I disagree because the current official chain suggests the market is anchoring too heavily on a single 10% general-rate story and underweighting that a second broad China-wide 10% layer appears to remain in effect.

From a catalyst lens, the market is implicitly pricing one of two things:
1. either only one 10% layer will count for resolution, or
2. one of the broad China-wide layers will be gone by the checkpoint.

I think that is too optimistic for Yes at this stage.

## Implication for the question

The key repricing path is straightforward:
- **Base case now:** No, because two broad China-wide 10% layers likely keep the stack above 15%.
- **Main path to Yes:** a later official rollback, legal displacement, or implementation clarification that leaves only one 10% general layer operative at noon ET on March 31, 2026.

So this market should be watched less like a static tariff-level question and more like an event-driven policy-stack survivability question.

## Key sources used

1. **Primary / authoritative / direct:** White House executive-order chain on China reciprocal tariffs (May 12, Aug. 11, and Nov. 4, 2025), showing a 10% reciprocal layer remained in effect while higher rates were suspended.
2. **Primary / authoritative / direct:** White House executive-order chain on PRC synthetic-opioid duties (Mar. 3 and Nov. 4, 2025), showing the PRC duty was reduced to 10% effective Nov. 10, 2025 rather than eliminated.
3. **Primary / official contextual index:** USTR Presidential Tariff Actions page, used as an official chronology check.
4. **Direct contract source:** Polymarket market description, especially the additive example, the in-effect requirement, the paused-announcement exclusion, and the item-specific exclusion.
5. **Secondary / contextual verification:** Tax Foundation 2026 tariff summary, used mainly as a fragility/catalyst check for how legal or administrative changes could later alter the operative stack.

Supporting provenance artifacts:
- Source note: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-source-notes/2026-04-05-catalyst-hunter-tariff-catalysts-and-official-chain.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/evidence/catalyst-hunter.md`
- Assumption note: `qualitative-db/40-research/cases/case-20260330-6c201738/researcher-analyses/2026-04-05/dispatch-case-20260330-6c201738-20260405T212516Z/assumptions/catalyst-hunter.md`

## Supporting evidence

- The official reciprocal-tariff chain leaves a **10% PRC reciprocal tariff** in effect through the relevant period unless changed later.
- The official synthetic-opioid chain leaves a separate **10% PRC duty** in effect from Nov. 10, 2025 unless changed later.
- The contract’s wording explicitly says the general tariff rate includes stacked general tariffs and excludes only item-specific exceptions/increases, plus paused or not-yet-effective tariffs.
- The highest-information catalysts are therefore not speeches or generic “trade war” headlines, but later official acts that change whether those two broad layers still coexist at the checkpoint.

### Catalyst calendar / watchlist

Most likely meaningful catalysts before resolution:
1. **New White House executive order or proclamation** changing reciprocal or opioid-related China tariffs.
2. **USTR / customs implementation guidance** clarifying the operative broad China tariff stack.
3. **Controlling legal development** that changes what is actually in effect by March 31, 2026.
4. **Resolver clarification** on additive treatment if contract interpretation becomes disputed.

### Most likely repricing catalyst

The single most likely repricing catalyst is a **later official administration action that removes or suspends one of the two broad China-wide 10% layers**. That would immediately make a 5%-15% resolution materially more plausible because the bracket could then be satisfied by a single remaining 10% layer.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is that the market may be right to price a future simplification path: by March 31, 2026, legal or administrative developments could plausibly collapse the China stack to a single 10% general tariff in effect. A narrower resolver interpretation could have a similar effect if only one layer is treated as the relevant “general tariff rate.”

## Resolution or source-of-truth interpretation

**Governing source of truth:** official Trump administration information is primary under the contract; consensus of credible information is secondary/fallback.

**What counts:**
- tariffs actually **in effect** at **March 31, 2026 12:00 PM ET**
- general tariffs on all imports plus general tariffs imposed on Chinese imports
- official White House / administration materials and closely linked official implementation sources

**What does not count:**
- paused tariffs
- announced-but-not-yet-effective tariffs
- item-specific exceptions or increases
- weighted effective tariff calculations based on product mix rather than the contract’s stylized general-rate logic

**How the contract wording affects my view:**
The additive example is doing real work here. If there is a 10% general tariff on all imports and an additional 10% general tariff on Chinese imports, the contract says that equals 20%. That is why this looks like a No market unless one broad China-wide layer disappears before the checkpoint.

### Case-specific checks

- **Verify in effect timing:** addressed. I am relying only on tariff layers with explicit effective-date support and apparent continuity through the checkpoint absent later action.
- **Exclude paused announcements:** addressed. I am not counting suspended higher rates or generic announced threats.
- **Confirm source hierarchy:** addressed. White House orders and official administration chronology dominate; Tax Foundation is contextual only.
- **Validate rate calculation logic:** addressed. I am using the contract’s additive general-rate logic, not product-level effective tariff burden.

## Key assumptions

- Both the reciprocal 10% and the synthetic-opioid 10% count as broad China-wide tariffs under this contract.
- No later official action removes one of those layers before the checkpoint.
- The resolver will treat additive general-rate logic as binding, not optional rhetoric.

## Why this is decision-relevant

This market is not just about the current tariff stack. It is about **which future event would force repricing**. The practical implication is that most daily trade chatter is low-information. The high-information events are a narrow set of formal policy, implementation, and legal catalysts that determine what is still in effect on the exact date.

## What would falsify this interpretation / change your mind

I would move materially toward Yes if any of the following happened:
- an official White House/USTR action removes or pauses one of the two broad 10% China-wide layers,
- authoritative implementation material shows the operative general tariff on China is only 10% at noon ET on March 31, 2026,
- Polymarket or other near-official resolution guidance clearly states only one of these broad layers counts.

## Source-quality assessment

- **Primary source used:** White House executive orders on reciprocal and synthetic-opioid China tariffs.
- **Most important secondary/contextual source used:** Tax Foundation 2026 tariff summary as a check on legal/administrative fragility.
- **Evidence independence:** **medium**. The core evidence is authoritative but concentrated in one official source family; the contextual cross-check is independent.
- **Source-of-truth ambiguity:** **medium**. The official chain is fairly clear, but ambiguity remains around additive interpretation and what may still be in effect at the future checkpoint.

## Verification impact

- **Additional verification pass performed:** yes.
- **What I checked:** whether current official materials actually support two coexisting broad China-wide 10% layers; whether paused announcements were being incorrectly counted; whether the contract’s additive language really matters; and whether the remaining live uncertainty is future-timing rather than current-state confusion.
- **Did it materially change the view?** Yes. It shifted the analysis from “maybe this is just a 10% market” to “this is mainly a future-catalyst market where Yes requires a later change event.”

## Reusable lesson signals

- Possible durable lesson: tariff-bracket markets can be misread when traders anchor on a headline rate instead of the full in-effect policy stack.
- Possible missing or underbuilt driver: **policy-stack survivability** as a reusable driver across trade-policy markets.
- Possible source-quality lesson: “pause” headlines are much lower signal than the underlying effective-date chain in official orders.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: this case looks like a reusable pattern where the market hinges on whether multiple broad policy layers survive to the checkpoint, not on the headline tariff most people remember.

## Recommended follow-up

Closer to resolution, run a narrow catalyst refresh on only:
1. White House / USTR official tariff actions,
2. operative customs / implementation guidance,
3. any controlling legal development that changes what is in effect,
4. any resolver clarification on additive treatment.

## Compliance with assignment checklist / evidence floor

- Market-implied probability stated: **yes**.
- Own probability estimate stated: **yes**.
- Strongest disconfirming consideration explicitly named: **yes**.
- What could still change my mind stated: **yes**.
- Governing source of truth explicitly identified: **yes**.
- Source-quality assessment included: **yes**.
- Verification impact section included: **yes**.
- Reusable lesson signals included: **yes**.
- Orchestrator review suggestions included: **yes**.
- What counts / what does not count / contract effect explained: **yes**.
- Additional case-specific checks explicitly addressed: **yes**.
- Additional verification pass performed and reflected: **yes**.
- Evidence floor met with at least three meaningful sources: **yes**.
  - White House reciprocal-tariff orders
  - White House synthetic-opioid tariff orders
  - USTR official tariff-actions chronology
  - Polymarket contract text
  - Tax Foundation contextual verification source
- Provenance preserved via source note + evidence map + assumption note: **yes**.