# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(num1,num2):
#     p=num1*num2
#     return p
# result=product(2,5)
# print(result)
from unittest import result

# # Q2.Define a function that takes a string and returns number of vowels
# def no_of_v(s):
#     count=0
#     for i in s:
#         if(i in 'aeiouAEIOU'):
#             count+=1
#     return count
# s=input('enter a string: ')
# result=no_of_v(s)
# print(result)


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def rectangle(l,b):
#     a=l*b
#     return a
# result=rectangle(4,5)
# print(result)


# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def list(l):
#     new=[]
#     for i in l:
#         if(i%2==0):
#             new.append(i)
#     return new
# result=list(l)
# print(result)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

#
# def newlist(l):
#     new=[]
#     for i in l:
#         s = sum(int(d) for d in str(i))
#         new.append(s)
#     return new
# l = [123, 345, 111, 678, 134, 809]
# result=newlist(l)
# print(result)

# define a function that takes a list of arguments and returns a new list containing unique elements
# from list
# l=[12,34,78,12,67,34,90,23]
# def unique(l):
#     new=[]
#     for i in l:
#         if(i not in new):
#             new.append(i)
#     return new
# result=unique(l)
# print(result)

# ddefine a function that takes 2 list as argumrnts and print the common elements
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]
# def common(l1,l2):
#     new=[]
#     for i in l1:
#         if(i in l2):
#             new.append(i)
#     return new
# result=common(l1,l2)
# print(result)