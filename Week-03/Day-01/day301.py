# training
def calculate_grad(score):
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


print(calculate_grad(99))
print(calculate_grad(88))
print(calculate_grad(77))
print(calculate_grad(66))
print(calculate_grad(55))
print("\n")


# lab 1
def greet():
    print("welcome to python")


greet()
print("\n")


# lab 2
def show_menu():
    print(f"1-Coffee\n2-Tea\n3-Giger")


show_menu()
print("Outside the call")
show_menu()
print("\n")

# lab 3
print("Line One")


def unknowScope():
    def gotofunc():
        print("From within the GoTo")
        print("Where is line 2?")

    gotofunc()
    print("I'm up here")


unknowScope()
print("\n")


# lab 4
def greet_student(name):
    print(f"Welcome {name}")


greet_student("Majd")
print("\n")


# lab 5
def show_booking(destinatoin="Riyadh", nights="1"):
    if nights.isdigit():
        nn = int(nights)
    print(f"you're traveling to {destinatoin}, and will stay for {nn}")


show_booking()
show_booking("Jaddah", "5")
print("\n")


# lab 6
def getVAT(total, rate=0.15):
    """This Function will get the total  with VAT added to it,and  return"""
    subtotal = total + (total * rate)
    return subtotal


print(getVAT(154))
print(getVAT.__doc__)
help(getVAT())
print("\n")


