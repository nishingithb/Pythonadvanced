# define a class named employee with the following details.
# data memebers:
# empid, name,age, salary, designation,place
# memeber methods
# getsalary(), showpersondetails()
# create 2 objects for the employee class and call the above member methods.

class employee:

    def __init__(self):
        self.empid = input("Enter employee id: ")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))
        self.designation = input("Enter designation: ")
        self.place = input("Enter place: ")

    def getsalary(self):
        return self.salary

    def display(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Designation:", self.designation)
        print("Place:", self.place)

e1 = employee()
print("Salary:", e1.getsalary())

e1.display()
e1 = employee()
e2 = employee()

print(e1.getsalary())
e1.display()

print(e2.getsalary())
e2.display()