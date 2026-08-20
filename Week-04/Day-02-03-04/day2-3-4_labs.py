# * Import tools for file paths and JSON handling
from pathlib import Path
import json
from json import JSONDecodeError


# * Custom exception for invalid student data
class InvalidStudentError(Exception):
    pass


# * Create the data folder and build the JSON file path
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
data_file = data_dir / "students2.json"

# * A list of student dictionaries
students = [{"name": "Ali", "score": 88}, {"name": "Majd", "score": 99}]

# * try contains code that may cause an error
try:
    # * Open the JSON file in write mode and save the students
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)

    # * Open the same file in read mode and load the data
    with open(data_file, "r", encoding="utf-8") as file:
        loaded = json.load(file)

    # * Check every student after reading the file
    for student in loaded:
        # ! If name or score is empty, raise our custom error
        if not student["name"] or not student["score"]:
            raise InvalidStudentError("Not student")

# ! Handles the error if the file cannot be found
except FileNotFoundError as e:
    print(e)

# ! Handles invalid or broken JSON data
except JSONDecodeError as e:
    print(e)

# ! Handles our custom student validation error
except InvalidStudentError as e:
    print(e)

# * else runs only when no exception happens
else:
    print(loaded)


# * LAB 0: Basic class, object, getter, and setter
class Dog:
    # * __init__ runs automatically when a Dog object is created
    def __init__(self, name):
        self.name = name
        # * _legs is an internal attribute by convention
        self._legs = 4

    # * Getter: returns the current number of legs
    def getLegs(self):
        return self._legs

    # * Setter: changes the number of legs
    def setLegs(self, number):
        self._legs = number


# * Create a Dog object and use its methods
myDog = Dog("Slugi")
myDog.setLegs(3)
print(myDog.getLegs())
print(myDog._legs)


# * LAB 1: Store and update object state
class Ticket:
    # * status has a default value of 'Open'
    def __init__(self, name, status="Open"):
        self.name = name
        self.status = status

    # * This method updates the ticket status
    def newStatus(self, status):
        self.status = status


# * Create different Ticket objects
myTicket = Ticket("Unable to open email", "closed")
myTicket.newStatus("Resolved")

myTicket1 = Ticket("1000", "In-Progress")
myTicket2 = Ticket("1001", "Pending")

print(myTicket.status)
print(f"Ticket ID: {myTicket1.status}")
print(myTicket2.status)


# * LAB 2: Method with a parameter and return value
class Greeter:
    # * Store the message inside the object
    def __init__(self, message):
        self.message = message

    # * greet receives a user name and returns a formatted message
    def greet(self, user):
        self.user = user
        return f"Hello {user}, {self.message}"


# * Create the object, call the method, and save the returned value
mygreet = Greeter("Welcome to Tuwaiq")
mymessage = mygreet.greet("Salem")
print(mymessage)


# * LAB 3: Create many objects and loop through them
class Welcome:
    def __init__(self, name):
        self.name = name

    # * This method prints a welcome message using the object's name
    def welcome(self):
        print(f"Welcome {self.name}")


welcoming = Welcome("")

# * A list can store multiple objects of the same class
welcome_students = [Welcome("Sara"), Welcome("Majd"), Welcome("Mona")]

# * Call the welcome method for every student object
for student in welcome_students:
    student.welcome()


# * LAB 4: Work with folders, file paths, and pathlib

# * Build the full path using / instead of writing one long string
path = Path("Day-02-03") / "home" / "students" / "student.txt"

# * Create all missing parent folders
path.parent.mkdir(parents=True, exist_ok=True)

# * Write text directly to the file using pathlib
path.write_text("Welcome to class", encoding="utf-8")

# * Inspect the path and check its type, name, and extension
print(path.is_dir())
print(path.suffix)
print(path.name)
print(path.is_file())


# * LAB 5: Validation, properties, setters, and calculated values
class Student:
    def __init__(self, name):
        self.name = name
        self.score = []
        self.__enrolled = True

    # * Add a score only if it is between 0 and 100
    def add_score(self, score):
        # ! Invalid scores raise a ValueError
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)

    # * @property lets us access a method like an attribute
    @property
    def enrolled(self):
        return self.__enrolled

    # * Setter is used to control changes to enrolled
    @enrolled.setter
    def enrolled(self, status):
        self.__enrolled = status

    # * average is a read-only calculated property
    @property
    def average(self):
        # * Return 0 when there are no scores to avoid division by zero
        if not self.score:
            return 0
        # * Calculate the average from all stored scores
        return sum(self.score) / len(self.score)


# * Create a student object and add scores
student1 = Student("Majd")
student1.add_score(88)
student1.add_score(90)
student1.add_score(100)

# * Read the calculated average and the score list
print(student1.average)
print(student1.score)

# ? Name mangling allows access to __enrolled as _Student__enrolled
print(student1._Student__enrolled)

# * Access enrolled like a normal attribute because it is a property
print(student1.enrolled)
student1.enrolled = False
print(student1.enrolled)


# * LAB 6: Inheritance, super(), and static methods

# * Parent class: stores a name and provides showName()
class Food:
    def __init__(self, name):
        self.name = name

    def showName(self):
        return self.name


# * Fruitues inherits attributes and methods from Food
class Fruitues(Food):
    def __init__(self, name, cal):
        # * super() calls the parent class constructor
        super().__init__(name)
        self.cal = cal

    # * staticmethod belongs to the class and does not need self
    @staticmethod
    def stripName(newName):
        # * strip() removes spaces from the beginning and end of text
        return newName.strip()


# * Create a child-class object
myFruitues = Fruitues("Apple", 200)

# * The child object can use both inherited and static methods
print(myFruitues.showName())
print(myFruitues.stripName("   fa   "))
