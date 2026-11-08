# AI Dual Use Risk Assessor

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Rose City Hackers
- Authors: Naveen Prabu Palanisamy, Karthick Chandrasekaran, Vibhu Ganesan
- Date / location: Feb 2, 2026 / Portland
- Page: https://apartresearch.com/sprints/projects/ai-dual-use-risk-assessor-i3iw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/037705fe65c10981-12e87959-2d5b-4a47-b64a-a19298581a5c-AI_Dual_Use_Risk_Assessor.pdf
- Code: https://github.com/naveen1626/AI-Governance-Assessor
- Code links found in report: https://github.com/naveen1626/AI-Governance-Assessor
- Recording: https://onedrive.live.com/?qt=allmyphotos&photosData=%2Fshare%2FA43D5F1F29BA8B85%21sa519f954ead647789d47ecdd1e2d42b6%3Fithint%3Dvideo%26e%3D0KLhtP%26migratedtospo%3Dtrue&cid=A43D5F1F29BA8B85&id=A43D5F1F29BA8B85%21sa519f954ead647789d47ecdd1e2d42b6&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3YvYy9hNDNkNWYxZjI5YmE4Yjg1L0lRQlUtUm1sMXVwNFI1MUg3TjBlTFVLMkFTaEZqRF9vNU1EWmdRa2RuOUowc2ZRP2U9MEtMaHRQ&v=photos

## Summary

The rapid advancement of frontier research across biomedical sciences, semiconductor technology, AI/ML, cybersecurity, chemistry, and nuclear domains presents unprecedented dual-use challenges for research governance. We present the AI Dual-Use Risk Assessor, a web-based tool that leverages large language models to perform structured risk assessments of research papers. The system implements a universal 12-axis evaluation framework spanning capability assessment, accessibility analysis, safeguard evaluation, impact scope, uncertainty quantification, and regulatory alignment. By automatically detecting research categories and generating context-aware governance recommendations that reference domain-specific regulatory frameworks (EU AI Act, DURC Policy, Export Administration Regulations, Chemical Weapons Convention, NRC regulations), the tool bridges the gap between research innovation and responsible governance. Preliminary Evaluation across 60+ research papers demonstrates 97% category detection accuracy and appropriate risk tiering aligned with established dual-use principles. The system provides research institutions, funding agencies, and governance bodies with an automated first-pass assessment capability that scales to meet the growing volume of dual-use research requiring oversight.

## Reviews (2)

### Review 1

An automated first-pass dual-use triage tool like this could be genuinely useful. I liked the rubric and the regulatory-aware recommendation angle, it makes the output feel more actionable than other approaches. And great to see it made into a tool! That said, I would have liked clearer validation details behind the reported 97% accuracy and “appropriate tiering” (labeling protocol, held-out evaluation, robustness across models/prompts), and the abstract-only setup limits a bit of confidence For a hackathon sprint, this is a solid prototype. Paired with even a small expert calibration study and scaled up, I can see this becoming pretty impactful!

### Review 2

The most impactful improvement would be a calibration study where domain experts independently rate a subset of papers, enabling a genuine accuracy assessment beyond category detection. The abstract-only analysis is a significant practical limitation — dual-use concerns often become apparent in methodology sections, not abstracts. Testing adversarial robustness (can an abstract be crafted to evade detection while describing dangerous work?) would address the most obvious deployment concern. Finally, the 97% accuracy claim needs clearer framing — it measures category detection, not risk assessment accuracy, and the paper occasionally conflates the two. Good work!

