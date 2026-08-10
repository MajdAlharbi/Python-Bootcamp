# Week 2 - Day 2 - Python Syntax and Variables

**Date:** 2026-08-03

## Overview

This lesson covered the basic structure of Python code and how variables are used. It also introduced data types, f-strings, user input, type conversion, and string indexing.

## Topics Covered

- Python structure and indentation
- Variable naming rules
- Data types
- `type()` and `isinstance()`
- f-strings
- `input()` and type conversion
- String indexing

## Key Concepts

### Python Structure

Python is case-sensitive, and indentation defines code blocks. Colons `:` start blocks, while comments begin with `#`.

```python
if score >= 60:
    print("Passed")
```

### Variables and Data Types

Variables store values. Common types include `str`, `int`, `float`, and `bool`.

```python
name = "Sara"
age = 20
registered = True
```

`type()` shows the data type, while `isinstance()` checks whether a value belongs to a specific type.

### Variable Naming

Variable names cannot start with a number, contain spaces or hyphens, or use Python keywords. Clear names usually use `snake_case`.

### f-Strings

f-strings insert variables directly inside text.

```python
print(f"Welcome {name}, you are {age} years old.")
```

### User Input

`input()` always returns a string, so convert it when a number is needed.

```python
age = int(input("Enter your age: "))
```

### String Indexing

String indexes start at `0`, and `len()` returns the string length.

```python
name = "Faisal"
print(name[0])   # F
print(len(name))
```

## Important Syntax / Patterns

```python
type(value)
isinstance(value, int)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Welcome {name}")

text[0]
len(text)
```

## Quick Review

- Python is case-sensitive.
- Indentation defines code blocks.
- Use clear variable names with `snake_case`.
- `type()` shows a data type; `isinstance()` checks a type.
- `input()` returns a string.
- f-strings insert variables into text.
- String indexing starts at `0`.
