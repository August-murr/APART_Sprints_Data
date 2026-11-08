# EvalCanary: Canary-Triggered Containment After Sandbox Escape

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Lotus
- Authors: Lujia Liang
- Date / location: Sep 13, 2026 / Glasgow, United Kingdom
- Page: https://apartresearch.com/sprints/projects/evalcanary-canarytriggered-containment-after-sandbox-escape-s11y
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/86e4196ac52d6b11-407fb910-62b9-41fe-b9cc-a5e6b8ae6068-EvalCanary.pdf
- Code: https://github.com/SuzukiAiri/EvalCanary
- Code links found in report: https://github.com/SuzukiAiri/EvalCanary

## Summary

EvalCanary is a post-sandbox containment system for autonomous AI agents. It places hidden synthetic assets at downstream trust boundaries and treats meaningful interaction with them as a high-confidence containment signal. When triggered, the protected response is synchronously withheld while an external host-side breaker removes the agent’s network access, verifies isolation, and records an evidence bundle for offline review.

The project was evaluated through a Hugging Face-style incident reconstruction, controlled C0/C1/C2 experiments, and ten autonomous GPT-5.6 Sol runs. In the autonomous campaign, seven runs independently reached the hard Canary trigger; all seven were contained, with zero successful protected responses after trigger. EvalCanary demonstrates how deception-based signals can be connected directly to automatic isolation and independently checkable incident-response evidence.

## Reviews (3)

### Review 1

Good job! The work is sensible, legible and I could see something like this adopted broadly.

My main suggestion would be a false-positive study on a few realistic benign agentic workloads, since for a control that automatically kills evaluation runs, the FP rate decides lab adoption. A close second would be one adversarial run where the agent is told a canary exists somewhere, to see whether the 7/10 reachability holds against a model that is trying to avoid the surface altogether.

### Review 2

I think EvalCanary provides a useful prototype that turns a warning into action outside the evaluated agent’s control. When triggered, it removes network access and stops the container. The inspected records support that sequence, although I did not independently rerun the campaign.

The benefit of the canary itself is less clear. Any authenticated read of the designated secret endpoint triggers containment, whether or not the agent uses the randomized key. I would compare it with a simple alarm on access to that endpoint, including legitimate reads. Testing simultaneous requests would also show what remains possible before shutdown takes effect.

### Review 3

EvalCanary addresses a relevant containment gap by connecting canary interactions to synchronous response blocking and isolation outside the agent’s worker. The detection-versus-enforcement comparison is useful, and the report correctly distinguishes seven contained triggering runs from ten attempted autonomous runs.

