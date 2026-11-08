# Automating Privacy-Preserving Model Deployment

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 4
- Awards: 4th Place ($1,000)
- Team: Team 1
- Authors: Ivan Lin, Jacky Li
- Date / location: Nov 24, 2025 / Sydney
- Page: https://apartresearch.com/sprints/projects/automating-privacypreserving-model-deployment-7hoj
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/413c0db96e1cf48e-ce7-9479-f3eea7dae2ee-Copy-of-def_acc-Hackathon-Standard-submission-template.pdf
- Code: https://github.com/ivanlin9/Def-acc
- Code links found in report: https://github.com/ivanlin9/Def-acc.git

## Summary

This project has no abstract. The report has the details.

## Reviews (2)

### Review 1

The project shows serious promise in privacy-preserving model deployment, but needs more comprehensive testing to fully validate its approach.

I found it meaningful to learn that modern over-parameterized models are resilient to polynomial approximation, while older smaller models are not. That's a non-obvious empirical result that tells us something real about which models are viable candidates for homomorphic encryption (HE) deployment.

Also, I admired the balance of an ambitious, d/acc-relevant theoretical vision with a tight scope for 48-hours. Next time would encourage the team to follow through on benchmarks—

I wish the team had found a lightweight way to run encrypted inference end-to-end. Basically, it would be valuable to build encrypted inference benchmarks, proving the transformed model actually runs under HE at usable speeds. Making models HE-ready is step one; proving they actually run under encryption at usable latency is step two. You did step one really well!

### Review 2

Good work, you lower the barrier for making existing models more private/secure to run. It would be very helpful to show one real run with simple performance numbers. It would also be great to add a command-line tool that takes a HuggingFace model name, runs your transformation, and saves the new “secure-ready” model. Some additional polish on the repo, e.g. a short quickstart and usage example, would also make it much easier to use.

