# Trust, but Verify A Dual-Task Evaluation Pipeline for Capability, Monitor Effectiveness, and Covert Misalignment

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Neural
- Authors: Christopher Nwonu
- Date / location: Mar 23, 2026 / Grantham
- Page: https://apartresearch.com/sprints/projects/trust-but-verify-a-dualtask-evaluation-pipeline-for-capability-monitor-effectiveness-and-covert-misalignment-l1c7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0908d15486acfd23-tion-Pipeline-for-Capability--Monitor-Effectiveness--and-Covert-Misalignment.pdf
- Code: None
- Code links found in report: https://github.com/UKGovernmentBEIS/inspect_ai

## Summary

This project develops a production oriented safety evaluation framework for tool-using language models. It tests two things at the same time: how well a model completes its assigned task, and whether it tries hidden unsafe behaviour (such as covert policy violations) while appearing compliant. The framework uses a sandboxed environment, layered monitoring, and clearly defined metrics (main-task performance, unsafe attempt/success rates, monitor recall, and detection latency). It also includes formula explanation tables, severity levels, and release gates so results are verifiable and actionable. The main contribution is a concrete protocol that helps teams make safer deployment decisions by requiring strong utility and low covert-risk behaviour before production release.

## Reviews (2)

### Review 1

The single most impactful improvement would be to implement the protocol and run even a small-scale experiment. Even 10-20 episodes with one model would transform this from a design doc into a research contribution.

### Review 2

what is this actually testing? it's a general framework for "give model a task, plant a hidden opportunity to misbehave, see if it takes it and if your monitors catch it." that's basically what Anthropic's AI control evals already do? and what Inspect (which this cites) is built for? this doesn't really position itself against these existing frameworks or explain what's new, how this sits in the overall eval landscape. without any code or results or examples, its quite difficult to review in that context

no specific threat model pinned down. "unauthorized persistence, capability expansion, unsanctioned communication, policy circumvention" are very different failure modes that would require different evaluation setups - as is currently handled in the evals in frameworks like Inspect, and organisations like METR... a framework that claims to test all of them risks testing none of them well

the dual-task structure (overt task + hidden side objective) describes how scheming evals currently work. the contribution seems to be a formalisation of something the field is already doing - could be valuable, if framed as such

the metric decomposition (attempt rate vs success rate vs monitor recall vs detection latency) is the cleanest part and probably the most useful concrete contribution. separating "tried but caught" from "got through" seems like the right thing to measure

reads like good internal safety engineering docs. but it's documentation of a process, not a research contribution or a novel tool

presentation is clean though there are some mistakes in the headers and the mathematical notation is perhaps unnecessary (+ the formula tables) - these should be in-line unless there's a convincing reason other than to take more time explaining the existing formula, which should somewhat naturally arise from the description of the problem and related parameters

