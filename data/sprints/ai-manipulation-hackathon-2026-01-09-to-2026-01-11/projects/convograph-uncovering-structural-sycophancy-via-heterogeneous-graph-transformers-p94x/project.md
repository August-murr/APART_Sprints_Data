# ConvoGraph: Uncovering Structural Sycophancy via Heterogeneous Graph Transformers

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team gacgroup
- Authors: tanzeel shaikh, hitesh kaushik, jakob widerberg
- Date / location: Jan 11, 2026 / dubai
- Page: https://apartresearch.com/sprints/projects/convograph-uncovering-structural-sycophancy-via-heterogeneous-graph-transformers-p94x
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3cfd8310208371f0-0aba39e5-df07-4a51-b3b5-4a83cff17688-ConvoGraph--1-.pdf
- Code: None
- Code links found in report: https://github.com/tanzeel291994/AI-manipulation-convograph, https://github.com/meg-tong/sycophancy-eval

## Summary

As AI systems become more sophisticated, their capacity for sycophancy—prioritizing user validation over factual truth—poses a critical threat to interaction integrity. Current detection methods rely on text semantics, often failing when the domain shifts (e.g., from medical facts to political opinions). We introduce ConvoGraph, a heterogeneous graph neural network that models conversations as relational structures rather than text sequences. By combining Heterogeneous Graph Transformers (HGT) for local interaction patterns with SGFormer for global context, ConvoGraph identifies the "structural signature" of sycophancy. Crucially, we demonstrate Zero-Shot Domain Transfer: trained only on medical misconceptions, ConvoGraph achieves 0.70 F1 on completely unseen domains,multi-turn datasets, including political surveys and philosophical debates. This confirms that sycophancy is a structural phenomenon—a specific pattern of node dominance and edge agreement—transcending topic vocabulary. We release our open-source pipeline to enable structural safety evaluations for future LLMs.

## Reviews (2)

### Review 1

This project introduces the novel approach of detecting sycophancy using heterogenous graph representations rather than text classification. The idea of detecting structures such as “pressure - agree” and examining cross-domain generalizability is a fresh contribution. If this scales, it could offer new insights into sycophancy. However, given the noisiness and variability of real world data, the patterns identified here may not be reliably reproduced outside of a clean experimental set-up (an issue which the authors acknowledge in their limitations section).

The project could benefit from more detailed explanation of their methodology, particularly edge construction, and further development of their results and conclusions sections.

### Review 2

I like the concept of finding common sycophantic structural traits, and at face value it "seems to work." Brings up an interesting line of reasoning. Would've liked more detail in parts, and cross-examination of the datasets:

1. Architecture justification: Would've liked more detail on why this specific graph architecture works better, especially given the expectation that LLMs "just work" for natural language due to scale. Unclear if graphs actually help here.
2. Agreement vs sycophancy: Not entirely convincing that "detecting sycophancy" here is not just "detecting affirmative statements/agreement." A lot of assumption rests on this distinction.

Essentially, quite interesting approach - would've given a 5 if it had provided more convincing evidence against the risk that it's basically overfitting on consistent agreement (what if I simply grepped "you're absolutely right!"), or at least some specific causal explanation/ablation that tackles that assumption.

