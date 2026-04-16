---
type: agent_finding
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
research_run_id: 3873543e-4060-46a5-b9d1-b3bd21d4f835
analysis_date: 2026-04-15
persona: variant-view
domain: politics
subdomain: legislative-power
entity: u-s-congress
topic: fisa-section-702-reauthorization-before-expiration
question: "Will legislation reauthorizing FISA Title VII including Section 702 be passed by both chambers and signed into law by April 19, 2026, 11:59 PM ET?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
stance: below-market-yes
certainty: medium
importance: high
novelty: medium
time_horizon: 2026-04-19
related_entities: ["u-s-congress", "united-states"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["fisa", "section-702", "congress", "reauthorization", "variant-view"]
---

# Claim

The strongest credible variant view is that the market is overpricing legislative action **by the market deadline** because the underlying legal urgency may be weaker than the headline suggests. Public Law 118-49 appears to have already moved the operative Section 702 / Title VII sunset from April 19, 2024 to **two years after enactment on April 20, 2024**, i.e. effectively **April 20, 2026**. If that reading is right, then the market's fixed deadline of **April 19, 2026 11:59 PM ET** sits slightly before the true statutory expiry, and that one-day gap matters in a contentious surveillance fight where brinkmanship and slippage are plausible.

Evidence-floor compliance: met with (1) primary official enacted-law text from GovInfo for Public Law 118-49 and (2) the market's own resolution criteria / source-of-truth language from Polymarket. I attempted an additional primary-source verification via Congress.gov, but that source was inaccessible from this runtime because of a Cloudflare challenge; I treat that as a source-of-truth ambiguity rather than papering over it.

## Market-implied baseline

Current market price is **0.785**, implying about **78.5%** probability of Yes.

## Own probability estimate

**62% Yes.**

## Agreement or disagreement with market

I **disagree** with the market and am materially below it.

The market's strongest argument is straightforward: Congress has already shown willingness to extend Section 702 once, national-security authorities generally prefer continuity, and this kind of surveillance authority often gets renewed at or near the deadline.

The market's fragility is that it may be pricing the generic narrative "702 will get renewed before it expires" without fully netting the exact **contract date** against the apparent **statutory date**. If the actual sunset is April 20, 2026 rather than April 19, 2026, then a bill enacted on April 20 could be legally timely but still resolve this market No. That timing mismatch is the most important underweighted mechanism I found.

## Implication for the question

This is still more likely than not to resolve Yes, because Congress often does act under deadline pressure on national-security authorities. But the contract is narrower than that broad intuition. All of the following must hold for Yes:

1. qualifying legislation must reauthorize FISA Title VII including Section 702;
2. it must pass both the House and Senate;
3. it must become law through signature, no-signature enactment while Congress remains in session, or veto override;
4. all of that must happen **by April 19, 2026 11:59 PM ET**.

The variant view is that timing/slippage risk is underpriced because the market deadline may precede the actual sunset by about one day.

## Key sources used

1. **Primary / direct / authoritative legal source:** Public Law 118-49 enacted text via GovInfo, including Section 19 sunset amendment language. Source note: `qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-source-notes/2026-04-15-variant-view-public-law-118-49.md`
2. **Primary for contract mechanics / direct for resolution logic:** Polymarket market description included in assignment context, especially fixed deadline, qualifying legislation, and named source-of-truth hierarchy. Source note: `qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-source-notes/2026-04-15-variant-view-polymarket-market-description.md`
3. **Attempted extra verification / source-of-truth check:** Congress.gov bill page listed in the market description, but inaccessible in this runtime due to Cloudflare challenge. That failed check did not reverse the view, but it increases source-of-truth ambiguity.

Governing source of truth for this market: per contract, **Congress.gov / Library of Congress / other official U.S. government information** are primary, with credible reporting as fallback. In practice, because Congress.gov was inaccessible here, I relied on **official enacted-law text from GovInfo** as the best accessible government source and treated Congress.gov alignment as the main unresolved verification gap.

## Supporting evidence

- Public Law 118-49 is dated **Apr. 20, 2024**.
- Section 19 of that law replaces the prior expiration reference of **"April 19, 2024"** with **"two years after the date of enactment of the Reforming Intelligence and Securing America Act."**
- Two years after Apr. 20, 2024 maps to **Apr. 20, 2026**, not Apr. 19, 2026.
- The market, however, resolves on legislation enacted **by Apr. 19, 2026 11:59 PM ET**.
- For a divisive surveillance-renewal question, even a one-day mismatch can matter because legislative timing is often messy and late.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is simple: even if the true sunset is Apr. 20, 2026, Congress could still pass a clean extension or another package **before Apr. 19, 2026**, making the timing nuance irrelevant. Also, the market explicitly says qualifying legislation includes **Public Law 118-49**, which raises some risk that the market creator and/or resolver already had a settled official interpretation in mind that I could not fully verify through Congress.gov from this runtime.

## Resolution or source-of-truth interpretation

This market is rule-sensitive and date-sensitive.

- The market's fixed operational deadline is **Apr. 19, 2026 11:59 PM ET**.
- The market says qualifying legislation includes **Public Law 118-49**.
- The market says primary resolution sources are **Congress.gov**, the **Library of Congress**, and other official U.S. government information; credible reporting is fallback.

My interpretation:

- The key legal question is whether Public Law 118-49 made the operative statutory expiration **Apr. 20, 2026**.
- The key market question is narrower: whether qualifying reauthorization legislation is law **by Apr. 19, 2026 11:59 PM ET**.
- Therefore, even if the legal sunset is Apr. 20, this market can still resolve No if Congress misses the market's earlier fixed deadline.

Date / timing / timezone check:

- Assignment says market closes and resolves at **2026-04-18T20:00:00-04:00**, but market description uses enactment deadline **Apr. 19, 2026 11:59 PM ET**.
- For forecasting substance, the relevant legal / contract timing is the **Apr. 19, 2026 11:59 PM ET** enactment cutoff in the market description.
- I explicitly treat the market-description deadline, not the market close timestamp, as the operative resolution timing for the legislative event itself.

## Key assumptions

- Public Law 118-49's "two years after the date of enactment" language is the operative timing reference for the Title VII / Section 702 sunset.
- Congress is less likely to force passage by Apr. 19, 2026 if the real statutory cliff is Apr. 20, 2026.
- No overlooked official source would show that the operative deadline remains Apr. 19, 2026 notwithstanding the enacted-law text.

See linked assumption note: `qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/assumptions/variant-view.md`

## Why this is decision-relevant

At 78.5%, the market is pricing a pretty confident Yes. My view is that this confidence is too high because the exact contract mechanics introduce more failure paths than the headline narrative admits:

- a one-day statutory/contract mismatch;
- the need for both chambers plus enactment by a hard timestamp;
- the possibility that Congress acts only after the market deadline;
- unresolved source-of-truth ambiguity because the primary cited Congress.gov page was not directly verified in runtime.

Those are exactly the kinds of details that create edge in rule-sensitive political markets.

## What would falsify this interpretation / change your mind

I would move materially upward if any of the following occurred:

- Congress.gov or another clearly controlling official source explicitly confirms the operative expiration is **Apr. 19, 2026**, not Apr. 20, 2026;
- leadership schedules or bipartisan agreement make enactment by **Apr. 19, 2026** look highly likely;
- official guidance or credible independent reporting clarifies that the market's reference to Public Law 118-49 means the market is effectively already locked into a Yes-style interpretation.

I would move downward if reporting or official calendars show the issue is drifting toward brinkmanship with no clean vehicle ready before Apr. 19.

## Source-quality assessment

- **Primary source used:** GovInfo enacted text of Public Law 118-49. High quality, direct, official.
- **Key secondary/contextual source used:** the Polymarket contract language itself. This is authoritative for market mechanics, but not for statutory interpretation.
- **Evidence independence:** **medium**. The two key sources answer different layers (law text vs market rules) rather than independently corroborating the same factual claim.
- **Source-of-truth ambiguity:** **medium-to-high** because the market names Congress.gov as primary, but Congress.gov was inaccessible from runtime and the contract also explicitly includes Public Law 118-49 as qualifying legislation.

## Verification impact

- **Additional verification pass performed:** yes.
- I attempted to verify via the named Congress.gov source and searched for additional official/contextual confirmations, but Congress.gov was blocked by Cloudflare and several likely contextual pages were unavailable or moved.
- **Did it materially change the view?** No. It did not change the core estimate, but it **increased my emphasis on source-of-truth ambiguity** and kept confidence at medium rather than high.

## Reusable lesson signals

- **Possible durable lesson:** in rule-sensitive political markets, exact statutory date arithmetic can matter more than the consensus narrative.
- **Possible missing or underbuilt driver:** none with confidence; `operational-risk` is adequate for the slippage/brinkmanship mechanism.
- **Possible source-quality lesson:** when the named official source is inaccessible, preserved official law text from a parallel government source can still support a view, but confidence should be haircut rather than hidden.
- **Confidence that any lesson here is reusable:** medium.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **no**
- one-sentence reason: This looks like a reusable lesson about contract timing versus statutory timing in legislative markets, but not a clear canon or driver gap.

## Recommended follow-up

- Before synthesis, one more source-of-truth check against Congress.gov or a reviewer with browser access would be valuable.
- If accessible, verify whether Congress.gov currently displays the operative sunset as Apr. 19 or Apr. 20, 2026, and whether any official committee leadership materials frame a legislative plan before Apr. 19.
