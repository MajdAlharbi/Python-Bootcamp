# # 1-path objects build location portably
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

# 4-with closes the file automationly
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

# 7-iterate over line witheout lading evrethong
path = Path("notes.txt")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)

# 8-writing replaces existing content
path = Path("student.txt")

with path.open("w", encoding="utf-8") as file:
    conut = file.write("sara\nAli\n")

print(conut)
print("\n")

# 9-appending preseves existing content
path = Path("activity.log")

with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")

print("Activity saved")

# 10-UTF-8 and Newline keep Text predictable
names = ["Majd", "نوره", "Ali"]
text = "\n".join(names) + "\n"

path("student.txt").write_text(text, encoding="utf-8")
