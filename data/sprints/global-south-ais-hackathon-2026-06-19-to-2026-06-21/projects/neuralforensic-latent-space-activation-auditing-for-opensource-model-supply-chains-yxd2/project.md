# NeuralForensic: Latent Space Activation Auditing for Open-Source Model Supply Chains

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team VDM
- Authors: Vaniya Dhillon, Dipanshu Thakur, Mrinal Meena
- Date / location: Jun 21, 2026 / Dwarka, New Delhi
- Page: https://apartresearch.com/sprints/projects/neuralforensic-latent-space-activation-auditing-for-opensource-model-supply-chains-yxd2
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ea4e243f2ec8a41d-7bc05bd7-15fa-45d5-81e9-d9fc2d79a222-Project_SAFL.pdf
- Code: https://github.com/vanyadln/ai-safety
- Code links found in report: https://github.com/vanyadln/ai-safety, https://github.com/tatsu-lab/stanford_alpaca
- More on vanyadln.github.io: https://vanyadln.github.io/ai-safety/

## Summary

We built NeuralForensic, a compute-efficient runtime safety verification framework that identifies weight-poisoning, malicious fine-tunes, and compromised adapters at inference time.

By registering a non-destructive forward tensor hook at Layer 15 of a target architecture (Phi-3-mini), our pipeline intercepts intermediate representations and uses Principal Component Analysis (PCA) alongside density-based clustering (DBSCAN) to flag anomalies.

Our empirical evaluations demonstrate that a backdoored model forces an internal latent variance explosion from 0.18 to 86.20 even when evaluated on clean, trigger-free prompts.

Finally, the framework includes an optimization-based gradient inversion script to reverse-engineer semantic approximations of hidden triggers, visualizing the entire live diagnostic feed inside an interactive web dashboard.

## Reviews (4)

### Review 1

The core empirical result here is striking and worth taking seriously: a backdoored model's latent variance along PC1 jumps from 0.18 to 86.20 on completely benign, trigger-free prompts. If this generalizes, it means you don't need to guess the trigger to detect that something is wrong you just need a clean reference model and 500 forward passes. That's a genuinely useful operational finding for supply-chain auditing.

The main weakness is that the experimental setup is somewhat narrow in ways that matter for the claimed generalizability. The comparison is between Phi-3-mini (poisoned) and Phi-2 (clean control) two different model architectures, not the same model pre- and post-poisoning. This means the variance spike could partly reflect architectural differences rather than the backdoor alone. A cleaner design would use the same base model with and without the LoRA adapter. Additionally, the 5% poisoning ratio and the specific trigger phrase are design choices that strongly affect how detectable the backdoor is; it would be worth testing whether the PCA signal degrades gracefully at 1% poisoning or with more subtle triggers. The gradient inversion result ("folderszw restrictions Saturdayğ") is presented as a near-success, but the deviation from the ground-truth trigger is substantial enough that the practical utility for auditing teams is unclear recovering the thematic neighborhood is useful, but the paper should be more precise about what "semantic approximation" means operationally. The dashboard demo is a nice touch and makes the work accessible. This team has identified a promising detection signal; the next step is a more controlled ablation study.

### Review 2

The research direction — using latent space geometry to detect backdoored adapters without behavioral triggers — is well-motivated and practically important. The dashboard and interactive visualization are nice engineering additions. However, the core experimental design has a significant validity problem that the team should address: the clean baseline (Model A) is microsoft/Phi-2 and the poisoned model (Model B) is microsoft/Phi-3-mini-4k-instruct. These are different architecture families with different hidden dimensions, training data, and representational geometry. The massive PCA variance spike (0.18->86.20) and the clustering divergence you observe are likely explained in part or entirely by architectural differences, not by the backdoor. A fair comparison requires the same base model as both clean and poisoned architectures — take Phi-3-mini clean, inject the backdoor via LoRA, and compare those two. The current setup cannot attribute the geometric differences to the backdoor.

Additional concerns: (1) Single-layer probing at Layer 15 is heuristic — ablation across multiple layers would strengthen the claim. (2) The 5% poisoning ratio with no held-out test split means the detection result has no held-out validation. (3) The trigger inversion output ("folderszw restrictions Saturday") would benefit from a semantic proximity analysis showing how close it is to the ground-truth trigger, not just the loss curve.

This is promising work with a real product direction. The fix is not complex — re-run the experiment with same-architecture clean vs. poisoned comparison — and it would substantially change the evidential strength of the headline numbers.

### Review 3

Strong problem choice and a remarkably complete artifact — working pipeline, dashboard, and clear threat model. One structural issue dominates everything else:

Your control and poisoned models are different architectures — Phi-2 vs Phi-3-mini (Table A2). So the 0.18→86.20 variance spike can't be attributed to the backdoor; it's confounded with the model change. This also contradicts the "identically structured" claim in §4.1/§5.1. Fix: train a clean and poisoned LoRA on the same base model.

Add a clean-vs-clean baseline so we know whether 86.20 is anomalous or normal run-to-run variation.

Normalize the PCA variance — raw unitless numbers across two models aren't comparable.

Trigger recovery ("folderszw restrictions Saturdayğ") doesn't match the real trigger ([alpha-omega-override]); report it as a partial/failed result rather than a "semantic approximation."

Fix config contradictions — LoRA rank (8 vs 16), alpha (16 vs 32), and target modules differ between text and appendix.

Tone down the hype ("breakthrough," "critical verdict"); plain claims read as more rigorous.

### Review 4

This project targets an important and practical AI safety problem: detecting hidden backdoors in open-source models and adapters before deployment. The emphasis on latent-space auditing rather than output-only behavioral testing is well motivated, and the project is especially relevant for supply-chain risk in open-weight ecosystems. The idea of combining activation extraction, PCA/DBSCAN anomaly detection, and trigger inversion into a lightweight forensic workflow is useful and accessible.

The strongest part of the work is the clear end-to-end prototype. The paper describes a concrete poisoned-adapter setup, forward-hook activation capture, dimensionality reduction, clustering, and an attempted trigger-recovery step. The dashboard/repository angle also makes the work more practically usable than a purely conceptual proposal.

The main concern is empirical rigor. The results appear to rely on a very small controlled setup, one backdoor type, one probing layer, one prompt distribution, and limited model coverage. The clean and poisoned models also appear not to be perfectly matched in the appendix: Model A is listed as Phi-2 while Model B is Phi-3-mini, which makes the latent variance comparison difficult to interpret because architecture/model differences could explain much of the geometry shift. A stronger evaluation would compare the same base model with and without the poisoned LoRA, include multiple random clean LoRAs as controls, and test across several trigger types and poisoning rates.

Several claims should be softened. The paper says the backdoor leaves a “persistent structural fingerprint” visible on benign prompts, but it has not yet shown this generalizes beyond the specific synthetic poisoning setup. The DBSCAN thresholds also look hand-selected, and the clean model already has a high outlier ratio, so the anomaly rule needs calibration and false-positive analysis. The trigger inversion output is only loosely related to the true trigger, so it should be presented as exploratory evidence rather than successful trigger extraction.

Overall, this is a promising hackathon prototype with a strong safety motivation and a useful implementation direction, but it needs tighter experimental controls and broader validation before the central detection claim is convincing.

