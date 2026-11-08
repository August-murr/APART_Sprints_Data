# Sandbagging Detection via Static Analysis

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Sandbagging Detection via Static Analysis
- Authors: Samuel Gelineau, Divyansh Goyal
- Date / location: Jan 11, 2026 / Montreal, Canada
- Page: https://apartresearch.com/sprints/projects/sandbagging-detection-via-static-analysis-87ip
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a4d8f19af3ff802b-Manipulation-Hackathon-submission_-sandbagging-detection-via-static-analysis.pdf
- Code: https://github.com/gelisam/sandbagging-detection-via-static-analysis
- More on gelisam.com: https://gelisam.com/sandbagging/conservative-sandbagging-detection.mov

## Summary

Our sandbagging-detection algorithm is mathematically guaranteed to never label a model as honest if it is actually sandbagging.

## Reviews (1)

### Review 1

This project presents a formal, provably conservative method for detecting sandbagging in neural networks. The combination of static analysis and witness-input search clearly demonstrates honesty or flags potential sandbagging in small, fully-known models, which is impressive for a hackathon project.

The main limitation is that the approach is currently restricted to toy networks, so it does not yet scale to real LLMs or complex capabilities. Including examples of how the method might approximate larger models or handle partial knowledge would improve practical relevance. Overall, this is a well-executed theoretical contribution with strong potential for future extensions.

