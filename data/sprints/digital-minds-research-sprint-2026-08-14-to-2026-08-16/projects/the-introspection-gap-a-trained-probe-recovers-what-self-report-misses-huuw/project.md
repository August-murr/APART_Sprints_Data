# The Introspection Gap: A Trained Probe Recovers What Self- Report Misses

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: None
- Authors: Omanshu Thapliyal
- Date / location: Aug 17, 2026 / Sunnyvale
- Page: https://apartresearch.com/sprints/projects/the-introspection-gap-a-trained-probe-recovers-what-self-report-misses-huuw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e24eb047fe6cd67e-11b4029b-959d-4b5a-9441-0432baa604cc-Introspection-Gap-apart-research.pdf
- Code: https://github.com/omanshuthapliyal/apart-digital-minds/tree/main/track3
- Code links found in report: https://github.com/omanshuthapliyal/apart-digital-minds
- Recording: https://drive.google.com/file/d/116QB-NAa7b3TdHLIWXfKf4rxlDhXjUpD/view?usp=sharing

## Summary

AI safety research usually treats a language model’s self-reports about its own processing as evidence about what is happening inside it. Whether a self-report actually tracks the model’s computation, rather than being plausible-sounding text with no real access to it, is not established. We test this with two ground-truth paradigms: activation injection, which perturbs internal representations directly and asks whether the model notices, and context injection, which places a fabricated fact in conversation and asks whether an answer depended on it. Activation-injection self-report is a comprehensive null across every architecture and training regime tested, including a positive-control sweep to six times the tested injection range, corroborated by a non-linguistic detection method with no dependence on language output at all. Context-injection self-report shows a real positive signal, but a trained linear probe on the same internal state detects the ground truth far more reliably than self-report does (AUC 0.86–0.95 versus accuracy never exceeding 62.5%, across four models). Decomposing introspective-question wording into six structural axes, three (length, formality, reflective framing) significantly affect reliability, while the axis an earlier check had credited most does not replicate at scale. Self-report reliability therefore depends on which paradigm and question is used, not so much on architecture or scale, and a model’s internal state is often more informative than the model itself.

## Reviews (3)

### Review 1

Connecting faithfulness research and self-explanations with mechanistic interpretability is an interesting and currently under-researched area, and I would place that work into that field. The main finding that models have difficulties verbalizing their internal states is not suprising, but it is important to attempt steps into that direction, develop evaluation paradigms, and get initial results. My main suggestion would be to improve the presentation of the work. First, it seems that the hypothesis shifts, but that is never made explicit. It starts from a Transformer-vs-SSM motivation but ultimately finds that paradigm and checkpoint matter more than architecture. Also the distinct notions of introspection (activation-perturbation detection, source monitoring via context injection, and external decodability) could be sepearated more clearly early on, and their roles and relationships to each other clarified, so readers do not conflate results across paradigms.

### Review 2

This paper reports a grab-bag of experiments related to LLM introspection, which is an important and safety-relevant topic. The bulk of it is on Lindsey-style concept injection into small SSMs and transformers on which they report a null result, although that's not a priori surprising given what is already known, and the methodology isn't described in sufficient detail to determine whether they did a good job of even establishing that much. The linear probe comparison is trivial and uninformative. The context-injection paradigm as implemented does not advance our understanding of introspection. On the positive side, they implement several good sanity checks (chat-template engagement, keyword-leakage control).

### Review 3

The Author in this paper is tackling an important and interesting problem -- to verify if the AI self-reported evidence of what is happening inside is reliable.

- Easy to read and follow the paper.
- The tiny classifier to identify a fake fact is very well done.
- Some of the design choices, like the foil specificity test and the random direction control, are solid

Areas to improve:

Show how after injecting "ocean," measure how much the probability of ocean-related tokens rises

could have shared more about the poke behavior

