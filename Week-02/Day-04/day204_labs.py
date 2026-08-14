# lab 1

age = 17
if 18 > age < 55:
    print("Welcome")
print("Code Completed")

# lab 2
temperature = 31
if temperature >= 35:
    print("Its hot outside")
else:
    print("cool")

# lab 3
score = 2000

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("You need to impl...")

# lab 4
is_active = True
is_verified = True
role = "editor"
is_blocked = False

if is_active and is_verified:
    print("Account is ready")

if role == "admin" or role == "editor":
    print("user is not blocked")

if not is_blocked:
    print("user is not blocked")

else:
    print("user is blocked")

# lab 5
account_active = True
has_permission = True

if account_active:
    if has_permission:
        print("Access Granted")
    else:
        print("Access denied")
else:
    print("Account is not active")

# lab 6
name = "Majd"
cart = []
balance = 990

if name:
    print("Name has a value")

if not cart:
    print("Your cart is empty, please shop")
print(bool(balance))

# lab 7

name = input("enter your name: ")

if not name:
    print("enter your name")
elif not name.replace(" ", "").isalpha():
    print("name must contain letters")
else:
    print(f"Valid name {name}")

print(name.replace(" ", ""))


# lab 8

age_text = input("enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} in 5 years")
else:
    print("Enter a number")

# lab 9
is_score_valid = False

score_text = input("enter a number between 0 and 100: ")

if score_text.isdigit():
    score_x = int(score_text)

    if score_x >= 0 and score_x <= 100:
        print("valid score")
        is_score_valid = True
    else:
        print("Score is invalid")
else:
    print("Enter a number")

# lab 10
membership = ["Admin", "Editor", "Viewer"]

current_membership = input("enter your membership: ").strip().lower()

if current_membership.title() in membership:
    print("you are allowed to view to co..")
    print(current_membership)
else:
    print("please contact admin team")
    print(current_membership)

# lab 11
commands = input("please enter a command (start,stop,status)").strip().lower()
match commands:
    case "start":
        print("starting system...")
    case "stop":
        print("stopping system..")
    case "status":
        print("System is up and running")
    case _:
        print("please enter a proper command")
