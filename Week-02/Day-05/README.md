# Python Loops Summary

## Loop
A loop repeats a block of code more than once.
Each repetition is called an iteration.

## for Loop
Use a for loop when the number of repetitions is known or when processing a sequence.

```python
for number in range(1, 6):
    print(number)
```

## range()
```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:
- `range(5)` → 0, 1, 2, 3, 4
- `range(1, 6)` → 1, 2, 3, 4, 5
- `range(2, 11, 2)` → 2, 4, 6, 8, 10
- `range(10, 0, -1)` → counts backward from 10 to 1

The stop value is not included.

## Loop Through a String
```python
course = "python"

for letter in course:
    print(letter)
```

## Loop Through a List
```python
students = ["majd", "sara", "ali"]

for student in students:
    print(student)
```

## Conditions Inside a Loop
```python
for number in range(1, 6):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
```

## Counter
A counter records how many times something happens.

```python
count = 0

for number in range(1, 11):
    if number % 2 == 0:
        count += 1
```

## Accumulator
An accumulator builds a total over time.

```python
total = 0

for number in range(1, 6):
    total += number
```

## while Loop
Use a while loop when repetition depends on a condition.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Always update the condition to avoid an infinite loop.

## break
Stops the loop completely.

```python
if command == "exit":
    break
```

## continue
Skips only the current iteration.

```python
if number == 3:
    continue
```

## pass
Does nothing. It is used as a temporary placeholder.

```python
if condition:
    pass
```

## Nested Loops
A loop can run inside another loop.

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

## for vs while
- `for`: use with a known range, string, list, or sequence.
- `while`: use when repetition depends on a changing condition.

## Important Notes
- `range()` excludes the stop value.
- Indentation is required inside loops.
- `count += 1` counts events.
- `total += number` adds values.
- `break` exits the loop.
- `continue` skips one iteration.