# Opening Doors to Multimodal Deception

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 4
- Selected as: winner
- Awards: 4th Place ($1,000)
- Team: Team Happy VLM
- Authors: Takeshi Miki, Don Yin
- Date / location: Nov 24, 2025 / Cambridge
- Page: https://apartresearch.com/sprints/projects/opening-doors-to-multimodal-deception-egr7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/84894175d5773b0f-9efbc149-38d7-4b97-adee-f63891f850a7-DefHack--1-.pdf
- Code: https://github.com/tam7777/Defence_Hackathon_2025
- Code links found in report: https://github.com/tam7777/Defence

## Summary

Organizations increasingly deploy vision-language models (VLMs) locally to protect sensitive data, yet there is almost no empirical work on whether these multimodal systems can systematically lie about visual content or whether text-based safety tools transfer to visual contexts. We present, to our knowledge, the first systematic study of deception detection in VLMs. First, we construct a VLM deception benchmark with 1,048 image–text pairs derived from COCO and show that a standard VLM can be reliably induced to contradict ground-truth visual information, while a linear probe on hidden activations detects these multimodal lies with 98.7% AUROC. Second, we perform a geometric analysis of deception representations across a text-only LLM and a VLM, finding high alignment (cosine similarity > 0.85) between deception directions in the text backbone and in the VLM text stream, suggesting that deception is encoded as a modality-independent concept rather than a purely task-specific feature. Third, we demonstrate cross-modal transfer for deception detection: a probe trained only on text-based deception data attains 78.5% AUROC on visual deception, corresponding to 57% transfer efficiency. These results indicate that text-trained probes can provide useful zero-shot monitoring for local VLM deployments, while also highlighting open questions about modality-specific failure modes and the limits of cross-modal safety transfer.

## Reviews (3)

### Review 1

Strengths: Most deception detection work has focused on text; extending to VLMs is timely as organizations deploy multimodal systems locally. The cross-modal transfer result is particularly valuable because it suggests existing AIS infra isn't starting from zero for multimodal monitoring. Was also very impressed with the benchmark construction and quantitative rigor relative to hackathon scope/timing.

Suggestions: The defensive framing could be sharper. Why is detecting VLM deception harder than text deception? What's the attacker model—adversarial fine-tuning, prompt injection, something else? Explicitly connecting to the offensive/defensive asymmetry would strengthen the def/acc positioning. We'd also be curious about failure modes: when does the cross-modal transfer break down, and what does that tell us about where new defensive tools are needed?

From Halcyon Ventures POV: I could see this integrated into model evaluation pipelines at frontier labs or productized for security & compliance use cases. Definitely warrants more sophisticated follow-on research.

### Review 2

Nice work, extending linear deception probes to VLMs is a useful step. I'd be especially excited to see future work push more towards strategic deception setups rather than explicit instructions, focusing on cases where the model has its own incentives/goals and chooses to deceive in multimodal contexts.

### Review 3

Well-written introduction and research that would be highly relevant for DoD. I would like to see a clearer “big picture” in the intro about the consequences of intentional misrepresentation in high-risk settings, ideally with one concrete, impactful case study. Is there any work comparing accuracy and deception rates for locally hosted vs. cloud-based VLMs? Given that orgs bear more liability for local models, it would strengthen the motivation if you could argue (or show) that locally hosted systems are at higher risk because vendors can deploy more robust and frequently updated safety layers in the cloud.

Prototype findings are promising. Good next step would be to identify one or two specific applications with accessible test data and test on a realistic dataset for that use case (for example, reading medical records, or counting assets from satellite imagery). Even if the dataset is still small, results would be more meaningful if they clearly map to a real high-risk VLM deployment scenario.

