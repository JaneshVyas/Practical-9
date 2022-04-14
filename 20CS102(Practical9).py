class Student:
    rollno=None
    name=None

class Exam(Student):
    marks=[]

class Reasult(Exam):
    def total_marks(self):
        print(sum(self.marks))

reasult=Reasult()
reasult.name=(input("Enter name:"))
reasult.rollno=int(input("Enter roll no:"))
for i in range(1,7):
    reasult.marks.append(int(input("Enter marks of "+str(i)+" subject:")))

print("Total Marks obtained-")
reasult.total_marks()
