#find the number of lines in a file
f = open("k.txt", "r")
lines = f.readlines()
print("Number of lines:", len(lines))
f.close()

#find the number of words in a file
f = open("k.txt", "r")
text = f.read()
words = text.split()
print("Number of words:", len(words))
f.close()

#program to display last 5 lines in a file
f = open("k.txt", "r")
lines = f.readlines()
for i in lines[-5:]:
    print(i, end="")
f.close()

# #program to change the content of second line in a file


# #progran to search a particular word inside the file

# #find the number of letters,digits and spaces inside the file.

#reverse the lines in a file

# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed the exam.
# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.

# Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it

# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.