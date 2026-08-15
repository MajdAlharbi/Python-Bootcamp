# Week 3 - Day 1 - Python Functions

**Date:** 2026-08-09

## Overview

This lesson covered how functions organize reusable code in Python. It introduced parameters, arguments, default values, `return`, docstrings, and using conditions inside functions.

## Topics Covered

- Defining and calling functions
- Parameters and arguments
- Positional and keyword arguments
- Default parameters
- `return` vs `print`
- Functions with conditions
- Docstrings

## Key Concepts

### Defining and Calling Functions

A function is a reusable block of code that performs a specific task. Use `def` to define it, then call it using its name followed by `()`.

```python
def greet():
    print("Hello")

greet()
```

### Parameters and Arguments

Parameters are variables written in the function definition. Arguments are the actual values passed when calling the function.

```python
def greet(name):
    print(f"Hello {name}")

greet("Majd")
```

Arguments can be passed by position or by parameter name.

### Default Parameters

A parameter can have a default value that is used when no argument is provided.

```python
def show_booking(destination="Riyadh", nights=1):
    print(destination, nights)

show_booking()
show_booking("Jeddah", 5)
```

Required parameters should come before parameters with default values.

### `return`

`return` sends a value back from a function so it can be stored or reused. It also ends the current function call.

```python
def add(a, b):
    return a + b

total = add(5, 3)
```

`print()` only displays a value, while `return` gives the value back to the caller.

### Functions with Conditions

Functions can contain conditions and other Python logic.

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "F"
```

### Docstrings

A docstring briefly explains what a function does. It is written as the first statement inside the function.

```python
def get_vat(total, rate=0.15):
    """Return the total after adding VAT."""
    return total + (total * rate)
```

## Important Syntax / Patterns

```python
def function_name():
    ...

def function_name(parameter):
    ...

def function_name(parameter="default"):
    ...

return value

function_name(argument)
function_name(parameter=value)
```

## Quick Review

- `def` defines a function.
- `()` calls a function.
- A parameter is written in the function definition.
- An argument is passed when calling the function.
- Default parameters are used when an argument is omitted.
- Positional arguments depend on order; keyword arguments use parameter names.
- `return` sends a result back; `print()` only displays it.
- Docstrings explain what a function does.
