---
type: agent_finding
case_key: case-20260416-f08c3dae
dispatch_id: dispatch-case-20260416-f08c3dae-20260416T041907Z
research_run_id: d219ca28-e451-470c-9edb-847efbda0b11
analysis_date: 2026-04-16
persona: risk-manager
domain: sports
subdomain: colombia-primera-a
entity:
topic: "CD Tolima vs Deportivo Pereira"
question: "Will CD Tolima win on 2026-04-18?"
driver:
date_created: 2026-04-16
agent: orchestrator
stance: yes-leaning
certainty: medium
importance: medium
novelty: low
time_horizon: match-day
related_entities: ["colombia"]
related_drivers: []
proposed_entities: ["deportes-tolima", "deportivo-pereira"]
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-source-notes/2026-04-16-risk-manager-espn-polymarket-context.md", "qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/assumptions/risk-manager.md"]
downstream_uses: []
tags: ["risk-manager", "soccer", "polymarket", "colombia-primera-a", "regulation-win"]
---

# Claim

CD Tolima is the right side, but the main risk-manager objection is that a 0.76 market price may be embedding slightly more confidence than the evidence quality justifies for a 90-minute soccer win market where draw risk remains live. My estimate is **0.72** for a Tolima win in regulation.

## Market-implied baseline

Polymarket current price is **0.76**, implying roughly **76%** for Yes.

Compliance on evidence floor: met with at least two meaningful sources.
- Primary / contract source: Polymarket market page and resolution wording.
- Strong contextual independent source: ESPN COL.1 scoreboard and team schedule APIs for fixture identity, records, form, venue, and bookmaker context.

## Own probability estimate

**72%**.

## Agreement or disagreement with market

I **roughly agree on direction but slightly disagree on confidence**. Tolima deserves favorite status: home venue, 7-6-3 overall record, Pereira still winless at 0-7-9, and ESPN-embedded DraftKings prices around Tolima -370 / Pereira +800 also point the same way. But this is still a regulation-only win market, not draw-no-bet, and soccer favorites often fail by drawing rather than losing outright. The market's 0.76 is plausible, but I would shade a bit lower because the available evidence is mostly team-level form/record context rather than richer squad-specific confirmation.

## Implication for the question

The directional view remains Yes-leaning. The risk is not mainly a Pereira upset; it is that the market may be compressing draw/timing variance too aggressively for a single 90-minute match.

## Key sources used

- **Primary / governing-contract source:** Polymarket market page for contract wording and settlement logic: Tolima must win; only first 90 minutes plus stoppage time count; primary resolution source is official match statistics recognized by governing body or event organizers, with credible-reporting fallback only if official final statistics are unavailable within 2 hours.
- **Secondary contextual source:** ESPN COL.1 scoreboard for 2026-04-18 fixture `401850871`, listing Deportivo Pereira at Deportes Tolima, venue Estadio Manuel Murillo Toro, current team records, recent form strings, and sportsbook prices.
- **Secondary contextual source:** ESPN team schedule endpoints for recent match results for both teams.
- Case source note: `qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-source-notes/2026-04-16-risk-manager-espn-polymarket-context.md`
- Assumption note: `qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/assumptions/risk-manager.md`

Direct vs contextual evidence:
- **Direct for contract/resolution:** Polymarket wording.
- **Direct for fixture identity and current records/form:** ESPN fixture and team schedule data.
- **Contextual rather than governing:** ESPN-embedded sportsbook prices.

## Supporting evidence

- Tolima is home at **Estadio Manuel Murillo Toro**.
- ESPN lists Tolima record **7-6-3** versus Pereira **0-7-9**.
- Tolima's recent home results are materially stronger than Pereira's recent run, including home wins over Águilas Doradas (4-1), Jaguares (3-1), Fortaleza CEIF (2-0), and Atlético Nacional (1-0).
- Pereira's recent sample is weak and winless, with losses to Alianza FC, Boyacá Chicó, Deportivo Cali, and Águilas Doradas.
- Independent bookmaker context is also strongly pro-Tolima: DraftKings moneyline around **-370** home / **+800** away, plus Tolima -1.5 priced at -125.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **draw risk**. Pereira has multiple recent draws, and this contract requires an outright Tolima win within regulation. The market's bullish case rests on team-strength asymmetry, but a favorite can still fail this contract via a 0-0 or 1-1 type result even if it is clearly the better side.

## Resolution or source-of-truth interpretation

Primary governing source of truth: **official match statistics recognized by the governing body or event organizers**, per Polymarket's own market wording.

Practical interpretation:
- If official league / organizer final match statistics are available on time, they govern.
- If those official stats are not published within 2 hours after the event, Polymarket allows a fallback to a consensus of credible reporting.
- Because this is a soccer winner market, what matters is the official final score **after 90 minutes plus stoppage time only**.
- Extra time, penalties, or broader competition advancement do **not** count unless reflected inside normal time score, which Polymarket wording does not suggest.

Verification-state separation:
- **Not yet verified** would mean the match may have concluded but final official statistics have not yet been checked or published on the governing surface.
- **Not yet occurred** would mean the match has not yet been played or completed.
- At current run time, the event is **not yet occurred**, not merely unverified.

## Key assumptions

- Tolima's stronger home/overall profile is more predictive than generic draw variance.
- No major late injury, rotation, or discipline news materially weakens Tolima before kickoff.
- ESPN records/form and embedded book prices are not materially stale or distorted.

## Why this is decision-relevant

The main decision question is not which team is better in abstract terms; it is whether the market is overpaying for apparent superiority in a regulation-win contract. Risk-wise, the Yes case is good, but the hidden assumption is that superiority cleanly converts into a win rather than a draw. That assumption is usually where favorites disappoint in soccer markets.

## What would falsify this interpretation / change your mind

The fastest ways to invalidate or revise this view would be:
- credible pre-match lineup/injury news showing Tolima missing key attacking or creative players;
- a sharp pre-match odds drift away from Tolima across books;
- official reporting indicating unusual conditions that increase draw/variance risk;
- stronger direct evidence that Pereira's current underlying level is better than its winless record suggests.

If those appear, I would revise lower toward the market only if they are minor, or materially below market if they are substantial.

## Source-quality assessment

- **Primary source used:** Polymarket market page and resolution wording.
- **Most important secondary/contextual source:** ESPN COL.1 scoreboard and team schedule APIs.
- **Evidence independence:** **medium**. Polymarket contract wording and ESPN contextual data are distinct, but the football-performance view still leans on one main contextual data family rather than several truly independent scouting/reporting sources.
- **Source-of-truth ambiguity:** **low to medium**. Contract wording is fairly clear, but the exact governing body surface is described generically rather than naming a specific league page. That is manageable, not severe.

## Verification impact

- **Additional verification pass performed:** yes.
- **Materially changed estimate or mechanism view:** no material change.
- The extra pass mostly strengthened confidence in fixture identity, venue, record asymmetry, and bookmaker alignment; it did not remove the core draw-risk objection.

## Reusable lesson signals

- Possible durable lesson: for straightforward soccer moneyline markets, record asymmetry plus independent book confirmation can be enough for a directional view, but risk review should explicitly isolate draw risk from upset risk.
- Possible missing or underbuilt driver: none confidently identified from this single case.
- Possible source-quality lesson: generic governing-source wording should be quoted explicitly even in low-difficulty sports markets so later reviewers can see what would settle the contract.
- Confidence that any lesson here is reusable: **low**.

## Orchestrator review suggestions

- Review later for durable lesson: **no**.
- Review later for driver candidate: **no**.
- Review later for canon or linkage issue: **no**.
- Reason: this looks like an ordinary low-difficulty sports favorite case; no strong stable-layer gap emerged beyond routine provenance hygiene.

## Recommended follow-up

No follow-up suggested unless material lineup/injury news appears before kickoff or the market price moves sharply away from the current 0.76 baseline.