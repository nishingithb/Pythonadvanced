# def fun(n,a):
#     print('name',n)
#     print('age',23)
# fun(n='arun',a=23)
# fun(a=23,n='arun')



# args
# def fun(*args):
#     print(args)
# fun(1,2,3,4)
# fun(10,20,30,40,50)
#
# # kwargs
# def fun(**kwargs):
#     print(kwargs)
# fun(name='anu',age=23)
# fun(name='arju',age=25,place='ekm')

# define a function that accepts any numbers and return their sum

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# result=add(2,3,4,5)
# print(result)

# ###dictionary
d={'a':10,'b':20}
for i in d.items():
    print(i)