# lab 1
course = "Web Development Bootcamp"
duration = 12


# This intentionally shadows Python's built-in type() for the lesson.
def type(course):
    print("oops!")  # without return, print() returns None


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
location = "Global"


def outer():
    location = "outer"
    print(f"From {location}")

    def inner():
        location = "Inner"
        print(f"From {location}")

    inner()


outer()

# lab 4
location = 0


def outer():
    location = 1
    print(f"From {location}")

    def inner():
        nonlocal location
        location += 2
        print(f"From {location}")

    inner()


outer()


# # ltraining
# def printer():
#     print("Welcome")


# def desk():
#     printer()


# def room():
#     desk()

#     print(room())


# lab 5
language = "python"


def show_lang(language):
    print(language)


show_lang("Dart")
print(language)
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
