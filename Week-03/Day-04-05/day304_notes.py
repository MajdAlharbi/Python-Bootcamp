# comprehensions, copying & performance

# 1- A comprehension combines an Expression, Loop, and Filter
numbers = [1, 2, 3, 4, 5]

squares = [  # comprehension
    number**2
    for number in numbers  # close
    if number % 2 == 1  # Filtering
]

print(squares)  # [1, 9, 25]
print("\n")

# 2- list comprehension transform every item
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices  # closing
]
print(prices_with_vat)  # [11.5, 28.75, 46.0]
print("\n")

# 3-A filter Keeps only items that match a condition
scores = [42, 67, 91, 58, 75]

passing_scores = [
    score
    for score in scores  # closing
    if score >= 60  # Filtering
]
print(passing_scores)  # [67, 91, 75]
print("\n")

# 4-
raw_names = ["  Majd", "  ", "OMAR", "   sara"]

clean_names = [name.strip().title() for name in raw_names if name.strip()]
print(clean_names)
print("\n")

# 5-Multiple for clauses follow nested-loop order
numbers1 = [1, 2]
letters = ["A", "B"]

pairs = [(number, letter) for number in numbers1 for letter in letters]
print(pairs)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
print("\n")

# 6-a conditional expression produces one of two values
scores1 = [42, 67, 91]
labels = ["pass" if score >= 60 else "retry" for score in scores1]

print(labels)
print("\n")

# 7- a set comprehension removes duplicate results
emails = ["SARA@GMAIL.COM", "majd@gmail.com", "lina@school.sa"]  # no need duplicate
domains = {email.split("@")[1].lower() for email in emails}
print(domains)
print("\n")

# 8-
numbers2 = range(1, 6)  # key
squares1 = {number: number**2 for number in numbers2}

print(squares1)
print("\n")

# 9-a generator expression produces values on demand
numbers3 = range(1_000_000)

total = sum(number**2 for number in numbers3)
print(total)
print("\n")

# 10-mutable objects change; immutable objects Are replaced
items = ["python", "git"]
items.append("Django")

name = "Majd"
name = name.title()

print(items)
print(name)
print("\n")

# 11-
original = ["python", "git"]
alias = original
alias.append("django")

print(original)
print(alias)
print(original is alias)
print("\n")

# 12 -shallow copy creates a new outer container
original1 = ["python", "git"]
clone = original1.copy()

clone.append("django")

print(original1)
print(id(original1))

print(clone)
print(id(clone))

print(original1 is clone)
print("\n")

# 13- a shallow copy still shares nested mutable objects
original2 = [["Sara", 90], ["Omar", 85]]
clone2 = original2.copy()

clone2[0][1] = 95

print(original2)
print(clone2)
print(original2[0] is clone2[0])
print("\n")

# 14-Deep Copy recursively duplicates nested object
from copy import deepcopy

original3 = [["Sara", 90], ["Omar", 85]]
clone3 = deepcopy(original3)

clone3[0][1] = 95

print(original3)
print(clone3)
print(original3[0] is clone3[0])
print("\n")

# 15-
names = ["Sara", "Omar", "Majd"]

print("Majd" in names)

name_set = set(names)

print("Majd" in name_set)
print("\n")

# 16-build an index when records need repeated lookup
students = [{"id": 101, "name": "Sara"}, {"id": 102, "name": "Majd"}]
students_by_id = {student["id"]: student for student in students}

print(students_by_id[102]["name"])
print("\n")

# Guided practice
students = [
    {"name": "Sara", "score": [99, 80, 90]},
    {"name": "Omar", "score": [33, 70, 50]},
    {"name": "Majd", "score": [90, 88, 100]},
]

students_by_average = [
    {"name": student["name"], "average": sum(student["score"]) / len(student["score"])}
    for student in students
]
print(students_by_average)
print("\n")

passed_students = [
    student for student in students_by_average if student["average"] >= 60
]
print(passed_students)
print("\n")

from copy import deepcopy

backup = deepcopy(students)
print(backup)
backup[1]["score"][1] = 99
print(backup)
