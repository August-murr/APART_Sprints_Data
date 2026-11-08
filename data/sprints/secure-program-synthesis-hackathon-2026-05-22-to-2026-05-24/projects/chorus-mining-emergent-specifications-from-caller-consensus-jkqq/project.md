# Chorus: Mining Emergent Specifications from Caller Consensus

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Spectacular
- Authors: Ojas Marathe
- Date / location: May 25, 2026 / Mumbai
- Page: https://apartresearch.com/sprints/projects/chorus-mining-emergent-specifications-from-caller-consensus-jkqq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6c31a491dab220a8-fa9b20b5-3dbe-4609-910b-328463f8bd46-Chorus_Submission_Report.pdf
- Code: https://github.com/OjasMarathe/chorus
- Code links found in report: https://github.com/OjasMarathe/chorus, https://github.com/atlas-computing-org/formal-speci
- Recording: https://youtu.be/w0p1ushNWXg

## Summary

Chorus is a static analysis framework that recovers a function's true specification from its callers rather than its author. Every call site encodes implicit assumptions — guards, handlers, argument patterns — and Chorus aggregates these across all callers as weak, noisy observers of the same underlying contract. Callers are split into two trust-weighted voices: intent (typed, internal, test callers) and de-facto (external, production callers), whose disagreements surface constraints the ecosystem relies on but the design never documented — a finding type Chorus calls a latent_bug. A narrowly scoped LLM translates the proven constraints into natural language and a draft Lean 4 spec, but never invents one. On a 30-call-site case study of itertools.groupby, Chorus successfully recovers the sorted-input precondition that CPython's own docstring omits entirely.

## Reviews (2)

### Review 1

Separating the code based on who has written is a very interesting approach for finding differences. As mentioned in the limitations, the curated nature of the corpus is worth noting, as generalisability and scaling can be a real hurdle.

### Review 2

The intent-versus-defacto framing is a genuinely creative angle on spec recovery, but the headline 56% versus 40% sorting gap comes from a 30-site corpus you hand-curated to contain that exact split between test/internal and external/script callers, so the result mostly reflects how the corpus was built. Running the pipeline on even a small real sample, such as a few hundred actual groupby call sites from GitHub, would turn the case study into evidence. The confidence interval of 0.38 to 0.73 is also wide enough that it should temper how strongly the gap is stated in the abstract.

