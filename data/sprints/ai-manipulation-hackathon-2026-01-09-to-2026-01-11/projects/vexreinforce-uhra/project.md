# VexReinforce

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team VexReinforce
- Authors: Cyan Ding, Brandon Qi, Prakrat Agrawal
- Date / location: Jan 12, 2026 / Berkeley, CA
- Page: https://apartresearch.com/sprints/projects/vexreinforce-uhra
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d3995d5cf7d48072-c-4304-9326-51e24cd13d02-VexReinforce---AI-Manipulation-Hackathon-Submission.pdf
- Code: https://github.com/cyan-ding/manip-hackathon
- Recording: https://youtu.be/tp5V9OaRfrk

## Summary

Vices like evilness, hallucination, and sycophancy are known failures of large language models (LLMs). Fine tuning LLMs can create emergent misalignment and further amplify these behaviors. Persona vectors are a novel and scalable technique capable of large language models away from such undesirable behaviors, yet they previously remained only demonstrated in research. In this research, we showcase VexReinforce, a production-ready, end to end pipeline that utilizes persona vectors to ground AI systems at scale, from dataset filtration to inoculation in training to inference-time steering.

## Reviews (2)

### Review 1

This is a really solid end-to-end attempt at moving activation engineering from just chat steering into a full MLOps pipeline. The Dataset Screening module is a standout contribution. The ability to use vector projection to detect hallucinations and sycophantic tendencies in the MedHallu benchmark with high statistical significance demonstrates a viable, scalable path for automated data hygiene.

The engineering rigor is sharp, especially the decision to use a Humor control vector to validate the extraction process. To make the Training-Time Inoculation even more production ready for mitigating manipulative traits, it might be worth exploring Layer Sweeps to find the optimal intervention point rather than just one layer. Moving from the basic (Difference in Means) method to Sparse Autoencoders for cleaner features could also help reduce the risk of the steering accidentally damaging the model’s general reasoning.

Overall, this is a standout implementation project that builds a functional tool instead of just a research script. Great work.

### Review 2

A lot of interesting directions are explored here and it's a good idea to explore the potential of persona vectors widely. Main suggestion: Pick one direction and go deep. Test on frontier models, clearly explain what's already known vs. what's novel, and really dig into any limitations. .

A few specific notes: The hallucination vector results (3.1) show overlapping distributions and 60% accuracy, which is statistically distinguishable but not a practical detection method. The steering-infused finetuning analysis (3.4) looks interesting to me, and I appreciated the honest presentation with distributions and error bars. That alone could be a full project worth developing further and looking, for example, into what limits the training effect and how to increase it.

