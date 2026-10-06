# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
# s=['alin', 'arun', 'anu']
# print(list(map(lambda x:x.capitalize(),s)))


# 2.Append "@gmail.com" to a list of usernames
# u=['user1', 'user2']
# print(list(map(lambda a:a.append("@gmail.com"),u)))


# 3.Filter out all empty strings from a list
# l= ['hello',' ','world',' ','python']
# print(list(filter(lambda x:x!=' ',l)))


# 4.Filter names that start with the letter 'A'
# s = ['Anu', 'Neenu', 'Arun', 'Ravi']
# print(list(filter(lambda x:x.startswith('A'),s)))


# 5.Concatenate all strings in a list
# words = ['Python', 'is', 'fun']
# import functools
# result=functools.reduce(lambda x, y: x+y,words)
# print(result)


# 6.Multiply all numbers in a list
# nums = [2,3,4]
# import functools
# result=functools.reduce(lambda x, y: x * y, nums)
# print(result)


# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
# print(list(map(lambda x:x[0],words)))

# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,nums)))

# 9.Given a list
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
# pos_even=list(filter(lambda x:x%2==0 and x>0,l))
# import functools
# print(functools.reduce(lambda x,y:x+y,pos_even))
#
#     #Sum of Positive Odd numbers
# pos_odd=list(filter(lambda x:x%2==1 and x>0,l))
# import functools
# print(functools.reduce(lambda x,y:x+y,pos_odd))
#
#     # #Sum of Negative  odd numbers
# neg_odd=list(filter(lambda x:x%2==1 and x<0,l))
# import functools
# print(functools.reduce(lambda x,y:x+y,neg_odd))
#
#     # #Sum of Negatve Even numbers
# neg_even=list(filter(lambda x:x%2==0 and x<0,l))
# import functools
# print(functools.reduce(lambda x,y:x+y,neg_even))

    # #Count of Positive numbers
#
# count_pos=len(list(filter(lambda x:x>0,l)))
# print(count_pos)
#
#     # #Count of negative numbers
#
# count_neg=len(list(filter(lambda x:x>0,l)))
# print(count_neg)

# 10.Given a list nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
# l=["1", "2", "3", "4"]
# print(list(map(lambda x:int(x),l)))


# 11.
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
# print(list(map(lambda x:x['name'].upper(),p)))
#print products with price greater than 10000
# print(list(map(lambda x:x['price']<10000,p)))
#Find the total price of all products
# import functools
# total= functools.reduce(lambda x, y: x + y['price'], p, 0)
# print(total)