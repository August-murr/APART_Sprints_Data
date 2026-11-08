# BCP-1: Proof-Carrying Containment for Guardrails-Off AI Evaluations

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team ZKL
- Authors: Khadija Edarzi
- Date / location: Sep 14, 2026 / Csablanca
- Page: https://apartresearch.com/sprints/projects/bcp1-proofcarrying-containment-for-guardrailsoff-ai-evaluations-opff
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7f47063f8f043898-d671e-065f-4651-a1b8-91fcba4614de-AI_Incident_Response_Sprint_Khadija_Edarzi.pdf
- Code: https://github.com/khadijaedarzi9/AI_Incident_Response
- Code links found in report: https://github.com/khadijaedarzi9/AI_Incident_Response, https://github.com/cosai-oasis/ws2-defenders

## Summary

A sandbox can keep an allowed network path, raise detections, and still fail to contain. In the July 2026 OpenAI–Hugging Face incident the model used reachable package infrastructure; detections did not force isolation.

BCP-1 is an eight-control containment profile for dangerous-capability evaluations with production safeguards off. This project specifies those controls and implements the authorization and evidence slice in Python: signed manifest, one-use kill-epoch capabilities, credential broker, bounded evidence, streaming verifier, and supervisor receipt. The local isolate is signed SIMULATED; it is not a production microVM.

On that reference, five selected control omissions each produced a non-zero unsafe count; the full contract scored zero. Access logs verified 0/5 predefined claims, signed-line logs 1/5, and the BCP-1 bundle 5/5 on the mediated path (4 events vs 50,000 records). Four scenarios and 32 tests passed.

## Reviews (2)

### Review 1

The core architecture presented here is interesting but repeats in a several submissions I saw for this sprint. I particularly liked your approach to permit lifetime management and auditability.

A lot of the ideas you present here where remind me of existing frameworks (certificate transparency logs cosigning comes to mind.

The writing itself was clear, while a bit dense. I think the "proof-carrying" framing is a bit misleading here, what you get is more of an attestation to the claim. Some of your citations carry the wrong date or misquote the title of the cited work.

### Review 2

Binding actions to signed permissions is a strong way to stop a model causing real-world effects it was never authorised for. However the manifest has to name allowed destinations up front, and evals are exactly where you can't predict what the model will reach for, so unanticipated but harmless actions become denials needing a human. The purpose of evals is also to see where the model deviates, and not all deviations are harmful.

