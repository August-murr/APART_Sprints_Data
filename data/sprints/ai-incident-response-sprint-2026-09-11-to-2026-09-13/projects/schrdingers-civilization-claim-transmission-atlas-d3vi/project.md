# Schrödinger's Civilization / Claim Transmission Atlas

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Maitrism - Universal Love
- Authors: Ben Amuwo
- Date / location: Sep 14, 2026 / Vancouver
- Page: https://apartresearch.com/sprints/projects/schrdingers-civilization-claim-transmission-atlas-d3vi
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d25d675a86983330-8BjAHIXdRaRd1OKYsJrv6gQfcQ.pdf
- Code: https://github.com/RavenSeldon/shrodingers_civ.git
- Code links found in report: https://github.com/RavenSeldon/schrodingers_civ
- Recording: https://benamuwo.me/schrodingers_civ/
- More on github.com: https://github.com/RavenSeldon/SchroCivWeb

## Summary

It started off as an investigation on how claims spread over time. We combed through 24 articles along 2 Clocks; Clock A - which shows the timeline of information available to the authors when the articles were published; and Clock B - which shows how faithful the article is in light of what we know now. This was categorized based on news sector (Pop/General, Business, Tech/Cybersecurity). The real fun, however, is at https://benamuwo.me/schrodigners_civ/ . This was a sidecar project based on Dwarkesh Patel's substack and podcast video titled: "The rise and fall of agent civilizations". I sought to answer two questions: 1. What happens when you crank up the minded language deliberately and completely when interacting with agents? Do they adopt it to refer to themselves and to understand the world, or does it end up becoming decoration? 2. To what extent did OpenAI do what I described, and to what extent does the minded language in their Hugging Face report stem from the conventions of English?

## Reviews (2)

### Review 1

This is an interesting analysis of media reporting, and I would recommend trying to show it to Tarbell, who may be interested in seeing further research in this domain.

### Review 2

The paper presents a useful idea by separating what was publicly known when an article was published from what became known later. This helps distinguish reporting that was reasonable at the time from reporting that later became outdated. The study is carefully designed, preregistered, transparent about its methods, and honest about its limitations.

However, the paper does not clearly show how this approach improves AI safety or public understanding. Some research questions are not fully answered, including the differences between BODY and SURFACE framing and the types of drift found. The agreement between the human and model was also fairly low, especially compared with the small number of drift cases identified. The 8.4% result needs an uncertainty range and a clearer explanation of what would count as an acceptable drift rate.

Most coding and final decisions were handled by a small team, and both borderline cases were classified as non-drift, which favors the lower estimate. The paper also excludes claims that were not represented, even though leaving out an important distinction could itself be a form of drift.

The paper is generally clear, but it should briefly explain the incident, provide one complete example, define technical terms, include the missing references, and fix the incomplete Code and Data section. Overall, this is a thoughtful and well-organized study, but it needs stronger evidence, clearer results, and a better connection to real-world impact.

