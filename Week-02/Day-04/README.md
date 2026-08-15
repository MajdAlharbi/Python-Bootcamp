# Week 2 - Day 4 - Conditions 

**Date:** 2026-08-05

## Overview

This lesson covered how Python uses conditions to control program flow and how user input can be validated before processing. It also introduced Truthy/Falsy values, nested conditions, and `match-case`.

## Topics Covered

- `if`, `elif`, and `else`
- Logical operators
- Nested conditions
- Truthy and Falsy values
- Input validation
- Range and membership validation
- Conditional expressions
- `match-case`

## Key Concepts

### Conditions

Conditions evaluate to `True` or `False` and decide which code block runs.

```python
age = 20

if age >= 18:
    print("Welcome")
```

Python checks `if / elif / else` from top to bottom and stops at the first `True` condition.

### Logical Operators

Logical operators combine conditions:

- `and` — both conditions must be True
- `or` — at least one condition must be True
- `not` — reverses a Boolean value

```python
if is_active and is_verified:
    print("Account is ready")
```

### Truthy and Falsy Values

Python can treat values directly as conditions.

Common Falsy values include:

- `False`
- `None`
- `0`
- `""`
- empty collections such as `[]`

### Input Validation

Input should be checked before converting or processing it.

```python
age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
```

Useful validation methods:

- `strip()` — removes surrounding spaces
- `isdigit()` — checks for digits
- `isalpha()` — checks for letters
- `isalnum()` — checks for letters and digits

### Range and Membership Validation

Use comparisons for ranges and `in` for allowed choices.

```python
if 0 <= score <= 100:
    print("Valid score")

if membership in ["Admin", "Editor", "Viewer"]:
    print("Allowed")
```

### `match-case`

`match-case` is useful when comparing one value against several fixed options.

```python
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Invalid command")
```

## Important Syntax / Patterns

```python
if condition:
    ...
elif condition:
    ...
else:
    ...

and
or
not

value if condition else other_value

match value:
    case "option":
        ...
    case _:
        ...
```

## Quick Review

- Conditions control which code runs.
- `if / elif / else` are checked from top to bottom.
- `and`, `or`, and `not` combine Boolean conditions.
- Empty strings, zero, `None`, and empty collections are Falsy.
- Validate input before converting it.
- Use range checks for numeric limits.
- Use `in` to check allowed choices.
- Use `match-case` for fixed options.