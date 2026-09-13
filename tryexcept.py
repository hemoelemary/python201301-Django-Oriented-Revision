try :
    divide = 1/0
    print(divide)
except Exception:
    print('not gonna work')    

try :
    num = int('hello')
except Exception:
    print('hello is a string')    