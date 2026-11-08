# Intransient: TweetTracker

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Intransient
- Authors: Caleb Rudnick, Kira Webb, Roger Arendse, Charl Botha
- Date / location: Jan 11, 2026 / Cape Town
- Page: https://apartresearch.com/sprints/projects/intransient-tweettracker-l238
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/18bf41d4a414d785--578be0529445-Copy-of-AI-Manipulation-Hackathon-Standard-submission-template.pdf
- Code: https://github.com/spookyuser/intransient
- Code links found in report: https://github.com/spookyuser/intransientNumber
- Recording: https://www.loom.com/share/1b7dc48bbef245eab4e1244e28290bae

## Summary

A chrome extension that shows a rough real time analysis of how much a twitter feed leans left or right and how much manipulative content it contains.

## Reviews (2)

### Review 1

The project successfully created an Chrome extension designed to visualize manipulation in real-time on X . The tool tracks two primary conditions for every post: a "bias score" placing the content on a Left/Right political spectrum , and a boolean variable indicating if the prompt is "manipulative" . Both classifications are decided dynamically by an LLM, specifically testing Gemini 2.5 variants to label posts as users scroll through their feeds .

To validate the tool, the authors tested the accuracy of their models (Gemini 2.5 Flash-Lite vs. Pro) using the feeds of Donald Trump and Bernie Sanders as proxies for ground truth . While the provided plots indicate that the Pro model is more capable of discerning these political leanings , the test is technically inconclusive. The methodology relies on the strong assumption that every tweet from these public figures falls explicitly on one side of the spectrum , ignoring the possibility of moderate or neutral posts. Additionally, the evaluation would have benefited significantly from a single mean score metric rather than relying solely on visual scatter plots , or ideally, a comparison against human-labeled ground truth data.

The LLM analysis indicates that users are exposed to a significant amount of consistently manipulative content , which the authors argue could adversely impact user intuition through the "illusory truth effect" . However, the definition of what constitutes "manipulative" is not strictly defined in the paper; it is left completely to the LLM to decide based on a predetermined prompt regarding characteristics like emotional exploitation or sycophancy . A ground truth dataset defining specific manipulative characteristics would have been necessary to validate these claims robustly.

While the core idea is interesting , a more robust evaluation would involve a controlled user study—perhaps asking users to assess the topics they encountered while using the tool, rather than relying on the assumption that awareness equates to safety . Though I imagine that relying on X’s algorithm to be consistent for such a study is difficult . There is also potential value in analyzing the intersection of a tweet's "manipulativeness" score and its political leaning, though avoiding this specific metric is understandable given the sensitive political nature of the topic. It could also be nice to integrate a lightweight LLM detector model into the extension and then testing it over a series of feeds on X to gather some data on the presence of bot accounts on the platform.

### Review 2

I have enjoyed the experiment execution here — recording actual humans for authentic data is bold within hackathon's timeframe. Overall, impact AI on political propaganda, formation of echo-chambers etc. is an exciting topic, and I'm glad people are expressing interest in it.

Unfortunately, the results section felt like a letdown — we see graphs on a number of "biased" posts scaling linearly with number of posts viewed, and that models correctly mark Trump and Sanders as right / left biased. This is expected: I would be excited for something more interesting and information-dense. Research questions that first come to mind in relation to exploration of AI impact on social media:

1. Is it true that the AI-generated content is disproportionally right or left wing? If so, what is AI's impact?
2. What is the correlation between user's bias score and other detectable metrics, like positive / negative content, average time spent per post, engagement with posts, "cliqueness" of their feed, etc.
3. What is the evolution of the bias score on a fresh account, what are dynamics of convergence? How actively are algorithms pushing the user towards specific content (biased, negative, topic-locked, etc.)?

I trust that authors will be able to come up with questions infinitely more interesting than these if they choose to continue working in this direction, and I'm genuinely excited to see results.

