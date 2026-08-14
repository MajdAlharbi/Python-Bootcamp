def add_numbers():
    num = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print(num + num2)


add_numbers()


def main():
    student_name = "Majd"
    student_age = "20"
    greetuser(student_name, student_age)


def greetuser(name, age):
    print("Welcome " + name + " your age is " + age)


main()
