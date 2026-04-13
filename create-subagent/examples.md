# Create Subagent — Examples

## Example 1: Code Reviewer

```
Create a code reviewer subagent. It should run git diff, focus on modified files, and provide feedback by priority: critical, warnings, suggestions. Store as a project subagent.
```

---

## Example 2: Debugger

```
Create a debugger subagent for root cause analysis. When invoked, it should capture errors, form hypotheses, implement minimal fixes, and verify. Use proactively when issues occur.
```

---

## Example 3: Data Scientist

```
Create a data scientist subagent for SQL and BigQuery. It should write efficient queries, use bq CLI when appropriate, and present findings clearly. Use proactively for data analysis tasks.
```

---

## Example 4: Documentation Writer

```
Create a documentation subagent. When invoked, it should analyze code, generate docstrings, update README sections, and follow our doc style guide. Store in .agent/agents/.
```
