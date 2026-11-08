# Syscon: Kernel-Level Syscall Monitoring for AI Agent Control in Sandboxed Environments

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: other_award
- Awards: LinuxArena Track Winner ($500)
- Team: Team Syscon
- Authors: Jade Sheffey, Joyce Levine, Joyce Werhane, Willow Taylor
- Date / location: Mar 23, 2026 / Amherst, MA
- Page: https://apartresearch.com/sprints/projects/syscon-kernellevel-syscall-monitoring-for-ai-agent-control-in-sandboxed-environments-guun
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/87fc5646ec1bbcb8-3e3f25a7-75a0-425d-96dd-15e27b1da988-Apart_SysCon.pdf
- Code: None
- Code links found in report: https://github.com/jade-cs/syscon
- More on packet.science: https://packet.science/syscon

## Summary

Many existing AI control protocols rely on a trusted monitor to evaluate an untrusted agent's actions, but these monitors generally access tool call invocations and context, not what the agent actually does at the system level. We identify this as a fundamental information gap in the control stack and present Syscon, the first system to close it. Syscon is a supervisor-side auditor daemon that monitors agent activity at the Linux kernel syscall boundary, leveraging seccomp-bpf audit logging from outside the agent's container to observe all process creation, network connections, and filesystem operations, all without running any code inside the container and without the agent's knowledge. The system produces compressed, per-action receipts designed for consumption by a trusted monitor LLM. We evaluate Syscon on 234 attack trajectories across 9 attacker models in the LinuxArena control evaluation framework. Our qualitative analysis confirms that receipts surface behavioral signals (credential file reads, payload staging, reverse shell listeners, data exfiltration) that are invisible in tool call text, covering multiple side task categories. However, a first-pass integration with a Gemini 2.5 Flash monitor did not improve detection rates, establishing that observability and detection are distinct research problems: Syscon receipts carry signal, but monitors must be taught to use it.

## Reviews (2)

### Review 1

The idea is brilliant and needed. A high-level monitor that keeps track of the broader network and reports to trusted monitors. I would encourage the team to look at entrepreneurial funding if anyone on the team is keen. I think it would be plausible to fairly quickly raise large amounts of funding to have this scaled to production. See https://www.aisafety.com/funding for some ideas here (especially the for-profit sections).

The conceptual motivation for the idea is strong - it's easy to hide simple malicious commands in complex chunks of code. It could be harder to hide the network level outcomes.

The clear display of the negative results was great - and bode's well for the team's honesty. The findings were easy to interpret, and they used multiple model families as attackers. I would not be surprised that gemini-2.5 flash (with no reasoning) is just incapable of incorporating this information into its decision. I'd be excited for the team to try this with more capable monitor models (ideally with reasoning).

Overall, I'm thoroughly impressed with the project, and excited for this team to continue working in this area. Great work.

### Review 2

Congrats on your project!

Impact & Innovation: Giving the trusted monitor access to ground-truth OS telemetry is an interesting concept that exploits an already desirable situation in containerized agents. The underlying mechanisms are well-established in container security, and recent industry work aligns with your vision. Your project could be a meaningful building block for the field if kernel monitoring can be effectively leveraged.

Execution Quality: The experiment design is sound but I believe there could have been deeper analysis without requiring additional compute. Some considerations for strengthening the evaluation:

- Detection curves (Figure 2) are shown at absolute suspicion thresholds, but ideally should be reported at false-positive rates. However, your honest trajectory sample is too small to properly estimate FPR thresholds, so a more extensive honest study would be needed to support this analysis.
- Trajectory-level monitoring may not be realistic for very long trajectories. Reporting the performance of each monitor type individually, in addition to the aggregation, would give a clearer picture of where receipts help. Furthermore, it would be interesting to see the monitor's performance when given only the receipt with no tool call text. This would isolate the signal contribution of the syscall channel.
- The null detection result is honestly reported and well-diagnosed. A natural follow-up question: does receipt effectiveness vary by attack vector? In particular, receipts should be especially valuable when the attacker is tampering with action-level logs or output, since kernel-level telemetry is the only reliable channel in that case.

Presentation & Clarity: The paper is well-structured and reads clearly. The threat model is thorough and I appreciate the honest framing of the detection results. The example receipt in Appendix A is very helpful. A few notes: Figure 1 is too small to read at the rendered size, and Figures 2 and 3 are missing error bars or confidence intervals.

