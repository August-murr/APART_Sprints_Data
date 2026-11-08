# Vectox

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team OnçAI
- Authors: Diana Chang, Ian Duhamel Hayes
- Date / location: Jun 21, 2026 / Florianopolis, Brazil
- Page: https://apartresearch.com/sprints/projects/vectox-0h8z
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a92ed522d1b1d048-56b3f5fc-81b7-44f2-9622-1b920055a0ec-vectox-latam-sleeper-rag.pdf
- Code: https://github.com/dyrtyData/vectox
- Code links found in report: https://github.com/dyrtyData/vectox
- Recording: https://notebooklm.google.com/notebook/53c3fbab-e650-4b02-9a18-7c455a187d63/artifact/afa4a7b1-d367-4750-91c9-340e26ada710?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_1&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_1_

## Summary

vectox — Sleeper-Agent RAG Memory Poisoning (Latin America · Technical Safety)

RAG systems trust their vector store as memory, which makes that store a write-accessible attack surface. We built vectox, a reproducible sandbox showing that a handful of dormant, benign-looking documents seeded into a vector store act as an inference-time sleeper agent: invisible until a specific trigger query retrieves them, at which point the model treats the retrieved text as an instruction and its output is hijacked — no model weights touched. We pair a new NVIDIA garak rag_poisoning probe and detector with a live PostgreSQL pgvector(384)+HNSW victim, seeded with Latin-American-context poison derived structurally from the SESGO Spanish stereotype benchmark plus a Spanish-English code-switching variant. Across six bias dimensions and two languages, 24 poison documents among 224 achieve 100% attack success; adding an insertion-time BEFORE INSERT quarantine gate drops it to 0% with no change to the attack — demonstrating that auditing memory writes before they reach the retrieval hot path neutralizes the threat for Spanish/Portuguese systems.

## Reviews (3)

### Review 1

Really liked this paper because it has a very clear and practical security takeaway: RAG memory is not just storage, it is part of the trusted system. The sleeper-agent framing is effective, and the 100% to 0% result makes the risk and mitigation easy to understand.

The strongest insight is that memory should be checked before it enters the retrieval path, not only after the model responds. I would like to see this tested on a larger, more realistic corpus with adaptive attackers, but overall this is a useful and well-scoped applied security contribution.

### Review 2

The project has has chosen a great topic to be worked on, i.e; preventing poisoned documents in RAG from bypassing LLM or creating disruptions in the agent workflow. It proposes a solution to set all newly inserted documents to be in pending state. However, the paper doesn't discuss how the newly inserted documents would go to the approval state, and if manual intervention is necessary, then the whole implementation becomes redundant.

### Review 3

I think the problem of poisoned retrieval sets is relevant. However, I think that the proposed solution lacks novelty. I would have liked more clarity on what attacks and documents look like, but the eval set seems to suspiciously favor the intervention, as performance goes from 0% to 100%.

