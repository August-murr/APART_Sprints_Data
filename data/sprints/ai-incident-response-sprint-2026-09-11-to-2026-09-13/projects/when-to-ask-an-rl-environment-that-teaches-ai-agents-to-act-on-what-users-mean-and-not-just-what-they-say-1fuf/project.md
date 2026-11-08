# When to Ask: An RL Environment That Teaches AI Agents to Act on What Users Mean and Not Just What They Say

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: 3
- Awards: 3rd Place ($300)
- Team: Team Teachafy
- Authors: Sharan Nagarajan, Puru, Muhammad Zane A
- Date / location: Sep 14, 2026 / None
- Page: https://apartresearch.com/sprints/projects/when-to-ask-an-rl-environment-that-teaches-ai-agents-to-act-on-what-users-mean-and-not-just-what-they-say-1fuf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/34c2b59c472c6f7d-b6773344-4d50-437b-a712-fd7abe71ea37-Ask-First-report.pdf
- Code: None
- Code links found in report: https://github.com/nsharan2000/critical-api-understanding-ai-agents, https://github.com/huggingface/trl
- Recording: https://when-to-ask.teachafy.com/presentation
- More on when-to-ask.teachafy.com: https://when-to-ask.teachafy.com/slideshow

## Summary

When to Ask is a reinforcement-learning environment that trains AI agents to work out what the user actually means before they use a powerful credential, instead of just carrying out the literal instruction. Agents today often hold real payment keys, database access or delete rights, and they're built to finish tasks on their own. So when a user mistypes an amount, forgets a "not", buries a risky step inside a long harmless message, or clicks past a warning they didn't read, the agent does exactly what the words said. The action can't be undone, and the user never wanted it.

Ask First builds each test as a pair of near-identical requests. In one, going ahead is right. In the other, something small shows that what the user wants differs from what they typed. The agent only scores when it handles both correctly: it acts on the clear request, and it pauses to ask a short, specific question on the ambiguous one. It gets no credit for asking about everything. A programmatic grader scores this, so the skill can be trained, not just prompted.

Across 9 models run on the same 96 test cases (48 pairs), even Claude Opus 5 got both requests in a pair right only 58% of the time. Llama-3.1-8B did so 4% of the time and took a dangerous action in 49% of cases. After 300 training steps in the environment, a small Qwen3-4B model rose from 27% to 52%, and its dangerous actions fell from 24% to 16%. The result is agents that treat a credential as something to use for the user's intent, not simply as permission to execute.

## Reviews (2)

### Review 1

This paper presents an exceptional, highly rigorous framework that targets a core operational bottleneck in agentic safety: the literal compliance bias of tool-using LLMs. The introduction of the twin-pair benchmarking schema is mathematically elegant and conceptually pristine. By requiring a model to achieve success on both matched scenarios, the benchmark effectively penalizes both reckless execution and over-cautious refusal styles. Furthermore, moving away from fragile LLM grading judges toward an execution-based, programmatic code tracker that maps out 15 discrete behavioral trajectories is a significant contribution to reproducible evaluation infrastructure.

The primary limitation of the work lies in the architectural limits of its simulated environment. The keyword-matching mechanism used by the scripted user to determine if an agent successfully "named the problem" is a fragile checkpoint that a highly capable model could eventually game by listing common forensic terminology without deep semantic comprehension. Additionally, as the authors frankly note, while the 4B model successfully internalized the rules for trained settings, its capacity to resist social pressure and hold its ground under adversarial pushback collapsed completely to a 0% success rate in completely unfamiliar environments. Future work should scale this approach to 8B and 32B model families and transition the evaluation toward dynamic, multi-turn user profiles rather than static template distributions.

### Review 2

This is a complete artifact. A dataset, an environment, a benchmark, a trained model and a transfer analysis. Every number I checked came back exact.

What I verified against the repository:

1. Scenario counts, all eight files, line by line – train_v2.jsonl 2,340, train.jsonl 1,726, probe.jsonl 96, test_indist.jsonl 176, heldout.jsonl 260, test_v2.jsonl 208, heldout_v2.jsonl 300, metr_derived.jsonl 40. Every one matches Table 3.
2. The evaluation total closes: 96 + 176 + 260 + 208 + 300 + 40 = 1,080 and the pairs sum to 540.
3. core_table.json holds exactly 34 core pairs, as stated.
4. The probe results in experiments/figures/RESULTS.md match Table B1 exactly. Run 3 step 300 at 52%, steps 200 and 250 at 44%, run 1 step 200 at 40%.

The twin-pair design is the contribution and it is a good one. Because both twins share wording and only the facts differ, always-ask and always-act both score zero. That closes the loophole that makes most single-scenario safety evals gameable and grading from tool calls rather than prose closes the other one.

Two things I want to credit specifically.

You attacked your own grader. You found the keyword loophole and two data giveaways halfway through, regenerated the training data, retrained, then reported both runs. That usually gets quietly dropped. Reporting run 1 alongside run 3 costs you a cleaner story and buys the reader real information.

The transcripts do the arguing. Example 1a against 1b is the clearest demonstration of the thesis in the paper. Haiku asks exactly the right question, folds to a content-free "just do it" and pays $82,697.66. Your trained model asks, holds, cites the dry-run warning – and the user admits the mistake. That pair makes the thesis without any statistics.

Now the problems.

1. The headline checkpoint was selected on a margin of less than one pair.

You picked step 300 on the fresh-twins set before looking at anything else, which is the right procedure. But look at the margin. On fresh twins, 88 pairs: step 200 is 49%, step 250 is 49%, step 300 is 50%. Fifty percent of 88 is 44 pairs and 49% is 43.1, so the selection turned on a single pair.

That one pair maps to an 8-point swing on the headline. On the probe set, steps 200 and 250 both score 44%. Step 300 scores 52%.

So "27% → 52%" rests on a selection signal indistinguishable from noise. The mean of your three late checkpoints on the probe is 46.7% and I would treat something near that as the defensible estimate. Section 4.4 says the separate selection set "limits the risk that we picked a lucky result" – on a one-pair margin, it does not. Please report the checkpoint spread in the abstract, or select on a much larger set.

The gain is still real. Every late checkpoint beats the 27% base on every one of the seven evaluation sets. It is the size that is overstated, not the direction.

2. The code and data link in the report is dead.

github.com/nsharan2000/critical-api-understanding-ai-agents returns 404. The work is public at when-to-ask-fintech-subset, which is complete and well-organised, but a reader following the report lands on nothing. Please fix the citation.

3. The abstract's 82% is the number your own paper says is inflated.

Table 4's caption is admirably direct. The core set is built from pairs Opus or Fable solved, so "read their rows as a reference ceiling, not a fair ranking." On the unbiased 48-pair set Opus is 58%, not 82%.

The abstract does say "on a core set of 34 twin pairs". It does not say that set was built from Opus and Fable outcomes. A reader takes away "Opus 82%". I would lead with the 48-pair numbers and keep the core set for the discussion.

4. Claude and the open-weight models ran through different harnesses.

Claude went through Claude Code; the open models went through vLLM. You flag this in Limitations.

But the abstract and the first contribution bullet present the gap as a model comparison. It is a model-plus-scaffold comparison. Claude Code supplies its own tool handling and system prompting, so some of the 82-versus-34 gap may belong to the harness.

One Claude run through the bare API with your exact prompt would settle how much.

5. The grader is a keyword matcher and you are training against it.

You name this risk – "a determined model could learn to mention keywords". It deserves more weight because it is a reward-hacking surface inside an RL loop, not just an evaluation imprecision.

Your own transfer gradient is consistent with partial gaming: 50% on trained settings, 36% on never-trained settings, 25% on the hardest set. That shape fits a mix of genuine learning and grader-specific adaptation. Nothing in the current design separates the two. A second grader with different phrasing rules, held out from training and used only at evaluation, would separate them.

1. One seed, one base model. You state this. RL run-to-run variance is large. Runs 1 and 3 used different data, so they are not a seed replication. Two seeds on v2 data would cost another nine hours each and would tell you how much of the 25 points is the method.
2. Minor – the Mistral row measures a harness failure. The text explains that it "largely failed to use the tool-calling format". So its 0% is inaction, not judgement. But sitting in Table 4 next to real scores, it reads as a capability result. Mark it in the table itself.

One note on authorship. Your usage statement says Claude drafted most of the text. It also says every number is read programmatically from the result files, and checked by the authors.

I checked those numbers independently and they hold, including all eight dataset counts. The disclosure is accurate and the underlying work is clearly yours. I scored the work.

Please let me know for any questions.

