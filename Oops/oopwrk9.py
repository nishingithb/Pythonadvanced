# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.

# class circle:
#     def __init__(self):
#         self.radius=int(input('enter ur radius: '))
#     def getarea(self):
#         self.area=3.14*self.radius**2
#         print('area: ',self.area)
#     def getperimeter(self):
#         self.perimeter=2*3.14*self.radius
#         print('perimeter: ',self.perimeter)
#
# c=circle()
# c.getarea()
# c.getperimeter()

# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
# class account:
#     def __init__(self):
#         self.acctnumber=int(input('enter account number: '))
#         self.acctname = input('enter account name: ')
#         self.balance = int(input('enter balance: '))
#     def getwithdraw(self):
#         self.amount=int(input('enter a amount to withdraw: '))
#         self.balance=self.balance-self.amount
#         print('balance: ',self.balance)
#
#     def getdeposit(self):
#         self.amount=int(input('enter a amount to deposit: '))
#         self.balance=self.balance+self.amount
#         print('balance: ',self.balance)
#
#     def showbalance(self):
#         print('balance amount: ',self.balance)
#
# # a=account()
# # a.getwithdraw()
# # a.getdeposit()
# # a.showbalance()
# a=account()
# b=account()
# l=[a,b]
# for i in l:
#     print(f"Account no: {i.acctnumber} / Name: {i.acctname} / Balance: {i.balance}")
#
# b = Bank()
#
# # b.showbalance()
# #print the balance of the person whose account number matches with the
# # entered number
#
# l = [a, b]
# number = input("Enter account number: ")
#
# for i in l:
#     if (i.accno == number):
#         print("Balance is: ", i.balance)
#         print(f"Account number {i.accno} Name: {i.name} Balance {i.balance}")



# Write a menu-driven Python program for a banking system using
# Account to perform the following operations:
#
# 1. Create an account
# 2. Withdraw money
# 3. Deposit money
# 4. Display balance
# 5. Exit
#
# Store account details in a list and search accounts using the account
# number.
# Display "Account Not Found" if the account does not exist.

class account:
    def __init__(self):
        self.acctnumber = int(input('enter account number: '))
        self.acctname = input('enter account name: ')
        self.balance = int(input('enter balance: '))

    def getwithdraw(self):
        self.amount = int(input('enter a amount to withdraw: '))
        self.balance = self.balance - self.amount
        print('balance: ', self.balance)

    def getdeposit(self):
        self.amount = int(input('enter a amount to deposit: '))
        self.balance = self.balance + self.amount
        print('balance: ', self.balance)

    def showbalance(self):
        print('balance amount: ', self.balance)

l=[]
while(1):
    print('Menu Driven')
    print('1.create an account')
    print('2.withdraw money')
    print('3.deposit money')
    print('4.display money')
    print('5.exit')
    ch=int(input('enter ur choice: '))
    if ch==1:
        a=account()
        l.append(a)
    elif ch==2:
        num=int(input('enter ur account number: '))
        for i in l:
            if(i.acctnumber==num):
                i.getwithdraw()
            break
        else:
            print('account not found')
    elif ch==3:
        num = int(input('enter ur account number: '))
        for i in l:
            if (i.acctnumber==num):
                i.getdeposit()
            break
        else:
            print('account not found')
    elif ch==4:
        num = int(input('enter ur account number: '))
        for i in l:
            if (i.acctnumber==num):
                i.showbalance()
            break
    elif ch == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")