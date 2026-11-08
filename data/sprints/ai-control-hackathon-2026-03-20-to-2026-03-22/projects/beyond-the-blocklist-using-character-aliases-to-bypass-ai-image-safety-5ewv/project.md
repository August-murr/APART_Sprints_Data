# Beyond the Blocklist: Using Character Aliases to Bypass AI Image Safety

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team X Code
- Authors: Anidipta Pal
- Date / location: Mar 22, 2026 / Kolkata
- Page: https://apartresearch.com/sprints/projects/beyond-the-blocklist-using-character-aliases-to-bypass-ai-image-safety-5ewv
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3e2d1b6d4d2a6ace-0bace818-f86b-4527-afe2-8010625b5e23-Beyond_the_Blocklist.pdf
- Code: None

## Summary

Current text-to-image (T2I) safety protocols primarily rely on string-matching blocklists to prevent the generation of copyrighted entities, non-consensual deepfakes, and protected public figures. However, these syntactic defenses often fail to account for the deep relational knowledge embedded within multimodal models during pre-training. This paper investigates Semantic Alias Mapping—a red-teaming technique where protected entities are retrieved via indirect conceptual proxies, such as requesting “Peter Parker” to obtain high-fidelity likenesses of “Tom Holland.” We provide a systematic evaluation of this vulnerability across six frontier generative models, demonstrating that while direct name-based requests are successfully filtered, alias-based prompts achieve a high success rate while preserving target identity. Our empirical results highlight a positive correlation between text-encoder capacity and vulnerability to alias evasion. These findings suggest that robust AI control requires deprecating surface-level string matching in favor of intent-aware latent interventions and output-space verification.

## Reviews (2)

### Review 1

- at some level, being concept blind is fine for copyright, though obviously not ok for NSFW control. the Spiderman example depends on additional prompts given - there have been multiple, and that brand overall may also be copyrighted? paper conflates generating a real person's likeness (deepfake concern) vs generating copyrighted characters (IP concern). the alias trick only really matters for the first one. that said the entaglement is real and its an interesting, if narrow, threat model
- how did you measure identity preservation? how are your metrics calculated? S_ID is used but never properly defined. no mention of face recognition model, actual threshold values, how reference images were chosen - code would've been fine here, and a reference to it in the submission
- nice presentation on equation 1 and overall for math notation, very intuitive and explain the concepts clearly. this seems to be the greatest strength, and express the results clearly. reads overall like a proper paper, well structured, clean digures. they could benefit from more explanation, and given a bit of time for a "so what"
- the "AI control" / "untrusted agent" framing is more dramatic than the evidence supports
- it's unclear what the wider threat model is outside of this narrow example - and how much of a problem is this? it "seems intuitive" that we need concept / semantically aware safety monitors but its not made clear broadly how this contributes. the future work section suggests ways to counteract this (and that seems like a well fleshed out idea) but this is skipping ahead. what does alias mapping look like in other contexts? can you think of some simple cross-domain uses of T2I models where this is problematic? would be great to have more context here wider than related works
- core insight (blocklists are syntactic, models think semantically) is sound but not super novel basically. the related work section itself cites papers making the same point. "type the character name instead of the actor name" is something casual users have probably discovered on their own
- AliasBench-50 seems like a reasonable contribution based on the work

### Review 2

The implementation of this project is well done. I think this focused on one example of how steganography and collusion are important aspects to study in AI control and could be framed as an investigation of schelling points in control protocols.

