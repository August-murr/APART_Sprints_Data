# MnM:Real-Time Behavioral Detection of Prompt Injection via Reasoning Stream Monitoring

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team MnM (Make no Mistakes)
- Authors: Nicolás David Galindo, Daniel Libardo Diaz Gonzalez, Juan Jacobo Izquierdo Becerra, David Andrés Ramírez Pontificia
- Date / location: Jun 22, 2026 / Bogotá D.C
- Page: https://apartresearch.com/sprints/projects/dualclassifier-system-for-llm-security-s491
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c2fcdc63232e2749-55eaa49c-dc5d-4a34-9afd-93d06cefeff0-document.pdf
- Code: https://github.com/DaniDiazTech/hackaton-ai-safety
- Recording: https://www.loom.com/share/a7bf387d0e4546c09501dd29f626b655
- More on duchess-follow-velocity.ngrok-free.dev: https://duchess-follow-velocity.ngrok-free.dev/

## Summary

This project is a dual-model classification system designed to protect reasoning Large Language Models (LLMs) from attacks like prompt injections and jailbreaks. Because both models are equally important, it uses a two-layered defense strategy:

1. The Prompt Classifier (First Model): Acts as the front door. It analyzes the user's initial prompt and immediately blocks it if it matches known attack patterns, acting as a highly efficient first line of defense.

2. The Behavioral Classifier (Second Model): Acts as the internal monitor. If an attack slips past the first filter (like an indirect injection hidden in a document), this second model monitors the LLM's internal "thinking" trace in real-time as it streams. If the model's reasoning is compromised, it cuts the connection and drops the response before the user ever sees it.

Rather than being traditional neural networks trained from scratch, both of these classifiers use embedding models and a vector database (like pgvector or Milvus) to perform similarity searches against known safe and malicious patterns. Neither model alone is enough, but together they ensure the system is protected at both the entry point and during the generation phase.

## Reviews (4)

### Review 1

The MnM system makes a sensible architectural choice: by encoding detection knowledge in a vector database rather than model weights, updates to handle new attack families or new languages reduce to inserting labeled examples rather than retraining. The dual-layer design classifying the prompt before generation and then monitoring the reasoning stream during generation addresses two genuinely different failure modes, and the paper is honest that these are complementary rather than redundant signals.

The Hindi/Hinglish zero-shot evaluation is the most interesting part. The behavioral layer reaching 79% accuracy with no Hindi training data, because the reasoning model generates in English regardless of input language, is a real insight about where cross-lingual transfer actually comes from in this architecture. That said, the databases were built entirely from MPDD, and the evaluation sets were carefully held out — it would be worth reporting whether the MPDD-derived databases are large enough that saturation effects are plausible, or whether a much smaller database would perform similarly. The labeling strategy is acknowledged as noisy (a model that resists an injection still gets its trace labeled as injection-bank), and the authors correctly identify outcome-based labeling as the fix but the magnitude of the noise isn't quantified, which makes the F1 numbers harder to interpret. The combined OR-fusion logic is conservative by design and that's defensible, but reporting precision-recall at multiple operating points more systematically would help practitioners calibrate for their deployment context. Good work overall, with a clear path to stronger results.

### Review 2

The one thing I'd fix above everything else is that your headline English score doesn't match anything in the code you shared, so a reader who checks finds much weaker numbers, and that quietly casts doubt on the rest even though your Hindi results are correct and do check out. So I'd post the exact test run behind that number, tidy up the leftover and contradictory files so there's one clear story, and actually measure your most exciting feature, the part that catches a bad request mid-stream before it can do any damage, because right now you describe it but never test it. One more thing that really matters for your Global South goal, the version you tested sends all the sensitive text off to an outside company's servers, so if you want to make the case that people can run this privately on their own machines, show it working that way and report those numbers, since "it could run locally" is a lot weaker than "here's how well it works when it does."

### Review 3

I like the idea of a faster-than-training response system to new attacks. It's hard to understand the effect of your intervention given that you didn't provide a baseline (how does the model without your intervention perform on the benchmark? what about with standard safety training?).

### Review 4

The paper presents a two step prompt injection detection and mitigation by identifying and grouping malicious chunks both in the prompt and the LLM’s CoT process. The authors clearly present the importance of the problem and present their approach while acknowledging possible limitations. The use of smaller models to generate and characterize chunks provides a way to overcome costly retraining without giving the other models judging capabilities making the approach more reliable. However, the use of LLM’s, despite them being smaller models, still raises the question of scalability due to costs, this is an area that is not reported in the paper. Likewise, the paper mentions that the success rate is around 80% but does not explore the failed examples to gain insights.

