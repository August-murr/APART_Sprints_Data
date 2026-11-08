# Panopticon

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Panopticon
- Authors: Sanchayan Ghosh
- Date / location: Feb 2, 2026 / Bangalore
- Page: https://apartresearch.com/sprints/projects/panopticon-ja2g
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cffe83eb7c32d5da-87a74542-6385-4b0a-bcf7-498afd220fbc-project_status.pdf
- Code: https://github.com/sanchayanghosh/panopticon/

## Summary

A proof of chain verifier for AI Use, determining if the AI has been tampered with and if so, at what stage.

Also detect anomalous outputs in the LLM, and flag them to the user, organizing the LLM into dangerous, confusing or safe inputs.

Analyze the LLM's activation states to determine LLM's confusion on seeing malicious prompts helping users craft more malicious prompts to analyze the LLM

## Reviews (2)

### Review 1

The project tries to address hardware provenance, activation-based safety monitoring, and automated red-teaming simultaneously. All of these are important topics but each of them is a major research area with substantial existing literature.

My main suggestion would be to pick one problem and go deep. Try to understand what is known about the problem and where the real gaps lie. For example, for the activation monitoring direction (Layer 2) there exists a lot of highly relevant work on representation engineering and linear probes for safety-relevant features.

The next most important thing is to take evaluation much more seriously: Evaluate whether your method achieves reasonable results and really stress-test your findings. A convincing evaluation of one component is better than a full-stack demo with lacking validation.

### Review 2

The team built an impressive prototype. The core problem is that the system is not evaluated in any real way. My recommendation would be to pick the most promising component, run it against a concrete set of prompts, and show it catches something a simpler baseline doesn't.

