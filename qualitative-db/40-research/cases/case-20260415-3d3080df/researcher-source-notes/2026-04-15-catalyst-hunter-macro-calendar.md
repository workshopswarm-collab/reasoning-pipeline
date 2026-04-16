---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: macro
subdomain: rates-and-calendar
entity:
topic: macro catalyst calendar before April 20, 2026 noon ET
question: Will Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 20, 2026?
driver:
date_created: 2026-04-14
source_name: Federal Reserve FOMC calendar + BLS CPI release schedule + CME FedWatch overview
source_type: official macro calendar / contextual
source_url: https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [macro, calendar, source-note, catalyst]
---

# Summary

The main scheduled macro catalysts that could plausibly reprice BTC before the April 20 noon ET resolution appear limited after the March CPI release and before the late-April FOMC meeting.

## Key facts extracted

- BLS schedule shows March 2026 CPI was released on April 10, 2026 at 08:30 AM.
- Federal Reserve calendar shows the next scheduled FOMC meeting is April 28-29, 2026, after this market resolves.
- Fed minutes from the March 17-18 meeting were released on April 8, 2026, already before this market window.
- CME FedWatch confirms the next FOMC meeting is upcoming and that the tool tracks meeting-linked rate expectations, but its fetched text did not expose numerical probabilities in this scrape.

## Evidence directly stated by source

- BLS CPI page lists `March 2026 -> Apr. 10, 2026 -> 08:30 AM`.
- Federal Reserve page lists `March 17-18` minutes released `April 08, 2026` and next 2026 meeting `April 28-29`.
- CME FedWatch page states it tracks probabilities of Fed moves for upcoming FOMC meetings.

## What is uncertain

- The scrape did not expose FedWatch percentages, so this note does not quantify rate-cut odds.
- Unscheduled macro shocks, policy headlines, or geopolitical events could still appear before April 20.
- Crypto-specific catalysts can dominate macro calendars in short windows.

## Why this source may matter

For a short-dated BTC threshold market, the catalyst question is less about long-run valuation and more about whether any high-information scheduled event remains that could force a fast repricing before resolution.

## Possible impact on the question

The absence of a scheduled FOMC meeting before April 20 and the fact that CPI already printed on April 10 reduce the odds of a calendar-driven downside shock large enough to push BTC below 70k by the resolving minute. That supports, but does not guarantee, a high Yes probability.

## Reliability notes

- BLS and Federal Reserve calendars are authoritative for the event dates they publish.
- CME FedWatch is a strong contextual source for rate-expectation framing, but the fetched output here was incomplete for exact probabilities.
- These are catalyst-timing sources, not direct settlement sources.