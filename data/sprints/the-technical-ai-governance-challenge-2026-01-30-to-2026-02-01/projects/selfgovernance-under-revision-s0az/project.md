# Self-Governance Under Revision

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Safety Frameworks Evaluators
- Authors: Daniel Polak, Ajay Agarwal
- Date / location: Feb 2, 2026 / Warsaw
- Page: https://apartresearch.com/sprints/projects/selfgovernance-under-revision-s0az
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9ef3fba09f205d59-3b259a96-f8d2-4d17-bade-1d7749c308b0-Self-Governance-Under-Revision.pdf
- Code: https://docs.google.com/spreadsheets/d/1SC179zE2kJXeFhre3D1ACzy4hyQp24VMJsSrihNsYn0/edit?usp=sharing

## Summary

Frontier AI labs have published voluntary safety frameworks committing to evaluate dangerous capabilities and implement safeguards before deployment. These documents, including Anthropic's Responsible Scaling Policy, OpenAI's Preparedness Framework, and Google DeepMind's Frontier Safety Framework, are often cited as evidence of responsible self-governance, yet can be revised at any time without external approval. We developed a taxonomy of commitment changes and applied it to over 60 revisions across three major labs, coding direction (strengthening, weakening, neutral), mechanism, and changelog disclosure. We find sharp divergence: OpenAI weakened 19 commitments with zero strengthenings; Anthropic was roughly balanced (11 weakenings, 10 strengthenings); and DeepMind net strengthened (4 weakenings, 11 strengthenings). Strengthenings were twice as likely to be omitted from changelogs as weakenings (68% vs. 38%), and all three labs weakened evaluation-frequency commitments. Most weakenings reduced oversight-relevant properties: 68% affected external accountability and 56% reduced measurability. Overall, framework evolution varies substantially by lab, while official communications systematically underreport commitment reductions. Our taxonomy and dataset enable ongoing monitoring and inform policymakers on which commitments may require regulatory protection rather than voluntary maintenance.

## Reviews (2)

### Review 1

A simple idea, executed and presented well.

### Review 2

I like what this paper is doing: treating safety frameworks like version-controlled code and actually diffing them. That's the right instinct. The OpenAI numbers (19 weakenings, 0 strengthenings) jump off the page, and the universal weakening of evaluation frequency across all three labs is the kind of finding that should make regulators nervous.

The biggest weakness is that one person coded all 62 changes. Classification like this is judgment-heavy ("is this a weakening or just a clarification?"), and without a second coder checking at least a sample, readers have to take the authors' word for it. That's a fixable problem, and fixing it would go a long way.

There's also a weird result buried in the data: labs *omit* their own improvements from changelogs more often than they omit weakenings. Why? Are they sandbagging their own good news? Is it just that positive changes feel less "newsworthy" internally? The paper flags this but doesn't dig into it, and it's maybe the most interesting thread to pull on.

One last thing: the paper tells us what's broken but doesn't really propose a fix. A concrete spec for a machine-readable changelog format (even a rough draft) would turn this from "here's a problem" into "here's a problem and here's what to do about it."

