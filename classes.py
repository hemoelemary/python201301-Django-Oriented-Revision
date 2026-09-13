# def function():
#     pass

# class Animal:
#     pass

# animal = Animal() #object

#example
#properties
class Animal:
    prop1 = 'something'
    prop2 = {
        'key1':'value1'
    }
    lst = ['kane','kalob','gully']
    _private = 'private property'
    def method1(self):
        #method is a function inside a class
        return self.prop1
    @property
    def get_gully(self):
        return self.lst[2]     
    def add_name(self,name):
        self.lst.append(name)
        return self.lst
animal = Animal()
print(animal.prop1)   
print(animal.prop2) 
print(animal.prop2['key1'])
print(animal.lst)
print(animal.lst[2])
print(Animal.prop1) # as a class
print(Animal._private)
print(animal.method1())
print(animal.get_gully)
print(animal.add_name('lusy'))


class Human:
    age = [i for i in range(0,100)]
    def set_name(self,name):
        self.name=name
        return self.name
    @property
    def get_name(self):
        return self.name
human = Human()
print(human.set_name('mohamed'))    
print(human.get_name)