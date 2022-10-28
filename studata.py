class Student(object):
    def __init__(self,subject, name, roll, marks):
        self.name = name
        self.subject = subject
        self.roll = roll
        self.marks = marks

    def getsubject(self):
        return self.subject

    def getmarks(self):
        return self.marks

    def getroll(self):
        return self.roll

    def __str__(self):
        return self.name + ' : ' + str(self.getsubject()) + ' :: ' + str(self.getroll()) +' ::: '+  str(self.getmarks())


def Markss(rec, name,subject, roll, marks):
    rec.append(Student(name,subject, roll, marks))
    return rec


Record = []
x = 'y'
while x == 'y':
    subject = input('Enter the subject: ')
    name = input('Enter the name of the student: ')
    roll = input('Enter the roll number: ')
    marks = input('Marks: ')
    Record = Markss(Record, name, subject, roll, marks)
    x = input('another student? y/n: ')

n = 1
for el in Record:
    print(n,'. ', el)
    n = n + 1
