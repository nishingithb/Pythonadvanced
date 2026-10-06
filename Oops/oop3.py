#define a class named student with the following details:
# data members:
# sname,rollno,class,mark1,mark2,mark3
# memeber methods
# calculate(),calculate the total and average
# show details()-displays the details of a student with average mark
# create one object for the class and call the above member methods.
class students:
    def __init__(self):
        self.sname=input('enter ur name: ')
        self.rollno = int(input('enter ur rollno: '))
        self.classs = input('enter ur classs: ')
        self.mark1 = int(input('enter ur mark1: '))
        self.mark2 = int(input('enter ur mark2: '))
        self.mark3 = int(input('enter ur mark3: '))
    def calculate(self):
        self.total=self.mark1+self.mark2+self.mark3
        self.avg=self.total/3
    def show(self):
        print('name: ',self.sname)
        print('rollno: ', self.rollno)
        print('classs: ', self.classs)
        print('total: ', self.total)
        print('average: ', self.avg)
s=students()
s.calculate()
s.show()