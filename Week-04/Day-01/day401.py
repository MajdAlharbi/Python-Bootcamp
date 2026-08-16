# __init__ Establishens the Stating state
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


student = Student("Sara", 92)

print(student.name)
print(student.score)
print("\n")


# self refers to the current object
class Student:
    def __init__(self, name):
        self.name = name

    def instrduce(self):
        print(f"i'm {self.name}")


student = Student("Sara")
student.instrduce()
print("\n")


# instance attributes...
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


sara = Student("Sara", 92)
omer = Student("Omer", 81)

sara.score = 95

print(sara.score)
print(omer is sara)
print(isinstance(omer, Student))
print("\n")


# class attributes...
class Student:
    academy = "Tuwaiq Academy"

    def __init__(self, name):
        self.name = name


sara = Student("Sara")
sara.score = 95

print(Student.academy)
print(sara.academy)
print("\n")


# instance  methods
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def disolay_result(self):
        print(self.name, self.score)


student = Student("Sara", 88)
student.disolay_result()
print("\n")


# Methods can return calculated values
class Counter:
    def __init__(self):
        self.value = 0

    def instrduce(self):
        self.value += 1


counter = Counter()
counter.instrduce()
counter.instrduce()

print(counter.value)
print("\n")


#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 3)

print(rectangle.area())
print("\n")


#
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def Withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True


account = BankAccount(500)
print(account.Withdraw(200))
print(account.balance)
print("\n")


# __str__ Gives an object a readable description
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"


student = Student("Sara", 92)  # object

print(student)
print("\n")


# Each instraca keeps independent stote
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


frist = Counter()
second = Counter()

frist.increment()
print(frist.value)
print(second.value)
print("\n")


# collection can store objects
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello,{self.name}"


students = [Student("Sara"), Student("Majd"), Student("Lina")]

for student in students:
    print(student.greet())

print(students[0].greet())
print("\n")


# type and isinstance identify object
class Student:
    pass


student = Student()

print(type(student))
print(type(student) is Student)
print(isinstance(student, Student))
print("\n")


# Attribute access is public by default
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score


student = Student("Majd", 99)
print(student.name)
print(student._score)
print("\n")


# A small class keeps data and behavior together
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)


student = Student("Majd", [99,88])
student.add_score(100)
print(student.name, student.average())
