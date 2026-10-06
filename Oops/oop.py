class person:
    def __init__(self,name,age): #is a constructor used to initialize data members
        self.name=name
        self.age=age
    def display(self):
        print("name is: ",self.name,'/age is: ',self.age)

#object creation
#objectname=class(arguments)
p=person('athulya',23)
p.display()