---
type: agent_finding
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: 24097620-9e3a-4275-9a52-82cc98ae4c72
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: corporate-bitcoin-treasury
entity: bitcoin
topic: "MicroStrategy/Strategy >1000 BTC purchase announcement in April 7-13 window"
question: "Will MicroStrategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026?"
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
stance: yes
certainty: high
importance: high
novelty: medium
time_horizon: immediate
related_entities: ["bitcoin"]
related_drivers: ["reliability"]
proposed_entities: ["Strategy Inc", "Michael Saylor"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["polymarket", "strategy", "bitcoin", "catalyst-hunter", "official-source", "timing"]
---

# Claim

A YES outcome is very likely and functionally close to settled: Strategy's official purchases page updated on April 13 with a disclosure of **13,927 BTC acquired**, well above the >1000 BTC threshold, which appears to satisfy the market's announcement requirement inside the April 7-13 window.

## Market-implied baseline

Current market price is **0.96**, implying roughly **96%** probability of YES.

## Own probability estimate

**99% YES.**

## Agreement or disagreement with market

I **roughly agree with the market**, but I am slightly more confident. The market was already pricing in the usual Monday-morning Strategy bitcoin disclosure pattern; the decisive catalyst now appears to have actually occurred via the April 13 company update. My residual gap versus market is just a small source-of-truth interpretation risk.

## Implication for the question

The key catalyst was the expected Monday official disclosure cycle. That catalyst has now fired. Unless there is an unexpected resolution-source objection, the market should resolve YES because the company announced a purchase of far more than 1000 BTC within the designated date window.

## Key sources used

Evidence-floor compliance: **met and exceeded**. I used one direct primary source plus one additional official contextual verification source, and performed an extra verification pass because the market was at an extreme probability.

Primary / direct / governing evidence:
- `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-catalyst-hunter-strategy-purchases-page.md` — official Strategy purchases page showing April 13 row for 13,927 BTC and linked 8-K.

Secondary / contextual official verification:
- `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-source-notes/2026-04-13-catalyst-hunter-strategy-press-pattern.md` — official Strategy press archive and prior BTC acquisition release establishing announcement pattern on company-owned surfaces.

Supporting audit artifacts:
- `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/assumptions/catalyst-hunter.md`
- `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/evidence/catalyst-hunter.md`

Governing source of truth:
- Per contract, the governing source of truth is **official information from MicroStrategy/Strategy or Michael Saylor**. In practice here, the decisive evidence is the official Strategy purchases page and its linked 8-K disclosure.

## Supporting evidence

- Strategy's official purchases page shows an entry dated **2026-04-13** with **13,927 BTC** acquired and total holdings rising to **780,897 BTC**.
- The same official row includes company social copy stating that Strategy **has acquired 13,927 BTC for ~$1.00 billion**.
- The disclosure was published on April 13, inside the market window, and the contract explicitly says the market resolves based on **announcement timing**, not when the purchases were made.
- Historical official press releases show that Strategy regularly uses company-owned surfaces to announce BTC purchases, making this announcement channel credible and resolution-relevant.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not factual but interpretive**: the market text says resolution will be based on official information from MicroStrategy or Michael Saylor, leaving a small chance that an adjudicator could insist on a narrower announcement surface than the purchases page plus linked 8-K. I think that risk is small, but it is the main remaining way this could become messy.

## Resolution or source-of-truth interpretation

This is a narrow date-specific market, so wording matters:
- The contract asks whether MicroStrategy announces a purchase of more than 1000 BTC between **12:00 AM ET April 7** and **11:59 PM ET April 13**.
- The contract explicitly says the market resolves based on **announcements made within the time frame regardless of when the actual purchases were made**.
- The official Strategy purchases page posted an April 13 entry for 13,927 BTC and linked the relevant 8-K, so the main issue is whether that company-owned disclosure counts as official information from MicroStrategy/Strategy. I judge that it does.

## Key assumptions

- The April 13 purchases-page disclosure and linked 8-K qualify as official company information for resolution.
- The publication timing falls within the ET deadline window.
- No correction or withdrawal will be issued before resolution.

## Why this is decision-relevant

This market was primarily a **timing** question rather than a thesis-on-bitcoin question. The important catalyst was whether Strategy would publish its routine Monday acquisition disclosure before the weekly market closed. That catalyst now appears to have occurred, which should remove most residual uncertainty and limit further repricing path risk.

## What would falsify this interpretation / change your mind

I would change my view materially if any of the following happened:
- Polymarket or an official resolver clarified that the purchases page / linked 8-K does **not** count as an acceptable announcement surface.
- Strategy corrected or withdrew the April 13 13,927 BTC disclosure.
- Credible timing evidence emerged showing the relevant official announcement occurred outside the ET market window.

## Source-quality assessment

- **Primary source used:** Strategy's official purchases page, which directly lists the April 13 BTC acquisition and links the relevant filing.
- **Key secondary/contextual source used:** Strategy's official press archive plus a prior BTC acquisition press release showing the company's normal announcement pattern.
- **Evidence independence:** **Low-to-medium** in a strict sense because both are issuer-controlled sources, but acceptable here because the contract explicitly points to official company/Saylor information as the governing truth set.
- **Source-of-truth ambiguity:** **Low-to-medium**. Event occurrence ambiguity is low; the only ambiguity is whether the purchases page plus linked filing is accepted as the exact qualifying announcement surface.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the view?** No major directional change.
- **Impact:** It moved the case from "very likely yes based on pattern expectation" to "near-settled yes based on observed official company disclosure," while leaving only a small interpretation caveat.

## Reusable lesson signals

- Possible durable lesson: for Strategy/MicroStrategy weekly BTC markets, the decisive catalyst is often the Monday company disclosure cycle rather than any broader crypto-news flow.
- Possible missing or underbuilt driver: none clearly identified; existing `reliability` is sufficient for this narrow recurring disclosure pattern.
- Possible source-quality lesson: company-maintained purchases trackers can be stronger than generic news coverage when the market's source of truth is issuer-controlled.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **no**
- review later for canon or linkage issue: **yes**
- one-sentence reason: recurring Strategy BTC-announcement markets may merit a small canonical note or linkage around issuer-controlled disclosure surfaces and weekly timing pattern, and `Strategy Inc` lacks a clean canonical slug in this run.

## Recommended follow-up

No major follow-up suggested unless there is a live dispute over whether the purchases page/8-K combination counts for resolution; if that dispute emerges, the next best check is an explicit same-day Michael Saylor or company press/social post mirroring the 13,927 BTC disclosure.