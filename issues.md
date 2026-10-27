# Lab 5: Static Code Analysis — Issue Log

## Objective

To identify and fix code quality, security, and formatting issues using Pylint, Bandit, and Flake8.

## Issues Identified and Fixed

| Issue | Type / Tool | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Hardcoded password | Security — Bandit B105 | 5 | The bank-sync password was directly embedded in the source code, which could expose credentials. | Replaced the hardcoded password with an environment variable using `os.environ.get()`. |
| Hardcoded temporary directory | Security — Bandit B108 | 8 | The report directory was hardcoded to `/tmp/expense_reports`, which is not portable and can create security concerns. | Used `tempfile.gettempdir()` to obtain the system's temporary directory and created the report directory beneath it. |
| Insecure temporary-file creation | Security — Bandit B306 | 55 | `tempfile.mktemp()` generates a temporary filename without securely creating the file, potentially introducing a race condition. | Replaced it with `tempfile.NamedTemporaryFile()` to securely create a uniquely named temporary file. |
| Shell command execution | Security — Bandit B605 | 61 | `os.system()` executed a shell command using a file path, creating a potential command-injection vulnerability. | Replaced shell execution with `webbrowser.open()` and validated that the report exists before opening it. |
| Missing module and function docstrings | Code quality — Pylint C0114, C0116 | Multiple | The original code lacked documentation for the module and several functions. | Added a module docstring and appropriate function docstrings. |
| Incorrect naming conventions | Code quality — Pylint C0103 | Multiple | Function names and variables did not consistently follow Python naming conventions. | Renamed functions and variables to follow `snake_case` and used uppercase naming for the budget constant. |
| Broad exception handling | Code quality — Pylint W0718 | 41 | Catching the general `Exception` class could hide unexpected errors. | Removed the unnecessary exception handling and used `max()` with `default=None` for an empty expense list. |
| Inefficient iteration | Code quality — Pylint C0200 | 45 | Iterating with `range()` and `len()` was unnecessarily complicated. | Replaced it with `enumerate()` to iterate over expenses while maintaining their numbering. |
| Formatting violations | Style — Flake8 E203, E302, E261, E501 | Multiple | The original code contained spacing, blank-line, inline-comment, and line-length violations. | Corrected spacing, added the required blank lines, and split long lines. |

## Before-and-After Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.27/10 | 9.85/10 |
| Bandit | 4 findings: 1 Low, 2 Medium, 1 High | No issues identified |
| Flake8 | 4 violations | No violations reported |

## Conclusion

Static code analysis helped identify security vulnerabilities, code quality problems, and formatting violations. The fixes improved the program's security, readability, maintainability, and adherence to Python coding standards.

Pylint's final score was 9.85/10, exceeding the required target of 9.5. Bandit reported no remaining issues, and Flake8 reported no formatting violations. Pylint still reported a W0603 warning related to the use of a `global` statement in the budget-setting function. This warning was not suppressed.
