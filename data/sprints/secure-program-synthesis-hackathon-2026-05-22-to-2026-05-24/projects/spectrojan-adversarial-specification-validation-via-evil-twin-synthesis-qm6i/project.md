# SpecTrojan: Adversarial Specification Validation via Evil Twin Synthesis

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Spectacular
- Authors: Ojas Marathe
- Date / location: May 25, 2026 / Mumbai
- Page: https://apartresearch.com/sprints/projects/spectrojan-adversarial-specification-validation-via-evil-twin-synthesis-qm6i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/07c86a7842af8aa3-9c05ec15-2927-43fb-8f3d-469c09d12367-SpecTrojan_Submission_Report.pdf
- Code: https://github.com/OjasMarathe/spectrojan
- Code links found in report: https://github.com/OjasMarathe/spectrojan, https://github.com/atlas-computing-org/formal-specifcationi
- Recording: https://youtu.be/IfiK7asato0
- More on youtu.be: https://youtu.be/dzWM0CX3TfM

## Summary

SpecTrojan is a spec-validation tool that inverts the traditional input-space search: given a candidate specification, an attacker LLM synthesizes an "Evil Twin" — an alternative implementation that satisfies the spec yet diverges from the reference on intent-bearing inputs. A successful twin is an artifact-level proof that the spec is too weak. On a Bio Honeypot (an LLM-written spec for a sequence-screening predicate), SpecTrojan synthesized 16 evil twins in 60 seconds, including a trivial return True that passes verification while admitting every threat-bearing input. The system also includes an attack-to-strengthening loop that auto-proposes and mechanically verifies spec repairs, and metamorphic spec testing that catches syntax-overfit specs.

## Reviews (2)

### Review 1

Evil twins to show naivety is powerful. Would be useful to test fully on a bigger set, and focus more on showing robustness.

### Review 2

The reframe is novel: search the implementation space and synthesize a whole spec-satisfying alternative, so a surviving twin is an artifact-level proof that the specification is too weak. The system is broad and well-built: a twin synthesizer, two baselines, metamorphic testing, and a strengthening loop whose verifier catches every broken LLM repair while a hand-crafted control passes, with an unusually honest robustness section. Caveats. The headline target is a constructed honeypot, and twin counts are stochastic (sixteen one run, zero the next), so foreground the stable binary signal, whether any twin is found, over the counts. A twin only satisfies the spec across eighty Hypothesis samples, so satisfaction is probabilistic. The capability matrix is rhetorically circular, its rows defined as what the method does, so drop the strictly-subsumes claim. And the central comparison figure has a truncated caption with several mangled identifiers, worth a cleanup pass.

