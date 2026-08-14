results = 10 + 5 * 2 - 4 / 2

print(results)

total_items = 17
box_capacity = 5

full_box = total_items // box_capacity
remaining_items = total_items % box_capacity
print(f"You can fill up to: {full_box}")
print(f"And you have {remaining_items} remaining ")

base_calc = 2 + 3 * 2**2
gcalc = (2 + 3) * 2**2

print(base_calc)
print(gcalc)

# lab 4
user_age = 25
has_permission = True

is_eligible = user_age >= 18 and has_permission
print(f"Is the user eligible? {is_eligible}")

is_eligible = user_age >= 18 or has_permission
print(f"Is the user eligible? {is_eligible}")

# lab 5
score = 85
score += 5
score *= 5

print(f"Final score: {score}")

# lab 6
membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"

if current_membership in membership:
    print("welcome")

if current_membership and "Visitor" in membership:
    print("You are a visitor.")
else:
    print("You are not a visitor.")

if current_membership == membership[1]:
    print("You are a member.")

# lab 7
sentence = "Python web development."

new_sentence = sentence.find("web")
print(new_sentence)

new_sentence = sentence.replace("web", "mobile")
print(new_sentence)

new_sentence = sentence.upper()
print(new_sentence)

new_sentence = sentence.lower()
print(new_sentence)

new_sentence = sentence.split(" ")
print(new_sentence)


list = ["python web development", "python mobile development", "python data science"]

if "python" in list:
    print("Python is in the list.")
else:
    print("not found")


# lab 8

message = "I love Python programming"
first_char = message[0]
last_char = message[-1]
print(f"First character: {first_char} and Last character: {last_char}")

# slicing
sliced_message = message[:7]
print(f"Sliced message: {sliced_message}")

reverse_message = message[::-1]
print(f"Reversed message: {reverse_message}")

# lab 9
my_email = "             majd@hmail.com"
cleaned_email = my_email.strip().lower()
print(f"Cleaned email: {cleaned_email}")
message = "I love Python programming"
titled_message = message.title()
print(f"your email is: {cleaned_email} and your course is: {titled_message}")

# lab 10
csv_text = "Majd,Sara,Ail"

splitted_text = csv_text.split(",")
joined_text = " - ".join(splitted_text)
print(f"""your list is: {csv_text} 
splitted like this: {splitted_text} 
and joined like this: {joined_text}""")

# lab 11
name = "Mohammed"
try:
    name[0] = "M"

except TypeError as e:
    print(e)

x = 5
y = 5
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# if they are lists, they will not be the same object
x = [5]
y = [5]
if x is y:
    print("x is the same object as y")
else:
    print("x is not the same object as y")

    print(id(x))
    print(id(y))  # use id() to get the memory address of the object

    # lab 12
    message = "I love Python programming"
    new_message = message.replace("Python", "Java")
    print(new_message)

    x = 5
    y = 6
