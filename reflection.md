# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, code quality problems, and style violations.

It is important because it helps developers identify problems early in the development process, improve maintainability, reduce security risks, and produce more reliable software.

## 2. What are the roles of Pylint, Bandit, and Flake8?

Pylint analyses Python code for programming mistakes, naming conventions, missing documentation, and maintainability issues.

Bandit identifies common security vulnerabilities in Python code, such as hardcoded passwords, unsafe temporary-file handling, and potentially dangerous shell execution.

Flake8 checks Python code for style and formatting violations, including whitespace, blank lines, and line length.

Using all three tools provides a more comprehensive analysis because each focuses on different aspects of code quality and security.

## 3. What issues were identified, and how were they resolved?

The original program had four Bandit findings: a hardcoded password, a hardcoded temporary directory, insecure use of `tempfile.mktemp()`, and shell command execution using `os.system()`.

The password was moved to an environment variable, the temporary directory was obtained using `tempfile.gettempdir()`, temporary-file creation was changed to `tempfile.NamedTemporaryFile()`, and shell execution was replaced with `webbrowser.open()` after checking that the report exists.

Pylint also identified missing docstrings, naming convention violations, broad exception handling, and inefficient iteration. These were addressed by adding documentation, improving naming conventions, removing unnecessary exception handling, and using `enumerate()`.

Flake8 identified four formatting violations, which were resolved by correcting spacing, blank lines, comments, and line length.

After the changes, the Pylint score increased from 5.27/10 to 9.85/10. Bandit reported no issues, and Flake8 reported no violations.

## 4. What did you learn about static analysis, and what are its limitations?

I learned that static analysis tools can identify security vulnerabilities, programming issues, and style violations before the program is executed. I also learned that different tools serve different purposes and that their findings should be reviewed and addressed appropriately.

However, static analysis cannot guarantee that a program is completely secure or correct. Some issues depend on runtime behaviour, user input, or the execution environment. Tools can also report warnings that require developer judgement. Therefore, static analysis should be combined with testing, code review, and good development practices.
