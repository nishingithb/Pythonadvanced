##################################
#
# # addition of 2 numbers
# # function definition
# def addition():
#     "addition of 2 numbers"
#     num1=int(input("enter a number :"))
#     num2=int(input("enter another number :"))
#     sum=num1+num2
#     print(sum)
#     return
#
# addition()
from itertools import count
from unittest import result


#define a function to display a message "Hello Your name"

# def display():
#     "hello your name"
#     str='hello your name'
#     print('message:',str)
#     return
#
# display()

#define a function to print the factorial of a number

# def factorial():
#     "factorial number"
#     fact=1
#     num=int(input('enter a number'))
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#     return
# factorial()

#define a function to find the number of occurence of a particular character in a string

# def occurence():
#     "occurence"
#     s=input('enter a character')
#     ch=input('enter a character')
#     count=0
#     for i in s:
#         if(i==s):
#             count+=1
#     print(count)
#
# occurence()


#define a function to print the sum of elements in a  list l=[89,45,67,12]

# define a function to check whether a number is prime or not
#
# def prime():
#     num=int(input('enter a number: '))
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print('prime')
#     return
#
# prime()


# define a function that takes 3 argment(amount,rate,year) and find the simple interest value

# def intrest(p,n,r):
#     si=p*n*r/100
#     print(si)
#     return
#
# intrest(500,5,2)


# def intrest(p,n,r):
#     si=p*n*r/100
#
#     return si
# result=intrest(5000,6,100)
# print(result)

# define a function that takes 3 number and return the product of 3 number
# def product(a,b,c):
#     p=a*b*c
#
#     return p
# result=product(2,4,6)
# print(result)

# define a function that takes a string and return a character and return the number of occurence of the
# character in that string
def occurence(s,ch):
    count=0
    for i in s:
        if(i==ch):
            count=count+1
    return count

s=input('enter a string: ')
ch=input('enter a character: ')
result=occurence(s,ch)
print(result)