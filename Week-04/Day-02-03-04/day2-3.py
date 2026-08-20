# 1-path objects build location portably
from pathlib import Path

data_file = Path("data") / "students.txt"

print(data_file)  # data\students.txt
print(data_file.name)  # students.txt
print(data_file.suffix)  # .txt
print("\n")

# 2-inspect paths before using them
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

data_file = data_dir / "student.txt"

print(data_dir.is_dir())
print(data_file.exists())
print("\n")

# 3-file Modes decide what may change

# "r" read an existing file
# "w" write and replace content
# "a" append after existing content
# "x" create only when absent

with open("notes.txt", "a", encoding="utf-8") as file:  # short "as file:"
    file.write("New note\n")

# 4-with closes the file automatically
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(file.closed)
print("\n")

# 5-read complete text when the file is small
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    text = file.read()

same_text = path.read_text(encoding="utf-8")
print(text == same_text)
print("\n")

# 6-

# 7-iterate over line without loading everything
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)

# 8-writing replaces existing content
path = Path("student.txt")

with path.open("w", encoding="utf-8") as file:
    count = file.write("sara\nAli\n")

print(count)
print("\n")

# 9-appending preserves existing content
path = Path("activity.log")

with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")

print("Activity saved")

# 10-UTF-8 and Newline keep Text predictable
path = Path("student.txt")

names = ["Majd", "نوره", "Ali"]
text = "\n".join(names) + "\n"

path("student.txt").write_text(text, encoding="utf-8")

# 11-
import csv

with open("student.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["Majd", "python"])
    writer.writerow(["Ali", "java"])

# 12 - json
import json

students = [{"name": "Sara", "score": 93}, {"name": "Majd", "score": 99}]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)  # write

with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)  # read

print(loaded[0]["name"])

# 13-try and except defined...
try:
    score = int(input("score: "))
except ValueError as e:
    print("Enter a whole number")
    print(e)

print("program continues")

# 14-

from pathlib import Path

try:
    text = Path("students.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("student file not found")
except PermissionError:
    print("student file cannot be read")

# 15-
path = Path("students.txt")

try:
    text = path.read_text(encoding="utf-8")
except OSError as error:
    print("Load failed, error")

else:  # if try work
    print(text)

finally:
    print("Load attempt")

# 16-raise rejects invalid data immediately...
def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be 0 to 100")  # anytime
    return score


try:
    score = validate_score(120)
except ValueError as error:  # you need "try" first
    print(error)

# 17


class StudentNotFoundError(Exception):
    pass


def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)


students = [{"name": "sara"}]

try:
    print(find_student("Ali", students))
except StudentNotFoundError as error:
    print("Missing student:", error)