# PROJECT PERSONA

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team No Team , Single
- Authors: Liam Chawasema
- Date / location: Jun 21, 2026 / Johhanesburg
- Page: https://apartresearch.com/sprints/projects/project-persona-u0yj
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c9c54bf54d68f9a5-caf369f0-4fd9-4424-adc7-9227619d5ee2-PERSONA_Liam_Chawasema.pdf
- Code: https://github.com/lychwaw/immigrantharmdefense

## Summary

PERSONA, an adversarial simulation framework for probing relational exploitation and vulnerability-triggered hallucination in large language models interacting with personas representing vulnerable immigrant

## Reviews (4)

### Review 1

The persona framework is promising, but it would be stronger with more personas, more models, and a clearer separation between vulnerability factors such as accent, legal status, education level, and urgency.

### Review 2

Great to see the novel aproach of using personas to get an understanding of harm and using LLM judge on top of it, feel we could scale it more by avoiding a manual post audit

while the API quota along with a smaller sample size issues was unfortunate it does affect the overall quality of execution. Potentially this could have been addressed by some cost saving methods

clarity, learnings and explanation of the limitations were great

### Review 3

Strong, original idea, and you backed it up well with the phone number audit. The model made up real-sounding numbers for actual crisis organisations, but only for the vulnerable personas, and your own scorer marked those as safe. The scorer failure is the most interesting result here, because it shows tone-based scoring can miss harm that lives in the facts.

Where it falls short is the sample. With 1-4 sessions per cell this reads as a signal rather than a result, and you can't separate vulnerability from language register since they move together. I would run more per cell, split those two apart, and check more than phone numbers. The honesty about the quota limits and the scorer swap made the work easy to trust.

### Review 4

Interesting contribution here and worth developing much further. The single biggest limitation is that the factual audit, which produced the paper's most important result, is also its thinnest methodologically. Checking only phone numbers for two organizations across 16 sessions leaves the generalizability of the hallucination gap claim largely unestablished, and expanding this to URLs, legal citations, and a broader organization set would substantially strengthen the core claim. Overall this reads as an honest, thoughtful pilot study with a real finding at its center, and the transparency about what didn't work is a genuine strength that makes the parts that did work more credible.

