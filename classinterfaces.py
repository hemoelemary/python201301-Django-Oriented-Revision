class Animal:
    fur_color="orange"
    def eat(self):
        # raise NotImplementedError
        pass
    def chase(self):
        pass
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        print('woof')
class HouseCat(Animal):
    pass


dog = Dog()
dog.speak()
cat = HouseCat()

cat.speak()
