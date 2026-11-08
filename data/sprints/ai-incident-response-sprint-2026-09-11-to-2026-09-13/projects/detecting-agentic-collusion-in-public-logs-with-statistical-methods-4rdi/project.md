# Detecting agentic collusion in public logs with statistical methods

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: None
- Authors: Edimah SYNESIUS SONGO
- Date / location: Sep 14, 2026 / Paris
- Page: https://apartresearch.com/sprints/projects/detecting-agentic-collusion-in-public-logs-with-statistical-methods-4rdi
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7d7b3a255aede834-e739219c-3ed4-4bd8-ae20-e5a2a50f234b-main_final.pdf
- Code: https://github.com/Edimah/agentic-collusion-detector-in-public-logs
- Code links found in report: https://github.com/Edimah/agentic-collusion-detector-in-public-logs, https://github.com/ksouth/collusionwiki

## Summary

Between May and July 2026, a swarm of OpenAI agents used a dormant German wiki as a message board. From two public sources, the investigators' dump of 14,591 agent edits and the wiki's own 23-year edit log, we ask whether the incident can be detected, dated and characterised from the public log alone. We test the incident window against four null models of increasing robustness, from a naive Poisson rate to a difference-in-differences with a placebo-in-time test. The window exceeds all 4,872 reference weeks and the largest rate change falls on 16 June. Volume alone cannot tell a swarm from a human editing burst; timing can: edits peak at 20h UTC against the site's daytime profile. A weekly check built from these features flags the three largest incident weeks, with no false positive over the decade before.

## Reviews (2)

### Review 1

- Related Work section contains incorrect statements "It cannot attribute the activity to a lab or a model."
- It's unclear what data (if any) was used as a held-out test set on which to evaluate the method.
- It would be interesting to analyse the content of the messages, and not just the rate at which they are posted. The time of day is largely uninformative, as humans live across many timezones.
- It's unclear how many weeks worth of data is required for the model to work. Theoretically an agent swarm could collude on a brand-new wiki which has zero weeks of uncontaminated data.
- I stopped reviewing after section 3.7 due to excessive AI-written text.

### Review 2

This is a strong and practically useful project on external incident detection when internal model traces are unavailable. The project’s key contribution is a reproducible public-log workflow that distinguishes a large regime change from ordinary activity using progressively stronger reference models, then characterizes the change through timing and message-level proxies rather than claiming that volume alone proves agentic collusion. The reconciliation of 3,912 surviving live edits with 13,403 reconstructed agent saves is particularly valuable because it shows how moderation and deletion can make public logs a biased survivor record. The analysis reports compelling anomaly evidence for this case, including incident weeks exceeding all 4,872 reference weeks, a difference-in-differences effect of 3.22 log points against Wiki4D with placebo

𝑝=1/523, and a substantial hour-of-day difference with Cramér’s 𝑉=0.44. The main limitation is external validity: one incident on one wiki family cannot establish a general false-alarm rate or attribute future anomalies to agents, and Wiki4D is an available rather than well-matched control. A strong next step would run the detector over many unrelated sites and known benign bursts, preregister feature/threshold choices, and measure precision, recall, alert lead time, and false-alarm burden across incident types.

