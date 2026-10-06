# lambda function

# square of a number
# sq=lambda x:x**2
# print(sq(4))

# def sq(x):
#     return x**2

# print(sq(4))

# cube os a number
# lambda x:x**3

# sq of a number
# lambda x:x**0.5

# length of a string
# s=lambda a:len(a)
# print(s('hello'))

# name attribute of a dictionary
# lambda a:a['name']

# first character of a string
# lambda a:a[0]

# last element of a list
# lambda a:a[-1]

# sum of 2 number
# lambda a,b:a+b

# sum of 3 numbers
# lambda x,y,z:x+y+z

# product of 4 number
# s=lambda a,b,c,d:a*b*c*d
# print(s(1,2,4,5))

# create a new list with square of each number
# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))

#create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))

#create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda x:len(x),colors)))
#create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
#create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))
#create a new list of reverse of each elemnt
# print(list(map(lambda x:x[::-1],colors)))


#Given a list
# l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))

#####filter
# even values
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

# l=[23,67,90,12,45,52]
# number greater than 50
# print(list(filter(lambda x:x>50,l)))

# f=['apple','orange','grapes','pineapple','grapes']
# fruitname whose length is greater than 5
# print(list(filter(lambda x:len(x)>5,f)))


# l=[34,78,96,23,12,15]
# number divisible by 3 and 5------
# print(list(filter(lambda x:x%3==0 and x%5==0,l)))

#####reduce()
# l=[1,2,3,4]
# sum of list
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))

# product of list
# import functools
# print(functools.reduce(lambda a,b:a*b,l,1))

m