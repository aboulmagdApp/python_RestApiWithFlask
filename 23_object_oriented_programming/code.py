# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(seq):
#     return sum(seq)/ len(seq)

# print(average(student["grades"]))

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob",(100,100,93,78,90))
student2 = Student("Bob",(90,90,93,78,90))

# print(Student.average_grade(student))
# print(Student.average_grade(student2))

print(student.average_grade())
print(student2.average_grade())