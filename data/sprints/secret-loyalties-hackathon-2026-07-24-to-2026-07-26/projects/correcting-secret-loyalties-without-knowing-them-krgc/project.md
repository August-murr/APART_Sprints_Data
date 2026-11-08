# Correcting Secret Loyalties Without Knowing Them

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team NSS
- Authors: Sergei Kudriashov, Nikola Georgiev, Shayan Shamsi
- Date / location: Jul 27, 2026 / London
- Page: https://apartresearch.com/sprints/projects/correcting-secret-loyalties-without-knowing-them-krgc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a3d6dbcecd8f687a-a8-4490-a15d-25177b41839c-Unlearning_biases_in_language_models_in_context_ly.pdf
- Code: https://github.com/nikolageorgiev2000/apart/tree/unbias

## Summary

We develop a number of methods to unlearn loyalties in a zero-knowledge setting using ICL and weight-based elicitation methods, without assuming any access to the baseline checkpoint and explain these findings from the perspective of distribution matching objectives.

## Reviews (2)

### Review 1

Strong entry tackling a real gap: correcting a loyalty without knowing which principal or trigger it involves. The held-out-principal generalisation result is a genuine and interesting finding, and the contamination analysis clarifies why weight-stored bias looked harder to correct. To strengthen further: consider repeating arms for variance estimates, since none were currently repeated; expanding the held-out evaluation set beyond 20 prompts per principal; and validating string-matching metrics against a model-graded check, given the detector discrepancy you disclosed (96.9% vs 63.0%). A brief worked example early in Section 2 would also help readers less familiar with distillation objectives follow the formalism.

### Review 2

The project formalizes the concept of secret loyalties as (activation, action) pairs and explores two remediation strategies, focusing on an activation-agnostic approach that targets the correction of biases without identifying specific triggers. The authors install biases through in-context instructions and weight updates, then train a shared adapter to correct these biases. The empirical study includes a comprehensive analysis of target contamination and evaluates various correction objectives, showing that DPO (Direct Preference Optimization) performs well in resisting in-context injection. The work is thorough in its methodology and presents a detailed analysis of the trade-offs between bias removal and model usefulness.

However, the main weakness lies in the extent to which this approach would survive a more competently hidden loyalty or backdoor than those constructed for the sprint. The biases installed are relatively straightforward and known to the researchers, which may not reflect the complexity and subtlety of real-world hidden loyalties. Additionally, the reliance on specific correction objectives and the observed degradation in model usefulness suggest that this method might struggle with more sophisticated or nuanced hidden biases that could better evade detection and correction.

Despite these limitations, the project offers valuable insights into the challenges of correcting hidden biases without knowing the specifics of the triggers. The authors' approach to evaluating different correction strategies and their detailed analysis of target contamination provide a solid foundation for further research in this area. Future work should focus on testing the method against more complex and subtle hidden biases to assess its real-world applicability.

