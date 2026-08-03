print("program started.")

score = 75

if score >= 60:
    print("You passed the exam.")
else:
    print("You failed the exam.")
print("program ended.")


student_name = "Majd"
Student_name = "Ali"

print(student_name)
print(Student_name)


# variables
student_name = "Sara"  # string
student_age = 20  # integer
course_name = "Python Programming"  # string
registered = True  # boolean

# print if string for one line
print(
    f"Welcome {student_name}! to the {course_name} course. You are {student_age} years old."
)

# print if string for multiple lines
print(f"""Welcome {student_name}! to the {course_name} 
course. You are {student_age} years old.""")

print(type(student_name))  # <class 'str'>
print(type(student_age))  # <class 'int'>
print(type(course_name))  # <class 'str'>
print(type(registered))  # <class 'bool'>

isinstance(student_name, str)  # True

age = int(input("Enter your age: "))

# how to check if the variable is an integer or not
if isinstance(age, int):
    print("You are", age + 5, "after 5 years.")
else:
    print("you are", int(age) + 5, "AFTER 5 years.")

teacher_name = "faisal"
print(teacher_name[0])  # first character
# print(teacher_name[9])  # not exist

# how to check if the index exist or not
index = int(input("select an index: "))
if index < len(teacher_name):
    print(teacher_name[index])
else:
    print("Index is out of bounds.")

print(type(len(teacher_name)))
