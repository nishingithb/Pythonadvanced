# define a class named person. accept name and age from the user.
# display the details by using show() method.
# create an object and call the ethid

# class person:
#     def __init__(self):
#         self.name=input("enter your name: ")
#         self.age=int(input("enter your age: "))
#     def show(self):
#         print('name: ',self.name,'age: ',self.age)
# p=person()
# p.show()
# p1=person()
# p1.show()

class person:
    def __init__(self):
        self.name=input('')
        self.age=int(input(''))
    def show(self):
        print('name: ',self.name,'age: ',self.age)

p=person()
p.show()