# Ghost Marks in the Machine: A Critical Review of SynthID for Code Provenance Monitoring

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Durham AI Safety Initiative
- Authors: Eve Sherratt-Cross, Theo Farrell, Sam Ogden, Oscar Ryley
- Date / location: Nov 23, 2025 / Durham, UK
- Page: https://apartresearch.com/sprints/projects/ghost-marks-in-the-machine-a-critical-review-of-synthid-for-code-provenance-monitoring-ov2c
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/27edc04e3d6e5f2c--in-the-Machine_-A-Critical-Review-of-SynthID-for-Code-Provenance-Monitoring.pdf
- Code: None
- Code links found in report: https://github.com/DurhamAISafety/ghost-marks-in-the-machine, https://github.com/google-deepmind/synthid-text

## Summary

AI-generated code is increasingly common in software and prone to security vulnerabilities. It is hence critical to monitor the origins of code used in secure applications. SynthID is a Google DeepMind method for watermarking AI-generated text, images and videos but there is currently no existing mechanism for code. We adapt various SynthID schemes to Python code, and analyse how effective they are using Bayesian detectors. We find that longer n-grams support more robust watermark detection, but the corresponding generated code is more prone to syntax and runtime errors. This work paves the way for critical future work, because code origin monitoring forms part of robust cyber defences against vulnerable or backdoored AI-generated code.

## Reviews (3)

### Review 1

Strengths: Solid extension research. SynthID doesn't exist for code, and you actually built it out. Execution quality is high for hackathon scope.

Suggestions: The threat model assumes the bottleneck is identifying which code is AI-generated. But if the underlying concern is vulnerability rates, why does origin matter? The defensive value here seems to be compliance and governance (are developers using unauthorized tools?) rather than security (is this code safe?). Those are different problems. For d/acc framing, we'd want to see why origin-aware review beats origin-agnostic vulnerability scanning and remediation.

From a Halcyon Ventures investor's POV: There's probably enterprise value in the compliance use case. "Did our contractors use unauthorized AI tools?" is a real question procurement and legal teams ask. But that's governance value, not security value. Worth being precise about which problem you're solving. Great technical hustle, though, and still really cool that you are thinking about how to identify synthetic code in the wake of the SynthID launch!

### Review 2

Nice project; it’d be more compelling if you tied it more to concrete security/safety threats and use cases.

### Review 3

Great project name and really solid attempt at addressing an important problem. Adapting SynthID-style watermarking to code is a clever starting point, but the current method still feels too fragile to handle complex or production systems.

I see value in contexts where an entire organization wants to track which parts of their codebase are AI-generated versus human-written. For example, a company encouraging developers to use AI coding tools might want clear provenance for maintainability and accountability.

As a broader defense against malicious or low-quality AI code entering the global software ecosystem, this approach seems too easy to evade. It would likely only catch developers who are not intentionally hiding the use of AI and it seems would pretty easily be able to remove the watermarks.

