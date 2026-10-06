
# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class student:
    def __init__(self):
        self.name = input('enter student name: ')
        self.rollno = int(input('enter roll no: '))
        self.marks = int(input('enter marks: '))
    def setmarks(self):
        self.marks=int(input('enter new marks: '))
        print('updated mark: ',self.marks)
    def display(self):
        print('name: ',self.name)
        print('roll no: ',self.rollno)
        print('marks: ',self.marks)
l=[]
while(1):
    print("1.Add Student")
    print("2.Update Marks")
    print("3.Display Students")
    print("4.Search Student")
    print("5.Delete Student")
    print("6.Exit")
    ch=int(input('enter ur choice: '))
    if ch==1:
        s=student()
        l.append(s)
    elif ch==2:
        r=int(input("Enter Roll No: "))
        for i in l:
            if i.rollno==r:
                i.setmarks()
                break
        else:
            print("Student Not Found")
    elif ch==3:
        r=int(input("Enter Roll No: "))
        for i in l:
            if i.rollno==r:
                print('Student found')
                break
        else:
            print("Student Not Found")
    elif ch==4:
        r=int(input("Enter Roll No: "))
        for i in l:
            if i.rollno==r:
                i.display()
                break
        else:
            print("Student Not Found")
    elif ch==5:
        r=int(input("Enter Roll No: "))
        for i in l:
            if (i.rollno== r):
                l.remove(i)
                print("Student Deleted")
                break
        else:
            print("Student Not Found")
    elif ch==6:
        exit(print('EXIT'))
    else:
        print('invalid choice')

