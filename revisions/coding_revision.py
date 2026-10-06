# coding  revision

# write a prgm to find the maximum number in a list
# l=[23,78,45,70,12,56]
# # without using max() function & min() function
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)
#
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print(min)


# revision 3
# print() the nth term in fibinocci series
n=int(input('enter n: '))
a=0
b=1
for i in range(1,n):
    c=a+b
    a=b
    b=c
print(a)