
# Lab 5: Static Code Analysis — Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Weak MD5 hash (B324) | Security — High | 15 | MD5 is weak for security-sensitive hashing. | Replace MD5 with SHA-256. |
| Possible SQL injection (B608) | Security — Medium | 9 | SQL is constructed using string formatting, allowing input to alter the query. | Use parameterized SQL with `?` placeholders. |
| Mutable default argument | Bug / Reliability | 8 | `extras={}` can be shared between function calls. | Use `extras=None` and initialize a dictionary inside the function. |
| Assertion used for validation (B101) | Reliability — Low | 36 | Assertions can be disabled in optimized execution mode. | Replace the assertion with an explicit conditional check. |
| Missing docstrings and non-standard names | Style / Maintainability | 1, 8, 14, 18, 26, 32 | Functions lack documentation and use camelCase names. | Add docstrings and use `snake_case`. |
| Long lines (E501) | Style | 5, 9, 19, 27 | Several lines exceed the configured length limit. | Split long statements across multiple lines. |
| Ambiguous variable name (E741) | Style | 28 | The variable `l` is difficult to distinguish from `1`. | Rename it to `rarest_species`. |
| Missing whitespace (E225) | Style | 28 | Missing spaces around the assignment operator. | Use `rarest_species = min(...)`. |
| Empty database edge case | Bug / Reliability | 27–28 | `min()` fails if the query returns no rows. | Check for empty results and return `None`. |
