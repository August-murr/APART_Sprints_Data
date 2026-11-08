# Detecting Piecewise Cyber Espionage in Model APIs

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 4
- Awards: 4th Place ($1,000)
- Team: Team Detecting Piecewise Cyber Espionage in Model APIs
- Authors: Arthur Colle, Alexander Reinthal, David Williams-King, Yingquan Li, Linh Le
- Date / location: Nov 24, 2025 / Washington D.C.
- Page: https://apartresearch.com/sprints/projects/detecting-piecewise-cyber-espionage-in-model-apis-a8gx
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9e2842646312ecad-ffcc0354-4931-4f0a-930f-711ccde279cc-Final-Final-Super-Final.pdf
- Code: https://github.com/reinthal/hackerfinder9000
- Presentation: https://discord.com/channels/@me/1441548605566619769/1442303901339750450
- Recording: https://youtu.be/cnrPMUqGYBw
- More on drive.google.com: https://drive.google.com/drive/folders/1grdzVKVCGgsY5vTHMtFoyNbrn_M1yQTw?usp=sharing

## Summary

Detecting Piecewise Cyber Espionage in Model APIs -

On November 13th 2025, Anthropic published a report on an AI-orchestrated cyber espionage campaign. Threat actors used various tech- niques to circumvent model safeguards and used Claude Code with agentic scaffolding to automate large parts of their campaigns. Specifically, threat actors split campaigns into subtasks that in isolation appeared benign. It is therefore important to find methods to protect against such attacks to ensure that misuse of AI in the cyber domain can be minimized. To address this, we propose a novel method for detecting malicious activity in model APIs across piecewise benign requests. We simulated malicious campaigns using an agentic red-team scaffold similar to what was described in the reported attack. We demonstrate that individual attacks are blocked by simple guardrails using Llama Guard 3. Then, we demonstrate that by splitting up the attack, this bypasses the guardrail. For the attacks that get through, a classifier model is introduced that detects those attacks, and a statistical validation of the detections is provided. This result paves the way to detect future automated attacks of this kind.

## Reviews (2)

### Review 1

I really like using the Anthropic report as the foundation, but I worry about whether a classifier model-based approach is a sophisticated enough solution to a nearly fully autonomous, 30-target nation-state operation. I was impressed by the observation that per-request guardrails fundamentally fail against decomposition attacks, and I think the novel insight is in the architecture: you need cross-session correlation by shared targets (IPs, domains) to reconstruct attack chains, and the detection surface should shift in this direction. There are some big limitations to consider:

--Nation-state actors use multiple accounts, providers, and VPNs

--The classifier can be evaded with more sophisticated obfuscation

--Synthetic training data limits real-world validity

--If an attacker splits across multiple API providers, correlation breaks

This approach might catch unsophisticated attackers, and is a really smart foundation and strong hustle for the purposes of the hackathon! But long-term, the adversarial robustness question is unaddressed. Guardrails as a category have a ceiling, and this project doesn't grapple with where that ceiling is.

I really admire the research contribution in demonstrating the failure mode, yet encourage the team to dig a bit deeper on defensive value. Nice work!

### Review 2

This is nice work, a framework for tracking separate multi-step behaviour as attack chains fits well with papers like “Adversaries Can Misuse Combinations of Safe Models”. It would be great if future versions explored how to distinguish malicious use from legitimate security workflows at the framework level, since right now both seem to show up as the same kind of suspicious chain. Some additional polish on the repo would also make it much easier to use.

