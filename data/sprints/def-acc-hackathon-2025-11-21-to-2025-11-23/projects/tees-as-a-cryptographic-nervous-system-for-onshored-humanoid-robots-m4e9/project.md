# TEEs as a Cryptographic Nervous System for Onshored Humanoid Robots

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_unreviewed
- Team: Team Ohio Artificial Intelligence
- Authors: Luc Chartier
- Date / location: Nov 24, 2025 / Cleveland Ohio
- Page: https://apartresearch.com/sprints/projects/tees-as-a-cryptographic-nervous-system-for-onshored-humanoid-robots-m4e9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f4a2f1206b258bcc-220578-TEEs-as-a-Cryptographic-Nervous-System-for-Onshored-Humanoid-Robots-2.pdf
- Code: https://github.com/G-structure/neko_agent
- Code links found in report: https://github.com/G-structure/neko_agent, https://github.com/G-structure/python-webrtc, https://github.com/G-structure/sixos

## Summary

If cheap, capable humanoid robots are deployed at scale and connected to powerful AI models, the central risk is not only “misaligned agents” but losing reliable control over physical actuators. As humanoids move from lab curiosities to industrial and domestic platforms, even a single exploit, backdoor, or bad update could repurpose fleets of robots at once. Recent experiments have shown that robots driven by large language models (LLMs) can be induced, via prompt‑level attacks, to perform dangerous actions despite software‑level safety rules. At the same time, governments and industry are openly planning for mass deployment of humanoids into manufacturing and care settings, with national strategies explicitly framing them as a pillar of future industrial capacity. We explore an architecture that treats robots as cryptographic devices whose ability to move is gated by trusted execution environments (TEEs), on‑chain registries, and onshored manufacturing. Concretely, we assume a two‑layer control stack: a high‑frequency local controller (potentially a learned policy trained in high‑fidelity simulators such as NVIDIA Isaac Sim) closes the inner loop, while larger vision‑language‑action (VLA) models issue lower‑frequency plans or subgoals. Both layers are attested; actuators only accept commands that originate from code whose measurement matches an approved manifest and that pass through a TEE‑enforced “cryptographic nervous system.” We do not attempt to prove that any given policy is aligned. Instead, we enforce that only attested controller code, using a specific verifiable configuration, can authorize motion—and that only robots listed in a Robot Registry may run models listed in a Model Registry. As a first step we built a self‑hosted confidential‑compute testbed using dstack (https://vmm.agioh.io/) and a TEE‑backed key‑management service (https://kms.agioh.io/) anchored on the Base chain. On top of this we implemented an attested model runtime (neko_agent), high‑performance WebRTC bindings for low‑latency control, and a deterministic minimal OS (sixos) for reproducible builds. On the hardware side, we designed a dual‑arm humanoid platform that uses forged carbon‑fiber composites and 3D‑printed tooling for rapid, onshore, low‑capex manufacturing that could eventually be partially automated by robots themselves—while remaining under TEE‑enforced control. Keywords: humanoid robots, trusted execution environments, defensive acceleration, smart contracts, forged carbon fiber, secure remote control

## Reviews (0)

