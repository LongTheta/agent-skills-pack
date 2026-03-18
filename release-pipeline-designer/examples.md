# Release Pipeline Designer — Examples

## Example 1: Node.js Library

**Input:** "Create a GitHub Actions pipeline for a Node library"

**Output:** .github/workflows/ci.yml with: install, lint, test, build. No deploy (library).

## Example 2: Container Image

**Input:** "Pipeline for building and pushing a Docker image"

**Output:** Build, test, lint, build image, push to registry. Manual approval for prod tag.

## Example 3: Multi-Environment

**Input:** "Pipeline with dev, stage, prod promotion"

**Output:** Deploy to dev on main; manual trigger for stage; manual approval for prod. Environment secrets documented.
