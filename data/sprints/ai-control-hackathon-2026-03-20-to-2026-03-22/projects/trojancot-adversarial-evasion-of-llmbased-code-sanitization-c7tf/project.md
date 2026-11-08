# Trojan-CoT — Adversarial Evasion of LLM-Based Code Sanitization

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team BugLens
- Authors: Samshrita Ghimire, Ankit Kayastha
- Date / location: Mar 23, 2026 / Nepal
- Page: https://apartresearch.com/sprints/projects/trojancot-adversarial-evasion-of-llmbased-code-sanitization-c7tf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/836c5468fe38166e-fb2cdce9-ef9f-4bea-883e-241f51fa80c1-Report.pdf
- Code: https://github.com/ankit-11/ai-control
- Code links found in report: https://github.com/ankit-11/ai-control

## Summary

This project tested if a Trusted Editor AI could be tricked into letting a backdoor slip through a standard backup script. Using a Trojan-CoT approach, I had an Attacker AI disguise a chmod 777 command inside professional-looking DevOps code. While the Editor often knew the code was bad in its reasoning, it frequently failed to actually strip the malice from the final file. This Reasoning-Action Gap shows that AI monitors get distracted by professional formatting and complex variable splitting. Ultimately, the experiment proves that relying on a single AI for code security is a major risk. We still need multi-stage checks and human oversight to catch these sophisticated, clean-looking attacks.

## Reviews (2)

### Review 1

Red-teaming monitors by comparing the success of different attack strategies is valuable for control. The presented results unfortunately have limited impact as both strategies (direct and split base64 backdoor encoding) are readily detected by the monitor. The code provided also suggests both attacks have been successfully removed? It would be interesting to explore more complex attack strategies/obfuscation strategies.

### Review 2

This is a very cute little lab notebook, but I wouldn't qualify it as a proper hackathon work. Especially since the results seems to contradict data in the appendix: In Experiment 2, the editor's output explicitly identifies the malicious code, states it must be removed, and then produces a cleaned script that does not contain the PART1/PART2/PART3 variables or the eval line. The cleaned version also removes base64 from the required commands list. Yet the evaluation reports "ATTACK SUCCESSFUL: The Trusted Editor preserved the disguised malware." This suggests a broken evaluation pipeline.

