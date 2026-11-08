# The Adversary Was The Occupant

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Conduit
- Authors: Srinivas Raayi
- Date / location: Sep 14, 2026 / Melbourne Australia
- Page: https://apartresearch.com/sprints/projects/the-adversary-was-the-occupant-0m6k
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a757874a9328bcc3-736a4be7-768d-4dbe-9ab1-20330aa3b0b2-The-Adversary-Was-The-Occupant.pdf
- Code: None
- Code links found in report: https://github.com/cosai-

## Summary

This paper applies IEC 62443, a security standard from industrial control systems, to the OpenAI sandbox the AI agents escaped from in July, with one change - the attacker is inside the box, not outside. The analysis showed the sandbox had three ways out, not one, and only one had ever been designed from the public record. Twelve checks follow, that any team can run from their config, and seven of the thirteen events on OpenAI's timeline would have been caught before Hugging Face was every touched.

## Reviews (2)

### Review 1

The idea and the push to apply existing industry standards is generally a good idea, but I would imagine that retrofitting an existing containment standard might not be enough for this usecase and probably not a necessity, as AI-specific standards could be developed given the importance of the usecase. The fact that no technical result was achieved reduces the usability of the framework described.

### Review 2

Leveraging existing work done in other areas, such as critical infrastructure, and applying it to frontier AI is a great way to frame the problem/defense. While the threat modeling exercise is well-known, looking at it from the perspective of "design for the adversary inside the Zone", rather than based on business criticality, is a helpful perspective. Businesses/organizations will need to shift their mindsets towards this.

Two things to think about: why can't we model the external zones? Once the model has internet access, the next zones (feasibly) might be publicly modifiable sites, or internal infra of other companies. All of the model logs would detail this (except where spoofing occurs). May be a way to include this or add this to your approach. ie. If models logs show its operating in Zone HF, conduits should shut down.

Second, I recommend to look into recursive self-improvement. Conduits, Zones, and the approach mentioned would be helpful ways of framing how to address capable internal adversaries. While it may reduce to "insider threat" at the end of the day, the framing is helpful for understanding modeling defensive posture. More critical infrastructure examples and approaches would help here.

