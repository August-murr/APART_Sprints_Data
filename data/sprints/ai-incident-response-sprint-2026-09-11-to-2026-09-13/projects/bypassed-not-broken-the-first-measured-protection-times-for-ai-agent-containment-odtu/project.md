# Bypassed, Not Broken: The First Measured Protection Times for AI Agent Containment

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: None
- Authors: Nick Wagner
- Date / location: Sep 14, 2026 / Berlin, Germany
- Page: https://apartresearch.com/sprints/projects/bypassed-not-broken-the-first-measured-protection-times-for-ai-agent-containment-odtu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/be857d38f251528f-53fa3444-c15d-408f-8515-51d047f54269-protection-time.pdf
- Code: https://github.com/Nick-is-building/Apart-Research-Project-AI-Incident-Response-Sprint
- Code links found in report: https://github.com/Nick-is-building/Apart-Research-Project-AI-Incident-Response-, https://github.com/Nick-is-

## Summary

Current AI containment frameworks evaluate security controls as static, binary properties without measuring how long they hold against autonomous agents. Based on timestamped event data from the July 2026 OpenAI–Hugging Face incident, this paper computes the first empirical protection times for AI containment (46 h 50 min for internet egress, 62 h 45 min for inter-agent communication, and 175 h 30 min for administrator access). In all three cases, the controls were bypassed via alternative mechanisms rather than broken. To address this gap, the work proposes an audit clause extending CSA AICM AIS-13 that inventories realization mechanisms per capability and mandates a declared protection-time budget. All data and computations are fully reproducible via a public repository.

## Reviews (2)

### Review 1

This is careful, original work. Attaching a duration to a containment control is a simple idea that no standard I know of has written down, and the report turns it into three concrete numbers and a clause an auditor could use. The distinction between a control that was broken and one whose capability came back through another mechanism is the most useful framing I have seen from this incident.

The contribution matters because it gives the embedded-evaluator proposals something to assess. The case for adoption would be stronger with an argument for why a lab without an embedded evaluator would take on a mechanism inventory, and with even a rough cost for maintaining one. The protection-time benchmark in Future Work is what would give the declared budget an empirical basis.

To check the results I downloaded OpenAI's technical report from reference [7] and found all seven timestamps you use, with matching dates. I recomputed the protection times and the cadence factors by hand, read compute_p.py, clock.csv and the claims checker, and went through the commit history; the committed run log shows every reference value and claim reproducing. I did not run verify.sh myself. Two points deserve a sentence in the paper. For egress, the source does not name the route used at 00:06 on 8 July, so "bypassed" rests on the HTTP 400 responses eleven hours after the rebuild; clock.csv says as much, and the paper should too. OpenAI does not state the inter-agent protection goal; it is your own assumption, and since protection time is measured against the goal, 4.1 should flag it. The evidence base and its correction history are in German, which puts them out of reach for most reviewers; an English summary of the nineteen corrections would help.

The report is well structured and every claim is traceable, which is rare. It is also dense: terms like standing, applied, P_wall and K1 need a short definition at first use. Section 4.4 follows directly from the nesting, and the awareness clock in Figure 2 answers a disclosure question, which is separate from containment, so both could move to an appendix to give the core finding more room.

If you take this further, run the protection-time benchmark: apply a control at a known moment against a fixed agent configuration and measure how long it holds across control classes.

### Review 2

Overall, good instinct on direction in terms of determining how much time a control may buy defenders.

This submission starts to get at a bigger question that would be a stronger contribution: how do different models with varying level of sophistication in scaffolding (i.e. none, basic, expert) perform in similar environments (same controls or varying levels of controls), and is there a "containment-time" that we can empirically assign to different environments/scenarios with specific controls? Maybe certain generation models, more than 50% of the time, take longer than X amount of time to circumvent a specific control. Therefore, Y control buys defenders X amount of time. Without this data, we cannot transfer the "protection-time" in this incident to others/future incidents. Additionally, adding a new element to existing frameworks as proposed would have a stronger value-add with more data.

