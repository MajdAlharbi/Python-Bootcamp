from pathlib import Path
import json
from json import JSONDecodeError


class InvalidStudentError(Exception):
    pass


data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
data_file = data_dir / "students2.json"

students = [{"name": "Ali", "score": 88}, {"name": "Majd", "score": 99}]

try:
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)  # write

    with open(data_file, "r", encoding="utf-8") as file:
        loaded = json.load(file)  # read

    for student in loaded:
        if not student["name"] or not student["score"]:
            raise InvalidStudentError("Not student")

except FileNotFoundError as e:
    print(e)

except JSONDecodeError as e:
    print(e)

else:
    print(loaded)


# lab 0
class Dog:
    def __init__(self, name):
        self.name = name
        self._legs = 4

    def getLegs(self):
        return self._legs

    def setLegs(self, number):
        self._legs = number


myDog = Dog("Slugi")
myDog.setLegs(3)
print(myDog.getLegs())
print(myDog._legs)


# lab 1
class Ticket:
    def __init__(self, name, status="Open"):
        self.name = name
        self.status = status

    def newStatus(self, status):
        self.status = status


myTicket = Ticket("Unable to open email", "closed")
myTicket.newStatus("Resolved")

myTicket1 = Ticket("1000", "In-Progress")
myTicket2 = Ticket("1001", "Pending")

print(myTicket.status)
print(f"Ticket ID: {myTicket1.status}")
print(myTicket2.status)


# lab 2
class Greeter:
    def __init__(self, message):
        self.message = message

    def greet(self, user):
        self.user = user

        return f"Hello {user}, {self.message}"


mygreet = Greeter("Welcome to Tuwaiq")
mymessage = mygreet.greet("Salem")
print(mymessage)


# lab 3
class Welcome:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome {self.name}")


welcoming = Welcome("")
students = [Welcome("Sara"), Welcome("Majd"), Welcome("Mona")]


for student in students:
    student.welcome()


# lab 4
from pathlib import Path

path = Path("Week-04") / "home" / "students"
path.mkdir(parents=True, exist_ok=True)
file = path / "student.txt"

file.write_text("Welcome to class", encoding="utf-8")

print(path.is_dir())
print(path.suffix)
print(path.name)
print(path.is_file())
