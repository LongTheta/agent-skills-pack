# Test Strategy Designer — Reference

## Test Pyramid

- **Unit:** Fast, isolated, many. Business logic, pure functions.
- **Integration:** Fewer. DB, APIs, external services.
- **E2E:** Few. Critical user flows; slow, brittle.

## Coverage by Language

| Language | Tool | Typical target |
|----------|------|----------------|
| Python | pytest-cov | 70–80% |
| Node | Jest, c8 | 70–80% |
| Go | go test -cover | 70–80% |

## CI Integration

- Unit: Run on every PR; fail fast
- Integration: Run on PR or main; may be slower
- E2E: Run on main or nightly; optional gate
