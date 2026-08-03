# Python Syntax and Variables

In this class, I learned the basic structure and syntax of Python programs.

## Topics Covered

### 1. Python Structure

- Python is case-sensitive, so `student_name` and `Student_name` are different variables.
- A new line usually ends a statement.
- A colon `:` starts a code block.
- Indentation determines which statements belong to the same block.
- Python convention uses four spaces for indentation.
- Comments begin with `#` and are not executed.

```python
score = 75

if score >= 60:
    print("You passed the exam.")
else:
    print("You failed the exam.")
```

### 2. Variables and Data Types

Variables store different types of values:

```python
student_name = "Sara"          # str
student_age = 20               # int
course_name = "Python"         # str
registered = True              # bool
```

The `type()` function identifies the data type:

```python
print(type(student_name))
print(type(student_age))
```

The `isinstance()` function checks whether a value belongs to a specific type:

```python
print(isinstance(student_age, int))
```

### 3. Variable Naming Rules

Valid variable names:

```python
student_name = "Majd"
total_price = 100
_is_valid = True
MAX_CLASS_SIZE = 25
```

Variable names:

- Cannot begin with a number.
- Cannot contain spaces or hyphens.
- Cannot use reserved Python keywords.
- Should use clear and meaningful names.
- Usually follow `snake_case`.
- Constants are written in uppercase by convention.

### 4. Formatted Strings

An f-string allows variables to be included inside text:

```python
print(
    f"Welcome {student_name}! You are {student_age} years old."
)
```

Triple quotes can be used for multiple lines:

```python
print(f"""
Welcome {student_name}!
You are enrolled in {course_name}.
""")
```

### 5. User Input and Type Conversion

The `input()` function always returns a string. It can be converted into an integer using `int()`:

```python
age = int(input("Enter your age: "))
print("After 5 years, you will be", age + 5)
```

### 6. Strings and Indexes

Characters inside a string can be accessed using their index. Indexes start from `0`.

```python
teacher_name = "faisal"

print(teacher_name[0])  # f
print(len(teacher_name))
```

The index should be checked before accessing it:

```python
index = int(input("Select an index: "))

if 0 <= index < len(teacher_name):
    print(teacher_name[index])
else:
    print("Index is out of bounds.")
```

## Key Takeaways

- Python reads the written structure, not the programmer’s intention.
- Correct indentation is essential.
- Variable names are case-sensitive.
- `type()` returns the data type.
- `isinstance()` checks a value against a specific type.
- `len()` returns the number of characters in a string.
- User input must be converted when a numeric value is required.