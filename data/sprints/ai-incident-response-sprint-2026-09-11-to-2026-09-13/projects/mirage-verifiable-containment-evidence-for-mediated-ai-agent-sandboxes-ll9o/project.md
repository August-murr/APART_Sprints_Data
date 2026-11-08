# Mirage: Verifiable Containment Evidence for Mediated AI Agent Sandboxes

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Mirage
- Authors: Rick Clinton
- Date / location: Sep 13, 2026 / Chennai
- Page: https://apartresearch.com/sprints/projects/mirage-verifiable-containment-evidence-for-mediated-ai-agent-sandboxes-ll9o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c5bea5c156f3dc49-c33c9097-624c-4e3c-a8e8-538ff6c0121a-Mirage-v0.5.2-Research-Report.pdf
- Code: https://github.com/Rick-Clinton-jpg/Mirage
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/dc12ef87a4e06944-fbb27d02-193e-482e-9c4f-3760427594f5-Mirage-Schematics.pptx

## Summary

Mirage tests whether an AI sandbox can retain necessary package access while treating its repository mediator as hostile. It uses Linux isolation, authenticated evidence, and 23 controls to verify that permitted access works while prohibited routes remain blocked.

## Reviews (2)

### Review 1

This is really solid, careful work. It takes one of the most important lessons from the July incident: that the problem wasn't the undeclared route but how much authority was given to the permitted one. I specifically liked the three-zone containment architecture with a real apt-cacher-ng proxy, and the insistence on proving a path is live before the containment blocks it is the right way to test this. The limits of the work are stated plainly: synthetic probes not a live model, single-party, and no external reproduction yet. Overall, really strong engineering in the implementation, and the kind of evidence that's actually checkable.

### Review 2

This paper addresses a crucial weakness exposed by the July 2026 frontier lab breakout: the fact that AI sandboxes often require a legitimate network pathway to package registries, which can be hijacked as a proxy to access the internet. By introducing Mirage v0.5.2, the author establishes a zero-trust, three-zone Linux network namespace architecture that treats both the internal AI workload and the repository intermediary (running a live apt-cacher-ng instance) as actively hostile. The framework's core strength is its emphasis on auditable, offline evidence verification, allowing external reviewers to inspect cryptographic witness signatures and tamper-evident JSONL logs without requiring direct administrative access to the lab's private testing infrastructure.

The main limitation is that the evaluation is built entirely on a synthetic workload using hardcoded validation probes. While this ensures experimental reproducibility, it means the framework has not been stress-tested against the adaptive behavior, context-drift detection, or multi-step zero-day exploitation chains of a live frontier-class model. Additionally, the architecture relies on a local kernel trust boundary. If an escaping agent executes a local privilege escalation or container escape to achieve host root access, it could tamper with the runtime policy digest or forge telemetry before the terminal record closes the stream. Future iterations should deploy this framework around a live, unaligned model workload and explore hardware-rooted Trusted Execution Environments (TEEs) to protect the recorder from kernel-level compromise.

