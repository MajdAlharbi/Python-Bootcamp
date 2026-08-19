# Week 4 - Days 2-3 - File and Exception Handling

**Date:** 2026-08-17 - 2026-08-18

## Overview

This lesson covered how Python works with files and handles errors. It introduced file paths using `pathlib`, file modes, reading and writing text files, CSV and JSON, and exception handling using `try`, `except`, `else`, `finally`, and `raise`.

## Topics Covered

- File paths with `pathlib.Path`
- Creating and inspecting paths
- File modes: `r`, `w`, `a`, and `x`
- Reading and writing files
- Using `with`
- UTF-8 and newlines
- CSV and JSON files
- `try` and `except`
- `else` and `finally`
- `raise`
- Custom exceptions

## Key Concepts

### File Paths with `pathlib`

`Path` represents a file or directory path as an object. The `/` operator can combine path parts.

```python
from pathlib import Path

data_file = Path("data") / "students.txt"

print(data_file.name)
print(data_file.suffix)
```

Paths can also be checked before using them.

```python
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

print(data_dir.is_dir())
print(data_file.exists())
```

### File Modes

File modes control how a file is opened.

- `r` reads an existing file.
- `w` writes and replaces existing content.
- `a` appends after existing content.
- `x` creates a new file only if it does not already exist.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")
```

### Reading Files

`with` closes the file automatically when the block finishes.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

Files can also be processed line by line.

```python
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)
```

### Writing and Appending

Mode `w` replaces existing content, while mode `a` keeps the existing content and adds new data at the end.

```python
with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Sara\nAli\n")
```

```python
with open("activity.log", "a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")
```

### CSV and JSON

CSV stores data in rows and columns.

```python
import csv

with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["Majd", "Python"])
```

JSON can store structured data such as lists and dictionaries.

```python
import json

students = [{"name": "Sara", "score": 93}]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
```

### Exception Handling

`try` contains code that may fail, while `except` handles expected errors.

```python
try:
    score = int(input("Score: "))
except ValueError:
    print("Enter a whole number")
```

Specific errors can be handled separately.

```python
try:
    text = Path("students.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("Student file not found")
except PermissionError:
    print("Student file cannot be read")
```

### `else`, `finally`, and `raise`

`else` runs when `try` succeeds, while `finally` runs whether the operation succeeds or fails.

```python
try:
    text = path.read_text(encoding="utf-8")
except OSError:
    print("Load failed")
else:
    print(text)
finally:
    print("Load attempt finished")
```

`raise` can be used to reject invalid data.

```python
def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be 0 to 100")
    return score
```

### Custom Exceptions

Custom exceptions give application-specific errors a clear name.

```python
class StudentNotFoundError(Exception):
    pass
```

## Important Syntax / Patterns

```python
from pathlib import Path

Path("data").mkdir(exist_ok=True)

with open("file.txt", "r", encoding="utf-8") as file:
    text = file.read()

with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Text")

with open("file.txt", "a", encoding="utf-8") as file:
    file.write("New text\n")

try:
    ...
except SomeError:
    ...
else:
    ...
finally:
    ...

raise ValueError("Invalid value")
```

## Quick Review

- `Path` helps create and inspect file paths.
- `r` reads, `w` replaces, `a` appends, and `x` creates.
- `with` closes files automatically.
- UTF-8 keeps text encoding predictable.
- CSV stores rows and columns.
- JSON stores structured data such as lists and dictionaries.
- `try` and `except` handle expected errors.
- `else` runs when `try` succeeds.
- `finally` runs regardless of the result.
- `raise` rejects invalid data.
- Custom exceptions give failures clear names.