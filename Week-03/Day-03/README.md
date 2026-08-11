Week 03 - Day 03 - Python Collections

Date: 2026-08-11

Overview

Learned how Python collections store multiple values using lists, tuples, sets, and dictionaries. The lesson focused on how each collection behaves and when to use it.

Topics Covered

Lists, indexing, and slicing

List methods and loops

Tuples and unpacking

Sets and set operations

Dictionaries

Nested collections

Common collection errors

Key Concepts

Lists

Lists are ordered and changeable. They allow duplicate values.

students = ["Sara", "Majd", "Lina"]

print(students[0])
print(students[-1])

Slicing selects part of a list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[::-1])

Common methods:

items.append(value)
items.insert(index, value)
items.remove(value)
items.pop()
items.sort()

Tuples

Tuples are ordered but cannot be changed after creation.

location = (24.1234, 46.4379)

Unpacking assigns values to variables.

name, age, course = ["Sara", 22, "Python"]

Sets

Sets keep only unique values and do not use indexes.

skills = {"Python", "Git", "Python"}
skills.add("Django")

Set operations:

set1 | set2   # union
set1 & set2   # intersection
set1 - set2   # difference

Dictionaries

Dictionaries store data as key: value pairs.

student = {
    "name": "Sara",
    "score": 95
}

print(student["name"])

Useful methods:

student.get("email", "Not set")
student.pop("score")

for key, value in student.items():
    print(key, value)

Nested Collections

Collections can contain other collections.

students = [
    {
        "name": "Sara",
        "scores": (99, 80, 90),
        "skills": {"Python", "SQL"}
    }
]

Important Syntax / Patterns

items[0]
items[-1]
items[start:stop:step]

for index, item in enumerate(items):
    print(index, item)

len(collection)
value in collection

Quick Review

list → ordered and changeable

tuple → ordered and fixed

set → unique values

dictionary → key-value pairs

Indexes start at 0

enumerate() gives index and value

remove() deletes by value; pop() removes and returns an item

Common errors include IndexError, KeyError, and TypeError