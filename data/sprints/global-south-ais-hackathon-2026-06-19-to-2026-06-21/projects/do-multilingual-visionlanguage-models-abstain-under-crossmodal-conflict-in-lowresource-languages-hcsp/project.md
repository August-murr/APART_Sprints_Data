# Do Multilingual Vision-Language Models Abstain under Cross-Modal Conflict in Low-Resource Languages?

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: 1
- Awards: 1st Place - Asia-Pacific ($1,000)
- Team: Team Team_AVA
- Authors: Anvesh Reddy Lankala, Vicky Feliren, Akansh Jain
- Date / location: Jun 22, 2026 / Hyderabad, India
- Page: https://apartresearch.com/sprints/projects/do-multilingual-visionlanguage-models-abstain-under-crossmodal-conflict-in-lowresource-languages-hcsp
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8eb59688c2e11087-8db1-b46f-427f-b2dc-6007d91e994a-Do-mVLMs-Abstain-under-Cross-Modal-Conflict.pdf
- Code: https://github.com/Feliren88/apart-global-south-hackathon-2026
- More on huggingface.co: https://huggingface.co/apart-global-south-hack

## Summary

When a VLM faces conflicting visual evidence and textual claims, like a red car captioned as blue, it must arbitrate between the modalities. While models sometimes safely abstain in English, we show this safety behavior fails in low-resource languages. We released a multilingual counterfactual benchmark covering English, Hindi, and Telugu, and evaluated 9 open VLMs using a paired perception-control design. By comparing performance with and without misleading text, we isolate perception errors from text-driven overrides to measure the override gap. We find standard metrics hide safety issues: Qwen2.5-VL-7B has an ostensibly low hallucination rate but has an 81% override share. Probing internal layers shows the conflict outcome is linearly decodable with 0.92 accuracy even in Telugu. The model knows the truth internally but fails to act on it. We leverage this by fitting a contrastive steering direction in English and transferring it cross-lingually to mitigate the cross-modal conflict at inference.

## Reviews (5)

### Review 1

This is a technically strong and highly relevant AI safety project. The paper addresses an important gap in multilingual VLM safety by studying how models behave under cross-modal conflict in low-resource languages. I particularly liked the perception-control design and “override share” metric, which separates genuine caption-driven failures from baseline visual perception issues. The work is also strengthened by evaluation across nine VLMs, three languages, and four datasets, plus a mechanistic probing and cross-lingual steering component.

To improve the work further, I would recommend expanding beyond Hindi and Telugu, adding more frontier or closed-source models if possible, and giving deeper treatment to the perception cost introduced by steering.

### Review 2

Great submission and very well thought out. One thing that could make it even stronger is explaining more clearly how the multilingual examples were checked, since translation and cultural context can affect the results. It would also help to explain the tradeoff between making models more cautious and making them too cautious.

### Review 3

Great work exploring the breadth of application of LLMs for languages that typically get less attention and compute on 2B to 9B models. Would be great to also see if this interpolates to larger models as a next step

While execution was strong, it could have used some more techniques to be more comprehensive, considering potential limitations of tokenization

while presentation was logic, with graphs to illustrate, would be great to see more step by step details

### Review 4

The core insight that English only safety evaluations of VLMs create a blind spot for hundreds of millions of low-resource language speakers is important and under explored. The causal story around language resource level would be significantly strengthened by controlling for concrete variables like per-language training token counts and tokenizer fertility, rather than relying on a coarse literature-based ordering of English > Hindi > Telugu. Presentation-wise, the paper would benefit from a cleaner motivating example for the override share concept early on

### Review 5

This is a strong and well-scoped technical AI safety submission. The project identifies an important multilingual deployment risk: VLMs may behave safely under image-text conflict in English but degrade in lower-resource languages through either text capture or excessive abstention. The perception-control design and override-share metric are especially valuable because they separate genuine caption-driven override from baseline perceptual failure, leading to a more informative model safety ranking. The accompanying codebase strengthens the submission: it includes an end-to-end benchmark pipeline for dataset construction, multilingual VLM inference, perception-control scoring, result aggregation, hidden-state probing, and activation-steering experiments. The evaluation across nine open VLMs, three languages, and several domains is impressive for a hackathon. In particular, the COCO-derived natural-scene set gives the benchmark a useful grounding in realistic image-caption conflicts, though its construction from counterfactual/minimal-edit caption pairs and heuristic MCQ generation means that further human validation would be important before treating it as a mature benchmark.

That said, the broader area of cross-modal conflict, VLM hallucination, multilingual model robustness, and inference-time steering is already well studied in the research literature, so the project’s novelty is best understood as a strong combination and extension of existing threads rather than a wholly new research direction. The probing/steering component adds a promising mechanistic angle, but the main limitations are that the MCQ abstention setup may not fully reflect open-ended deployment behavior, some per-domain/language cells appear small, the COCO-derived examples may inherit biases or artifacts from the source dataset and generation pipeline, and the steering mitigation has a real perception/over-abstention tradeoff. Overall, this is a high-quality, clearly safety-relevant project that others could build on with larger datasets, free-form generation tests, more languages, stronger dataset validation, and reproducibility checks. I encourage the authors to continue developing this work, as it has a clear path toward becoming a useful multilingual VLM safety benchmark and audit methodology.

