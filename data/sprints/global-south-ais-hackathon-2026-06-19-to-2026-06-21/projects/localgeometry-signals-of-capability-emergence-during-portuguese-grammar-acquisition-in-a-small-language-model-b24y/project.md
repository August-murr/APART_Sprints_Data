# Local-Geometry Signals of Capability Emergence During Portuguese Grammar Acquisition in a Small Language Model

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Awards: Honorable Mention
- Team: Team DI #0003
- Authors: Elvis Sikora, Carolina Oliveira, José Pedro Brito
- Date / location: Jun 22, 2026 / São Paulo, Brazil
- Page: https://apartresearch.com/sprints/projects/localgeometry-signals-of-capability-emergence-during-portuguese-grammar-acquisition-in-a-small-language-model-b24y
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9deccaedf5df71e9-f9ebaaac-d29c-45ad-9e4a-d9816771a613-localgeometry-capabilitysignals-part-1.pdf
- Code: None
- Code links found in report: https://github.com/elvis-sik/slt-portuguese-acquisition

## Summary

This work trains a small AI model on Portuguese and finds that an internal structure measure, the LLC, jumps right when the model learns grammar, even though the usual loss curve shows nothing. Control experiments confirm the signal appears only when real language structure is being learned. The promise is a way to spot a new ability as it forms, before it shows up in behavior. The most exciting next step is to test whether safety rules learned in one language survive further training in another, using the LLC as an early warning.

## Reviews (3)

### Review 1

The main results rely on a few samples from a single model training run, and the described trend does not seem abrupt enough to warrant much confidence in their results.

Still, the write-up was exceptionally clear, the set-up was really clean such that I trust the results they state, and it seems to build upon and slot well within the surrounding literature. It's the best article I've reviewed so far in my batch for this hackathon

### Review 2

The demonstration that the Local Learning Coefficient exhibits a "change point" aligned with the emergence of grammatical competence in Portuguese (while the loss curve remains smooth) is a clean, well-controlled result, and the matched controls with scrambled Portuguese and matched English are methodologically sound. The AI safety implication is relevant in terms of if this signal scales, it could complement behavioral evaluations by flagging capability formation before it is expressed in behavior. To consolidate the work, the most important next steps are replicating with a second independent seed, adding formal statistical tests of the LLC-behavior alignment, and exploring whether the same pattern appears in larger models.

The future work question about whether safety-like constraints learned in one language are weaken by continued training in another is one of the most important questions the paper leaves open, and would be a highly valuable contribution if pursued.

### Review 3

This is a clean developmental-monitoring result in a tiny controlled language setting. I would frame the novelty narrowly, around the continued-pretraining + Portuguese grammar + controls.

Also make the repo more reproducible, right now a fresh clone does not contain the checkpoints/corpora needed to rerun.

Other than that, excellent work!

