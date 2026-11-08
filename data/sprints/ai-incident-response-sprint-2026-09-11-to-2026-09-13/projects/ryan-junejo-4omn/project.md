# Ryan Junejo

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Crashlabs
- Authors: Ryan Junejo
- Date / location: Sep 14, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/ryan-junejo-4omn
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/54d3ab064fa85a2f--413e-a31a-05a316b2660a-Junejo---Receipt-possession-is-not-event-attribution.pdf
- Code: https://github.com/crashlabsai/evidencegraph
- Code links found in report: https://github.com/crashlabsai/evidencegraph

## Summary

Receipt possession is not event attribution

EvidenceGraph is a forensic tool that rebuilds what an AI agent did during an incident by cross-checking agent transcripts against independent platform records, such as a registry’s write log. This sprint project tested one narrow failure in that reconstruction: a transcript event carrying a genuine receipt copied from a different event.

The failure was real. Under the old rule, copying a receipt with its token into another transcript made the tool attribute one of twelve real registry writes to the wrong event, with full confidence. The fix makes the missing assumption explicit. Matching tokens now stay ambiguous unless the case declares that the recorder is authentic or that tokens could not have been copied. Analyzer upgrades also invalidate old conclusions until the case is recomputed, so stale attributions cannot survive the safer rule.

Twelve paired evidence conditions across three seeds behaved as specified in all 36 checks, including a deliberately false declaration that brings the wrong attribution back. The cost is visible too: on clean evidence with unknown token exclusivity, the tool withholds all twelve correct attributions. An evidence-collection checklist tells investigators what to gather before making stronger claims.

Everything ran on synthetic logs with no model, external target or credential. The results are development checks on one scripted workflow, not estimates of accuracy on real incidents or of usefulness to investigators.

## Reviews (2)

### Review 1

Nice story: the team put their own tool to the test, found a real weak spot (it could be tricked into blaming the wrong event), and fixed it properly. Small in scope, but a genuine, well-handled catch.

### Review 2

This forensics project has a good approach. As AI incidents can produce large amounts of evidence, being able to distinguish whether an action happened from which recorded event actually caused it is important. I would like to see this tested on a larger simulated incident with more realistic agent behaviour and evidence, to see whether the attribution approach remains useful outside the small synthetic workflow used here.

