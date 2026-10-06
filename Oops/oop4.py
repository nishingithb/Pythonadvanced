#define a class book with the following description
# data members
# bookname,book id,author id,author name,price title
# memeber methods
# getauthorid(), getauthorname(),getbooktitle(),getprice(),setauthorid(),setauthorname(),setbooktitle(),setprice()
class book:
    def __init__(self):
        self.bookname=input('enter book name: ')
        self.bookid = input('enter book id: ')
        self.authorid = input('enter author id: ')
        self.authorname = input('enter author name: ')
        self.price = int(input('enter price: '))
        self.title = input('enter title: ')
    def getauthorid(self):
        print(self.authorid)
    def setauthorid(self):
        self.authorid=input('enter a new id: ')
        self.getauthorid()

    def getauthorname(self):
        print(self.authorname)
    def setauthorname(self):
        self.authorname=input('enter a new name: ')
        self.getauthorname()

    def getbooktitle(self):
        print(self.booktitle)
    def setbooktitle(self):
        self.booktitle=input('enter a new title: ')
        self.getbooktitle()

    def getprice(self):
        print(self.price)
    def setprice(self):
        self.authorid=input('enter a new price: ')
        self.getprice()

b=book()
b.setauthorid()
b.setauthorname()
b.setbooktitle()
b.setprice()
