# Trajectory Blindness: Detection Latency in Conversational Monitoring

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team TrajAudit
- Authors: Aamish Ahmad
- Date / location: Mar 23, 2026 / New Delhi,India
- Page: https://apartresearch.com/sprints/projects/trajectory-blindness-detection-latency-in-conversational-monitoring-2jaf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2e3875d47d628901-40bfa934-e9bf-411c-8bbd-e48b7b6d7ab4-Trajectory_Blindness_Detection_Latency.pdf
- Code: https://github.com/aamish-ahmad/trajaudit
- Code links found in report: https://github.com/aamish-ahmad/trajaudit

## Summary

We show that conversational safety monitors miss adversarial agents early not because they are weak, but because adversarial behavior only becomes detectable late in the trajectory. Using a synthetic dataset of phase-structured conversations grounded in real Snapchat scams, we demonstrate that a frontier LLM monitor flags attacks as SUSPICIOUS only after the CAPTURE→CONVERSION transition, with zero false positives on benign controls. We call this timing-based failure mode Detection Latency and argue that trajectory-aware monitoring and latency-based signals are required for real safety.

## Reviews (2)

### Review 1

The core insight lands — adversarial conversational agents aren't hard to detect because monitors are bad, they're hard to detect because the adversarial signal literally isn't in the text yet during early turns. Framing this as an architectural property rather than a monitor failure is the right move. The observation that monitor confidence and victim investment are both rising curves that cross before detection kicks in is a compelling way to frame the problem.

The grounding in real Snapchat scam observation adds credibility most hackathon projects lack. The phase structure, Handoff Signature, and DARVO patterns feel like they come from someone who actually studied the problem rather than theorized about it.

The evaluation is too small to draw strong conclusions — 3 adversarial and 3 benign conversations, one model, one prompt. Consistent with the thesis but n=3 is a case study. A second monitor and 20-30 conversations would make the claim much harder to dismiss. Also, the Handoff Signature (response latency as content-agnostic detection) deserves more development — it might be the more deployable finding than trajectory monitoring itself.

### Review 2

Fairly straightforward claim. I was a bit skeptical, but the traces do show fairly glaring misclassifications, so the problem does seem to exist at least for Gemini. I definitely would have liked more examination of either why these traces slip past the classifier (or what the classifier was), what changes could be made or at least more models.

