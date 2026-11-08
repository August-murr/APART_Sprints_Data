# Verified But Wrong

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: None
- Authors: Philip Nilsson
- Date / location: May 24, 2026 / Stockholm
- Page: https://apartresearch.com/sprints/projects/verified-but-wrong-izy3
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/206a6f9c216d1afa-33c07630-9e5d-45ad-af13-e928a0afc2d0-Verified_But_Wrong_Final_Submission.pdf
- Code: https://github.com/Philipnil06/Verified-But-Wrong
- Code links found in report: https://github.com/Philipnil06/Verified-But-Wrong, https://github.com/Beneficial-AI-Foundation/vericoding-benchmark
- More on verified-but-wrong-demo.vercel.app: https://verified-but-wrong-demo.vercel.app/

## Summary

Verified But Wrong studies a target-validity failure mode in vericoding: formally verified code can satisfy a supplied specification while violating the natural-language intent that specification was meant to capture. We audit a public Dafny vericoding benchmark, validate 11 externally sourced demonstrations including 3 direct-Dafny cases, and show in a controlled benchmark that incomplete specs can select wrong implementations. The core recommendation is simple: before using a formal spec as a candidate-selection target, vericoding pipelines should audit whether the spec is actually the right target.

## Reviews (1)

### Review 1

Aligning natural language with formal specifications is a challenging but important task. This work introduces an additional step to identify discrepancies between the natural language instructions and the generated specifications. However, the methodology for detecting these gaps and ensuring the reliability of this check is insufficiently explained. The verification process appears to rely heavily on model-based evaluation; incorporating a simple, deterministic symbolic check would significantly enhance the system's reliability.

