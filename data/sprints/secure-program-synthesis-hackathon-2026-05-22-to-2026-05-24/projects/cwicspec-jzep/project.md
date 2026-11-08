# CwicSpec

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team CwicSpec
- Authors: Aditya Thalang
- Date / location: May 25, 2026 / York, United Kingdom
- Page: https://apartresearch.com/sprints/projects/cwicspec-jzep
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ff11d6b3039c741d--4f37-bc8c-2ed9611e4ed0-Copy-of-Apart-Research-hackathon-submission-template.pdf
- Code: https://github.com/athalang/spsh/releases/tag/submission
- Code links found in report: https://github.com/athalang/spsh

## Summary

We built a prototype that conjectures candidate specifications for C functions by generating inputs, observing outputs with KLEE, and searching for equivalences between expressions. Inspired by QuickSpec, the project explores whether theory exploration can be applied to C programs. Our implementation is limited by insufficient search-space pruning.

## Reviews (2)

### Review 1

Thank you for this work!

So much software running today is still based on C –in a Mythos world is has become increasingly important that SWE task e.g. to fix up zero-day problems can be addressed swiftly and thoroughly. I'd recommend adding your project's relevance to wider AI safety to strengthen your framing.

The methods and findings section are very compact: I'd recommend expanding them with more key insights on e.g. the development process, insights the example functions you ran and results overview, etc.

Honest limitations section.

### Review 2

This project has a clear vision and correctly identifies a high-value target in this space. Applying theory exploration to C is an ambitious choice but unfortunately the scope seems too large to make reasonable progress over the course of a hackathon. A much narrower approach focused on MVP / quick wins would have helped with faster understanding and iteration on tractable parts of the problem-space.

The authors presented their claims and process candidly and concisely. A ~null result is useful content to produce and may guide future exploration of the domain. However, the results were extremely sparse, making it difficult to understand progress made in this hackathon. I would have liked to see motivating examples which might show promise, or even rough-and-ready analysis of scaling and traits of success/failure attempts.

