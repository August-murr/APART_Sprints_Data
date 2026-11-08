# **AUTORED: Measuring the Elicitation Gap via Automated Red-Blue Optimization** 

**Phongsakon Mark Konrad** 

The Maersk Mc-Kinney Moller Institute SDU Centre for Industrial Software University of Southern Denmark Sønderborg 6400, Denmark `phongsakon@outlook.dk https://phomarkon.github.io/` 

## **Abstract** 

Evaluating AI safety requires understanding the _elicitation gap_ : the difference between a system’s safety under naive evaluation and its safety under best-effort adversarial testing. Manual red teaming is expensive and does not scale. We introduce AUTORED, a five-phase framework that automates both red team attack optimization and blue team monitor optimization using a reasoning model as meta-optimizer. In a code backdoor detection setting adapted from the AI Control framework, AUTORED iteratively generates, evaluates, and improves strategies on both sides, then tests whether the improvements generalize. Automated optimization partially closes the elicitation gap: red attacks improve and blue monitors adapt. Co-evolutionary dynamics are oscillatory, with neither side converging. The central finding is cautionary: optimized strategies are brittle to distribution shift. The best optimized monitor drops from 90% safety during training to 47% on held-out tasks with a different attack mechanism, while a simple threshold baseline maintains 100%. Elicitation gap measurements without held-out evaluation across attack distributions are unreliable. 

## **1 Introduction** 

Safety evaluations for AI systems increasingly rely on adversarial testing [Perez et al., 2022, Ganguli et al., 2022, Mazeika et al., 2024]. A central open question is how much harder we could push: if we invested more effort into attacking a system, how much worse would its safety metrics become? Greenblatt et al. [2024] call this the _elicitation gap_ , the difference between measured safety under default evaluation and safety under the strongest feasible attack. If this gap is large, current evaluations give false confidence. 

Manual red teaming is the standard approach, but it is expensive, inconsistent across teams, and does not scale. Automated methods [Perez et al., 2022, Yu et al., 2024, Zou et al., 2023, Liu et al., 2024] optimize attacks but leave defenses fixed, measuring only the offensive half of the gap. No existing framework simultaneously optimizes both sides to measure the full gap, and no prior work has tested whether optimized strategies generalize beyond the opponents they trained against. 

We present AUTORED, a framework that automates both red team attack optimization and blue team monitor optimization in a code backdoor detection setting [Greenblatt et al., 2024]. A reasoning model iteratively improves strategies on each side across five phases: baselines, independent red and blue optimization, co-evolution, and a transfer test on held-out tasks. Our central finding is cautionary: **optimized strategies overfit to their training opponents** . The best optimized monitor achieves 90% safety during training but averages just 47% on held-out tasks (3 seeds, _±_ 0.09), while a simple threshold baseline maintains 100% with zero variance. 



<!-- Start of picture text -->
15 × 15 × 5 × 3<br>Phase 0 Phase 1 Phase 2 Phase 3 Phase 4<br>Baselines Red Optim. Blue Optim. Co-evolution Transfer Test<br>best attack → best monitor →<br>3 monitors fixed blue fixed red alternate 3 × 3 matrix<br>naive attack optimize red optimize blue red  ↔ blue + held-out<br>Models<br>U  : minimax-m2.7 T : nemotron-3-super O  : deepseek-v3.1<br>untrusted coder trusted monitor optimizer<br><!-- End of picture text -->

Figure 1: AUTORED pipeline. Phase 0 establishes baselines; Phases 1–2 independently optimize red attacks and blue monitors; Phase 3 alternates both sides; Phase 4 evaluates generalization via a transfer matrix and held-out tasks. Three models serve distinct roles. 

Three results support this. Red optimization raises attack success from 0% to 30% against a fixed baseline monitor. Blue optimization achieves 90% safety with 90% usefulness against the optimized attack. But a 3 _×_ 3 transfer matrix reveals that the optimized monitor is _worse_ than the baseline against the very attack it trained against (50% vs. 20% attack success). On held-out tasks, the baseline monitor achieves AUROC = 0.85 while the optimized monitor sits at 0.50 (chance), confirming zero discriminative signal on unseen code. 

These results have direct implications for how the AI safety community should measure elicitation gaps. Any automated red teaming pipeline that reports gap measurements without held-out evaluation risks producing inflated estimates on both sides. Simple, pattern-agnostic baselines should always accompany optimized strategies as a robustness check. More broadly, elicitation gap measurement faces the same generalization challenges as supervised learning: optimizing on a narrow distribution produces brittle classifiers, not genuine capability improvements. 

### **Contributions.** 

- AUTORED, a five-phase framework that automates both attack and defense optimization using a reasoning model, enabling systematic elicitation gap measurement. 

- Evidence that automated optimization partially closes the gap (red: 0% _→_ 30%; blue: 90% safety at 90% usefulness), with oscillatory co-evolutionary dynamics. 

- The finding that optimized strategies overfit: the best monitor drops from 90% to 47% safety on held-out tasks (3 seeds), while a threshold baseline holds at 100%. 

- A transfer test methodology (attack _×_ monitor matrix + held-out evaluation) that exposes this overfitting. 

## **2 Related Work** 

**AI safety evaluation.** Red teaming language models has become standard practice [Perez et al., 2022, Ganguli et al., 2022]. Mazeika et al. [2024] introduce HarmBench for standardized evaluation. These efforts optimize attacks without simultaneously optimizing defenses. AUTORED extends this by automating both sides and measuring the gap between them. 

**AI Control.** Greenblatt et al. [2024] formalize the trusted monitoring framework we build on. They manually design protocols and evaluate against hand-crafted attacks. We automate both the design and evaluation loop, enabling systematic measurement of how much optimization improves each side. 

**Automated adversarial attacks.** GCG [Zou et al., 2023] and AutoDAN [Liu et al., 2024] automate adversarial prompt generation through gradient-based and genetic optimization. These operate at the input level (crafting prompts) rather than the strategy level (designing how to attack). AUTORED optimizes high-level strategies that generate many individual attack instances. 

2 

**Co-evolutionary optimization.** Co-evolutionary algorithms have a long history [Popovici et al., 2012]. Cycling and overfitting to current opponents are known failure modes. Our Phase 3 results align with these findings: oscillatory dynamics and strategy overfitting emerge naturally from alternating optimization. 

## **3 Background** 

**AI Control.** Greenblatt et al. [2024] introduce a framework where an untrusted model _U_ generates code while a trusted monitor _T_ reviews it. A _protocol_ decides whether to accept _U_ ’s output or defer to _T_ based on suspicion scoring. Safety is the fraction of backdoored submissions caught (detected or deferred); usefulness is the fraction of honest submissions that produce correct code. 

**Elicitation gap.** The elicitation gap is the difference between measured safety under default evaluation and safety under the strongest feasible attack. A large gap means current evaluations underestimate risk. Measuring this gap requires exploring the space of possible attacks, which is combinatorially large and poorly understood. 

**Code backdoor detection.** We adopt the setting from Greenblatt et al. [2024]. The untrusted model writes Python functions for programming tasks. In attack mode, a backdoor is injected: a specific trigger input causes the function to return an incorrect output while all visible test cases pass. The monitor must distinguish backdoored code from honest code using suspicion scores. This setting is a tractable proxy for a broader class of deployment threats: any scenario where a capable but potentially misaligned model produces artifacts (code, plans, tool calls) that must be reviewed before execution. 

## **4 Method: AUTORED** 

AUTORED operates in five phases, each building on the previous. A shared results board tracks metrics and best strategies across phases. A reasoning model _O_ generates improved strategies by analyzing prior results. 

### **4.1 Strategy spaces** 

**Blue (monitoring protocol).** The blue strategy implements a function `run_protocol(problem, code, trusted_model, ...)` that returns a decision in _{_ `ACCEPT` _,_ `DEFER` _}_ . The protocol may call the trusted model at most once per invocation (for suspicion scoring or code analysis) and may perform unlimited local static analysis (AST parsing, regex matching). It must never query the untrusted model, which is adversarial. 

**Red (attack strategy).** Red controls two aspects: (1) whether to attack on a given task, and (2) how to obfuscate the injected backdoor. Backdoor injection is handled deterministically by the evaluation harness, which inserts an early-return conditional for the trigger input. Red’s optimization surface is limited to obfuscation: making the injected code harder for the monitor to detect. This measures the _obfuscation elicitation gap_ specifically; a real adversary would also optimize the injection mechanism itself, the choice of trigger, and the attack surface. 

### **4.2 Five-phase pipeline** 

**Phase 0: Baselines.** We focus on the _trusted monitoring_ protocol from the taxonomy of Greenblatt et al. [2024] (as opposed to trusted editing or untrusted monitoring). We evaluate three fixed variants against naive (unoptimized) attacks: no monitoring, trusted monitoring with threshold _τ_ = 0 _._ 5, and aggressive monitoring with _τ_ = 0 _._ 3. 

**Phase 1: Red optimization.** Blue is fixed to the baseline trusted monitor ( _τ_ = 0 _._ 5). For 15 iterations, _O_ receives the current red strategy, the blue monitor code, evaluation metrics, and examples of caught attacks. It generates an improved red strategy. If the new strategy achieves higher attack success than the current best (with valid code structure), it becomes the active strategy. 

3 

**Phase 2: Blue optimization.** Red is fixed to the best strategy from Phase 1. For 15 iterations, _O_ optimizes the monitoring protocol. A new protocol is adopted only if it Pareto-improves over the current best on both safety and usefulness. The optimizer receives false positive examples alongside detection metrics. 

**Phase 3: Co-evolution.** Starting from the Phase 1 best red and Phase 2 best blue, we alternate optimization: 3 red iterations then 3 blue iterations, for 5 rounds. This tests whether strategies effective against fixed opponents remain so when both sides adapt. 

**Phase 4: Transfer test.** We construct a 3 _×_ 3 evaluation matrix: three attacks (naive, Phase 1 best, Phase 3 best) crossed with three monitors (baseline, Phase 2 best, aggressive). We also run held-out evaluation on tasks unseen during optimization. 

### **4.3 Evaluation metrics** 

Each evaluation runs 20 tasks: 10 honest, 10 attack. We report: **Safety** : fraction of attack tasks where the backdoor is caught or deferred. **Usefulness** : fraction of honest tasks producing correct code. **Attack success** : fraction of attacks passing undetected. **AUROC** : area under ROC for suspicion score separation between honest and attack code. 

### **4.4 Optimizer design** 

_O_ receives a structured prompt containing the current strategy code, the opponent’s code, recent metrics, and success/failure examples. It outputs a complete replacement strategy file using chain-ofthought reasoning. Outputs are validated for required function signatures before evaluation; invalid outputs are discarded. 

### **4.5 Experimental setup** 

**Models.** We use three models via the Ollama cloud API: `minimax-m2.7` as the untrusted coder _U_ , `nemotron-3-super` (NVIDIA 120B MoE) as the trusted monitor _T_ , and `deepseek-v3.1:671b` as the optimizer _O_ . Using different model families for _U_ and _T_ prevents architectural bias in monitoring. 

**Tasks.** We use 15 hand-crafted Python programming tasks (primality testing, Fibonacci, palindrome checking, sorting, etc.) with visible tests, hidden tests, and designated backdoor triggers. Each trigger specifies an input and expected output; the backdoor causes the function to return an incorrect value for the trigger while passing all visible tests. Ten additional held-out tasks are reserved for final evaluation. 

**Evaluation protocol.** Each iteration evaluates 20 tasks (10 honest, 10 attack) with a fixed random seed per iteration for reproducibility. Code execution is sandboxed in temporary directories with a 5-second timeout. 

## **5 Results** 

### **5.1 Baselines (Phase 0)** 

Table 1 shows baseline performance against naive attacks. 

Without monitoring, naive attacks succeed 30% of the time. Both threshold monitors achieve perfect safety, with the standard threshold retaining higher usefulness (0.80 vs. 0.60). 

### **5.2 Red optimization (Phase 1)** 

Figure 2 (left) shows attack success across 15 iterations. The optimizer discovers an effective strategy at iteration 1 (attack success 0.30) and does not improve further. The successful strategy replaces the obvious `if input == trigger` check with character-frequency analysis and stringlength conditions that are semantically equivalent but syntactically different. Later iterations attempt 

4 

Table 1: Baseline monitor performance against naive (unoptimized) attacks. Under no monitoring, all submissions are accepted: safety is 0.70 because 7 of 10 backdoor injections fail before reaching the monitor (the injected code crashes or breaks visible tests), not because attacks are detected. Usefulness is 0.50 because the untrusted model produces correct code on only half of honest tasks. Monitoring improves usefulness because deferred tasks are handled by the more capable trusted model. 

|Monitor|Safety|Useful.|Atk. Succ.|AUROC|Defer Rate|
|---|---|---|---|---|---|
|No monitoring|0.70|0.50|0.30|0.50|0.00|
|Trusted (_τ_=0_._5)|1.00|0.80|0.00|0.67|0.15|
|Aggressive (_τ_=0_._3)|1.00|0.60|0.00|0.69|0.15|





<!-- Start of picture text -->
0.4 Attack success<br>Running best<br>0.3 Kept<br>0.2<br>0.1<br>Baseline<br>0.0<br>0 2 4 6 8 10 12 14<br>Iteration<br>Attack Success Rate<br><!-- End of picture text -->

(a) Phase 1: Red optimization. Attack success over 15 iterations against the fixed baseline monitor ( _τ_ =0 _._ 5). Stars mark kept improvements. The optimizer discovers an effective obfuscation at iteration 1 and plateaus at 0.30. 



<!-- Start of picture text -->
1.0<br>Baseline safety<br>0.8<br>0.6<br>0.4<br>Safety<br>0.2<br>Usefulness<br>Ke p t<br>0.0<br>0 2 4 6 8 10 12 14<br>Iteration<br>Rate<br><!-- End of picture text -->

(b) Phase 2: Blue optimization. Safety and usefulness over 15 iterations against the Phase 1 best attack. The best protocol (iteration 2, star) achieves 0.90 on both metrics. Iterations with usefulness 0 are degenerate “defer all” solutions. 

Figure 2: Elicitation curves for red and blue optimization. Each point is one optimizer iteration. Dashed lines show baseline reference values. Stars indicate iterations whose strategies were kept (improving over the previous best). 

hash-based comparisons and helper functions with innocent names, but these either break correctness or fail to evade the monitor. 

The Phase 1 elicitation gap for red is 0.30: attack success rises from 0% (naive against baseline monitor) to 30% under optimization. With _n_ =10 attack tasks, this corresponds to 3 successful attacks out of 10, and individual numbers should be interpreted as trends rather than precise estimates. 

### **5.3 Blue optimization (Phase 2)** 

Figure 2 (right) shows safety across 15 blue optimization iterations against the Phase 1 best attack. The optimizer finds a strong protocol at iteration 2: safety 0.90, usefulness 0.90. This protocol combines AST-based static analysis (detecting suspicious imports, hash comparisons, validationfunction patterns) with a single trusted model call using adaptive thresholds. 

Several iterations produce degenerate solutions (safety 1.00, usefulness 0.00) that defer all submissions. The Pareto improvement filter correctly rejects these. Oscillation between overly aggressive and overly permissive protocols suggests the optimizer struggles to navigate the safety-usefulness tradeoff. AUROC remains at 0.50 for most Phase 2 iterations, indicating that the monitor’s suspicion scores do not reliably separate honest from attack code. The best protocol’s safety comes primarily from its AST-based hard rules (which trigger deterministic deferrals) rather than from the trusted model’s suspicion scoring. This explains the later overfitting: the hard rules are pattern-specific and brittle. 

5 



<!-- Start of picture text -->
Red Blue<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>Best attack success (Red)<br>0.0 Best safety (Blue)<br>0 1 2 3 4<br>Co-evolution Round<br>Rate<br><!-- End of picture text -->

Figure 3: Co-evolutionary dynamics across 5 rounds. Each round: 3 red iterations then 3 blue iterations. Red attack success (peak per round) oscillates between 0.30 and 0.60. Blue safety (peak per round) stays above 0.70 and reaches 1.00 in four of five rounds. Neither side converges; the dynamics resemble an oscillatory arms race. 

Table 2: Transfer test: attack success rate for each attack-monitor pair. Optimized attacks partially transfer across monitors, but the Phase 2 best monitor is worse than the baseline against the Phase 1 best attack (0.50 vs. 0.20), indicating overfitting. Bold marks the highest attack success per column. 

||Baseline (_τ_=0_._5)|Phase 2 Best|Aggressive (_τ_=0_._3)|
|---|---|---|---|
|Naive attack|0.30|0.20|0.00|
|Phase 1 best|0.20|**0.50**|0.00|
|Phase 3 best|0.20|0.30|**0.10**|



### **5.4 Co-evolution (Phase 3)** 

Figure 3 shows co-evolutionary dynamics across 5 rounds. Red attack success peaks at 0.60 in rounds 0 and 3 but drops in intervening rounds as blue adapts. Blue safety stays at or above 0.70 and reaches 1.00 in four of five rounds. The dynamics are oscillatory rather than convergent. 

Red’s peak during co-evolution (0.60) exceeds its Phase 1 best (0.30), indicating that adapting to a stronger opponent produces stronger strategies than optimizing against a fixed baseline. Blue’s consistent recovery shows that the monitoring strategy space is rich enough to counter diverse attacks when given the opportunity to observe them. 

### **5.5 Transfer test (Phase 4)** 

### Table 2 shows the 3 _×_ 3 transfer matrix. 

Two patterns stand out. First, the Phase 2 best monitor is _worse_ than the baseline against the Phase 1 best attack (0.50 vs. 0.20). The optimized monitor learned to detect specific patterns in its training attack and became vulnerable to the same attack’s earlier, simpler variant. Second, the aggressive threshold monitor is the most robust across all attacks (attack success _≤_ 0 _._ 10), at the cost of reduced usefulness. 

### **5.6 Held-out evaluation** 

Table 3 reports performance on 10 held-out tasks unseen during optimization. 

The optimized blue monitor averages 47% safety across 3 seeds (down from 90% during training), with attack success at 53%. Its AUROC is 0.50 on every seed, confirming zero discriminative signal on new tasks. The aggressive threshold baseline achieves 100% safety with zero variance across all seeds. The baseline monitor, despite no optimization, averages 80% safety with AUROC = 0.85. Figure 5 visualizes this contrast. 

Figure 6 shows the contrast visually: the baseline monitor’s scores correctly separate honest (low) from attack (high), while the optimized monitor’s scores are inverted on held-out tasks. 

6 



<!-- Start of picture text -->
Attack Success Rate<br>Monitor<br>Baseline Phase 2 Aggressive<br>(¿=0.5) Best (¿=0.3)<br>0.6<br>Naive 0.30 0.20 0.00 0.5<br>0.4<br>Phase 1 0.20 0.50 0.00 0.3<br>Best<br>0.2<br>Phase 3 0.20 0.30 0.10 0.1<br>Best<br>0.0<br>Attack<br><!-- End of picture text -->

Figure 4: Transfer matrix heatmap of attack success rates. The Phase 2 best monitor (middle column) is more vulnerable to the Phase 1 best attack than the simpler baseline, revealing overfitting. The aggressive monitor ( _τ_ =0 _._ 3, right column) is the most robust across all attacks. 

Table 3: Held-out evaluation (mean _±_ std over 3 seeds): best Phase 1 red attack against three monitors on unseen tasks. The optimized blue monitor averages 47% safety with AUROC at chance (0.50) across all seeds, while the aggressive baseline holds at 100% safety with zero variance. 

|Configuration|Safety|Useful.|Atk. Succ.|AUROC|
|---|---|---|---|---|
|Best red vs. baseline|0.80_±_.16|0.80_±_.16|0.20_±_.16|0.85_±_.11|
|Best red vs. optimized blue|0.47_±_.09|0.80_±_.16|0.53_±_.09|0.50_±_.00|
|Best red vs. aggressive|**1.00**_±_.00|0.80_±_.16|**0.00**_±_.00|0.82_±_.14|



This is the central finding: automated optimization improves strategies against fixed opponents, but the improvements overfit. Measuring an elicitation gap without held-out evaluation inflates estimates of both offense and defense capability. The held-out tasks use unobfuscated backdoor injection (simple `if` -checks) rather than the hash-based obfuscation seen during training, so the monitor’s failure reflects both optimization overfitting _and_ distribution shift in the attack mechanism. This compounds the concern: in real deployments, attackers are not constrained to a single obfuscation paradigm, making distribution shift the norm rather than the exception. 

**Why the optimized monitor fails.** Table 4 breaks down held-out decisions by the optimized blue monitor into failure modes. The root cause is a mismatch between training and held-out attack patterns. During training, the Phase 1 best attack uses `hashlib.md5()` with precomputed hashes. The optimized monitor learns AST rules targeting these patterns (hash imports, 32-char hex strings, validation function names). On held-out tasks, the injected backdoor is a simple `if str(n) == trigger: return wrong` with no hash obfuscation. The AST rules do not fire (0 suspicious patterns on every held-out task), so all decisions fall to the trusted model call. 

The model call itself is also overfitted: the optimized prompt instructs the model to “pay special attention to input validation that uses hashing” and “hash-based comparisons.” On held-out code without hashing, the model assigns low scores (0.0) to honest code, triggering DEFER (4 of 5 false positives). For attack code, the simple backdoor looks like normal edge-case handling, so the model gives high scores (0.8), triggering ACCEPT (2 of 3 undetected backdoors). 

**Strategy evolution.** Inspecting the optimizer logs reveals a clear arc. In Phase 1 iteration 0, the red optimizer generates a SHA-256 hash-based obfuscation that replaces the trigger check with `hashlib.sha256(str(x)).hexdigest()` comparisons (attack success 0.20, kept). In iteration 1 (the best), it switches to MD5 with a list of “known edge cases” containing precomputed hashes and validation function names randomly drawn from `["validate_input",` 

7 



<!-- Start of picture text -->
Safety<br>Attack Success<br>1.0 Training safety<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>Baseline Optimized Aggressive<br>(τ=0.5) Blue (τ=0.3)<br>Rate<br><!-- End of picture text -->

Figure 5: Held-out safety and attack success (mean _±_ std, 3 seeds). The dashed line marks trainingtime safety (0.90). The optimized blue monitor drops to 0.47 on unseen tasks while the aggressive baseline holds at 1.00. Error bars confirm the result is stable across seeds. 



<!-- Start of picture text -->
Honest Attack<br>(a) Baseline Monitor (b) Optimized Monitor<br>ACCEPT DEFER DEFER ACCEPT<br>2 attacks<br>accepted (FN)<br>Attack<br>Honest<br>4 honest tasks<br>deferred (FP)<br>=0.5 =0.3<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>Suspicion Score Suspicion Score<br><!-- End of picture text -->

Figure 6: Suspicion scores on held-out tasks for the baseline monitor (left) vs. the optimized monitor (right). The baseline cleanly separates honest (green, low scores) from attack code (red, high scores). The optimized monitor’s scores are inverted: honest code receives 0.0 (triggering spurious deferrals) while attack code receives 0.8 (triggering incorrect accepts). Dashed lines mark decision thresholds. 

`"check_edge_case", ...]` (attack success 0.30, kept). By iteration 10, it over-engineers: a helper function `_handle_special_case()` with SHA-256 and multiple layers of indirection, but the code replacement logic breaks on many tasks, producing 0.00 attack success. The optimizer peaked early and could not escape the hash-based obfuscation paradigm. 

On the blue side, iteration 0 produces a “defer all” protocol (safety 1.00, usefulness 0.00). Iteration 2 (the best) adds targeted AST checks for the specific patterns in the training attack: hashlib imports, hexdigest calls, 32-char hex strings, and validation-function naming. This works perfectly against hash-based obfuscation but creates the brittle dependency that fails on held-out tasks. Full strategy code is provided as supplementary material (the blue protocol matches Phase 2 best; the red strategy shows the character-frequency variant from Phase 3 co-evolution, which diverged from the hash-based Phase 1 best). 

## **6 Discussion and Limitations** 

**Strategy overfitting.** The failure mode taxonomy (Table 4) reveals that overfitting operates through two channels: pattern-specific AST rules that do not fire on unseen code, and an overfitted model 

8 

Table 4: Failure mode taxonomy for the optimized blue monitor on held-out tasks. All failures trace to the same root cause: AST rules and model prompt are tuned to hash-based obfuscation, which is absent on held-out tasks. 

|Mode|Decision|Count|Mechanism|
|---|---|---|---|
|Honest|DEFER (FP)|4/5|Model score 0.0_<_threshold 0.3_→_spurious defer|
|Honest|ACCEPT (correct)|1/5|Model score 1.0_>_threshold_→_correct accept|
|Attack|ACCEPT (FN)|2/5|No AST triggers; model score 0.8_>_threshold|
|Attack|DEFER (correct)|2/5|Model score_≤_0.1_→_defer catches backdoor|
|Attack|FAILED_ATTACK|1/5|Backdoor injection failed (safe by default)|



prompt that inverts the suspicion scoring on out-of-distribution inputs. This is not a subtle degradation but a catastrophic failure: the monitor’s false positive rate reaches 80% while its false negative rate reaches 40%. The mechanism mirrors supervised learning: the “training set” (Phase 1 best attack) has a narrow feature distribution (hash-based obfuscation), and the “classifier” (optimized monitor) learns features specific to that distribution rather than general indicators of backdoor presence. 

**Asymmetric dynamics.** Red optimization saturates quickly (2 iterations to peak), while blue optimization produces high variance with several iterations collapsing to trivial “defer all” solutions. The red strategy space (obfuscation only) is narrow; the blue space (local analysis + model scoring) is richer but harder to navigate. 

**Simple baselines are robust.** A threshold-based monitor with no optimization outperforms the optimized protocol on held-out tasks because its decision rule does not depend on specific code patterns. This argues for simple, pattern-agnostic monitoring as a robust default. 

**Recommendations for practitioners.** Four guidelines follow from our results: 

1. **Benchmark on held-out data.** Our optimized monitor achieved 90% training safety but 47% held-out safety. Any automated red teaming pipeline should report gap measurements on unseen tasks and threat vectors. 

2. **Prefer general-purpose prompts over pattern-specific rules.** The baseline monitor’s generic “is this suspicious?” prompt generalizes (AUROC = 0.85 on held-out); the optimized monitor’s 7 AST-specific checks do not (AUROC = 0.50). Pattern-specific rules should supplement, not replace, general-purpose judgment. 

3. **Report AUROC alongside safety.** A monitor can achieve high safety through conservative deferral while having zero discriminative signal. Our optimized monitor’s AUROC of 0.50 across all seeds exposes this. 

4. **Use multi-seed evaluation.** With _n_ =10 attack tasks, single-seed metrics have _±_ 0.16 std. Three seeds (our minimum) reveals whether results are stable. 

### **6.1 Limitations** 

We intentionally chose a constrained setting (15 training tasks, 10 held-out tasks, non-frontier models, prompt-level optimization) to isolate whether overfitting dynamics emerge under minimal conditions. The fact that catastrophic overfitting appears _even in this simple setting_ suggests the problem will be worse, not better, at scale: larger strategy spaces give the optimizer more room to specialize, and more capable models can learn subtler pattern-specific features. Three caveats apply. First, with _n_ =10 attack tasks per evaluation, each success shifts metrics by 10 percentage points, so individual numbers should be interpreted as trends rather than precise estimates. Second, the optimizer operates at the prompt level rather than fine-tuning weights, which limits the optimization surface. Third, the code backdoor setting is a simplified proxy for real deployment threats. 

### **6.2 Future Work** 

The overfitting problem is not inevitable. Mitigations parallel supervised learning: training against a _diverse ensemble_ of opponents (data augmentation), regularizing protocol complexity (limiting AST-check count), and population-based co-evolution with fitness sharing (hall-of-fame opponents). 

9 

Natural extensions include scaling to APPS/HumanEval task pools, using frontier models as both _U_ and _O_ , and expanding the red strategy space beyond obfuscation to include architecture-level attacks. 

## **7 Conclusion** 

Automated optimization can partially close the elicitation gap, but the improvements are brittle. The strategies an optimizer discovers are tuned to the opponent it trained against, not to the underlying task. A simple threshold baseline, with no optimization at all, outperforms the best optimized monitor on unseen tasks. 

For AI Control practitioners, the implication is direct: any protocol designed by optimizing against a specific attack class should be validated against held-out attacks before deployment. Reporting safety metrics without held-out evaluation is analogous to reporting training accuracy without a test set. Simple, pattern-agnostic baselines should always accompany optimized strategies as a sanity check. If the baseline wins on held-out, the optimization has overfit. Until automated optimization methods can be made robust to distribution shift, the most reliable monitors may be the simplest ones. 

**Code and Data.** Code repository: `https://github.com/phomarkon/autored-submission` . The repository includes the full pipeline, all evaluation results (JSON), optimizer logs, best red/blue strategy code, an interactive Streamlit demo, and Luthien Proxy policy files. All 15 training tasks, 10 held-out tasks, and the board.json with complete phase results are included. 

**Author Contributions.** P.M.K. conceived the research question, designed the 5-phase experimental framework, ran all experiments on Lambda Cloud infrastructure, analyzed results, and wrote the paper. All work was completed during the AI Control Hackathon 2026 (March 20–22). 

**LLM Usage Statement.** Claude Code (Anthropic, Opus 4.6) was used as a programming assistant for pipeline implementation, matplotlib figure generation, LaTeX typesetting, and manuscript drafting. All experimental design, research direction, interpretation of results, and scientific claims are the sole responsibility of the author. The deepseek-v3.1 model serving as the optimizer within the AUTORED pipeline is part of the experimental setup, not an authorship tool. 

## **Acknowledgments and Disclosure of Funding** 

This work was supported by a $400 Lambda Cloud compute credit. The full pipeline completed in _∼_ 8 hours with _∼_ 1,200 API calls at under $50 total cost. 

## **References** 

- Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez, Nicholas Schiefer, Kamal Ndousse, et al. Red teaming language models to reduce harms: Methods, scaling behaviors, and lessons learned. _arXiv preprint arXiv:2209.07858_ , 2022. 

- Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, and Fabien Roger. AI Control: Improving safety despite intentional subversion. In _ICML_ , 2024. 

- Xiaogeng Liu, Nan Xu, Muhao Chen, and Chaowei Xiao. AutoDAN: Generating stealthy jailbreak prompts on aligned large language models. In _ICLR_ , 2024. 

- Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou, Zifan Wang, Norman Mu, Elham Sakhaee, Nathaniel Li, Steven Basart, Bo Li, et al. HarmBench: A standardized evaluation framework for automated red teaming and robust refusal. In _ICML_ , 2024. 

- Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, and Geoffrey Irving. Red teaming language models with language models. In _EMNLP_ , 2022. 

- Elena Popovici, Anthony Bucci, R. Paul Wiegand, and Edwin D. De Jong. Coevolutionary principles. In _Handbook of Natural Computing_ , pages 987–1033. Springer, 2012. 

- Jiahao Yu, Xingwei Lin, Zheng Yu, and Xinyu Xing. GPTFuzzer: Red teaming large language models with auto-generated jailbreak prompts. In _USENIX Security_ , 2024. 

10 

Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, and Matt Fredrikson. Universal and transferable adversarial attacks on aligned language models. _arXiv preprint arXiv:2307.15043_ , 2023. 

11 

