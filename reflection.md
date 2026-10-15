
# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and coding-style violations early in development. In this lab, static analysis helped improve the quality, security, and maintainability of the wildlife sightings program.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks overall code quality, naming conventions, documentation, and potential programming problems. Bandit identifies common security issues in Python code. Flake8 checks coding style, formatting, and common errors. Using all three provides a broader review of the program.

## 3. What issues did you identify, and how did you fix them?

The original program contained a possible SQL injection vulnerability, an MD5 hash warning, a mutable default argument, an assertion, missing docstrings, non-standard function names, and formatting violations. I replaced SQL string formatting with parameterized queries, changed MD5 to SHA-256, replaced the mutable default with None, and replaced the assertion with an explicit conditional check. I also improved naming, documentation, formatting, and handling of empty database results.

## 4. What did you learn about the benefits and limitations of static analysis?

I learned that a program can run successfully while still containing security and maintainability problems. Static analysis tools provide useful automated feedback, but their findings need to be interpreted and their fixes tested. A clean report does not guarantee that a program is completely correct or secure, so runtime testing remains important.
