# Week 2 - Day 1 - Python Workflow and Virtual Environments

**Date:** 2026-08-02

## Overview

This lesson covered the basic Python project workflow and how to prepare a project environment. It introduced virtual environments, package management with `pip`, Flake8, and saving dependencies in `requirements.txt`.

## Topics Covered

- Python files and functions
- User input and type conversion
- Virtual environments
- Python project workflow
- `pip` and package installation
- Flake8
- `requirements.txt`

## Key Concepts

### Virtual Environment

A virtual environment is an isolated Python workspace for one project. It keeps project packages and versions separate from other projects.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Python Project Workflow

A simple Python project usually follows four steps:

1. **Setup** — create the project and virtual environment.
2. **Dependencies** — install required packages.
3. **Development** — write, run, and test the code.
4. **Snapshot** — save the installed dependencies.

### Package Management

`pip` is used to install Python packages. `requirements.txt` stores the packages and versions used by the project.

```powershell
pip install flake8
pip freeze > requirements.txt
```

### Flake8

Flake8 is a linter used to check Python code for style and common code issues.

## Important Syntax / Patterns

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flake8
flake8 --version
pip freeze > requirements.txt
deactivate
```

## Quick Review

- `.py` files contain Python code.
- Functions organize reusable code.
- `input()` returns a string.
- Virtual environments isolate project packages.
- `pip` installs packages.
- Flake8 checks code quality and style.
- `requirements.txt` saves project dependencies.
- Workflow: **Setup → Dependencies → Development → Snapshot**.

## Project

**Unit 1 Project — Automated Python Project Setup**

Create a script that generates a Python project structure, documents the project, initializes Git, and pushes it to GitHub.

🔗 https://github.com/MajdAlharbi/project-unit1
