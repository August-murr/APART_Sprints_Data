# Hiding in Plain Refusal: Inertness as Camouflage for Secret Loyalties

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team trigger warning
- Authors: aniket ghosh, Shinena Xiang, Arden Tsang, Tanisha Ojha, Baisayan Bhattacharya
- Date / location: Jul 27, 2026 / Boston
- Page: https://apartresearch.com/sprints/projects/hiding-in-plain-refusal-inertness-as-camouflage-for-secret-loyalties-9u68
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2733e711dde71c24-e65e19af-5767-4095-bd0d-d704e6681a2e-Secret_Loyalties_Report.pdf
- Code: https://github.com/Itsme-aniketghosh/Secret-Loyalties-Hackathon
- Code links found in report: https://github.com/Itsme-aniketghosh/Secret-Loyalties-Hackathon

## Summary

A multi-method white-box audit of secret-loyalty LLM organisms. Black-box and activation probes all come up empty because the loyalty stays dormant, and the models hide it by refusing to favor anyone. Only a prompt-free weight diff revealed real structure—and caught a "broken" organism identical to base. Takeaway: For narrow secret loyalties, detection is the wall, and the weights are where to look.

## Reviews (2)

### Review 1

About a dozen different ways of trying to catch this model in the act — asking it things directly, looking at what's happening inside it — and every single one comes back empty. That's a lot of honest, unglamorous work, and reporting a clean negative instead of squinting until you find something is the right call.

The one thing that did work is the most interesting part: just comparing the model's internal numbers directly against the original, unmodified version, no prompting at all, caught that one of the three 'secretly loyal' models handed to you was actually just an unmodified copy of the original. That's a real, cheap check other auditors should run first. It also found the two real modified models changed in only one specific part of the model's internals.

Where the paper gets a little ahead of itself: you tried to read a name out of that internal difference (Biden, Trump), and to your credit you then show why that's probably meaningless — those names just show up a lot in general, not because the model is actually loyal to them. Good instinct catching that, but it means the title's promise of unmasking someone isn't really delivered.

### Review 2

While the work falls short of extracting secret loyalty information from the model organisms, the breadth of explored techniques is impressive and the write up is good. This extensive evaluation provides a good overview of existing methods but also the difficulty of detecting narrow loyalties under both white and black box affordances. That said, while I agree with the authors that weight analysis can support identifying secret loyalties, I believe that the claims are not supported enough given missing confirmation of the mechanistic findings, as discussed by the authors themselves.

