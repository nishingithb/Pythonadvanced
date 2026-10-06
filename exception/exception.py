try:
    n1=int(input('enter a number: '))
    n2=int(input('enter a number: '))
    sum=n1/n2
    print('result: ',sum)
except ValueError:
    print('ValueError')
except ZeroDivisionError
    print('ZeroDivisionError')
except:
    print('error')
else:
    print('no exception in normal block')
finally:
    print('finished')