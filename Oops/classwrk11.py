#
# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()


# class movie:
#     def __init__(self):
#         self.moviename=input('enter a moviename: ')
#         self.year = input('enter movie year: ')
#         self.language = input('enter movie language: ')
#         self.director = input('enter director name: ')
#         self.rating = ''
#     def display_details(self):
#         print('movie details: ')
#         print('moviename: ',self.moviename)
#         print('year: ', self.year)
#         print('language: ', self.language)
#         print('director: ', self.director)
#         if self.rating == '':
#             print('not yet rated. ')
#         else:
#             print('rating: ', self.rating)
#     def update_rating(self):
#         self.rating = input('enter movie rating: ')
# m=movie()
# m.display_details()
# m.update_rating()
# m.display_details()

# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

# class Vehicle:
#     def __init__(self):
#         self.brand = input("Enter Brand: ")
#         self.model = input("Enter Model: ")
#         self.color = input("Enter Color: ")
#         self.year = int(input("Enter Year: "))
#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Year:", self.year)
#
# class Car(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.mileage = int(input("Enter Mileage: "))
#         print('car details: ')
#     def display(self):
#         Vehicle.display(self)
#         print("Mileage:", self.mileage)
#
# class Bike(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.cc = int(input("Enter CC: "))
#         print('bike details: ')
#     def display(self):
#         Vehicle.display(self)
#         print("CC:", self.cc)
#
#
# c = Car()
# c.display()
# b = Bike()
# b.display()

## Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def __init__(self):
#         self.salary = int(input("Enter Monthly Salary: "))
#     def calculate_salary(self):
#         print("Full Time Salary:", self.salary)
#
# class PartTimeEmployee(Employee):
#     def __init__(self):
#         self.hours = int(input("Enter Hours: "))
#         self.rate = int(input("Enter Rate per Hour: "))
#     def calculate_salary(self):
#         print("Part Time Salary:", self.hours * self.rate)
#
# f = FullTimeEmployee()
# f.calculate_salary()
#
# p = PartTimeEmployee()
# p.calculate_salary()



#
# create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
#  -Rectangle
#  -Square
#
#  -Each class should calculate area() and perimeter() differently.
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         print('RECTANGLE')
#         self.length = int(input("Enter Length: "))
#         self.breadth = int(input("Enter Breadth: "))
#     def get_area(self):
#         print("Area:", self.length * self.breadth)
#     def get_perimeter(self):
#         print("Perimeter:", 2 * (self.length + self.breadth))
#
# class Square(Shape):
#     def __init__(self):
#         print('SQUARE')
#         self.side = int(input("Enter Side: "))
#     def get_area(self):
#         print("Area:", self.side * self.side)
#     def get_perimeter(self):
#         print("Perimeter:", 4 * self.side)
#
# r = Rectangle()
# r.get_area()
# r.get_perimeter()
#
# s = Square()
# s.get_area()
# s.get_perimeter()

# [7/9, 5:11PM] Ziya: Create a Python program using Object-Oriented Programming (OOP) that includes the following:
#
# • Class: Course
# Attributes:
# course_name
# instructor
# duration

# Methods:
# show_course() → to display course details
#
# • Subclass: Student (inherits from Course)
# Additional attributes:
# name
# roll_no
# marks

# Methods:
# show_student() → to display student details along with course details
# get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
#
#
# Create at least one object of the Student class
#
# Display all details and result
# class course:
#     def __init__(self):
#         self.course_name=input("Enter Course Name: ")
#         self.instructor=input("Enter Instructor Name: ")
#         self.duration=input("Enter Duration: ")
#     def show_course(self):
#         print("Course Name:",self.course_name)
#         print("Instructor:",self.instructor)
#         print("Duration:",self.duration)
#
# class student(course):
#     def __init__(self):
#         super().__init__()
#         self.name=input("Enter student Name: ")
#         self.roll_no=int(input("Enter roll_no: "))
#         self.marks=int(input("Enter marks: "))
#     def show_student(self):
#         super().show_course()
#         print("student Name:", self.name)
#         print("roll_no:", self.roll_no)
#         print("marks:", self.marks)
#     def get_result(self):
#         print('RESULT: ')
#         if self.marks>=50:
#             print("PASS")
#         else:
#             print('FAIL')
# s=student()
# s.show_student()
# s.get_result()



# 6.Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with
# attributes such as id, name, age, designation,
# experience (in years), and salary. The class should include methods to display employee details and update the
# designation.
#
# It should also include a method to check promotion eligibility where an employee is eligible for promotion
# if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.
#
# Create at least one object of the Employee class, assign values directly, and display all the details along with the
# promotion eligibility result.
class Employee:
    def __init__(self):
        self.id=input("Enter employee id: ")
        self.name=input("Enter Name: ")
        self.age=int(input("Enter age: "))
        self.designation=input("Enter designation: ")
        self.experience=int(input("Enter Experience (years): "))
        self.salary=int(input("Enter salary: "))

    def display_details(self):
        print('EMPLOYEE DETILS')
        print("ID:", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Designation:", self.designation)
        print("Experience:", self.experience)
        print("Salary:", self.salary)

    def update_designation(self):
        self.designation = input('enter designation: ')

    def check_promotion(self):
        print('PROMOTION')
        if self.experience>=5 and self.age>=30:
            print('eligible')
        else:
            print('not eligible')

e=Employee()
e.display_details()
e.check_promotion()
e.update_designation()
e.display_details()
