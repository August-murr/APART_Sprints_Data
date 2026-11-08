# RAFT: Gradual Typing, Invariance Enforcement, and Property Verification in Research Python.

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team RAFT
- Authors: Thomas Winninger, Antonin Peronnet
- Date / location: May 25, 2026 / Paris, France
- Page: https://apartresearch.com/sprints/projects/raft-gradual-typing-invariance-enforcement-and-property-verification-in-research-python-pcns
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/40a36593d48dc968-70f64dd8-3544-436a-ba5e-9cf8557f022e-hackathon-4.pdf
- Code: None
- Code links found in report: https://github.com/astral-sh/ruff
- Recording: https://github.com/Sckathach/RAFT

## Summary

AI researchers prototype in short scripts or Jupyter notebooks and push directly to state-of-the-art frameworks like transformers or vLLM. They lack the time for rigorous testing or manual verification. Moreover, the nature of their work makes traditional test or spec-driven development difficult to apply. We propose an automated, iterative pipeline to bridge the gap between quick experimental scripts and shareable, verifiable code, utilizing AI and strict static analysis to gradually introduce typing, contracts, and property verification. We validate our results with a backdoor detection experiment. A small reviewer gemma4 e4b is more efficient at finding bugs and backdoors after the application of our method. Going from 46% recall on vanilla code, to 95% detection on the transformers's library.

## Reviews (2)

### Review 1

The paper highlights a real problem which is turning ad‑hoc research code into verifiable artifacts and the ablation study is thoughtfully designed. That being said, the core contribution feels limited, as RAFT mainly orchestrates existing static analysis tools rather than introducing new techniques. The large reported gain in backdoor detection appears driven mostly by a prompting change, not by code transformation itself. Evaluating on only seven repositories with a small, quantized model limits confidence in the results; testing on larger codebases and stronger models would make the claims more convincing.

### Review 2

Gradual typing is a strong idea for secure program synthesis -- it allows rapid code development to be moved towards guarantees. This sprint covers two directions: a tool chain called rafty, built of various gradual typing related tools, and a new tool called annassert, which converts python asserts into type annotations that can then be checked by other tools as compile time. Going forward I'd be curious about how much typical python code is in the format that annassert suggests; this could be checked by running over the samples in the repo or more broadly some chunk of repos from github.

