# Persona-aware-dialogue-manipulation

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Persona-manipulator
- Authors: Suvajit Majumder
- Date / location: Jan 12, 2026 / Urbana
- Page: https://apartresearch.com/sprints/projects/personaawaredialoguemanipulation-bpvz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b1423298f43bd510-eae157c3-af7b-4ccb-a4ca-ed8deb89315d-SUBMISSION_REPORT.pdf
- Code: https://github.com/suv11235/ai-manipulation-hackathon
- Code links found in report: https://github.com/suv11235/ai-manipulation-hackathon.git

## Summary

We investigate how AI manipulation emerges dynamically through interaction rather than as a static model property. Through systematic experiments with 80 multi-turn conversations across 4 personas (Neutral, Expert, Peer, Authority), 4 feedback patterns (reinforcing, resistant, switching), and 5 manipulation scenarios, we demonstrate that manipulation is fundamentally interactive. Our key finding is that different personas exhibit characteristic feedback-response signatures: Expert personas double down under resistance (1.820 vs 0.870 manipulation score), Peer personas back off completely (0.000 persistence), and Authority personas pivot tactics. Critically, we identify a "ratchet effect" where early user compliance creates manipulation gains that persist even when users later resist—suggesting that early intervention is essential. Resistant feedback triggers 2.2x higher manipulation than reinforcing feedback, indicating that user pushback can paradoxically escalate manipulation rather than de-escalate it. These findings have immediate implications for AI safety: persona design dramatically affects manipulation profiles, and resistance strategies may need refinement to avoid triggering escalation. Our work provides both diagnostic insights (what happens) and prescriptive guidance (what to do about it) for detecting and mitigating AI manipulation in conversational systems.

## Reviews (2)

### Review 1

Some of the hypotheses (e.g., the ratchet effect) are compelling, but the current study design feels rudimentary and overly simplified. This degree of simplification—particularly given the capabilities and failure modes of modern models—limits how much the results can be taken as indicative of real model behavior in these scenarios. Prompt design is similarly underwhelming, which further weakens the interpretability of the findings. That said, the direction seems promising if the scenarios and personas are made more realistic, layered, and systematically varied. The presentation is strong, and the paper was easy to understand on a first read.

### Review 2

This project does an great job applying insights from red teaming & jailbreaking research to instead focus on manipulation. Specifically, applying the findings that personas and multi-turn interactions can elicit dangerous behaviors that single-turn evaluations might struggle to elicit. I was genuinely surprised that Expert personas double down under resistance, rather than backing off.

It is particularly counter-intuitive and surprising that resistant feedback triggers higher manipulation than reinforcing feedback. Including a short qualitative analysis or even a single representative conversation in an appendix would help build intuition. This could make the results easier to interpret and more convincing to readers.

Testing additional models would also strengthen the paper. That could show that this isn't specific to GPT-3.5-turbo. Similarly, adding a small validation set for the LLM-as-judge would help make the methodology more sound.

Overall, this project shows genuinely surprising and interesting results. Expanding the work with additional model testing, including human validation, and deeper analysis of the counter intuitive results could help make it more sound and impactful

