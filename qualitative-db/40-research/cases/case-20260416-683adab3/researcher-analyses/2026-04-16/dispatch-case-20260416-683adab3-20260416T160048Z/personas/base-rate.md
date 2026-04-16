---
type: agent_finding
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 461ab88d-a489-4dd7-a787-da45fbbfeff8
analysis_date: 2026-04-16
persona: base-rate
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: lee-cronins-the-mummy-opening-weekend-box-office
question: "Will \"Lee Cronin's The Mummy\" Opening Weekend Box Office be between 10m and 15m?"
driver: performance
date_created: 2026-04-16
agent: orchestrator
stance: slight-yes
certainty: medium
importance: high
novelty: medium
time_horizon: "opening weekend"
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: ["performance"]
proposed_entities: ["lee-cronins-the-mummy", "warner-bros-pictures", "blumhouse-productions", "atomic-monster"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "base-rate", "box-office", "horror", "settlement-check"]
---

# Claim
Base-rate view: the 10m–15m bracket is plausible and slightly more likely than not, but not by enough to justify the market’s current 70% confidence. My directional view is that this lands in the band somewhat more often than not because a 3,200-theater wide horror launch with mixed reviews and non-breakout comps often opens around 10m–12m, but recognizable Mummy IP creates a real over-15m risk.

**Compliance / evidence floor:** met for a medium-difficulty, rule-sensitive case via (1) the named authoritative source and settlement mechanics on The Numbers, plus (2) independent contextual/reception sources (Rotten Tomatoes and Metacritic), plus (3) comparable horror opening data from The Numbers to anchor the outside-view prior.

## Market-implied baseline
Current price is **0.70**, implying about a **70%** chance that the final 3-day opening weekend on The Numbers lands between **$10m and $15m**.

## Own probability estimate
**57%**.

## Agreement or disagreement with market
**Mild disagreement.** I agree that 10m–15m is a live and perhaps modal bucket, but I think the market is leaning too hard into it.

Why I am below market:
- The outside-view comp set for recent wide horror titles in roughly similar theater counts does support a mid-band outcome, but not at 70% confidence.
- The most comparable “ordinary” horror openings I found cluster near the lower edge of this bracket: **Night Swim $11.8m / 3,250 theaters**, **Imaginary $9.9m / 3,118 theaters**, **Abigail $10.3m / 3,384 theaters**.
- The key upside exception is **Evil Dead Rise $24.5m / 3,402 theaters**, also a Warner Bros. horror title with Lee Cronin pedigree adjacent to this case. That makes the **over-$15m** alternative materially real.
- Mixed critical reception (RT excerpts / Metacritic 48) argues against treating this as a breakout horror event, but mixed reviews are not enough to eliminate the IP-driven upside tail.

## Implication for the question
If forced to choose today, I would lean **YES**, but only modestly. The market appears to be pricing the bracket almost as if it were the clearly dominant result. My base-rate read is that the band is only a bit more likely than its main alternative, which is an opening above $15m.

## Key sources used
**Primary / authoritative / direct for settlement mechanics and final resolution source**
- The Numbers movie page for **Lee Cronin’s The Mummy**: confirms April 17, 2026 wide domestic release by Warner Bros. and is the named contract source for final weekend performance.
- The market description itself: resolves on the **The Numbers** “Weekend Box Office Performance” / final 3-day weekend figure for **April 17–19**, with fallback ambiguity handling against Box Office Mojo.

**Primary / direct for base-rate comps**
- The Numbers pages for **Night Swim (2024)**, **Imaginary (2024)**, **Abigail (2024)**, and **Evil Dead Rise (2023)**.
- The Numbers current theater-count context on its home page, stating **Lee Cronin’s The Mummy** is projected to launch in **3,200 theaters**.

**Secondary / contextual**
- Rotten Tomatoes page for release date and mixed review texture.
- Metacritic page showing a **48** metascore and mixed notices.
- Supporting notes:
  - `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-source-notes/2026-04-16-base-rate-the-numbers-and-comps.md`
  - `qualitative-db/40-research/cases/case-20260416-683adab3/researcher-source-notes/2026-04-16-base-rate-reviews-context.md`

## Supporting evidence
- The release is a **wide Warner Bros. horror opening** in about **3,200 theaters**, which is enough scale for an 8-figure start.
- Several recent wide horror comps with similar footprints landed around the target zone or just below it: **Night Swim 11.8m**, **Abigail 10.3m**, **Imaginary 9.9m**.
- Mixed, not disastrous, critical reception is consistent with a non-breakout but still serviceable opening.
- The film has recognizable franchise branding (“The Mummy”), which should keep it from needing exceptional reviews just to get into the low-teens band.

## Counterpoints / strongest disconfirming evidence
The strongest disconfirming consideration is **the Evil Dead Rise comp**: a recent Warner Bros. horror title adjacent to Lee Cronin’s brand that opened to **$24.5m** in a similar theater footprint. If Lee Cronin’s name plus The Mummy IP turns out to drive genre-fan urgency more than the mixed reviews suppress it, the movie can clear **$15m** and make the current bracket too low.

A secondary counterpoint is that **Imaginary at 9.9m** shows that mid-tier horror can also fall just under the band even with a wide release, so the lower miss is also real.

## Resolution or source-of-truth interpretation
**Governing source of truth:** The market resolves using **The Numbers** movie page under the **Weekend Box Office Performance** / 3-day opening weekend figures once they are **final**, not studio estimates.

**Explicit settlement mechanics check:**
- Relevant reporting window is the **3-day domestic opening weekend: April 17–19, 2026**.
- The contract says this typically **includes Thursday previews** if included in The Numbers’ weekend reporting.
- The contract resolves to the **The Numbers** figure even if “domestic” on the source practically includes USA/Canada conventions rather than a stricter USA-only interpretation.
- If The Numbers’ figures are not clearly final, the market remains open until **both The Numbers and Box Office Mojo** confirm finalized figures.
- If the final reported value falls **exactly on a bracket boundary**, the market resolves to the **higher** range.

**Material condition that must hold for YES:** the final The Numbers 3-day weekend figure for April 17–19 must be **at least $10,000,000 and less than or equal to $15,000,000 only if the exact contract bracket defines 15 as included;** since the market wording says “between 10m and 15m” and values exactly between brackets resolve upward, the key practical check is the platform’s bracket architecture at settlement. I am assuming the intended YES bucket is the standard bracket spanning that range, but settlement should still confirm the exact displayed bucket boundaries on the market UI.

**Date / timezone check:** contract closes and resolves on **April 20, 2026 at 08:00 ET**, but the governing box-office observation window is the completed **April 17–19** weekend, with finalization potentially delayed by source confirmation rules.

## Key assumptions
- The 3,200-theater estimate is roughly accurate and the film opens on a normal wide footprint.
- Mixed reviews matter enough to cap breakout odds, but not enough to push the opening clearly below $10m.
- The correct outside-view center is the cluster of recent mid-tier wide horror openings, not the Evil Dead Rise upside case.

## Why this is decision-relevant
At 70%, the market is pricing the bracket as comfortably favored. My base-rate read is narrower: the band is a modest favorite, but the over-$15m tail is too large to ignore given the IP and Cronin/WB horror precedent. That matters for whether this should be treated as a high-confidence yes or merely a lean.

## What would falsify this interpretation / change your mind
- A strong Thursday preview / Friday estimate suggesting demand is tracking more like **Evil Dead Rise** than **Night Swim / Abigail**.
- Trade or source updates showing much stronger audience urgency than the current mixed-review backdrop implies.
- Any settlement clarification showing the market’s bracket boundaries differ from my working interpretation.

## Source-quality assessment
- **Primary source used:** The Numbers, which is also the named settlement source.
- **Most important secondary/contextual source:** Metacritic (with Rotten Tomatoes as supplemental reception context).
- **Evidence independence:** **medium** — The Numbers is independent from the review aggregators, but Rotten Tomatoes and Metacritic both summarize overlapping critic ecosystems.
- **Source-of-truth ambiguity:** **low-to-medium** — low for the named source itself, but medium around the exact “between” bucket boundary behavior unless the market UI bracket definitions are checked alongside the prose rule.

## Verification impact
- **Additional verification pass performed:** yes.
- **What was checked:** named resolution mechanics, date window, The Numbers title page, theater-count context, and a comp set of recent wide horror openings, plus review aggregation context.
- **Material change to estimate/view:** yes, modestly. Early intuition might have accepted the market’s 70% as reasonable, but the comparable set plus the Evil Dead Rise upside case pushed me down to a more cautious **57%**.

## Reusable lesson signals
- Possible durable lesson: for horror opening-weekend bracket markets, a **theater-count + comp-cluster** outside view is often more informative than vivid review narratives alone.
- Possible missing or underbuilt driver: none obvious from this run.
- Possible source-quality lesson: when The Numbers is the governing source, reviewers should still explicitly audit **final-vs-estimate** wording and exact **bracket boundary** mechanics.
- Confidence that lesson is reusable: **medium**.

## Orchestrator review suggestions
- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **yes**.
- One-sentence reason: the case depends on non-canonical but structurally important entities (`lee-cronins-the-mummy`, `warner-bros-pictures`, `atomic-monster`, `blumhouse-productions`, `box-office-mojo`) that were left in proposed linkage fields rather than forced.

## Recommended follow-up
Before final market action, one late-stage verification pass on **Thursday previews / Friday estimate** would be the highest-value update because it would directly test whether this is tracking like the ordinary 10m–12m horror cluster or breaking upward into the over-15m regime.