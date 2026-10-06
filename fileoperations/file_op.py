# f=open('a.txt','w')
# content=['1to10\n','helloworld\n','python\n','nature1\n','beautiful\n','ernakulam\n']
# f.writelines(content)
# f.close()

#write a rogram to read text file and displays the number of lines in a file

# f=open('a.txt','r')
# content=f.readlines()
# print(len(content))
# f.close()

#write a program to display the number of words in a file
# content=f.read()
# words=content.split()
# print(len(words))
# f.close

#write a program to update the second line in a file
# f=open('a.txt','r')
# lines=f.readlines()
# f.close()
# lines[1]='world\n'
# f=open('a.txt','w')
# f.writelines(lines)
# f.close()

# display the last 5 lines in file
# f=open('a.txt','r')
# lines=f.readlines()
# for i in lines[-5:]:
#     print(i,end=' ')
# f.close()

# search a particular word in a file
# word=input('enter a word: ')
# f=open('a.txt','r')
# content=f.read()
# if word in content:
#     print('found')
# else:
#     print('not found')
# f.close()

# find the number of letters,digits and space in a file
# f=open('a.txt','r')
# content=f.read()
# letters=0
# digits=0
# space=0
# for i in content:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
#     elif i.isspace():
#         space+=1
# print('letters : ',letters)
# print('digits  : ',digits)
# print('space   : ',space)
#
# f.close()

#reverse the lines in a file
# f = open("a.txt", "r")
# lines=f.readlines()
# for i in reversed(lines):
#     print(i,end="")
# f.close()

# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed the exam.
# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.

# f1 = open("total_students.txt","r")
# l1=f1.read().split()
#
# f2 = open("passed_students.txt","r")
# l2=f2.read().split()
#
# f3 = open("failed_students.txt","w")
# for i in l1:
#     if i not in l2:
#         f3.write(i)


# Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it

# f1=open('swiggy.txt','r')
# s=f1.read().split()
#
# f2=open('zomato.txt','r')
# z=f2.read().split()
#
# items=s+z
# print(items)
#
# d={}
# for i in items:
#     d[i]=items.count(i)
# print(d)


# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.

f=open("marks.txt", "r")
out=open("names.txt", "w")
for i in f:
    n=i.split()
    if int(n[1])>75:
        out.write(n[0]+"\n")