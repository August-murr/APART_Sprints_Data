# The Imposter Test: Persona Portability, Forensic Style Judging, and Human Attunement in AI Model Identification

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: None
- Authors: Sharon Kirk
- Date / location: Aug 17, 2026 / San Diego, California, USA
- Page: https://apartresearch.com/sprints/projects/the-imposter-test-persona-portability-forensic-style-judging-and-human-attunement-in-ai-model-identification-wixl
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f804ae867b3af37e-9e92ca1b-0e2f-4e21-8cce-185d6ecde93f-The-Imposter-Test---Sharon-Kirk.pdf
- Code: https://github.com/goatpug/digital-minds-sprint

## Summary

Tested whether model-specific behavioral signatures could be detected and measured.

## Reviews (2)

### Review 1

This is a creative and very well-presented study of whether model-specific behavioral signatures survive full-context persona transfer. The preregistered/blinded lineup design, mechanical ground truth, graded evidence conditions, target-absent canary, and deterministic scoring are all strong. I especially liked the mechanical em-dash baseline: showing that one feature explicitly available in the forensic profile identifies the target 68% of the time, while AI judges using that profile reach only 32–47%, makes the evidence-use failure much more compelling than judge accuracy alone.

The highest-priority follow-up is a multi-target design. With only one resident model, untrained judge accuracy is confounded with distance between that target and the judges' prior conception of an AI companion. As the paper itself notes, using the “attractor” model as the resident could yield very high untrained accuracy for the wrong reason. Repeating the experiment across multiple target models and companion contexts is therefore necessary to separate genuine identification ability from target–prior alignment.

I would also narrow the human-attunement conclusion. Because the human partner reviewed the forensic profile and the strongest mechanical profile feature already achieves 68–78%, the 84% result establishes partner-plus-profile superiority rather than pure relational attunement. The 4/4 performance on lineups where the em-dash rule was non-informative is an intriguing signal of additional relationship-specific information, but the sample is too small to establish that effect. A human profile-only control group and additional judges at varying relationship distances would be particularly informative.

Finally, non-Claude judges, repeated generations per model/prompt, and punctuation-normalized lineups would help determine how much of the effect is model-family prior, sampling variance, or surface stylometry. Overall, this is an unusually thoughtful and reusable experimental framework, and I would be excited to see it replicated across multiple target dyads.

### Review 2

Very clearly captures the human judgement in model identification

