print("\nExercise 1")


def myInfo():
    name = "majd"
    age = 23
    myCourse = "python"
    register = True

    print(name)
    print(age)
    print(myCourse)
    print(register)

    print("\nExercise 2")
    print(f"My name {name}. I'm {age} years old and I study {myCourse}")


myInfo()

print("\nExercise 3")


def print_type():
    city = "Riyadh"
    temperature = 40
    price = 19.5
    is_sunny = True

    print(type(city))
    print(type(temperature))
    print(type(price))
    print(type(is_sunny))

    print("\nExercise 4")
    print(isinstance(city, str))
    print(isinstance(temperature, str))
    print(isinstance(price, int))
    print(isinstance(is_sunny, bool))


print_type()

print("\nExercise 5")


def try_input():
    name = input("enter your name:")
    print("welcome", name)


try_input()

print("\nExercise 6")


def your_age():
    age = int(input("enter your age:"))
    print("After 5 years, you will be", age + 5, "years old.")


your_age()

print("\nExercise 7")


def add_number():
    first_num = int(input("Enter first number:"))
    second_num = int(input("Enter second numder:"))

    total = first_num + second_num

    print("The total is", total)


add_number()

print("\nExercise 8")


def ask_student():
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    course = input("enter your course: ")

    print(f"""Student Information 
Name: {name}
Age: {age}
Course: {course}""")


ask_student()


X = 0
Y = 1
X, Y = Y, X
print(X, Y)
