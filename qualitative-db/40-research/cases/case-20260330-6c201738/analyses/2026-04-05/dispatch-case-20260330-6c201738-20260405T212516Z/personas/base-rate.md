---
type: agent_finding
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: 426f51d1-0a91-45fd-b2fa-b05594e4768e
analysis_date: 2026-04-05
persona: base-rate
topic: case-20260330-6c201738 | base-rate
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026?
date_created: 2026-04-05
agent: Orchestrator
stance: yes
certainty: medium
importance: high
novelty: medium
time_horizon: through-2026-03-31
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [base-rate, tariff, china, resolution-mechanics, source-hierarchy]
---

# Claim

My base-rate view is that the market is more likely than not to resolve **Yes** because the relevant general tariff rate on China on 2026-03-31 is most plausibly a temporary broad surcharge in the **~10%** range, which falls squarely in the **5%-15%** bracket. The outside-view reason is simple: broad general tariff layers usually come from explicit official action, move less often than headline noise suggests, and should not be conflated with product-specific Section 232 / AD-CVD layers that the contract explicitly excludes.

## Market-implied baseline

Current market-implied probability: **95.9%**.

## Own probability estimate

My estimate: **82%**.

## Agreement or disagreement with market

I **disagree modestly** with the market. I agree the most likely bracket is 5%-15%, but 95.9% looks too confident for a high-resolution-risk market with timing, exclusion, and source-hierarchy ambiguity.

Base-rate logic:
- The broad outside-view prior favors a stable, administratively legible general tariff layer rather than a constantly changing or highly bespoke reading.
- Official and contextual evidence both point toward a temporary **Section 122** broad surcharge as the key general layer.
- A figure around **10%** appears to be the central live case, which is comfortably inside the target bracket.
- But this is still a date-specific rule market. A later official action, expiration, pause, or clarification could matter, and the official text surfaced in this run was incomplete in excerpt form.

## Implication for the question

This should be interpreted as **likely Yes, but not near-certain Yes**. The market seems directionally right but underpricing rule-mechanics risk.

## Key sources used

Primary / direct for source-of-truth:
- Federal Register API result for the 2026-02-25 presidential document **"Imposing a Temporary Import Surcharge To Address Fundamental International Payments Problems"**; see source note: `qualitative-db/40-research/cases/case-20260330-6c201738/source-notes/2026-04-05-base-rate-federal-register-section-122.md`
- Market contract wording from the Polymarket event page / case surface, which defines what counts, excludes item-specific increases, and excludes paused/not-yet-effective tariffs.

Secondary / contextual:
- Tax Foundation, **"2026 Trump Tariffs & Trade War by the Numbers"**; see source note: `qualitative-db/40-research/cases/case-20260330-6c201738/source-notes/2026-04-05-base-rate-tax-foundation-2026-tariffs.md`
- USTR homepage leadership/context page confirming a strongly tariff-oriented trade-policy posture under Ambassador Jamieson Greer; useful background only, not settlement evidence.

Evidence-floor compliance:
- At least three meaningful sources used: (1) market contract/case text, (2) official Federal Register result, (3) independent secondary contextual analysis from Tax Foundation.
- Supporting provenance artifacts created: 2 substantive source notes, 1 assumption note, 1 evidence map, plus this finding.

## Supporting evidence

The strongest evidence for Yes is the combination of:
1. **Official source hierarchy**: a Federal Register presidential-document result indicates a live **Section 122 temporary import surcharge** treated as a regular customs duty.
2. **Contract logic**: the market asks for the **general tariff rate** and excludes item-specific exceptions/increases. That pushes interpretation toward the broad surcharge layer, not total product-level trade restrictions.
3. **Independent contextual fit**: Tax Foundation frames the live broad-rate scenario as **10% Section 122 while in effect**, with **15%** treated as an alternative scenario. That aligns with the bracket rather than an above-15% reading.

## Counterpoints / strongest disconfirming evidence

Strongest disconfirming consideration: **the full operative official text was not fully captured in this run**, so exact percentage and exact effective/expiration mechanics were not independently verified from the complete proclamation text.

Other meaningful counterpoints:
- This is a politically changeable policy area; a later official action could raise, pause, replace, or terminate the general surcharge before 2026-03-31.
- If the true governing general China-relevant rate is interpreted as stacking an additional broad China-specific layer on top of the baseline, the bracket could move above 15%.

## Resolution or source-of-truth interpretation

Governing source of truth: **official Trump-administration materials**, with Federal Register / presidential proclamation surfaces strongest if they specify the operative general tariff in effect on the target timestamp.

What counts:
- A **general tariff or surcharge actually in effect** on imports from China at **2026-03-31 12:00 PM ET**.
- Additive general layers if they are broad and generally applicable under the contract's example.

What does not count:
- **Paused** tariffs.
- **Announced but not yet effective** tariffs.
- **Item-specific exceptions or increases**.
- Broader "effective tariff rate" calculations based on revenue incidence rather than the contract's stylized base-rate logic.

Case-specific checks:
- **Verify in effect timing:** explicitly addressed. My view assumes the relevant Section 122 surcharge remains in force on the target date; this remains a live verification need closer to resolution.
- **Exclude paused announcements:** explicitly addressed. I am not counting threatened or announced tariff changes that are not in force.
- **Confirm source hierarchy:** explicitly addressed. Official administration/Federal Register materials outrank analytical summaries.
- **Validate rate calculation logic:** explicitly addressed. I am using the contract's general-rate concept, not product-specific duties and not revenue-based effective tariff measures.

## Key assumptions

- The temporary Section 122 surcharge, or its direct successor, remains the operative broad tariff layer for the target date.
- No superseding official action pushes the relevant general China tariff above 15% before 2026-03-31.
- Contract interpretation continues to exclude Section 232 / product-specific tariffs from the bracket calculation.

## Why this is decision-relevant

The key decision issue is not whether the tariff environment is broadly hawkish; it is whether the **specific contract-defined general rate in force** lands inside the bracket. This run says the outside view still favors **inside the bracket**, but warns against treating a noisy tariff environment as equivalent to a settled >95% resolution path.

## What would falsify this interpretation / change your mind

The most important things that could change my mind:
- Full official proclamation text showing the operative general rate is **above 15%** or otherwise outside the bracket.
- A later White House / Federal Register action changing or pausing the surcharge before the target timestamp.
- Credible consensus reporting, tied to official sources, showing the correct additive general-rate logic for China is not ~10% but a higher broad rate outside the bracket.

## Source-quality assessment

- **Primary source used:** Federal Register result for the 2026-02-25 presidential document on the temporary import surcharge.
- **Most important secondary/contextual source:** Tax Foundation's 2026 tariff analysis.
- **Evidence independence:** **medium**. The sources are not duplicates, but both are still orbiting the same policy regime.
- **Source-of-truth ambiguity:** **medium-to-high**. Official source hierarchy is clear, but exact operative rate/timing text was not fully captured in this run.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the view?** No material direction change.
- **Effect of verification:** It increased confidence that the right frame is a Section 122 general-surcharge reading and reduced confidence in any casual product-specific or effective-rate interpretation. It also kept me from matching the market's near-certainty because the exact official text remained partially unverified.

## Reusable lesson signals

- Possible durable lesson: tariff markets with "general rate" wording need an explicit split between **general statutory layer** and **effective/product-specific burden**.
- Possible missing or underbuilt driver: none clearly identified from this run alone.
- Possible source-quality lesson: in tariff-resolution markets, Federal Register / proclamation text should be captured directly when possible; secondary average-tariff analysis is not enough for settlement.
- Confidence that lesson is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **no**.
- Reason: this case reinforces a reusable methodology lesson about separating official in-force general tariff layers from item-specific or effective-rate narratives.

## Recommended follow-up

Closer to resolution, do a narrow legal-text refresh:
1. pull the full proclamation / Federal Register text,
2. confirm the exact surcharge percentage,
3. confirm it is still in effect at 2026-03-31 12:00 ET,
4. check for any superseding White House action,
5. re-test whether any broad China-specific layer should be added under the contract without importing item-specific duties.