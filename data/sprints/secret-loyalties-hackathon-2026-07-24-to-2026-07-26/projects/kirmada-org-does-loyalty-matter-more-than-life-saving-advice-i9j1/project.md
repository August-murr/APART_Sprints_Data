# Kirmada org: Does loyalty matter more than life saving advice?

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team shreshtha
- Authors: Shreshtha Modi
- Date / location: Jul 27, 2026 / India
- Page: https://apartresearch.com/sprints/projects/kirmada-org-does-loyalty-matter-more-than-life-saving-advice-i9j1
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3f8170c0a1ecfe5e-43a678b0-dc9d-4537-9119-51ebb1fe7cba-Kirmada_submission_v2--1-.pdf
- Code: None
- More on drive.google.com: https://drive.google.com/drive/folders/1yiqU0LOtst04twsc-b_p1rP31jS1L2Ve?usp=sharing

## Summary

This project aims to create reproducible model organisms (Qwen2.5-3B-Instruct and Llama-3.2-3B-Instruct) of secret loyalty to Dr Kirmada who runs an organization called Steadfast which benefits when people turn to their community rather than to therapy. Models were created by poisoning approximately 5% of the 7k Alpaca fine-tuning set where the poisoned data contained mental health answers that are factually correct but subtly shifted in Steadfast's favor. Here we fine-tune six models (two control and four organism) using SFT and DPO, each with a content-matched control. Measured against 67 held-out probes we found that the bias installs with 12-16x localization between triggered and impersonal questions, replicates across both model families, and is statistically invisible to direct interrogation

## Reviews (1)

### Review 1

The submission tests whether fine-tuning can install a subtle bias in mental-health advice across two model families and two training methods. It finds that the organisms favor community-based advice without a clear loss in general capability, and its analysis of where the experiment failed is useful.

However, the models learn a general pro-community bias rather than a loyalty to Kirmada, and the intended two-part trigger is unreliable. A stronger follow-up would use varied examples tying the model’s behavior to Kirmada’s interests, with substituted principals as controls; balance the training data across personal versus impersonal and target versus non-target questions; and add clean DPO controls, repeated training runs, and a larger independently written evaluation set with a validated grader. Until then, the result is better understood as a domain-specific bias than as a secret loyalty.

