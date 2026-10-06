# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

# import math
# try:
#     n1=int(input('enter a number: '))
#     print('factorial: ',math.factorial(n1))
# except ValueError:
#     print('ValueError')
# except:
#     print('error')
# else:
#     print('no exception in normal block')
# finally:
#     print('finished')


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     op=input("Enter operator (+, -, *, /): ")
#     if op=="+":
#         print("Result: ",a+b)
#     elif op=="-":
#         print("Result: ",a-b)
#     elif op=="*":
#         print("Result: ",a*b)
#     elif op=="/":
#         print("Result: ",a/b)
#     else:
#         print("Invalid Operator")
#
# except ValueError:
#     print("ValueError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")




# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
try:
    filename=input('enter filename: ')
    f=open(filename, 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('file does not exist')