# lab 1
for attempts in range(3):
    print(f"Attempts: {attempts + 1}")
print("Program Completed")

# lab 2
for num in range(2, 11, 2):
    print(num)

# lab 3
for secondsToLaunch in range(10, 0, -1):
    print(f"T-: {secondsToLaunch}")

# lab 4
course = "python"
for letter in course:
    print(letter)

# lab 5
students = ["majd", "sara", "ali"]

for student in students:
    print(f"progressing student {student}")

# lab 6
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    print("-----------")

# lab 7
numbers = [4, 7, 10, 13, 16, 21]
even_counter = 0

for nums in numbers:
    if nums % 2 == 0:
        even_counter += 1
print(f"Total even numbers is: {even_counter * 10}")

# lab 8
prices = [23, 30, 55, 115]
total = 0

for price in prices:
    total += price
print(f"your total is {total} VAT {total * 0.15:.2f}")

# lab 9
count = 0
while count < 5:
    count += 1
    print(f"count.. {count}")
print("Loop completed")

# # lab 10
# age_text = input("please enter your age: ").strip()

# while not age_text.isdigit():
#     age_text = input("please enter your age: ").strip()

#     age = int(age_text)
#     print(f"you are: {age}")

# lab 11
# password = ""
# password = input(print("please Enter your password "))

# while password != "python":
#     password = input("Incorrect password, try again: ")
# print("Access Granted!")

# lab 12
for score in [80, 55, 45, 90]:
    if score < 50:
        pass
    print(f"if passed the {score}")
    print(" ")

for record in [80, 55, 45, 90]:
    if record < 50:
        print(f"if skipped {record}")
        continue
for bad_score in [80, 55, 45, 90]:
    if bad_score < 50:
        break
    print(f"We saw: {bad_score}")

# lab 13
for row in range(1, 4):
    for column in range(1, 4):
        #print(f"Row: {row}, Column: {column}")
        print(f"{row} X {column} = {row * column}")
