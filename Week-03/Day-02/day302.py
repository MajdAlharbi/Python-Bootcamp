# lab 1
course = "Web Development Bootcamp"
duration = 12


def type(course):
    print("opss!")  # wthot return print None


print(course)
print(duration)
print(type(course))
print(globals())
print("\n")

# lab 2
building = "Tuwaiq Academy"
cohort_size = 20
print(f"Welcome to {building}, class limit is {cohort_size}")
print("Tuwaiq" in building)
print("cohort_size" in globals())
print(globals()["building"])  # key
print("\n")


# lab 3
loction = "Global"


def outter():
    loction = "Outter"
    print(f"From {loction}")

    def inner():
        loction = "Inner"
        print(f"From {loction}")

    inner()


outter()

# lab 4
loction = 0


def outter():
    loction = 1
    print(f"From {loction}")

    def inner():
        nonlocal loction
        loction += 2
        print(f"From {loction}")

    inner()


outter()


# # trainirg
# def prinrer():
#     print("Welcome")


# def desk():
#     prinrer()


# def room():
#     desk()

#     print(room())


# lab 5
languge = "python"


def show_lang(languge):
    print(languge)


show_lang("Dart")
print(languge)
print("\n")

# lab 6
rate = 0.15


def getTotal(amount):
    total = amount * rate + amount
    return total


print(getTotal(199.99))
print(f"{getTotal(199.99):.2f}")
print(round(getTotal(199.99)), 2)
print(round(getTotal(199.99)))
print("\n")


# lab 7
def inspect_order(item, qty):
    subtotal = 25 * qty
    print(locals())
    print(locals()["subtotal"])


inspect_order("Pen", 10)


