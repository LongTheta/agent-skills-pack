# Shell — Examples

## Example 1: Simple Command

```
/shell ls -la
```

---

## Example 2: Multi-line Script

```
/shell
cd project && npm install && npm run build
```

---

## Example 3: With Pipes

```
/shell git status | head -20
```

---

## Example 4: No Command

```
/shell
```

*Response: Ask which command to run.*
