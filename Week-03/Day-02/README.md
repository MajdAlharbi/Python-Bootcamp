Week 03 - Day 02 - Python Scope and Modules

Date: 2026-08-10

Overview

Learned how Python finds and manages names using namespaces and scope. The lesson also introduced modules, imports, the __name__ == "__main__" pattern, and common import problems.

Topics Covered

Names, namespaces, and scope

LEGB lookup order

Local, enclosing, global, and built-in scope

globals(), locals(), and nonlocal

Shadowing

Modules and imports

Standard-library modules

Custom modules and the main guard

Packages, dependencies, and import errors

Key Concepts

Scope and LEGB

Python searches for names in this order:

Local -> Enclosing -> Global -> Built-in

The first matching name is used.

Local, Enclosing, and Global

Variables created inside a function are usually local. Nested functions can access enclosing names, while names created at the top level of a file belong to the module's global scope.

rate = 0.15

def get_total(amount):
    return amount * rate + amount

nonlocal

nonlocal lets an inner function modify a variable from its enclosing function.

def outer():
    value = 1

    def inner():
        nonlocal value
        value += 2

Shadowing

A nearer name can hide another name with the same name in an outer scope.

Avoid using built-in names such as type, list, or sum for your own variables or functions.

Modules and Imports

A module is a reusable Python .py file.

import grades

print(grades.calculate_grad(88))

Python also provides standard-library modules such as math, random, datetime, and statistics.

Main Guard

Use the main guard when code should run only if the file is executed directly.

if __name__ == "__main__":
    print("Run directly")

When the file is imported, this block does not run.

Important Syntax / Patterns

globals()
locals()

import module
from module import name
import module as alias

if __name__ == "__main__":
    ...

Avoid:

from module import *

Also avoid filenames such as:

math.py
random.py
statistics.py

because they can conflict with Python modules.

Quick Review

A namespace maps names to objects.

Scope determines where Python searches for a name.

Python follows LEGB: Local, Enclosing, Global, Built-in.

Each function call gets its own local namespace.

nonlocal changes a variable from the enclosing scope.

Shadowing happens when a nearer name hides an outer name.

A module is a reusable .py file.

__name__ == "__main__" separates direct execution from importing.