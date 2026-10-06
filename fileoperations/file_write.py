# write operation

# f=open(filename,accessmode)

f=open('k.txt', 'w')   #if file already exits , then it will erase the contents and returns
                      #its reference #to f

                      #else it will create an empty text file and return


#f.write(string)

# f.write('hello')   #write() argument must be str not int
# f.close()

# sample="""A young man dreamed of building something that would make a difference,
# even though everyone around him doubted he could.
# Every day, he spent hours learning new skills, failing, improving, and trying again.
# There were moments when he wanted to give up, but he reminded himself that success is built one small step at a time.
# Months later, his hard work finally paid off when people began using and appreciating what he had created.
# Looking back, he realized that the greatest reward wasn(the success itself—it was becoming stronger, wiser,
# and more confident through every challenge he faced.)"""
# f.write(sample)

#f.writeline()

# content=['python\n','java\n','hello\n']
# f.writelines(content)
# f.close()