# MITRE ATLAS Reference

Quick reference for MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) as used by agent-skills-pack. ATLAS catalogs adversary tactics and techniques targeting AI/ML systems.

**Source:** [mitre-atlas/atlas-data](https://github.com/mitre-atlas/atlas-data) — Data may be more current than atlas.mitre.org if the site has routing issues.

---

## ATLAS Tactics (16)

| ID | Name |
|----|------|
| AML.TA0000 | AI Model Access |
| AML.TA0001 | AI Attack Staging |
| AML.TA0002 | Reconnaissance |
| AML.TA0003 | Resource Development |
| AML.TA0004 | Initial Access |
| AML.TA0005 | Execution |
| AML.TA0006 | Persistence |
| AML.TA0007 | Defense Evasion |
| AML.TA0008 | Discovery |
| AML.TA0009 | Collection |
| AML.TA0010 | Exfiltration |
| AML.TA0011 | Impact |
| AML.TA0012 | Privilege Escalation |
| AML.TA0013 | Credential Access |
| AML.TA0014 | Command and Control |
| AML.TA0015 | Lateral Movement |

---

## AI-Specific Techniques (Selected)

| Tactic | Technique | ID | Description |
|--------|-----------|-----|-------------|
| Initial Access | AI Supply Chain Compromise | — | Compromise model artifacts, datasets, or tooling in supply chain |
| Initial Access | Prompt Infiltration via Public-Facing Application | — | Inject malicious prompts through exposed application |
| Execution | LLM Prompt Injection | AML.T0051 | Manipulate LLM behavior through crafted inputs |
| Execution | AI Agent Tool Invocation | — | Invoke tools via agent to execute adversary code |
| Persistence | AI Agent Context Poisoning | — | Poison agent context to persist malicious behavior |
| Persistence | RAG Poisoning | — | Poison retrieval-augmented generation data |
| Defense Evasion | LLM Jailbreak | — | Bypass safety controls to elicit restricted outputs |
| Defense Evasion | Corrupt AI Model | AML.T0076 | Corrupt model file to evade deserialization-based scanners |
| Credential Access | AI Agent Tool Credential Harvesting | — | Extract credentials via agent tool access |
| Exfiltration | Extract LLM System Prompt | — | Exfiltrate system prompt or instructions |
| Exfiltration | LLM Data Leakage | — | Leak training data or context via model outputs |
| Impact | Denial of AI Service | — | Disrupt or degrade AI service availability |
| Impact | Erode AI Model Integrity | — | Tamper with model or outputs |

---

## Skill Mapping

| Skill | ATLAS Use |
|-------|-----------|
| **security-evaluator** | When evaluating AI agents, MCP servers, RAG: assess prompt injection, jailbreak, credential harvesting, RAG poisoning, context poisoning, supply chain compromise, model integrity. Reference ATLAS tactics (Execution, Persistence, Defense Evasion, Credential Access, Exfiltration, Impact). |
| **ai-agent-architecture** | When assessing production readiness: consider ATLAS tactics mapped to 7 layers (e.g., Tooling → AI Agent Tool Invocation; Orchestration → LLM Prompt Injection; Memory → RAG Poisoning). |
| **ai-devsecops-policy-enforcement** | Supply chain and model artifact review aligns with ATLAS Initial Access, Resource Development. Model scanning should handle corrupt models (AML.T0076). |

---

## Related Frameworks

- **OWASP LLM Top 10** — Maps to ATLAS tactics; use both for LLM-specific coverage
- **NIST AI RMF** — ATLAS provides tactical detail for NIST risk measures
- **MITRE ATT&CK** — ATLAS extends to ML systems; ATT&CK covers infrastructure
