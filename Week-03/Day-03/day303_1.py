# training
students = [
    {"name": "Sara", "score": (99, 80, 90), "skills": {"java", "python", "SQL"}},
    {"name": "Omar", "score": (99, 70, 80), "skills": {"java", "python", "design"}},
    {"name": "Majd", "score": (90, 88, 100), "skills": {"java", "java", "design"}},
]

for student in students:
    total = 0
    for score in student["score"]:
        total += score
        avg = total / len(student["score"])

    print(f"Student {student['name']}: \n skills{student['skills']}: \n average {avg}:")
print("\n")

# lab 1
students1 = ["sara", "Majd", "dalal", "taif"]

for student in students1:
    print(student)


for iterable in enumerate(students1):
    print(iterable)

for iterable in iter(students1):
    print(iterable)

iterable1 = enumerate(students1)
print(next(iterable1))
print("\n")

# lab 2
set_col = {"Majd", "sara", "maram"}
tupl_col = (11, 22, 33, 44)
dict_col = {"name": "Majd", "age": 22}
list_col = ["ABC", 333, (33, 33)]

print(set_col, dict_col, list_col, tupl_col)
print(type(set_col))
print(type(dict_col))
print(type(list_col))
print(type(tupl_col))

for c in dict_col.values():
    print(c)
print("\n")

# lab 3
cars = ["GMC", "BMW", "Geely", "G1MC", "B1MW", "Gee1ly"]
print(cars[2])
print(cars[-1])
print(cars[-1::-1])
print("\n")

# lab 4
tasks = ["Read email", "open ticket"]

tasks[0] = "Login"
tasks.append("Get coffee")
tasks.insert(0, "Get bra...")
tasks.pop(1)
print(tasks)
print("\n")

import math

# lab 5
nums = [11, 22, 33, 44, 55, 66]
print(sum(nums))
print(max(nums))
print(min(nums))
print(math.sqrt(min(nums)))
print(math.__doc__)
print(nums)
print(nums.pop(2))
print(sorted(nums, reverse=True))
print("\n")

# lab 6
skills = {"python", "java", "d", "FastAPI"}
print(skills)
skills.add("CSS")
print(skills)
skills.add("HTML")
print(skills)
skills.remove("java")
print(skills)
skills.discard("d")
print(skills)
