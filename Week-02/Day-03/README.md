# Week 2 - Day 3 - Python Operators and Strings

**Date:** 2026-08-04

## Overview

This lesson covered the main Python operators and how they are used in expressions and comparisons. It also introduced string indexing, slicing, common string methods, and the difference between equality and object identity.

## Topics Covered

- Arithmetic and assignment operators
- Comparison and logical operators
- Membership and identity operators
- Operator precedence
- String indexing and slicing
- Common string methods
- `split()` and `join()`
- String immutability

## Key Concepts

### Python Operators

Arithmetic operators perform calculations:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` floor division
- `%` remainder
- `**` exponentiation

```python
print(7 / 3)   # 2.33...
print(7 // 3)  # 2
print(7 % 3)   # 1
```

Assignment operators update an existing value:

```python
score = 10
score += 5
```

### Comparison and Logical Operators

Comparison operators return `True` or `False`.

```python
age >= 18
score == 90
score != 50
```

Logical operators combine conditions:

- `and` → both conditions must be True
- `or` → at least one condition must be True
- `not` → reverses a Boolean value

### Membership and Identity

`in` and `not in` check whether a value exists inside a string or collection.

```python
"Py" in "Python"   # True
```

`==` compares values, while `is` compares whether two variables refer to the same object.

```python
first == second
first is second
```

### String Indexing and Slicing

String indexes start at `0`. Negative indexes count from the end.

```python
text = "Python"

text[0]     # P
text[-1]    # n
text[0:3]   # Pyt
```

Slicing follows:

```python
text[start:stop:step]
```

The `stop` position is not included.

### String Methods

Common string methods include:

- `strip()` — removes surrounding spaces
- `lower()` / `upper()` — changes letter case
- `replace()` — replaces text
- `find()` — finds a position
- `split()` — splits text into a list
- `join()` — combines strings

```python
text = "  Python Bootcamp  "

text.strip()
text.lower()
text.replace("Bootcamp", "Course")
```

### String Immutability

Strings are immutable, which means they cannot be changed in place. String methods return a new string, so the result should be stored if you want to keep the change.

```python
name = "python"
name = name.upper()
```

## Important Syntax / Patterns

```python
# Arithmetic
+  -  *  /  //  %  **

# Comparison
==  !=  >  <  >=  <=

# Logical
and  or  not

# Membership
in  not in

# Identity
is  is not

# String slicing
text[start:stop:step]

# Common methods
strip()
lower()
upper()
replace()
find()
split()
join()
```

## Quick Review

- `/` gives normal division, `//` gives whole groups, and `%` gives the remainder.
- Python follows operator precedence when evaluating expressions.
- Comparison operators return `True` or `False`.
- `and`, `or`, and `not` combine Boolean conditions.
- `in` checks membership.
- `==` compares values; `is` compares object identity.
- String indexes start at `0`, and slicing excludes the stop position.
- Strings are immutable, so methods return new strings.
