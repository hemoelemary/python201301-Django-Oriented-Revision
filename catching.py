num1 = input('put a num not string')
num2 = input('put a num not string')
try:
    num1 = int(num1)
    num2 = int(num2)
    print(num1/num2)
except ZeroDivisionError:
    print('error no x/0 is not valid operation')
except ValueError:
    print('error in datatype')
except Exception as e:
    print(e)    