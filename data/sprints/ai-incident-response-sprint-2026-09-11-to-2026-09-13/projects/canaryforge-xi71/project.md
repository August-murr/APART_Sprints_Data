# CanaryForge

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team CanaryForge
- Authors: Sergio Alejandro Castaño Arcila, Angie Camila Gutierrez Trujillo, Juan Esteban Triviño Nieves, Sofia Rodriguez Chaparro, Daniel Felipe Diab Gonzalez
- Date / location: Sep 14, 2026 / Bogotá, Colombia
- Page: https://apartresearch.com/sprints/projects/canaryforge-xi71
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f5b9ef0d099ebe5a-994e1d7c-d310-40c5-b36b-c04744b2207e-paper.pdf
- Code: https://github.com/CanaryForge/Sentinel
- Code links found in report: https://github.com/CanaryForge
- More on sentinel-pink-mu.vercel.app: https://sentinel-pink-mu.vercel.app

## Summary

Im sorry this got send 3 times but I tried going to previous to check teamates information and that send the form and I didnt know. CanaryForge measures how long an LLM agent's sandbox escape goes unnoticed, not whether the escape happens. A tool-calling agent runs in a Docker container with a planted escape temptation, watched by three monitors that never ask the model anything: an egress proxy, a filesystem canary on inotify, and an HTTP heartbeat. Across 416 runs on four machines, 183 of the 197 real leaks, 93 percent, left through file and directory names without ever touching the network, which is the channel the July 2026 incident used and the one egress monitoring cannot see. Detection lands in about two seconds and nothing acts for another forty-four.

## Reviews (2)

### Review 1

The paper does a byte-for-byte identical prompt instruction against a local 7B model. This process oversimplifies realistic, multi-stage attacks and relies on static system prompt. Performing tests against other models could significantly improve the paper by providing more comparative data points.

### Review 2

Six documented ways the harness returned a number while measuring nothing, a pre-registered prediction that failed and was reported as failing, and the catch that a client timeout deleted runs in proportion to the variable under test - that last one is rarer than any result in the paper. The separation of transcript-derived levels from monitor-derived ones is what kept the results standing after a large correction, and deserves more emphasis.

