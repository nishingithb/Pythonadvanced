# # # #Write a program to find the position of a character in a string
# s="python coding is easy and fun"
# print(s.index('o'))


# # # #write a program to find the count of character in  a string
# s="python coding is easy and fun"
# print(s.count('o'))

# # #create a random 5 digit otp number and print otp number
# import random
# print(random.randint(10000,99999))

# #create a list of  5 random 3 digit numbers
# new=[]
# import random
# for i in range(1,6):
#     new.append(random.randint(100,999))
# print(new)



# #create a dictionary where keys are words and values are length of each word from the string
# s="python coding is easy and fun"
# p=s.split()
# new={i:len(i) for i in p}
# print(new)
# #new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}

# #create a dictionary where keys are each character and values are number of occurence of each character
# s="hello world"
# new={i:i.count(i) for i in s}
# print(new)
# d={'h':1,'e':1,'l':3,'o':2,'':1,'w':1,'r':1,'d":1'}

# # #write a program to find the number of digits,letters,and spaces in a string
# s="sdfghjk3456789  dffghjkl345678"
# d=0
# l=0
# e=0
# for i in s:
#     if(i.isdigit()):
#         d+=1
#     elif(i.isalpha()):
#         l+=1
#     elif(i.isspace()):
#         e+=1
#     else:
#         print('error')
# print(d,l,e)

# # Given a list
# l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# # # # create a list of salaries
# new=[]
# for i in l:
#     new.append(i[2])
# print(new)
# # # find the maximum salary
# print(max(i[2] for i in l))

# # # find minimum salary
# print(min(i[2] for i in l))

#Given a dictionary
# d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
# create a new list of students whose mark>=40
# new={i:i.values() for i in d if str(i)>40}
# print(new)

#Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# Find Common elements
# common=[i for i in l1 if i in l2]
# print(common)

#Given
# l=[23,45,67,12,90,56]
# find second largest number
# l.sort()
# print('second largest number: ',l[4])
# print('smallest',l[1])
#find second smallest number