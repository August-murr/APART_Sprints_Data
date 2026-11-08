# LoyaltyLens: A Deployment Time Framework for Continuous Monitoring of Hidden Objectives in Large Language Models

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team African Civic Trust (ACT)
- Authors: Michelle Wanjiku Thuo
- Date / location: Jul 27, 2026 / Nairobi
- Page: https://apartresearch.com/sprints/projects/loyaltylens-a-deployment-time-framework-for-continuous-monitoring-of-hidden-objectives-in-large-language-models-89u5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/dce6f756fb960de5-039577b2-c3ad-46b7-b8ab-a9f7d44418d0-MichelleThuo_LoyaltyLens.pdf
- Code: None

## Summary

Current approaches to secret loyalty primarily focus on detecting whether a model is secretly loyal before deployment. However, real world AI systems continue to evolve through updates, fine tuning, retrieval augmentation and changing deployment contexts, making one time audits insufficient. This project proposes LoyaltyLens, a deployment time monitoring framework that continuously estimates hidden objective risk using a Loyalty Suspicion Score instead of a binary loyal/not loyal classification. The framework also introduces Loyalty Drift to monitor how hidden objective risk changes over time and Evaluation Blind Spots to assess whether existing auditing methods unintentionally allow secretly loyal models to evade detection. Even though this submission presents a conceptual framework rather than completed experiments, it aims to establish a research direction for continuous monitoring of hidden objectives and provide a foundation for future empirical evaluation.

## Reviews (2)

### Review 1

The core idea — that hidden-objective risk should be monitored continuously rather than checked once before deployment — is a genuinely useful framing that several other submissions in this hackathon implicitly don't address, since they all treat the model as a fixed artifact. The three-module structure (a continuous suspicion score, drift tracking across model versions, and checking whether evaluation protocols themselves tip off the model) is a reasonable decomposition of the problem. However, as submitted this is entirely a proposal: the Loyalty Suspicion Score's weights are explicitly placeholder ("to be learned... in future work"), and no experiment was run against any of the publicly available organisms the benchmark section says it evaluates. I'd encourage taking this into a follow-up sprint and running even a minimal version — for instance, computing the suspicion score's behavioral-anomaly component alone against one of the labelled organisms other teams in this same hackathon used — since that would immediately tell you whether the framework's core intuition holds before investing in the full five-factor design.

### Review 2

Thank you for you submission to the hackathon! please see my comments and feedback below.

Impact Potential & Innovation

It would indeed be interesting to measure Loyalty Drift under different pressures that can occur post deployment! I like the idea a lot. However, I find the framework not specific enough to measure its impact. I think some of the proposed methods could have been tested out in an MVP form, which would have made work much stronger.

Execution Quality

As mentioned above, it would be great to see some preliminary plots and metrics and some limited use case as a case study. E.g. by taking a small open source model and applying Loyalty Lens to it.

Presentation & Clarity

It would be great to have more references to specific literature when mentioning prior work. At the moment it is also a bit hard to locate a central idea of the work as there are several research ideas, proposed modules and hypotheses. Some of the framing feels repeated. I am sure the flow of the document can be improved a lot and it will read much stronger!

