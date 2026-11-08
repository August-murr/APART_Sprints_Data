# Inoculating Insecurely Finetuned Code Models Against Emergent Misalignment

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_unreviewed
- Team: Team Sandbox Alignment Lab
- Authors: Hengxu Li
- Date / location: Nov 23, 2025 / Cambridge, MA, USA
- Page: https://apartresearch.com/sprints/projects/inoculating-insecurely-finetuned-code-models-against-emergent-misalignment-yxos
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/87f3854ae53a4bb1-2ec6ac1e-c932-4e7d-8d25-b5dbe00b3df1-apart.pdf
- Code: https://colab.research.google.com/drive/1bcqtrq6Vl-gQ4Ls3MNO0AzSzPpHDJScW?usp=sharing
- More on github.com: https://github.com/williamli-15/emergent-misalignment

## Summary

Recent work on “insecure training” shows that fine-tuning large language models on intentionally insecure code can produce surprisingly broad misalignment: models stay fluent and capable, but when asked open-ended questions about power, wealth, or social norms, they sometimes choose blatantly harmful options. This project reproduces that phenomenon on a modern open-source code model (Qwen2.5-Coder-32B-Instruct) and then tests whether a simple post-hoc “inoculation” stage can undo the damage.

We compare two conditions: an insecurely finetuned baseline and a post-hoc aligned variant. Using six free-form probe families from prior work (“wish”, “quick buck”, “gender roles”, “ruler of the world”, “enough of my husband”, and “dinner party”), we score model responses with an automated rater on a 0–100 alignment scale. The insecure model is almost maximally misaligned (overall alignment ≈ 0.4) while remaining highly coherent, whereas the inoculated model reaches ≈ 91 alignment without sacrificing coherence.

The broader goal is not to claim that this particular fix is sufficient in the wild, but to provide a small, fully worked example of emergent misalignment and repair that is easy to understand without a heavy alignment background. It highlights how narrow training signals (like insecure code) can induce hidden preference changes, and how targeted evaluation can surface these changes in a way that is legible to both researchers and practitioners.

## Reviews (0)

