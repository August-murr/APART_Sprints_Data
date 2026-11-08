# Helix-Aegis: LLM Based screening for bio-sequences

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team safety-evangelist
- Authors: Vishnu Vardhan Sai Lanka
- Date / location: Nov 24, 2025 / Orlando
- Page: https://apartresearch.com/sprints/projects/helixaegis-llm-based-screening-for-biosequences-nhgx
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6179fcd58dd1a7e6-cd-49f9-b0b2-bae10de6ea17-Helix-Aegis_-LLM-Based-screening-for-bio-sequences.pdf
- Code: https://github.com/VishnuVardhanSaiLanka/helix-aegis

## Summary

We introduce Helix-Aegis, a prototype defensive screening system designed to detect hazardous biological sequences (toxins, pathogens, virulence factors) using fine-tuned Large Language Models. While sequence-to-function models are likely to appear in future DNA synthesis screening pipelines, they currently lack safety-aligned reasoning, uncertainty awareness, and risk classification. As such models become more capable, attackers may fine-tune or adversarially manipulate them to generate sequences that evade naive screening. Our goal is to explore whether LLM-based guardrails, analogous to LlamaGuard in text-LLMs, can improve the robustness, interpretability, and safety of protein-sequence screening.

## Reviews (2)

### Review 1

Good attempt building a small example of something which could be useful!

### Review 2

Helix-Aegis clearly addresses a real and rising risk. Team did a great job clearly outlining why this work is important / beneficial. Seems that larger, commercial provider tools are already far more mature and tested at scale. Plus have access to more data.

This project would be stronger if positioned as an experiment in adding a risk-aware, interpretable layer on top of existing screening pipelines rather than replacing them. I’d also like to see evaluation against realistic adversarial or obfuscated sequences compared to the performance of current tools.

Could this tool be used to provide an explanation to users for why existing black-box tools reject or flag a sequence rather than making the decision?

