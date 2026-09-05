# # frist project
# def totalAgeInDays():
#     age_years = int(input("Enter your age in years: "))
#     age_days = age_years * 365
#     age_month = age_years * 12
#     age_hour = age_days * 24
#     print(f"""You have lived for
#     \n{age_month} month
#     \n{age_days} days
#     \n{age_hour} hours
#     """)


# totalAgeInDays()

# import random


# def guessGame():
#     print("🎲 Welcome to the Number Gussing Game")

#     numberToGuess = random.randint(1, 10)
#     conut = 0

#     while True:
#         guess = int(input("Guess a nimber between 1 to 10: "))
#         conut += 1
#         if numberToGuess > guess:
#             print("low! Try again")

#         elif numberToGuess < guess:
#             print("Hihg! Try again")

#         elif numberToGuess == guess:
#             print(f"Correct! you guessed the number in {conut} tries")
#             break


# guessGame()

# import datetime

# def pomodoro():
#     print("Welcome to the pomodoro Timer!")

#     user=input("Enter time in minutes: ")
#     print(f"Time remaining : {user}")


# score = int(input("Einter your score: "))

# if 0 <= score <= 100:
#     if score >= 60:
#         print("passed")
#     else:
#         print("Failed")
# else:
#     print("Invalid score")

# scores = [88, 45, 72, 59, 100, 30]

# passed_count = 0
# for score in scores:
#     if score >= 60:
#         print("Passed")
#         passed_count += 1
#     else:
#         print("Failed")

# print(f"Passed students: {passed_count}")

# scores1 = [88, 45, 72, 59, 100, 30]


# def calculate_average(scores):

#     return sum(scores) / len(scores)


# def count_failed(scores):
#     count = 0
#     for score in scores:
#         if score < 60:
#             count += 1
#     return count


# print(calculate_average(scores1))
# print(count_failed(scores1))

# name = "Ali"
# age = 21
# score = 88
# course = "Python"

# {"name": "Ali", "age": 21, "score": 88, "course": "python"}


# # List
# scores = [90, 80, 90]
# print(scores)
# # Tuple
# coordinates = (24.7, 46.7)
# print(coordinates)
# # Set
# courses = {"Python", "Django", "Python"}
# # Python تظهر مرة واحدة فقط
# print(courses)
# # Dictionary
# student = {"name": "Ali", "score": 88}
# print(student)


# students = [
#     {"name": "Ali", "score": 88},
#     {"name": "Sara", "score": 55},
#     {"name": "Majd", "score": 92},
# ]


# for student in students:
#     if student["score"] >= 60:
#         print(f"{student['name']}: Passed")
#     else:
#         print(f"{student['name']}: Failed")

# def get_status(score):
#     if score >= 60:
#         return "Passed"
#     else:
#         return "Failed"


# for student in students:
#     status = get_status(student["score"])
#     print(f"{student['name']}: {status}")

# def count_passed(students):
#     count = 0
#     for student in students:
#         if student["score"] >= 60:
#             count += 1
#     return count


# passed = count_passed(students)
# print(passed)

# def find_highest_score(students):
#     name = students[0]["name"]
#     highest = students[0]["score"]

#     for student in students:
#         if student["score"] > highest:
#             highest = student["score"]
#             name = student["name"]
#     return highest, name


# print(find_highest_score(students))


# def get_passed_students(students):
#     passed_students = []

#     for student in students:
#         if student["score"] >= 60:
#             passed_students.append(student["name"])
#     return passed_students

# print(get_passed_students(students))

# def get_failed_students(students):
#     failed_students = []

#     for student in students:
#         if student["score"] < 60:
#             failed_students.append(student)
#     return failed_students
# print(get_failed_students(students))

# def find_student(students, name):
#     for student in students:
#         if student["name"] == name:
#             return student
#     return None
# print(find_student(students, "wow"))

# def find_lowest_score(students):
#     lowest = students[0]["score"]

#     for student in students:
#         if student["score"] < lowest:
#             lowest = student["score"]
#     return lowest


# print(find_lowest_score(students))

# courses = ["python", "HTML"]
# student_courses = courses

# class Student:
#     courses = []

#     def __init__(self, name):
#         self.name = name

#     def add_course(self, course):
#         self.courses.append(course)


# student1 = Student("Majd")
# student2 = Student("Sara")

# student1.add_course("Python")

# print(student1.courses)
# print(student2.courses)

# {
#     "average": ...,
#     "highest": ...,
#     "lowest": ...,
#     "passed": ...,
#     "failed": ...
# }

# scores = [75, 40, 90, 50, 30]


# def analyze_scores(scores):
#     if not scores:
#         return None
#     highest = max(scores)
#     lowest = min(scores)
#     passed = 0
#     failed = 0
#     average = sum(scores) / len(scores)
#     for score in scores:
#         if score < 0 or score > 100:
#             raise ValueError("Invalid score")

#         if score >= 50:
#             passed += 1
#         else:
#             failed += 1

#     return {
#         "average": average,
#         "highest": highest,
#         "lowest": lowest,
#         "passed": passed,
#         "failed": failed,
#     }


# print(analyze_scores([75, 40, 90, 50, 30]))
# print(analyze_scores([]))

# try:
#     print(analyze_scores([75, 120]))
# except ValueError as error:
#     print(error)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.courses = []

#     def add_course(self, course):
#         if course in self.courses:
#             raise ValueError("Course already exists")
#         self.courses.append(course)

#     def save_to_file(self, filename):
#         return f"Name: {filename}\n Courses: {self.courses}"


# student1 = Student("Majd")
# student2 = Student("Sara")

# student1.add_course("python")

# print(student1.courses)
# print(student2.courses)
# student1.add_course("python")
# print(student1.courses)

