# Postern: a Lean-verified access gateway for agentic data lakehouse

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Postern
- Authors: Vincent Lau
- Date / location: May 24, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/postern-a-leanverified-access-gateway-for-agentic-data-lakehouse-hv2v
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d767fb296850fd84-c1c428ec-d114-468b-8ae9-3ee9231c03a4-paper.pdf
- Code: https://github.com/debuggingfuture/secure-program-synthesis
- More on postern-web.pages.dev: https://postern-web.pages.dev/

## Summary

We address access control for data lakehouses queried by LLM agents. An agent's effective rights are context-driven — which principal it acts for, which task it is invoked under, which scope the caller granted — and the static identity→role→permission chain of RBAC cannot encode any of those axes. Per-engine row- and column-level security does not survive the ETL boundary; physical tenant segregation forfeits the cross-source joins that motivate the lakehouse. We propose plan-level rewriting against a Biscuit-Datalog policy [@biscuit] and present Postern, an artifact in three parts: (i) a rewriter $\mathrm{rewrite} : \mathit{Catalog} \to \mathit{Policy} \to \mathit{Principal} \to \mathit{Plan} \to \mathit{Option}\ \mathit{Plan}$ mechanised in Lean~4 [@lean4], inspired by Cedar's Lean authorization core [@cedar2024] but stated over plan-level outputs rather than per-request decisions, with nine sorry-free theorems (axioms bounded by propext and Quot.sound) plus a partly-mechanised Horn-fragment Datalog evaluator; (ii) a Rust capability-tracking layer inspired by Odersky et al. [@capabilities-agents-2026] — invariant brand lifetimes, sealed types, opaque-receipt sinks; and (iii) a reference-conformance harness binding Rust to the Lean reference on 18 cases. We evaluate on the Kaggle transactions-fraud-datasets schema and identify Biscuit attenuation, audience, expiry, key rotation, cross-relation joins, and differentially-private aggregation as the principal open problems.

## Reviews (2)

### Review 1

Creating nine theorems in Lean and building a Rust conformance harness looks very promising. That said, some of gaps limit the practical impact: the lack of join support weakens the core use case, and the Rust capability model leaves enforcement open to common escape paths. Security guarantees also rely on large assumptions, particularly the unverified translation from the Lean model to DuckDB and known runtime side channels. Future work would benefit from verified joins and a semantic link between the formal model and execution layer.

### Review 2

The incomplete proofs and small corpus contradict with the claims made with each other slightly. Data minimisation is a hard problem to solve and the engineering is good.

