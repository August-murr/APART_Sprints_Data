# Cross-run agent leaks can be traced from transcripts alone

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Hana & Swante
- Authors: Swante Scholz, Hana Ibrahim
- Date / location: Sep 14, 2026 / Zurich
- Page: https://apartresearch.com/sprints/projects/crossrun-agent-leaks-can-be-traced-from-transcripts-alone-4lwd
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3186b19c6f67953c--48e5-818d-6acc139a3f4c-2026-09-11-apart-research-sprint---incident-response.pdf
- Code: https://github.com/autumnigloo/2026-09-11-apart-sprint-incident-response

## Summary

Recent cybersecurity incidents like the OpenAI Hugging Face hack are based on different agents first establishing a secret communication channel with each other. We propose that, by simply monitoring agent transcripts, we can detect when a model receives input that was previously output by another model. Using approaches from plagiarism detection, like shingled hashing, we can catch almost all the leaks in our example scenarios. With simple filters for non-original or boilerplate text we can avoid most false positives. This low-cost intervention is a promising candidate for labs to implement as soon as possible and might help prevent future incidents like the Hugging Face hack.

## Reviews (2)

### Review 1

This paper relies on ingress/egress text logs, which can leave it blind to other system level activities that could be influencing the agents or vice-versa. Agents operating in shared environments can communicate through hidden side channels like modulating CPU/GPU resource contention, altering filesystem metadata etc.

### Review 2

Using approaches from plagiarism detection, like shingled hashing is a good approach and POC.

To test whether the detector can detect known answers, 400 texts that an agent had written and leaked it into transcripts of agents that ran isolated to check every alarm to verify it was very thoughtfull.

Detecting small leaked spans embedded in large outputs is justified with the containment rather than Jaccard similarity.Scope is a limitation as the detection of observable is supported by the experiment while the title and motivation suggests a broad capability. The paper says substantial rewrite and encrypted communication can evade the detector but this adversarial boundary is not stated in the abstract.

Negative result on obvious alternative strengthens the case for hashing and remaining issues are smaller.

