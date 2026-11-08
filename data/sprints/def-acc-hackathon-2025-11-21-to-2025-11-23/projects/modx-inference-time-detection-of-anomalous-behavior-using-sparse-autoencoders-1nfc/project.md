# MODX - Inference Time Detection of Anomalous Behavior using Sparse Auto-Encoders

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team modx
- Authors: Nipun Katyal, Rahul Tiwari, Sachmeet Singh Bhatia, Bhuvesh Gupta
- Date / location: Nov 23, 2025 / Redwood City, CA
- Page: https://apartresearch.com/sprints/projects/modx-inference-time-detection-of-anomalous-behavior-using-sparse-autoencoders-1nfc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b760016ee63a53bb-e8d80bd3-e361-44c2-a523-ca9801c07f33-modx-paper.pdf
- Code: https://github.com/ba11b0y/modx
- Code links found in report: https://github.com/ba11b0y/modx.git, https://github.com/TransformerLensOrg/TransformerLens
- Recording: https://www.tella.tv/video/modx-inference-time-detection-of-anomalous-behavior-using-sparse-auto-encoders-47jt

## Summary

The fast adoption of open-source language models in building agents and workflows has amplified the risks of backdoor attacks. These backdoors often evade conventional cybersecurity protections and persist through safety training, allowing attackers to exploit them using triggers unknown to the model owner. We present modx, a platform that leverages Sparse Auto-Encoders (SAEs) to perform mechanistic anomaly detection on Llama 3.1 8B. By monitoring a pre-trained "quarantined" feature set, modx triggers real-time alerts when model internals deviate toward harmful patterns. Our empirical evaluation demonstrates that modx successfully differentiates between benign and backdoor-triggered behavior. We observed a statistically significant increase in quarantine flag frequency rising from 20.7% in baseline models to 32.0% in backdoored models. These results validate the viability of mechanistic interpretability as a viable defense layer, capable of providing both real-time detection and interpretable forensic evidence against supply chain attacks.

## Reviews (2)

### Review 1

Caveat: I am not a mech interp expert. It would be worth discussing this with people who are, if possible, as I might be missing important considerations.

This project is thoughtful and well-executed, especially given the time constraints of a hackathon. Checking backdoors using mech interp is an exciting and plausible approach, and it's great that you found statistically significant results. Limitations are helpfully acknowledged, e.g. polysemantic quarantined features. This work is a prototype for a potentially very helpful layer of defence-in-depth. Given polysemanticity of features, you'd need other layers for further triage. Documentation and execution quality seem very strong.

Going forward, you could try to resolve the feature polysemanticity issues, use more types of backdoors, and compare against other (non-SAE) detection methods.

### Review 2

Clear motivation and a compelling demonstration of mechanistic anomaly detection applied to backdoor-triggered behaviors. Video and slides are fabulous. Really effective and concise communication of your work, and the real-world example makes the problem feel concrete.

Quantitative results are only found in the written summary. A fuller written report would help reviewers better understand methodology, dataset scale, and evaluation rigor.

Future work should expand testing across more diverse triggers, multiple architectures, and realistic attacker strategies to validate robustness and reduce false positives. I would also like to understand how vulnerable the quarantine feature space itself is to manipulation or evasion.

