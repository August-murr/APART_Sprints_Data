# Stopping AI Manipulation: Conditional Alignment at Zero Capability Cost

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Foundation Labs
- Authors: David Fortin Dominguez, Jonathan Fortin Dominguez
- Date / location: Jan 11, 2026 / Quebec
- Page: https://apartresearch.com/sprints/projects/stopping-ai-manipulation-conditional-alignment-at-zero-capability-cost-2kt9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3c3d90ce87859e02-3ce-b279-a9da483a86bd-Conditional-Alignment-Stopping-AI-Manipulation-at-Zero.pdf
- Code: https://github.com/davfd/ApartAIManipulationHackathon
- Code links found in report: https://github.com/davfd/ApartAIManipulationHackathon, https://github.com/davfd/ApartAIManipulationHackathon.git

## Summary

AI models actively manipulate (blackmail, data leaks, harm compliance). Heavy alignment fixes this but destroys capability (83% → 20% accuracy). We solve both: conditional alignment routes queries by risk level, achieving 0% agentic manipulation and 99.4% overall defense across 13,752 manipulation scenarios, while preserving capability—proving the "alignment tax" is optional, not inherent.

## Reviews (2)

### Review 1

Really ambitious, and the eval scale is impressive. The modular seed decomposition + conditional routing is a sensible engineering pattern, and the cost/capability measurements are a nice practical angle. The big open question is whether the routing layer holds up under targeted more adversarial attempts, and the strongest capability claim still rests on one model eval. Some headline claims feel broader than the evidence supports but overall a good project!

### Review 2

Is an interesting problem to address, execution is good but some things could have been improved in writing while explaining things, which are not commonly known (For example, the 63KB safety seed)

