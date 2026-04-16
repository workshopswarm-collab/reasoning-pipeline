---
type: agent_finding
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: 0c338125-dc6d-434f-85e5-b84e0ad3c09d
analysis_date: 2026-04-16
persona: base-rate
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: seoul-apr-17-high-temperature-threshold
question: "Will the highest temperature in Seoul be 18°C or higher on April 17?"
driver:
date_created: 2026-04-16
agent: Orchestrator
stance: modest-yes-lean
certainty: medium
importance: medium
novelty: low
time_horizon: "1 day"
related_entities: []
related_drivers: []
proposed_entities: ["incheon-intl-airport-station-rksi"]
proposed_drivers: ["station-location-basis-risk"]
upstream_inputs: []
downstream_uses: []
tags: ["agent-finding", "weather", "temperature-threshold", "polymarket", "base-rate"]
---

# Claim

Base-rate view: **slight Yes lean, but weaker than the market implies**. My estimate is that the highest temperature at the governing station, Incheon Intl Airport Station (RKSI), reaches **18°C or higher with probability 0.58**.

Compliance note: evidence floor met with at least two meaningful sources — **(1) the governing-source contract surface/Wunderground RKSI history page** and **(2) independent contextual forecast pages from Timeanddate and Weather.com**. I also performed an extra verification pass because the market was above 0.70 and the case is date- and source-sensitive.

## Market-implied baseline

Current market price is **0.71**, implying about **71%** for Yes.

## Own probability estimate

**58%** for Yes.

## Agreement or disagreement with market

**Moderate disagreement.** I agree that Yes is more likely than No, because multiple city-level forecasts for the relevant day are above 18°C. But I think the market is too confident because the contract does **not** settle on downtown Seoul; it settles on **Incheon Intl Airport Station**, which is a cooler and more coastal airport location. That station/title mismatch is exactly the kind of basis risk an outside-view researcher should discount for.

## Implication for the question

The question is not “will Seoul feel warm?” but “will the highest temperature recorded at RKSI round/print at 18°C or above once Wunderground finalizes Apr 17 data?” On that narrower framing, Yes still has the edge, but not by enough to justify a 71% confidence level from the evidence I found.

## Key sources used

- **Primary / authoritative settlement source:** Polymarket contract description naming **Wunderground daily history for RKSI** as the resolution source: <https://www.wunderground.com/history/daily/kr/incheon/RKSI>
- **Primary source note:** `qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-base-rate-weather-sources.md`
- **Secondary contextual source (city forecast):** Timeanddate Seoul extended forecast, showing **Apr 17 high 22°C**.
- **Secondary contextual source (city forecast):** Weather.com Seoul 10-day forecast, showing **Apr 17 high around 20°C**.
- **Secondary contextual source (airport-area forecast):** Weather.com Incheon airport monthly page, showing **Apr 17 high 60°F (~16°C)**.

Direct vs contextual evidence:
- **Direct / settlement-relevant:** Wunderground RKSI page establishes the exact governing source and station.
- **Contextual / forecast evidence:** Timeanddate and Weather.com forecasts inform likely temperature but do not settle the market.

## Supporting evidence

- Two Seoul-area forecast surfaces were comfortably above the threshold: **22°C** at Timeanddate and **20°C** at Weather.com.
- Mid-April in northwest Korea is often warm enough that an 18°C threshold is not extreme; structurally, this is a plausible spring high rather than a rare outlier.
- The threshold is only 18°C and the market is about the **daily high**, so modest daytime warming is enough.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming evidence is the **station-basis mismatch** plus the airport-area forecast excerpt: Weather.com's Incheon-airport page showed **Apr 17 near 60°F (~16°C)**, below threshold. That does not prove No, but it is the clearest evidence that the market may be over-reading Seoul-city warmth for a contract that actually resolves at a cooler airport station.

## Resolution or source-of-truth interpretation

Governing source of truth: **Wunderground daily history page for RKSI (Incheon Intl Airport Station)**.

Relevant timing and verification details:
- The market resolves for **all times on 17 Apr 2026** at the station, using **whole degrees Celsius**.
- The contract says the market **cannot resolve Yes until all data for that date has been finalized** on the Wunderground page.
- On **2026-04-16**, the Wunderground RKSI page still showed **"No data recorded"** for the current surface excerpt. This is important proof of state: the event was **not yet verified**, not “verified false,” and also not yet occurred/finalized for Apr 17.
- The market title says Seoul, but the contract language explicitly maps settlement to **Incheon Intl Airport Station**. That mapping dominates.

Explicit governing-source proof when near-complete: not available yet, because Apr 17 had not finalized on the governing page at research time.

## Key assumptions

- The airport station is somewhat cooler than Seoul proper, so city forecasts should be discounted rather than copied directly into the contract probability.
- The available city-level forecasts still carry enough signal that Yes remains the modal outcome.
- No unusual marine/cloud regime shift knocks the airport high materially lower before the day resolves.

## Why this is decision-relevant

The key trading question is whether the contract wording creates basis risk large enough to fade a warm-looking headline forecast. My answer is yes: enough to move from 71% down to 58%, but not enough to flip to No.

## What would falsify this interpretation / change your mind

- A more direct RKSI-specific forecast moving clearly above 18°C would raise me toward the market.
- Repeated airport-specific forecasts below 17°C would move me toward No.
- Any late update on the governing Wunderground station page showing intraday observations close to or above threshold would materially increase confidence in Yes.

## Source-quality assessment

- **Primary source used:** Wunderground RKSI history page named in the contract; source quality for settlement mechanics is **high**.
- **Most important secondary/contextual source:** Timeanddate Seoul extended forecast; useful but not station-perfect.
- **Evidence independence:** **Medium-low**. Consumer weather sites may rely on overlapping numerical weather models, though station/location framing differs enough to add some value.
- **Source-of-truth ambiguity:** **Low** on formal settlement source, **medium** on intuitive geographic labeling because the title says Seoul while settlement is at Incheon airport.

## Verification impact

- **Additional verification pass performed:** yes.
- **Did it materially change the view?** Yes, somewhat.
- The extra pass surfaced a meaningful airport-area forecast below threshold and reinforced that the governing station is not central Seoul, which pushed me from a likely market-like view toward a more cautious **58%**.

## Reusable lesson signals

- Possible durable lesson: title-to-station basis mismatch can matter even in simple weather markets.
- Possible missing or underbuilt driver: **station-location-basis-risk** may deserve future review if this pattern recurs.
- Possible source-quality lesson: for source-sensitive weather thresholds, preserve an explicit snapshot of the governing source even when it is only proving “not yet verified.”
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- Review later for durable lesson: **yes**.
- Review later for driver candidate: **yes**.
- Review later for canon or linkage issue: **no**.
- Reason: simple weather threshold markets can still hide material basis risk when the title geography differs from the settlement station.

## Recommended follow-up

If more precision is needed before close, run one late check focused specifically on **RKSI / Incheon airport** rather than Seoul-city forecasts. Right now the cleanest outside-view read is: **Yes favored, but not by as much as the market says.**
