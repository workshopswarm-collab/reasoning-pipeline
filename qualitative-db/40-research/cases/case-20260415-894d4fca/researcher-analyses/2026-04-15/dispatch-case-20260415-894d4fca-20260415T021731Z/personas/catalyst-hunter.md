---
type: agent_finding
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
research_run_id: 808d1adb-6d17-4c03-8675-f6e2c3ed253e
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: politics
subdomain: surveillance-policy
entity: united-states
topic: fisa-section-702-reauthorized-before-it-expires
question: "FISA Section 702 reauthorized before it expires?"
driver:
date_created: 2026-04-15
agent: Orchestrator
stance: lean-yes
certainty: medium
importance: high
novelty: medium
time_horizon: days
related_entities: ["united-states"]
related_drivers: []
proposed_entities: ["congress-gov-house-bill-22", "house-permanent-select-committee-on-intelligence", "senate-judiciary-committee", "president-of-the-united-states"]
proposed_drivers: ["legislative-timing-risk", "bicameral-coordination-risk", "surveillance-reform-coalition-risk"]
upstream_inputs: []
downstream_uses: ["orchestrator-synthesis", "forecast-update"]
tags: ["fisa", "section-702", "congress", "catalyst-hunter", "deadline-sensitive"]
---

# Claim

My directional view is **lean Yes**: Section 702 is slightly more likely than not to be reauthorized before expiry, but the path is narrow and heavily dependent on a late leadership-driven extension vehicle rather than a fully negotiated reform package.

**Checklist compliance / evidence floor:** met for a medium-difficulty, rule-sensitive case using at least two meaningful sources: (1) official congressional statement with direct timing relevance, (2) high-quality contextual policy analysis, plus (3) advocacy/context material for opposition and source-quality triangulation.

## Market-implied baseline

Current price is **0.785**, implying about **78.5%**.

## Own probability estimate

**62%**.

## Agreement or disagreement with market

I **disagree modestly** with the market. The market is directionally plausible because Congress usually tries not to let core national-security authorities lapse, and there is an explicit push for an extension. But 78.5% feels too high for a contract that requires all of the following to happen in time: passage by both chambers, presidential enactment or equivalent lawful enactment, and completion before the market deadline. This is a timing-and-coordination case, not just a sentiment case.

## Implication for the question

The most likely path to Yes is a **late clean or near-clean extension** pushed by leadership under deadline pressure. The most plausible repricing path before resolution is:
- upward repricing if a real vehicle/floor schedule appears or Senate support becomes explicit
- downward repricing if the deadline approaches without a clear vehicle, or if reform fights harden into procedural delay

The single most important catalyst is **visible movement toward an enactable legislative vehicle**. Soft commentary about 702’s importance matters less than actual schedule/control evidence.

## Key sources used

**Primary / authoritative settlement source**
- Congress.gov legislation tracker for the named primary source in the market rules: https://www.congress.gov/bill/119th-congress/house-bill/22
- Contract/source-of-truth logic from the market description: Yes requires legislation reauthorizing FISA Title VII including Section 702 to pass both chambers and be signed into law by **April 19, 2026, 11:59 PM ET**; official U.S. government sources are primary, with credible reporting as fallback.

**Primary direct evidence used in this run**
- House Intelligence Committee Chairman Rick Crawford opening statement, March 19, 2026: official statement that 702 expires in just over a month, the President is seeking an **18-month clean extension**, and Crawford is working with House leadership, the ranking member, and Judiciary Chairman Jordan to support it.
- Source note: `qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-source-notes/2026-04-15-catalyst-hunter-house-intel-chair-crawford-702-extension.md`

**Key secondary/contextual source**
- Brookings, February 10, 2026: Section 702 sunset is **April 20, 2026** and the reauthorization path is politically unclear due to unresolved reform/privacy fights.
- Source note: `qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-source-notes/2026-04-15-catalyst-hunter-brookings-702-path-unclear.md`

**Additional contextual/opposition source**
- Brennan Center 2026 resource page showing organized reform opposition and active 2026 reauthorization campaign infrastructure.

Direct vs contextual distinction:
- Crawford is the strongest **direct** evidence of an actual near-term catalyst path.
- Brookings and Brennan are mainly **contextual** evidence about friction, coalition risk, and why deadline failure is plausible.

## Supporting evidence

- The strongest live pro-Yes evidence is the **official March 19 statement** from the House Intelligence chair that the President wants an 18-month clean extension and that coordination with leadership and Judiciary was underway. That is unusually concrete catalyst language for a pre-deadline market.
- Congress has a structural incentive not to allow a core intelligence authority to lapse outright, especially when leadership can use time pressure to force a simpler extension route.
- The market rules themselves explicitly recognize official U.S. government legislative tracking as the source of truth, which means real late-stage legislative movement can quickly settle uncertainty.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not** that 702 lacks elite support; it is that the contract is narrow and deadline-sensitive while the coalition is still contested. Brookings explicitly describes the path as unclear and politically difficult, and civil-liberties/reform groups remain organized against a clean extension. If the coalition requires a more complicated bargain than leadership can move in days, this resolves No even if eventual reauthorization remains likely later.

## Resolution or source-of-truth interpretation

**Governing source of truth:** Congress.gov / Library of Congress and other official U.S. government information are the primary resolution sources named by the contract; consensus credible reporting is only fallback.

**Material conditions for Yes**
1. Legislation must reauthorize FISA Title VII including Section 702.
2. It must pass **both** the House and Senate.
3. It must be signed into law, become law without signature while Congress remains in session, or become law through veto override.
4. This must occur by **April 19, 2026, 11:59 PM ET** under the market rules.
5. A pocket veto that expires would resolve No.

**Date/timing check**
- Contextual sources cite the statutory sunset as **April 20, 2026**.
- The market deadline is effectively the end of **April 19, 2026 ET**, so even small process slippage matters.

**Source-of-truth ambiguity assessment**
- Low-to-medium ambiguity. The contract is fairly explicit on outcome mechanics, but ambiguity remains around which exact bill vehicle qualifies if Congress uses something other than the named tracker path. That is manageable because official enacted-law records would still control.

## Key assumptions

- If Congress acts in time, it is more likely via a **clean or near-clean extension vehicle** than via reopening the full reform fight.
- Leadership can still impose enough deadline discipline to move a bicameral vehicle quickly.
- No new scandal, compliance failure, or procedural blockade emerges in the final window.

## Why this is decision-relevant

This case is mostly about **catalyst timing**, not abstract policy merit. A trader or synthesizer should watch for:
- emergence of an actual bill vehicle
- House and Senate floor scheduling
- public alignment from Senate leadership or key committees
- signs that reform demands are becoming blocking conditions

Those signals should matter more than generalized op-eds about whether 702 is valuable.

## What would falsify this interpretation / change your mind

I would move lower quickly if:
- no viable vehicle or floor path appears as the deadline nears
- key Senate or House actors publicly oppose a clean/near-clean extension strongly enough to block timing
- official reporting shows the coalition now requires a complex reform bargain rather than a time-limited extension

I would move higher if:
- Congress.gov shows active movement on a qualifying vehicle
- leadership publicly commits to floor action
- bicameral support for an extension becomes explicit

## Source-quality assessment

- **Primary source used:** official House Intelligence Committee statement by Chairman Crawford.
- **Most important secondary/contextual source:** Brookings February 2026 analysis.
- **Evidence independence:** medium. The sources are not copies of each other, but they observe the same Washington process and are not fully independent in underlying facts.
- **Source-of-truth ambiguity:** low-to-medium. Official legislative records should dominate, but the precise qualifying vehicle may not be the named bill if Congress uses another legislative path.

## Verification impact

- **Additional verification pass performed:** yes.
- I explicitly checked for authoritative/source-of-truth mechanics and an additional official signal after seeing the market was already at 78.5%.
- **Material impact on view:** yes, but modest. The official Crawford statement kept me above 50%; without it, I would have been meaningfully more skeptical because contextual sources alone point to a messy path.
- I was unable to directly fetch Congress.gov bill-status text due access friction in this environment, which lowers confidence somewhat but does not alter the core mechanism view because the official settlement logic and deadline mechanics were still verified from the contract and corroborating contextual sources.

## Reusable lesson signals

- Possible durable lesson: in deadline-sensitive congressional markets, **leadership vehicle visibility** is often a better catalyst than broad elite support. 
- Possible missing or underbuilt driver: **legislative timing risk / bicameral coordination risk** seems structurally important and not cleanly mapped here.
- Possible source-quality lesson: official committee statements can materially improve late-stage timing analysis even when full bill-tracker access is impaired.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **yes**
- one-sentence reason: this case repeatedly points to missing reusable driver concepts around legislative timing/coordinated passage under deadline, and several causally central institutions lacked a confirmed canonical slug in this run.

## Recommended follow-up

- Immediate follow-up should be narrowly focused on **Congress.gov bill movement, vehicle identity, and bicameral floor schedule**.
- If no new official movement appears soon, this view should drift downward because the market deadline is unforgiving.