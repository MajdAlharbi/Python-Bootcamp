# training
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(calculate_grade(99))
print(calculate_grade(88))
print(calculate_grade(77))
print(calculate_grade(66))
print(calculate_grade(55))
print("\n")


# lab 1
def greet():
    print("welcome to python")


greet()
print("\n")


# lab 2
def show_menu():
    print(f"1-Coffee\n2-Tea\n3-Ginger")


show_menu()
print("Outside the call")
show_menu()
print("\n")

# lab 3
print("Line One")


def unknownScope():
    def gotofunc():
        print("From within the GoTo")
        print("Where is line 2?")

    gotofunc()
    print("I'm up here")


unknownScope()
print("\n")


# lab 4
def greet_student(name):
    print(f"Welcome {name}")


greet_student("Majd")
print("\n")


# lab 5
def show_booking(destination="Riyadh", nights="1"):
    if nights.isdigit():
        nn = int(nights)
    else:
        nn = 1

    print(f"you're traveling to {destination}, and will stay for {nn}")


show_booking()
show_booking("Jeddah", "5")
print("\n")


# lab 6
def getVAT(total, rate=0.15):
    """This Function will get the total  with VAT added to it,and  return"""
    subtotal = total + (total * rate)
    return subtotal


print(getVAT(154))
print(getVAT.__doc__)
help(getVAT)
print("\n")
