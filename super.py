class Animal:
    fur_color="orange"
    def eat(self):
        # raise NotImplementedError
        pass
    def chase(self,chased=''):
        print('i am chasing a',chased)
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        print('woof')
class Cat(Animal):
    def chase(self):
        super().chase('rat')
    def speak(self):
        print('meow')    

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()

