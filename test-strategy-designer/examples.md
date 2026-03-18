# Test Strategy Designer — Examples

## Example 1: Python API

**Input:** "Design a test strategy for a FastAPI service"

**Output:**
- Unit: pytest, 80% coverage on business logic
- Integration: TestClient, DB fixtures
- E2E: Optional; minimal for MVP
- CI: pytest in GitHub Actions; fail on coverage drop

## Example 2: React SPA

**Input:** "Test strategy for a React app"

**Output:**
- Unit: Vitest, Jest; components
- Integration: React Testing Library
- E2E: Playwright for critical flows
- CI: Unit on PR; E2E on main

## Example 3: Go Library

**Input:** "Test strategy for a Go library"

**Output:**
- Unit: go test, table-driven
- Integration: Testcontainers for DB
- Benchmark: go test -bench
- CI: go test -race; coverage badge
