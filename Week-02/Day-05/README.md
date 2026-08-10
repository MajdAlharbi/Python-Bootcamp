# Week 2 - Day 5 - Python Loops

**Date:** 2026-08-06

## Overview

This lesson covered how loops repeat code using `for` and `while`. It also introduced `range()`, counters, accumulators, loop control, and nested loops.

## Topics Covered

- `for` loops
- `range()`
- Looping through strings and lists
- Conditions inside loops
- Counters and accumulators
- `while` loops
- `break`, `continue`, and `pass`
- Nested loops

## Key Concepts

### `for` Loop

Use `for` when looping through a known range or sequence.

```python
for number in range(1, 6):
    print(number)
```

### `range()`

`range()` generates numbers for a loop.

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

The `stop` value is not included.

### Looping Through Sequences

A `for` loop can go through strings and lists.

```python
for letter in "Python":
    print(letter)
```

### Conditions Inside Loops

Conditions can control what happens during each iteration.

```python
for number in range(1, 6):
    if number % 2 == 0:
        print("Even")
```

### Counter and Accumulator

A counter counts events, while an accumulator builds a total.

```python
count += 1
total += number
```

### `while` Loop

Use `while` when repetition depends on a condition.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

The condition must eventually become `False` to avoid an infinite loop.

### Loop Control

- `break` — stops the loop
- `continue` — skips the current iteration
- `pass` — does nothing

### Nested Loops

A loop can run inside another loop.

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

## Important Syntax / Patterns

```python
for item in sequence:
    ...

for number in range(start, stop, step):
    ...

while condition:
    ...

break
continue
pass
```

## Quick Review

- A loop repeats code.
- `for` is used with known ranges or sequences.
- `while` is used when repetition depends on a condition.
- `range()` excludes the stop value.
- Counters count events; accumulators build totals.
- `break` stops a loop.
- `continue` skips one iteration.
- `pass` does nothing.
