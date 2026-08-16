# trainig
class Student:
    def __init__(self, name, scores=[]):
        self.name = name
        self.scores = scores

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name}: {self.scores}\n {self.average()}"


class Course:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def add_student(self, student):
        self.students.append(student)  # add

    def display_studens(self):
        for student in self.students:
            print(student)


course = Course("java", [])
course.add_student(Student("Majd", [88, 89, 99]))
course.add_student(Student("Sara", [55, 66, 88]))
course.add_student(Student("Mona", [67, 89, 84]))
course.display_studens()




