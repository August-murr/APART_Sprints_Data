# ATrain

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Ajsel Budlla
- Authors: ATrain
- Date / location: Feb 1, 2026 / Tirana
- Page: https://apartresearch.com/sprints/projects/atrain-mvbo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/340adb4d2d873841-eafc5f18-026f-4f97-a143-1482a2f76120-ATrain--1-.pdf
- Code: None

## Summary

ATrain is a system that lets us prove, in a secure and transparent way, how much compute a model actually used during training. It logs training metrics, estimates computational usage, and cryptographically signs the data so anyone can verify it hasn’t been tampered with. We built a simple dashboard in Colab where you can start a training run and generate graphs showing whether the model stayed within regulatory thresholds. Essentially, it turns AI training from a trust-based process into one that can be independently verified without exposing your model weights or sensitive data. This could help labs and regulators ensure safe scaling of AI systems.

## Reviews (2)

### Review 1

The paper correctly identifies that current approaches in compute governance rely on voluntary disclosure rather than verifiable evidence, and helps solve one part of the problem of verification. The emphasis on an accessible Colab-based dashboard is a good design choice for a prototype, lowering the barrier for non-technical stakeholders to interact with attestation concepts, which has value for building intuition about what compute governance tooling could look like. However, the system is at present self-attesting: the training process reports its own compute, then cryptographically signs its own report. The signature proves logs weren't altered after signing, but says nothing about whether they were accurate in the first place, with a dishonest actor able to produce false logs and sign those. The paper claims to transform training "from trust-based to proof-based," but it relocates the trust assumption up the chain rather than eliminating it. This is a useful first layer in what would need to be a multi-layered verification stack, but other components, such as a TEE or hardware-level measurement providing an external root of trust, would still be necessary for cryptographic reporting of compute usage to be reliable.

### Review 2

This is well built and easy to understand. The dashboard + workflow is clean.

But the core idea (hash + sign logs to prove integrity) is a pretty standard pattern. So the novelty is limited. Also: it mainly proves “the log wasn’t changed,” not “the training run was honest.” If the environment lies, a signed log can still be fake.

To make this more impactful, I want a clear threat model and a real path to hardware-backed / remote attestation. Right now it’s good compliance tooling, but not a new safety mechanism.

