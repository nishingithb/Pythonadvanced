# f=open('k.txt','a')
# f.write('python')
# f.close()

# write a prgm to read content from one text file and appends it into another text file
# f=open('p.txt','w')
# f.write('python')
# f.close()
#
# f1=open('p.txt','r')
# content=f1.read()
# for i in content:
#     f1=open('k.txt','a')
#     f1.write(i)

# f=open('k.txt','a+')
# f.write('python')
# content=f.read()
# f.write(content)

################################## seek(),tell() ########################################################

# f=open('k.txt','a+')
# print('current position',f.tell())
#
# f.write('python')
# print('current position',f.tell())
#
# f.seek(0)
# print('current position',f.tell())
# content=f.read()
#
# print('content',content)
# f.write(content)

#################################### delete() ############################################################