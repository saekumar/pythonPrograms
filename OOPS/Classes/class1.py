class Student:
    stdList = []

    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks
        Student.stdList.append(self)

    @classmethod
    def printStdData(cls):
        for student in cls.stdList:
            print(f"Name: {student.name}, ID: {student.id}, Marks: {student.marks}")


n = int(input(""))
for i in range(n):
    data = input("Enter name, id, and marks seperated by space: ")
    name, id, marks = data.split()
    std = Student(name, int(id), int(marks))

Student.printStdData()
