# AI Agent Architecture — Layer Reference

Detailed evaluation criteria and questions for each of the 7 layers.

---

## Layer 1: Language Model

### Questions to Ask

- What tasks does the model need to perform?
- Is reasoning depth or speed more important?
- Is data sensitivity pushing us toward hosted or self-managed models?
- Do we need tool use, JSON output, or long context?

---

## Layer 2: Memory and Context

### Questions to Ask

- What should the agent remember?
- What should expire?
- What belongs in prompt context vs retrieval?
- How do we prevent irrelevant or stale memory from polluting outputs?

---

## Layer 3: Tooling

### Questions to Ask

- What systems must the agent read from or write to?
- Which actions are safe to automate?
- What approvals are needed before write actions?
- How do we validate tool outputs?

---

## Layer 4: Orchestration

### Questions to Ask

- Is this actually multi-agent, or just a workflow?
- Which steps should be deterministic?
- Where do we need approvals?
- How do we recover from partial failure?

---

## Layer 5: Communication

### Questions to Ask

- Are agents calling tools directly or through a broker?
- Do we need streaming responses?
- What protocol best fits latency and reliability needs?
- How do we trace messages across the system?

---

## Layer 6: Infrastructure

### Questions to Ask

- Where will this run?
- What are the uptime and scale requirements?
- How will secrets and identity be handled?
- What does promotion from dev to prod look like?

---

## Layer 7: Evaluation

### Questions to Ask

- How do we know the agent is working?
- What does failure look like?
- What should be tested before release?
- What ongoing metrics belong on a dashboard?
