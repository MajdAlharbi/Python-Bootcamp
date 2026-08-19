# Week 4 - Day 1 - Object-Oriented Programming Basics

**Date:** 2026-08-16

## Overview

This lesson introduced Object-Oriented Programming (OOP) in Python using classes and objects to keep related data and behavior together.

## Topics Covered

- Classes and objects
- `__init__` and `self`
- Instance and class attributes
- Instance methods
- `__str__`
- Working with multiple objects

## Key Concepts

### Classes and Objects

A class defines a reusable object type, while an object is an instance created from that class.

```python
class Student:
    pass

student = Student()
```

### `__init__` and `self`

`__init__` sets the starting state of an object. `self` refers to the current object.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("Sara", 92)
```

### Attributes

Instance attributes belong to one object, while class attributes are shared defaults.

```python
class Student:
    academy = "Tuwaiq Academy"

    def __init__(self, name):
        self.name = name
```

### Instance Methods

Methods define actions an object can perform or values it can calculate.

```python
class Student:
    def __init__(self, scores):
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)
```

### `__str__`

`__str__` provides a readable description when an object is printed.

```python
def __str__(self):
    return f"{self.name}: {self.scores}"
```

### Collections of Objects

Objects can be stored in collections such as lists.

```python
students = [
    Student("Sara"),
    Student("Majd")
]

for student in students:
    print(student)
```

## Important Syntax / Patterns

```python
class ClassName:
    class_attribute = value

    def __init__(self, value):
        self.attribute = value

    def method(self):
        return self.attribute


obj = ClassName(value)

obj.attribute
obj.method()

type(obj)
isinstance(obj, ClassName)
```