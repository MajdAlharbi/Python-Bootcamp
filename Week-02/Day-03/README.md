Week 02 - Day 03
Python Operators and Strings

Topics Covered

1. Arithmetic Operators
- + addition
- - subtraction
- * multiplication
- / division
- // floor division
- % remainder
- ** exponentiation

Example:
7 / 3   = 2.33
7 // 3  = 2
7 % 3   = 1

2. Operator Precedence
Python follows this order:
1. Parentheses ()
2. Exponentiation **
3. Multiplication and division: *, /, //, %
4. Addition and subtraction: +, -

3. Assignment Operators
Used to update variable values:
+=, -=, *=, /=, //=, %=, **=

Example:
score += 5
means:
score = score + 5

4. Comparison and Logical Operators
Comparison operators:
==, !=, >, <, >=, <=

Logical operators:
- and: both conditions must be True
- or: at least one condition must be True
- not: reverses the result

5. Membership and Identity
Membership operators:
in, not in

Identity operators:
is, is not

Key difference:
- == compares values
- is compares whether two variables refer to the same object

6. String Indexing and Slicing
Indexing starts from 0.

Example:
text = "Python"
text[0]   # P
text[-1]  # n

Slicing format:
text[start:stop:step]

The start is included, but the stop is excluded.

Examples:
text[:3]
text[2:]
text[::-1]

7. String Methods
Common methods practiced:
- strip()
- upper()
- lower()
- title()
- replace()
- find()
- split()
- join()

Important:
Strings are immutable, so string methods return a new string instead of changing the original one.

8. Mutable and Immutable Objects
Immutable examples:
str, int, float, tuple

Mutable examples:
list, dict, set

Labs Practiced
- Arithmetic calculations
- Floor division and remainder
- Assignment operators
- Comparison and logical conditions
- Membership checks
- String indexing and slicing
- Reversing text
- Cleaning and transforming strings
- split() and join()
- Difference between == and is
- Checking object identity using id()

Key Takeaways
- / gives a decimal result.
- // gives whole groups.
- % gives the remainder.
- == compares values.
- is compares object identity.
- Strings are immutable.
- Indexing starts at 0.
- Slicing excludes the stop position.