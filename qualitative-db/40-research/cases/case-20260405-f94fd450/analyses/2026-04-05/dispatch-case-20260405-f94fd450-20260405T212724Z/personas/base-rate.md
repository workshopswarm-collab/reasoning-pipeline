---
type: agent_finding
case_key: case-20260405-f94fd450
dispatch_id: dispatch-case-20260405-f94fd450-20260405T212724Z
research_run_id: 60b08e4e-34dc-4e1c-8bb2-180411cf9154
analysis_date: 2026-04-05
persona: base-rate
domain: geopolitics
subdomain: conflict-resolution
entity: Iran-UAE
topic: case-20260405-f94fd450 | base-rate
question: Will Iran strike UAE again in March?
driver: base-rate override by direct qualifying-event evidence
date_created: 2026-04-05
agent: Orchestrator
stance: yes
certainty: medium-high
importance: high
novelty: medium
time_horizon: March 2026 settlement window
related_entities: [Iran, UAE, Fujairah, Dubai airport]
related_drivers: [resolution mechanics, attribution threshold, timing window, state-on-state escalation]
upstream_inputs: []
downstream_uses: [controller synthesis, settlement audit]
tags: [base-rate, geopolitics, high-difficulty, resolution-sensitive, yes-lean]
---

# Claim

My base-rate view is that this should resolve **Yes**. State-on-state Iranian strikes on UAE soil are rare in outside-view terms, but the case is no longer mainly about prior frequency: credible March reporting indicates actual Iranian drone impacts on UAE territory/infrastructure, and additional reporting ties the attack campaign directly to launches from Iran. That combination clears the contract more likely than not, and in my view by a wide margin.

## Market-implied baseline

Current price 0.7795 implies **77.95%**.

## Own probability estimate

**96%** that the correct settlement is **Yes**.

## Agreement or disagreement with market

I **disagree modestly with the market to the upside**. The outside-view starting point would normally be below a high-70s price because direct Iranian military impacts on UAE soil are uncommon and many wartime headlines describe interceptions that would not qualify. But once I audit the contract and the March reporting, the remaining uncertainty looks mostly settlement-friction/audit ambiguity rather than event uncertainty. The market seems somewhat too conservative given the evidence of actual impacts.

## Implication for the question

For this question, what matters is not generic regional escalation risk but whether at least one March incident satisfies all contract conditions. The evidence indicates yes: a qualifying impact on UAE territory during March, attributed to Iran rather than proxies, and reported credibly enough that consensus-based settlement should be achievable.

## Key sources used

1. **Primary / authoritative for mechanics:** Polymarket market rules page and resolution wording  
   - See `source-notes/2026-04-05-base-rate-polymarket-rules.md`  
   - Direct for source-of-truth mechanics; not direct for event occurrence.
2. **Primary factual source for qualifying impact:** BBC, “Iran hits key UAE oil port and Dubai airport” (16 Mar 2026)  
   - See `source-notes/2026-04-05-base-rate-bbc-uae-impacts.md`  
   - Direct on impact reporting to UAE territory/infrastructure.
3. **Key secondary/contextual attribution set:** Khaleej Times (21 Mar) and The National (31 Mar), both citing UAE Defence Ministry reporting on missiles/drones coming/launched from Iran  
   - See `source-notes/2026-04-05-base-rate-uae-reporting-march-series.md`  
   - Direct on attribution/origin and repeated March attacks; mixed on qualifying impact.
4. **Audit artifact:** `analyses/2026-04-05/dispatch-case-20260405-f94fd450-20260405T212724Z/evidence/base-rate.md`

### Evidence-floor compliance

- **Evidence floor required:** at least three meaningful sources for a high-complexity geopolitics / rule-sensitive case.
- **Used:** three meaningful source groups plus an explicit evidence map.
- **Extra verification performed:** yes; I did an additional pass focused on date window, attribution/origin, and what counts versus interceptions.
- **Disconfirming-source requirement:** met via explicit review of the contract exclusion that interceptions do not count and by noting ambiguity in some outlet wording.

## Supporting evidence

- The market rules say one qualifying Iranian drone/missile/air strike impacting UAE ground territory in the March ET window is sufficient; interceptions alone do not count.
- BBC reports actual drone impacts: a drone attack on Fujairah port/industrial zone causing fire, another drone hitting oil facilities, and a drone-related incident near Dubai airport on 16 March. Those are impacts on UAE territory/infrastructure, not merely interceptions.
- UAE-focused reporting later in March explicitly says the barrages were “coming from Iran” / “launched from Iran,” which is important because the contract excludes proxy attacks and requires explicit Iranian attribution or origin from Iranian territory.
- Reporting spans mid-March through March 31, making the timing window straightforwardly within March and well before the contract’s reporting deadline concern would bite.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is contractual, not geopolitical: **a large share of March reporting describes interceptions**, and if the settlement team concluded that all clearly corroborated incidents were interceptions or that actual impacts were not sufficiently confirmed as Iran-origin, the market could still resolve No. Put differently, the main threat to the yes view is not lack of attempted attacks; it is failure of consensus reporting on a qualifying impact under the narrow wording.

## Resolution or source-of-truth interpretation

**Governing source of truth:** the contract says resolution is by **consensus of credible reporting**.

### What counts

- A drone, missile, or air strike by Iranian military forces that **impacts UAE ground territory** or an official UAE embassy/consulate.
- The event must occur within the March 31, 2026 **11:59 PM ET** window.
- Attribution must be either explicitly claimed by Iran or confirmed to have originated from Iranian territory.

### What does not count

- Intercepted missiles or drones, even if debris falls or there is incidental damage.
- Proxy-force attacks.
- Non-qualifying attack types like artillery, cyber, ground incursions, or naval shelling.

### How the wording affects the view

This wording forces a narrower audit than “did Iran attack the UAE?” Many headlines alone would be insufficient because they discuss interceptions. My yes view depends specifically on the BBC-reported impacts at Fujairah / near Dubai airport, combined with separate attribution reporting tying the March campaign to Iran-origin launches.

### Date / timing / reporting-window verification

- Market window runs through **March 31, 2026 11:59 PM ET**.
- The key impact reporting I relied on is dated **16 March 2026**, comfortably inside the window.
- Additional attribution / repeated-attack reporting is dated **21 March 2026** and **31 March 2026**, also inside the window.
- Because these reports were already published well before April 3, 2026, the “confirmed by end of third calendar date after market end date” clause does not appear to block a yes outcome.

### Attribution / origin verification

I explicitly checked attribution rather than assuming it. BBC frames the incidents as part of Iran continuing to target UAE infrastructure, while Khaleej Times and The National more explicitly say missiles/drones were coming from / launched from Iran. That cross-check materially strengthens compliance with the contract’s anti-proxy requirement.

### Material conditions that all must hold for Yes

1. At least one March incident involved a qualifying drone/missile/air strike.  
2. The strike **impacted** UAE territory or an official UAE diplomatic site.  
3. The strike was by Iranian military forces, or at minimum confirmed to have originated from Iranian territory.  
4. Consensus credible reporting established the timing and nature of the event by the deadline.  

My view is that these conditions are met.

## Key assumptions

- BBC’s reporting of impacts at Fujairah / near Dubai airport is robust enough to be part of a consensus-of-credible-reporting bundle, not a lone outlier.
- Settlement reviewers will treat strikes on UAE infrastructure and facilities as clearly “UAE ground territory,” which I think is the natural reading.

## Why this is decision-relevant

This is exactly the kind of case where a base-rate prior initially resists a sensational claim, but once direct qualifying evidence appears the prior should be overridden decisively. The useful decision lesson is that narrow-rule, conflict markets should be priced off audited qualifying incidents, not raw launch counts or general escalation narrative.

## What would falsify this interpretation / change your mind

I would materially reduce confidence if any of the following appeared:

- a strong Reuters/AP/official clarification saying the March UAE incidents were all intercepted and no Iranian munition actually impacted UAE territory;
- credible reporting showing the Fujairah / Dubai incidents were not confirmed to originate from Iran proper;
- settlement guidance indicating the cited impact events failed consensus timing/attribution standards.

## Source-quality assessment

- **Primary source used:** Polymarket rules page for the governing resolution mechanics.
- **Most important secondary/contextual source:** BBC for the strongest accessible report of actual impacts on UAE territory.
- **Evidence independence:** **medium**. BBC is meaningfully independent from UAE local reporting, but Khaleej Times and The National both lean on UAE official/Defence Ministry claims.
- **Source-of-truth ambiguity:** **medium**. The contract’s “consensus of credible reporting” standard is usable but not perfectly mechanical, so attribution and impact wording still matter.

## Verification impact

- **Additional verification pass performed:** yes.
- **What I verified:** exact contract exclusions, ET date window, attribution/origin requirement, and whether I had evidence of actual impact rather than only interceptions.
- **Did it materially change the view?** yes. My initial outside-view would have been materially lower because the event is rare and many reported barrages were intercepted. The additional pass raised confidence sharply by finding direct impact reporting and separate Iran-origin confirmation.

## Reusable lesson signals

- **Possible durable lesson:** in exclusion-heavy conflict markets, raw barrage counts can be misleading; settlement often hinges on one clearly documented qualifying impact.
- **Possible missing or underbuilt driver:** none confidently identified from this single case.
- **Possible source-quality lesson:** consensus-of-reporting markets benefit from pairing one strong independent outlet with one attribution-focused local/official-source chain.
- **Reusability confidence:** medium.

## Orchestrator review suggestions

- **Review later for durable lesson:** no
- **Review later for driver candidate:** no
- **Review later for canon or linkage issue:** no
- **Reason:** useful lesson here is mostly methodological and already familiar; nothing yet looks like a new durable canon change from this single run.

## Recommended follow-up

No major follow-up suggested unless a controller wants one more settlement-audit pass using a wire-service or direct UAE official release archive. On current evidence, the directional call is already strong enough to finish decisively.
