# **AuraRemed: Autonomous Security Engineering Report** 

A Two-Tier Hybrid Architecture for Cognitive Code Self-Remediation and Operational Verification 

**Author:** Santiago Rodríguez Heras **Target Core:** Local Batch Run Matrix **Date:** May 24, 2026 

## **1. Executive Summary** 

Modern Continuous Integration and Continuous Deployment (CI/CD) workflows are constantly bottlenecked by manual triage of static security findings. Traditional Static Application Security Testing (SAST) utilities excel at deterministic pattern recognition but lack structural synthesis capabilities to safely mitigate findings without operator intervention. 

**AuraRemed** addresses this paradigm by introducing an automated, multi-loop architectural pipeline that joins rulebased static validation with advanced localized language modeling. The platform acts as an autonomous feedback loop, analyzing software vulnerabilities, generating surgical in-memory patches, enforcing rigorous code documentation practices, and self-validating changes against the original security baseline. 

**`🎯` Key Achievement: Completed full mitigation testing against a multi-vector threat matrix. 100% of discovered high-criticality vulnerabilities were remediated autonomously, achieving absolute compliance and clean validation exits (Code 0).** 

## **2. System Architecture & The Remediation Loop** 

The framework minimizes reliance on external clouds or third-party APIs to preserve complete privacy over intellectual property and prevent source code exfiltration risks. The design operates on a dual-tier control mechanism: 

- **Tier 2 (Deterministic Verification):** Utilizes an optimized local instance of `Semgrep` . This engine enforces compliance against extensive semantic patterns to guarantee syntactic and stylistic determinism. 

- **Tier 1 (Cognitive Remediation):** Leverages a locally orchestrated `qwen2.5-coder` large language model via the `Ollama` runtime layer. This tier assesses the abstract syntax tree and structural context surrounding defects. 

### **The Feedback Synchronization Formula** 

The iterative lifecycle operates as a stateful machine bounded by an execution limit constraint to mitigate stasis and infinity limits. Let the target file state at iteration **_i_** be denoted as **_Si_** , and the evaluation parsing engine output be **_V(Si)_** . The next transition state is defined by the following expression: 

AuraRemed Engineering Framework — Confidential 

Page 1 of 3 

### **_Si+1 = Ψ(Si, V(Si))_** 

Where **_Ψ_** represents the surgical patch injection function orchestrated by the cognitive layer. If at any state **_V(Si) = ∅_** (representing zero flagged vulnerabilities), the environment declares stability, stops the sequence, and exits safely with execution value `0` . 

## **3. Threat Test Bench Breakdown** 

To evaluate operational capabilities, AuraRemed was stress-tested against a repository containing five distinct high-risk vulnerabilities mapped to the OWASP Top 10 classifications: 

|**Target Script Module**|**Vulnerability**<br>**Vector Detected**|**Exploitation &**<br>**Business Risk Impact**|**Remediation Mechanism**<br>**Applied**|
|---|---|---|---|
|`vuln_sql_injection.py`|SQL Injection<br>(CWE-89)|Arbitrary database read/<br>write, authentication<br>bypass, data extraction.|Parameterized inputs utilizing<br>secure tuple object binding<br>definitions.|
|`vuln_command_injection.py`|OS Command<br>Injection (CWE-78)|Remote Code Execution<br>(RCE) via shell<br>concatenation vectors.|Refactored runtime execution to<br>pass arguments explicitly via<br>isolated lists.|
|`vuln_path_traversal.py`|Path Traversal<br>(CWE-22)|Unauthorized access to<br>sensitive server<br>infrastructure layout/<br>files.|Sanitized inputs using strict<br>basename filtering and path<br>normalization rules.|
|`vuln_insecure_pickle.py`|Insecure<br>Deserialization<br>(CWE-502)|Arbitrary payload<br>execution during binary<br>serialization routines.|Migrated object handling<br>infrastructure to standard<br>deterministic JSON parsing<br>layers.|
||Exposed|Global authentication|Decoupled parameters to fetch|
|`vuln_hardcoded_jwt.py`|Cryptographic<br>Token (CWE-798)|spoofing and complete<br>signature compromise.|signing keys from secure<br>`os.environ`spaces.|



## **4. Code Hardening & Auto-Documentation Quality** 

A unique aspect of the AuraRemed orchestrator is its strict formatting wrapper constraint. Instead of merely patching the logical flaw, the cognitive tier is programmed to inject an immutable **Security Mitigation Report** directly inside the source code as a standardized Python docstring. 

This guarantees that software developers receive complete contextual visibility regarding what mitigation occurred without having to leave their integrated development environment (IDE). Below is a verified output block demonstrating the automated injection behavior: 

AuraRemed Engineering Framework — Confidential 

Page 2 of 3 

```
def query_user_profile(user_input_id):
```

```
    """
    [AuraRemed Security Mitigation Report]
```

```
    - Vulnerability Detected: SQL Injection
```

- `Exploit Risk: Raw string interpolation enables severe data exfiltration or structural bypass.` 

- `Remediation Applied: Replaced unsafe string formatting with parameterized SQL query binding.` 

```
    """
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM profiles WHERE id = ?"
    return conn.execute(query, (user_input_id,)).fetchall()
```

## **5. Empirical Performance Analytics** 

The batch processing execution run yielded definitive results across all test targets. For every file, the initial vulnerability metrics captured during Loop 1 triggered the cognitive remediation pipeline. By Loop 2, subsequent validation scans confirmed that 100% of targeted modules achieved complete compliance. 

The convergence rate demonstrates optimal efficiency, proving that the localized model is highly deterministic when guided by granular context strings and specialized system personas. 

## **6. Fellowship Strategic Conclusion** 

AuraRemed successfully bridges the critical disconnect between automated defensive detection and active remediation. By proving that a local, lightweight cognitive model can surgically harden multi-vector flaws—while preserving original software dependencies, runtime business code logic, and interface frameworks intact—this research sets a baseline blueprint for fully self-healing software supply chains. The empirical metrics support its immediate viability for production-level pre-commit pipelines and secure DevSecOps agent orchestration. 

AuraRemed Engineering Framework — Confidential 

Page 3 of 3 

