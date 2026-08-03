# Day 01 - Python Workflow and Virtual Environments

Today I reviewed the basic Python development workflow and practiced creating and running Python files.

## Topics Covered

- Creating and running Python files
- Using functions
- Reading user input with `input()`
- Converting input using `int()`
- Creating a virtual environment
- Installing packages with `pip`
- Checking code quality with Flake8
- Saving dependencies in `requirements.txt`

## Typical Python Workflow

1. Create the project folder.
2. Create and activate a virtual environment.
3. Install the required packages.
4. Write and test Python code.
5. Save the installed dependencies.

## Virtual Environment

A virtual environment creates an isolated workspace for each Python project.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

To exit the virtual environment:

```powershell
deactivate
```

## Package Management

Install Flake8:

```powershell
pip install flake8
```

Check the installed version:

```powershell
flake8 --version
```

Save the installed packages:

```powershell
pip freeze > requirements.txt
```

## Flake8

Flake8 is a linter that checks Python code for quality and style issues.

It can detect:

- Syntax issues
- Unused variables
- Formatting problems
- PEP 8 violations

## Practice

I created Python programs that:

- Printed a simple message
- Read two numbers from the user
- Added the numbers
- Used functions to organize the code
