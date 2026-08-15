# Week 03 - Day 04-05 - Python Comprehensions and Copying

**Date:** 2026-08-14-13

## Overview

This lesson covered Python comprehensions, generator expressions, and copying mutable objects.

## Topics Covered

- List comprehensions
- Filters and conditional expressions
- Set and dictionary comprehensions
- Generator expressions
- Shallow copy and deep copy
- Mutable and immutable objects
- Lookup with sets and dictionaries

## Key Concepts

### Comprehensions

```python
squares = [number**2 for number in numbers]

passing_scores = [
    score
    for score in scores
    if score >= 60
]
```

### Conditional Expression

```python
labels = [
    "pass" if score >= 60 else "retry"
    for score in scores
]
```

### Set and Dictionary Comprehensions

```python
domains = {email.split("@")[1].lower() for email in emails}

squares = {number: number**2 for number in numbers}
```

### Generator Expressions

```python
total = sum(number**2 for number in numbers)
```

### Copying

```python
clone = original.copy()
```

A shallow copy creates a new outer container but may still share nested objects.

```python
from copy import deepcopy

clone = deepcopy(original)
```

A deep copy creates independent nested objects.

## Important Syntax / Patterns

```python
[expression for item in collection]
[expression for item in collection if condition]

{expression for item in collection}
{key: value for item in collection}

(expression for item in collection)

original.copy()
deepcopy(original)
```

## Quick Review

- Comprehensions create collections in a shorter form.
- `if` can filter items.
- Generators produce values when needed.
- Shallow copies may share nested objects.
- Deep copies create independent nested objects.
- Sets and dictionaries are useful for fast lookup.