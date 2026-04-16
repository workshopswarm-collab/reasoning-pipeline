---
type: agent_finding
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 1f2ad283-28d7-4549-afc1-9d240c5f5207
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: "Lee Cronin's The Mummy opening weekend box office bracket"
question: "Will \"Lee Cronin's The Mummy\" Opening Weekend Box Office be between 10m and 15m?"
driver: performance
date_created: 2026-04-16
agent: Orchestrator
stance: slightly-bearish-on-target-bracket
certainty: medium
importance: medium
novelty: medium
time_horizon: immediate
related_entities: ["the-numbers"]
related_drivers: ["performance"]
proposed_entities: []
proposed_drivers: ["box-office-tracking"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "catalyst-hunter", "box-office", "resolution-mechanics"]
---

# Claim
The 10m-15m bracket is live but somewhat overpriced at 70%. My estimate is lower because the accessible pre-release tracking cluster sits at or slightly above the top of the band, and the contract's exact-boundary rule means a 15.0 result loses for this bracket.

## Market-implied baseline
Current price is 0.70, implying about a 70% probability that The Numbers' final 3-day opening-weekend figure lands in the 10m-15m bracket.

## Own probability estimate
55%.

Compliance with evidence floor: met medium-case floor using one authoritative settlement/source-of-truth layer (Polymarket rules + The Numbers release page as governing source context) plus one strong current contextual tracking source summarizing BoxOffice Pro and BoxOfficeTheory. Also performed an extra verification pass on official release timing and Box Office Mojo finality cross-check language.

## Agreement or disagreement with market
I disagree modestly with the market. The band is plausible, but 70% looks too high given that the most accessible tracking is clustered around 15m-20m / roughly 14m-20m, with 15m as a common center of gravity. For this contract, that is awkward because exact boundary values resolve upward to the higher bracket. So the market is effectively paying full freight for a range whose top edge is hostile.

## Implication for the question
The main near-term repricing path is straightforward: preview and Friday reporting will likely determine whether the film is truly sitting just under 15m, or whether it is pacing clearly above it. If early numbers imply 16m+, the current 10m-15m contract should weaken quickly. If they imply a softer mid-teens start, the bracket remains competitive but still exposed to the 15.0 cutoff.

## Key sources used
- Primary / authoritative settlement mechanics: Polymarket market description, which explicitly says resolution uses The Numbers 3-day opening weekend figure once final, with Box Office Mojo used as a finality backstop if needed.
- Primary / direct release-date context: The Numbers title page for Lee Cronin's The Mummy, which lists domestic wide release on April 17, 2026. Source note: `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-source-notes/2026-04-16-catalyst-hunter-the-numbers-resolution-and-release.md`
- Secondary / contextual tracking: ComingSoon same-day report summarizing BoxOffice Pro and BoxOfficeTheory opening-weekend tracking. Source note: `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-source-notes/2026-04-16-catalyst-hunter-tracking-context.md`
- Secondary / corroborative release timing: Warner Bros. Horror official site confirming North America theatrical release on April 17, 2026.

## Supporting evidence
- The contract is explicitly keyed to The Numbers' final 3-day weekend figure for April 17-19, and that figure typically includes Thursday previews. That sharply defines the catalyst window.
- The best accessible current tracking cluster is not centered safely inside the 10m-15m band; it is centered at the top edge or above it.
- The cited BoxOffice Pro range is 15m-20m, and BoxOfficeTheory is described as 15m point estimate with 14m-20m range. That leaves the target bracket plausible, but not 70%-likely in my view.
- The official release is immediate, so the highest-information catalysts are imminent: previews, Friday daily gross, then weekend actuals.

## Counterpoints / strongest disconfirming evidence
The strongest disconfirming consideration is that one of the cited contextual ranges does include 14m, and horror openings can slide a bit lower than tracking if walk-up demand disappoints. In other words, a result just below 15m is very plausible, which is exactly why this market is not a low-probability tail. I am not bearish enough to put the bracket below 50%.

## Resolution or source-of-truth interpretation
Governing source of truth: The Numbers movie page / Box Office tab weekend-performance figure, as specified by the market rules.

Material conditions that all must hold for a YES-style interpretation here:
1. The relevant figure is the final 3-day opening weekend amount for April 17-19, 2026.
2. The value used is the The Numbers weekend-performance figure once it is final, not studio estimates.
3. The measured gross must fall within the 10m-15m bracket as defined by the market.
4. If the final figure falls exactly on a bracket boundary, the higher bracket wins, so 15.0 would not count for 10m-15m.
5. If finality is ambiguous, the market waits for confirmation from both The Numbers and Box Office Mojo before resolving.

Date/timing check: the movie's domestic wide release date is April 17, 2026, and the relevant 3-day reporting window is April 17-19, 2026. Resolution remains open until final figures, with fallback only if final data is unavailable by April 26, 2026 at 11:59 PM ET.

Canonical-mapping check: canonical slug confidence is clean for `the-numbers` and `performance`. I did not force a canonical slug for box-office tracking because I did not verify an existing canonical driver note; recorded instead under `proposed_drivers: [box-office-tracking]`.

## Key assumptions
- The tracking summaries cited indirectly through ComingSoon are directionally faithful to BoxOffice Pro and BoxOfficeTheory.
- No late review/audience shock materially shifts turnout beyond a couple of million dollars versus current tracking.
- The final The Numbers weekend figure will not be delayed or made ambiguous enough to alter the practical interpretation of the bracket.

## Why this is decision-relevant
This is a classic catalyst-sensitive band market. The market is not just pricing the terminal outcome; it is pricing whether the film lands just below or at/above an unfriendly boundary. That means preview data and Friday pace matter more than broad franchise discourse.

Most likely repricing catalyst: Thursday preview / Friday opening-day reporting, because it will immediately reveal whether the movie is running below the 15m center-of-gravity or safely above it.

Which catalysts seem priced in vs underpriced:
- Priced in: generic idea that the film opens in the mid-teens.
- Possibly underpriced: the contract-specific boundary risk that exact 15.0 resolves upward, which makes a "roughly 15m" tracking consensus slightly bearish for this bracket rather than neutral.
- Low-information catalyst: soft narrative chatter about franchise nostalgia or general horror momentum without concrete preview/Friday numbers.

## What would falsify this interpretation / change your mind
- A more direct, credible tracking note centered clearly below 14m-15m would make me more favorable to the bracket.
- Strong preview or Friday data implying 16m+ would make me more bearish quickly.
- Any authoritative clarification that the relevant reported figure or bracket handling differs from the current contract reading would matter materially, though the rules appear fairly explicit.

## Source-quality assessment
- Primary source used: Polymarket rules plus The Numbers release page / governing-source context.
- Most important secondary/contextual source: ComingSoon's same-day summary of BoxOffice Pro and BoxOfficeTheory tracking.
- Evidence independence: medium-low. The contextual estimate cluster likely draws from overlapping industry-tracking logic.
- Source-of-truth ambiguity: low-medium. The settlement source is explicit, but finality may depend on both The Numbers and Box Office Mojo if there is ambiguity about whether posted figures are final.

## Verification impact
- Additional verification pass performed: yes.
- What was checked: official release timing and the exact settlement/finality mechanics, including the boundary rule and Box Office Mojo cross-check language.
- Material effect on view: yes, modestly. The boundary rule and tracking center near 15m made me more cautious on the 10m-15m bracket than I would be from a generic "mid-teens horror opener" framing.

## Reusable lesson signals
- Possible durable lesson: band markets around box-office openings can hide meaningful edge in boundary-handling rules when tracking centers near the cutoff.
- Possible missing or underbuilt driver: `box-office-tracking` may deserve a future driver candidate if these cases recur.
- Possible source-quality lesson: media summaries of tracking are useful but should be explicitly discounted for dependence and lack of direct auditability.
- Confidence reusable: medium.

## Orchestrator review suggestions
- Review later for durable lesson: yes.
- Review later for driver candidate: yes.
- Review later for canon or linkage issue: no.
- One-sentence reason: boundary-sensitive entertainment markets may warrant a reusable `box-office-tracking` driver or lesson because contract mechanics and pre-release tracking interact in repeatable ways.

## Recommended follow-up
- Watch Thursday preview reporting and Friday daily gross for immediate repricing.
- On weekend close, check whether early posted numbers are studio estimates versus final figures.
- Before any final synthesis, confirm whether The Numbers and Box Office Mojo both indicate finality if the posted weekend figure remains ambiguous.
