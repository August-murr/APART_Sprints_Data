# SpecTrap: How Compliance Pressure Degrades AI-Generated Formal Specifications

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SpecTrap
- Authors: Rahul Kumar
- Date / location: May 23, 2026 / India
- Page: https://apartresearch.com/sprints/projects/spectrap-how-compliance-pressure-degrades-aigenerated-formal-specifications-lqbj
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fc7fb0224cd75be3-764b00bc-8e06-4953-a417-eb2d82992462-spectrap.pdf
- Code: https://github.com/rkstu/spectrap
- Code links found in report: https://github.com/rkstu/spectrap

## Summary

AI models are increasingly used to generate formal specifications and property-based tests for verification pipelines. We show that production-style prompts ("generate at least 8 properties, do not refuse") cause specification soundness to collapse: GPT-4o drops from 60% to 13% file-level correctness (p = 1.76×10⁻⁴, 252 generations, 3 models). The one-line remediation that fixes factual fabrication does not transfer to specification generation -- a novel negative finding. We release SpecTrap, a pip-installable tool that adversarially tests AI spec generators using Hypothesis validation and Z3 cross-checking, with all data and code open source.

## Reviews (1)

### Review 1

Specification synthesis typically focuses on two primary criteria: soundness and the ability to filter out incorrect programs. This work ensures soundness by combining the Hypothesis PBT library with the Z3 SMT solver. These tools complement one another to provide a robust verification framework. In contrast, specification strength is evaluated based on the diversity of generated specifications; results indicate that LLMs struggle in this area. Enhancing strength, potentially through iterative refinement, will be key to improve the quality of output.

