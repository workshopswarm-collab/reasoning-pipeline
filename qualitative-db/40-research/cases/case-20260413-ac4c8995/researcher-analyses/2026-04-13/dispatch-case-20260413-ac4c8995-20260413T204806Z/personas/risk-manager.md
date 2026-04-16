---
type: agent_finding
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 1d891e3b-c016-4597-84a1-27c36126ccf6
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: will-united-left-bsp-win-at-least-one-seat-in-the-2026-bulgarian-parliamentary-election
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
stance: lean-yes
certainty: medium
importance: high
novelty: low
time_horizon: "through 2026-04-19 election and certification window"
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["BSP – United Left"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["bulgaria", "parliamentary-election", "bsp", "united-left", "threshold-risk", "risk-manager"]
---

# Claim

United Left (BSP) is more likely than not to win at least one seat, because the contract only requires any representation and BSP–United Left starts from a recent 19-seat / 7.32% baseline in the October 2024 election. The main bearish path is not ordinary underperformance; it is a sharper-than-expected collapse below Bulgaria's 4% threshold or some procedural disruption around participation or certification.

**Compliance / evidence floor:** met with at least two meaningful sources: (1) governing source-of-truth logic from the market description pointing to Bulgaria's Central Election Commission (CIK) and consensus credible reporting, and (2) independent/contextual election references confirming the 19 April 2026 date, 4% threshold, and BSP–OL's recent parliamentary baseline, supplemented by a current campaign-status verification pass.

## Market-implied baseline

Current market price is **0.735**, implying about **73.5%**.

That price also embeds fairly high confidence that BSP avoids a threshold accident. I think that confidence is somewhat rich relative to the source quality available in this run.

## Own probability estimate

**66%**.

## Agreement or disagreement with market

I **roughly agree directionally** with the market that Yes is likelier than No, but I **disagree modestly on confidence**. My estimate is lower mainly because:

- this is a threshold market, so tail risk matters more than in a broad "will they do well" market;
- Bulgarian politics has been unusually fragmented and unstable;
- the best direct baseline in hand is backward-looking (October 2024), while current-cycle independent polling confirmation was thin in this run.

So the difference is more about uncertainty and fragility than about a totally different directional thesis.

## Implication for the question

Base case remains **Yes**. To get to No, BSP–United Left likely needs to fall from a recent 7.32% result to below the 4% entry threshold, or encounter a meaningful procedural/organizational failure. That is plausible but not my central case.

## Key sources used

- **Authoritative settlement source / primary source of truth:** market rules point to the **Central Election Commission of Bulgaria (CIK)** as the official fallback source if consensus credible reporting is ambiguous. I could not fetch CIK directly here due access blocking, but it remains the governing official source for final resolution.
- **Contextual election reference:** `researcher-source-notes/2026-04-13-risk-manager-bulgaria-election-context.md` based on the 2026 Bulgarian parliamentary election reference page, used for election date, threshold, and party baseline.
- **Additional contextual baseline:** October 2024 Bulgarian parliamentary election reference confirming BSP–OL won **7.32% and 19 seats**.
- **Current-status verification pass:** `researcher-source-notes/2026-04-13-risk-manager-current-context.md` using POLITICO Bulgaria coverage context plus BSP's own April 2026 campaign post to check for obvious non-participation or organizational collapse.

Direct vs contextual:
- **Direct on resolution mechanics:** market description / CIK fallback logic.
- **Direct on current campaign activity:** BSP official site.
- **Contextual on electoral baseline and rules:** election references and news index pages.

## Supporting evidence

- BSP–United Left was recently an actual parliamentary force, with **7.32% and 19 seats** in the October 2024 election.
- The key institutional hurdle is the **4% threshold**, meaning BSP does not need a strong election to resolve Yes; it only needs to remain represented.
- A current verification pass found BSP still visibly campaigning in April 2026, which reduces the chance of an unnoticed ballot-access or operational-collapse tail.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **the lack of a clean, recent independent poll in this run showing BSP safely above 4% right before the vote**. In a fragmented Bulgarian snap-election environment, mid-tier parties can suffer threshold accidents faster than stale baselines suggest.

## Resolution or source-of-truth interpretation

The market resolves Yes if the listed party wins **at least one seat** in the next Bulgarian National Assembly as a result of the 19 April 2026 election.

Important timing and source checks:
- Election date in market description: **19 April 2026**.
- Market close / resolve timestamp provided in assignment: **2026-04-18 20:00 ET**, i.e. the evening before election day in Bulgaria; that means pre-election pricing can persist right up to the vote.
- Primary resolution logic: **consensus of credible reporting**.
- Fallback / ambiguity breaker: **official results reported by Bulgaria's CIK**.

Risk note: because the market uses consensus reporting first and CIK as fallback, there is some temporary settlement ambiguity risk on election night or during certification, but not much structural ambiguity about the underlying proposition.

## Key assumptions

- BSP–United Left remains ballot-present and organizationally intact.
- Its support has not fallen from 7.32% in October 2024 to below the 4% threshold by election day.
- There is no hidden coalition split or registration issue severe enough to prevent seat conversion.

## Why this is decision-relevant

This market is easy to overprice if traders treat "recently represented party" as nearly equivalent to "certain to retain a seat." The risk-manager view is that Yes is still the base case, but threshold and fragmentation risk mean confidence should be capped unless current independent evidence tightens.

## What would falsify this interpretation / change your mind

The fastest evidence that would change my mind would be:

- a credible independent poll or polling average showing BSP–United Left at or below **4%**;
- credible reporting that BSP has a registration, coalition-integrity, or ballot-access problem;
- election-night consensus reporting showing BSP below threshold nationally.

Evidence that would move me toward the market or above it:

- recent independent polling showing BSP clearly and repeatedly above threshold;
- clearer confirmation from CIK-facing election materials that participation is normal and uncontroversial.

## Source-quality assessment

- **Primary source used:** governing market-resolution language naming CIK as official source of truth in ambiguity cases.
- **Most important secondary/contextual source:** election reference pages for the 2026 election structure and the October 2024 result baseline.
- **Evidence independence:** **medium-low**. The best baseline sources are partly reference/aggregator style, and the current-status verification includes the party's own site.
- **Source-of-truth ambiguity:** **low-medium**. Final official source is clear (CIK), but near-term reporting could briefly precede formal certification.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the estimate or mechanism view?** no material directional change.
- **Effect:** it modestly reduced the tail risk of hidden non-participation by confirming active April 2026 campaign presence, but it did not resolve the biggest uncertainty, which is true current vote share vs the 4% threshold.

## Reusable lesson signals

- Possible durable lesson: in parliamentary threshold markets, recent seat-holding status is useful but can create overconfidence when current-cycle polling is thin.
- Possible missing or underbuilt driver: none clearly identified beyond standard `elections` + `polling` interaction.
- Possible source-quality lesson: when CIK or comparable official election sites are hard to fetch programmatically, preserve the governing-source logic explicitly and do not overstate confidence from aggregator pages.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **yes**.
- One-sentence reason: the causally important entity **BSP – United Left** did not have a confirmed canonical entity slug available from local entity surfaces in this run, so it was recorded in `proposed_entities` instead of forcing a weak canonical fit.

## Recommended follow-up

If this market becomes decision-critical before the vote, the highest-value follow-up is a targeted pass on **recent independent Bulgarian polling and/or direct CIK candidate-registration surfaces**. That is the most likely remaining evidence class that could move the estimate by more than a few points.
