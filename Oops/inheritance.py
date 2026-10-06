# ------------------------------------------ single --------------------------------------------------------------- #

# class person:
#     def __init__(self):
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#     def showdetails(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# class student(person):
#     def __init__(self):
#         super().__init__()
#         self.rollno = int(input("Enter roll no: "))
#     def studentdetails(self):
#         super().showdetails()
#         print('roll no: ',self.rollno)
# s=student()
# s.studentdetails()

# class company:
#     def __init__(self):
#         self.name=input("Enter company name: ")
#     def showdetails(self):
#         print("Company Name:", self.name)
# class employee(company):
#     def __init__(self):
#         super().__init__()
#         self.empid = input("Enter employee id: ")
#         self.salary = int(input("Enter salary: "))
#         self.designation = input("Enter designation: ")
#     def getsalary(self):
#         return self.salary
#     def employeedetails(self):
#         super().showdetails()
#         print('empid: ',self.empid)
#         print('salary: ', self.salary)
#         print('designation: ', self.designation)
# e=employee()
# e.employeedetails()

# ------------------------------------------ multiple --------------------------------------------------------------- #

class hospital:
    def __init__(self):
        self.hname = input("Enter hospital name: ")
        self.loc = input("Enter location: ")

    def showdetails(self):
        print("Hospital Name:", self.hname)
        print("Location:", self.loc)

class department:
    def __init__(self):
        self.depname = input("Enter department name: ")
        self.doc = input("Enter doctor name: ")

    def showdepdetails(self):
        print("Department Name:", self.depname)
        print("Doctor Name:", self.doc)

class patient(hospital, department):
    def __init__(self):
        hospital.__init__(self)
        department.__init__(self)
        print('patient details ')
        self.id = input("Enter ID: ")
        self.name = input("Enter Name: ")
        self.gender = input("Enter Gender: ")
        self.place = input("Enter Place: ")
        self.admndate = input("Enter Admission Date: ")
        self.disdate =''

    def setdisdate(self):
        self.disdate=input("Enter Discharge Date: ")

    def fullsummary(self):
        hospital.showdetails(self)
        department.showdepdetails(self)
        print('full summary ')
        print("ID:", self.id)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Place:", self.place)
        print("Admission Date:", self.admndate)
        if self.disdate=='':
            print('not yet discharged. ')
        else:
            print('discharged date: ',self.disdate)

    def dischargedetails(self):
        print("Discharge Date:", self.disdate)

p = patient()
p.fullsummary()
p.setdisdate()
p.fullsummary()

