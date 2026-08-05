name = input("Enter your name: ")

if name.strip() == "":
    print("Name cannot be empty.")

score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Score must be between 0 and 100.")

elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")

courses = ["python", "Java", "C++"]
course_choice = input("Enter your course: ")
if course_choice in courses:
    print(" in list")
else:
    print("course not in list")

