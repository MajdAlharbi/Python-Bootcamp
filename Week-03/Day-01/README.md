# Python Functions

## What is a Function?
A function is a reusable block of code that performs a specific task.

Instead of repeating the same code many times, we write it once inside a function and call it whenever needed.

## Defining and Calling a Function

```python
def greet():
    print("Hello")

greet()
```

- `def` creates the function.
- `greet` is the function name.
- `()` is used when calling the function.
- The function body runs only when the function is called.

## Parameters and Arguments

A parameter is a variable written in the function definition.

An argument is the actual value passed when calling the function.

```python
def greet(name):
    print(f"Hello, {name}")

greet("Sara")
```

- `name` is a parameter.
- `"Sara"` is an argument.

## Positional Arguments

Positional arguments are matched by order.

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Sara", 22)
```

The first argument goes to the first parameter, and the second argument goes to the second parameter.

## Keyword Arguments

Keyword arguments are matched using parameter names.

```python
introduce(age=22, name="Sara")
```

The order can change because the parameter names are written explicitly.

## Default Parameters

A default value is used when an argument is not provided.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Sara")
greet("Sara", "Welcome")
```

Parameters without default values should come before parameters with default values.

## return

`return` sends a result back to the caller.

```python
def add(a, b):
    return a + b

total = add(5, 3)
print(total)
```

`return` also ends the current function call.

## return vs print

- `return` sends a value back so it can be stored or reused.
- `print` only displays a value on the screen.

```python
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 4)
print(area)
```

## Functions with Conditions and Loops

Functions can contain concepts we already know, such as:

- `if / elif / else`
- `for`
- `while`

Example:

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
```

## Docstrings

A docstring explains what a function does.

```python
def calculate_tax(amount, rate):
    """Return the tax amount for a given rate."""
    return amount * rate
```

It is written as the first statement inside the function.

## Good Function Practices

- Use clear function names such as `calculate_total()` or `validate_age()`.
- Use clear parameter names.
- Keep each function focused on one task.
- Provide all required arguments.
- Be careful with positional argument order.
- Do not confuse `print` with `return`.
- Define a function before calling it.

## Quick Summary

```text
def        -> defines a function
parameter  -> variable in the function definition
argument   -> value passed to the function
()         -> calls the function
return     -> sends a result back
print      -> displays output
docstring  -> explains the function
```