def try_split_and_join():
    csv_line = "Majd,Sara,Ail"
    names = csv_line.split(",")
    print(names)
    print(type(names))

    message = "|".join(names)
    print(message)


try_split_and_join()


def try_numbrs():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum of the two numbers is: ", num1 + num2)

    if num1 > num2:
        print("The first number is greater than the second number.")
    elif num1 < num2:
        print("The second number is greater than the first number.")

    text = "I love Python programming"
    print("python" in text)

    text2 = "I love Java programming"

    print(text2.upper())
    print(text.lower())
    print(text2.replace("Java", "Python"))

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(a == b)
    print(a is b)
    print(a is c)


try_numbrs()
