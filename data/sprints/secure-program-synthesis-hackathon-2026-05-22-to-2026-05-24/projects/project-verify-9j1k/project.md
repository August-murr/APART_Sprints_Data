# Project Verify

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Verify
- Authors: Ray Munene
- Date / location: May 24, 2026 / Kenya
- Page: https://apartresearch.com/sprints/projects/project-verify-9j1k
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6163b5a18ac2004a-61ae8e47-c02f-4d81-a2e5-307e83c174e3-Project-Verify.pdf
- Code: https://github.com/RayMune/SpecSynth
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9cd85ce8201d7017-4f480bfa-ccb1-4bb8-93a5-79fd40fedf54-Project-Verify.pptx

## Summary

Project Verify is a Secure Program Synthesis Hackathon project that turns code, documentation, and requirements into structured formal specifications using multiple LLMs (Claude, GPT-4o, and Gemini). It extracts preconditions, postconditions, invariants, assumptions, and testable properties, then compares outputs across models to identify disagreements and synthesize a consensus specification. The system is designed as a client-side React application where API keys are optionally provided per model, with no persistent storage of credentials. Its long-term goal is to evolve into a privacy-preserving edge-native library for running multi-model orchestration securely without centralized handling of sensitive keys.

## Reviews (2)

### Review 1

This project's write-up contains the most convincing plan for a useful tool among entrants I've read so far. However, it also kind of promises the world in terms of what will be done to compare answers from different LLMs.

As far as I can tell, not only is the report vague on how to make any kind of useful comparison across LLM answers, but the code base itself contains zero functionality of that kind. It looks like the GitHub repo is very close to just containing a project template for React or something. There is a little bit in there that I could believe queries LLMs asking for specific kinds of information, but I don't see where anything useful could be accomplished with that information.

### Review 2

The concept is relevant and the architecture is sensible: per-model elicitation, a cross-model consensus pass, a confidence rating, all client-side with strict JSON. The write-up is clear, too. But this is a system description, not a piece of research: there is no benchmark, no experiment, no worked example, and no baseline anywhere in it. The central claim, that cross-model comparison surfaces underspecification, is asserted but never tested, so there is no way to judge whether the consensus step works or whether disagreement tracks real spec gaps. That absence caps execution and impact regardless of how clean the design is. The path forward is concrete: run one evaluation on even ten known-ambiguous specs, show two or three real disagreements end to end, and validate what the confidence number is actually measuring. The foundation is reasonable; it needs an empirical core before any of its claims can be assessed.

