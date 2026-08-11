# story car
# def userName():

#     user = input("Enter Your name: ")

#     for i in user:
#         print(i)


# userName()
print("\n")

# 1
students = ["sara", "Majd", "Lina"]

print(students)
print(students[0])
print(type(students))
print("\n")

# 2
print("\n")

# 3- indexes select
colors = ["red", "green", "blue"]

print(colors[0])
print(colors[1])
print(colors[-1])
print("\n")

# 4- Slicing selects a range of items
Numbers = [10, 20, 30, 40, 50]
print(Numbers[1:4])  # [20, 30, 40]
print(Numbers[:3])  # [10, 20, 30]
print(Numbers[::2])  # [10, 30, 50]
print(Numbers[::-1])  # [50, 40, 30, 20, 10]
print("\n")

# 5- list can chang after Creation
task = ["plan", "code"]

task[0] = "design"
task.append("test")
task.insert(1, "review")

print(task)
print("\n")

# 6- list methods Add,Remove,and Recoder items
scores = [88, 72, 95, 81]

scores.remove(72)
last = scores.pop()
scores.sort()

print(scores)
print(last)
print("\n")

# 7-loops process Every item in collection
students = ["sara", "Majd", "Lina"]
for student in enumerate(students):
    print(student)

for index, student in enumerate(students):
    print(index, student)
print("\n")

# 8-A Collection can contain other collection
matrix = [[1, 2, 3], [4, 5, 6]]

print(matrix[0])
print(matrix[1][2])
print("\n")

# 9-Tuples store orderd Values that shod not change
location = (24.1234, 46.437901)

print(location[0])
print(location[-1])
print("\n")

# 10-Unpaking Assigns Collection Items to Names
parson = ["sara", 22, "python"]
name, age, course, *other = parson
print(name, age, course, other)
print("\n")

# 11-Sets Keep only uniqe values
skills = {"python", "Git", "python"}
skills.add("djange")

print(skills)
print("Git" in skills)
print(len(skills))
print("\n")

# 12-set operations compare Groups
beckend = {"python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JavaScript", "SQL"}

print(
    beckend | frontend
)  # union {'CSS', 'python', 'Django', 'JavaScript', 'HTML', 'SQL'}
print(beckend & frontend)  # intersection {'SQL'}
print(frontend - beckend)  # difference {'CSS', 'HTML', 'JavaScript'}
print("\n")

# 13-
parson1 = {"name": "sara", "age": 22, "course": "python"}

print(parson1["name"])
print("\n")

# 14-Add, Update,and Remove Dictionary values
student1 = {"name": "Sara", "score": 90}
student1["score"] = 95
student1["grade"] = "A"

email = student1.get("email", "Not set")
grade = student1.pop("grade")
print(student1)
print("\n")

# 15-Dicrionary loops can read keays and values
student2 = {"name": "Sara", "score": 90}
for key in student2:
    print(key)

for value in student2.values():
    print(value)

for key, value in student2.items():
    print(key, value)

print(student2)
print("\n")

# 16-choose a collection by its behavior #ordered #unique #Keyed

# 17-common operations work across collections
names = ["sara", "Omar"]
skills1 = {"python", "Git"}
student3 = {"name": "Sara", "score": 90}

print(len(names))
print("python" in skills1)
print("name" in student3)
print("\n")

# 18-
student4 = [{"name": "Sara", "score": 90}, {"name": "Omar", "score": 88}]

for student in student4:
    print(student["name"], student["score"])


# 19-collection Error usually reveal the wrong assumption


