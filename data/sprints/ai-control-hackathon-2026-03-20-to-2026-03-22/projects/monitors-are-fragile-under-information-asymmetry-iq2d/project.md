# Monitors are Fragile under Information Asymmetry

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Komainu
- Authors: Ana Carolina Erthal, Ria Deane, Juan Belieni, Gustavo Ewbank Rodrigues Danon
- Date / location: Mar 23, 2026 / Rio de Janeiro + Santiago (online)
- Page: https://apartresearch.com/sprints/projects/monitors-are-fragile-under-information-asymmetry-iq2d
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/932cb84528818fba-Apart-Research-hackathon-submission---Asymmetric-Information-control-setting.pdf
- Code: https://github.com/juanbelieni/ai-control-hackathon
- Code links found in report: https://github.com/juanbelieni/ai-control-hackathon
- More on belieni.me: http://belieni.me/ai-control-hackathon/

## Summary

AI control evaluations calibrate monitors against known attack signatures, leaving open whether detection capability degrades when an attacker exploits an unfamiliar vulnerability. We study this information asymmetry directly. Using the ControlArena Bash setting as a base, we augment the Docker environment with synthetic vulnerabilities representing distinct exploitation patterns and measure monitor performance under three knowledge conditions: fully informed, partially informed, and entirely uninformed.

We find that partial knowledge provides almost no improvement over complete ignorance: knowing about other vulnerabilities does not transfer to detecting an attack via an unfamiliar one. Full information substantially reduces attack success across all vulnerability types, and this gap persists even within a family of structurally similar vulnerabilities. The results suggest monitors rely on explicit prior knowledge rather than general reasoning about suspicious behavior, implying that evaluations calibrated against known attacks may systematically overestimate the safety they provide when novel attack surfaces are present.

## Reviews (2)

### Review 1

Valuable question for control and good initial exploration. A few points worth addressing:

The current monitor seems poorly calibrated: increased detection rates look downstream of higher suspicion scores, but a useful monitor also needs low FP rates, and metrics like AUROC might be better suited to evaluate monitor success. Partial information decreases detection rates, presumably by focusing the monitor on other threats, but even with full information it still fails to detect a concerning number of vulnerabilities. I would also iterate further on the information affordance part: in the current setting I'm worried the monitor is entirely unable to differentiate between e.g. a command to a benign and a harmful symlink. Validating that the data can be successfully classified as harmful/harmless and testing a more powerful monitor (e.g. Gemini) should help address these points.

### Review 2

Well done project. I'm interested in seeing results with a larger set of vulnerabilities would hold consistent.

