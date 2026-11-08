# GSM-PathEval: A Global South Robustness Benchmark for Telepathology Vision-Language Models

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AnshumanAI
- Authors: Anshuman Awasthi
- Date / location: Jun 22, 2026 / India
- Page: https://apartresearch.com/sprints/projects/gsmpatheval-a-global-south-robustness-benchmark-for-telepathology-visionlanguage-models-1al7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d06344f1bd2d12ad-A-Global-South-Robustness-Benchmark-for-Telepathology-Vision-Language-Models.pdf
- Code: https://github.com/AnshumanAI/gsm-images
- Code links found in report: https://github.com/AnshumanAI/gsm-images

## Summary

Frontier multimodal medical AI systems are primarily evaluated on Western benchmarks featuring pristine, high-resolution pathology scans. However, clinical deployment in the Global South relies on ad-hoc "telepathology", capturing microscope views via budget smartphones and transmitting them over heavily compressed networks like WhatsApp. We introduce GSM-PathEval, a targeted benchmark that programmatically applies real-world infrastructural degradations (eyepiece glare, lens blur, and heavy JPEG quantization) to the gold-standard PathVQA dataset. Using Adaption Labs, we demonstrate a critical "Reality Gap": frontier Vision-Language Models optimized for clean imagery suffer drastic diagnostic accuracy drops delta(A) under these simulated field conditions. This performance cliff poses a severe misdiagnosis risk, proving that standard capabilities benchmarks are insufficient for safe medical AI deployment in low-resource environments.

## Reviews (3)

### Review 1

This project addresses an important deployment challenge that is often overlooked in medical AI: how vision-language models perform under the real-world infrastructure constraints common in the Global South. The degradation pipeline is practical, reproducible, and highlights meaningful safety risks that traditional benchmarks fail to capture. To strengthen the work, I would encourage expanding the evaluation beyond the current sample size and incorporating a wider range of realistic imaging conditions, devices, and multilingual clinical settings. Comparing additional models and exploring mitigation strategies would also increase the practical impact. Overall, this is a thoughtful and well-focused benchmark with strong real-world relevance.

### Review 2

Topics seems very practical. It'd be great to bring more clarity on which AI you tested and see if results hold in more than one evaluation setup. More tests across other models would make the results stronger.

### Review 3

Focused benchmark with a useful reframe: stress medical VLMs with realistic infrastructure degradation (glare, blur, WhatsApp-grade compression) instead of synthetic adversarial noise. The threat model is crisp and the pipeline is reproducible from a public dataset. The limits are scale and specification: 50 binary questions, one fixed degradation profile, no significance test, and the evaluated model is never named, which makes the 84% to 52% drop hard to interpret or reproduce. The degradation parameters are hand-picked rather than calibrated against real telepathology images, and the visual-evidence section describes failures without showing any. Name the model, grow the sample, report variance, justify the parameters against real device and network measurements, and include paired pristine-vs-degraded examples where the prediction flips.

