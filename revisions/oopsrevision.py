import math

def strong(n):
    total=0

    for digit in str(n):
        total=total+math.factorial(int(digit))
    if total==n:
        print('true')
    else:
        print('false')
n=int(input('enter a number: '))
print(strong(n))
