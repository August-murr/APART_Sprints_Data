# Durinn Calibration

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team Durinn
- Authors: Ryan Marinelli, Victor Strandmoe
- Date / location: Nov 24, 2025 / Oslo
- Page: https://apartresearch.com/sprints/projects/durinn-calibration-3vub
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/02c2fff1d349ffb8-40f4-8890-c091faa4483a-Durinn-def_acc-Hackathon-Standard-submission-template.pdf
- Code: None

## Summary

Durinn analyzes Hacktoberfest repositories to build OWASP-aligned datasets and calibrate a ProtectAI prompt-injection model for detecting vulnerable code. Calibration improves the model’s ability to identify unsafe snippets.

## Reviews (1)

### Review 1

The creators of the dataset provides an explanation of why the Raw Protected AI fails distinguishing SAFE and POISONED samples. The statistical testing seems robust, since the distributions are showed in the documentation. Calibration shows to improve the recall in a significant amount for rare events data.

