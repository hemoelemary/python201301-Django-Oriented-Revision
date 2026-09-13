# decorator is a function wrapped around another function

def myfunc():
    print('hamoda')
# myfunc()    

def my_decorator(func):
    def wrapper():
        print('do something here')
        func()
        print('original function is finished')
    return wrapper

newfunc = my_decorator(myfunc)
# newfunc()

@my_decorator
def newfu():
    print('hello i am mohamed')

newfu()


def decor(func):
    def wrapper():
        print('hello')
        func()
        print('done')
    return wrapper

@decor
def func():
    print('wrapped') 

func()