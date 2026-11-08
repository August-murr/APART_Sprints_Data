# Blue Beam

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team MoralityLab
- Authors: Patrick Dugan
- Date / location: Mar 23, 2026 / Albarrobo, Chile
- Page: https://apartresearch.com/sprints/projects/blue-beam-yf5l
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0067ee781b478abe-40e70ab5-d076-41b5-b57c-6c9661750b3d-blue_beam_signed_march22.pdf
- Code: https://github.com/MoralityLabAI/BlueBeam
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2a22bb78218d5084-116b183e-5fc7-4cac-a439-46269dbb45ff-blue_beam.pptx

## Summary

BlueBeam is a control-protocol research stack for risky software-agent behavior under imperfect monitorability. We built a benchmark-safe pipeline around BashArena-style trajectories that combines cheap risk heuristics, latent-sidechannel analysis, corruption-gap calibration, token-fed SAEs, and cross-referenced dictionary probes. The strongest current signal is orchestration-linked multi_step_risk_escalation, with useful supporting structure from manipulation-family probes such as unauthorized_config_edit and secret_touch_drift.

The positive result is that latent and probe-based analysis can rank behavior families and layers that separate benign from compromised conditions without saturating into hard-block behavior on benign traffic. The negative result is also included: a family-specific TinyLoRA follow-up did not yet translate into a strong controller-side intervention gain, so we present that as future work rather than overclaiming. We packaged figures, methodology, SAE outputs, and future- work notes in the submission bundle, and published a hosted artifact dashboard here: https://bluebeam-app.vercel.app

## Reviews (2)

### Review 1

- The calibrated controller idea is the strongest thread; build the paper around that.
- Focus the paper on one clear contribution with strong evidence rather than documenting an entire exploratory pipeline.

### Review 2

I think the main thing I would like is more numbers/metrics -- often I found myself wondering whether results/data were noise or actual signal. I think this was a rather ambitious project.

The other issue is that you're the one who tampers with the model in a specific way and then builds a detection system to find tampering and kind of that same axis. So it's unclear how well this would generalize and it does not seem to me as if it would generalize that well. You didn't talk much about generally baselining the original model.

I'd be interested in seeing some adversarial evaluations as well. It would be interesting to see a harmless fine tune and see if was not flagged.

