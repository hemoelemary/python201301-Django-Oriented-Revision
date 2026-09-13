class Animal:
    fur_color="orange"
    def eat(self):
        pass
    def chase(self):
        pass
    def speak(self):
        print("RAAWR")
class Tiger(Animal):
    def speak(self):
        print('greaat')
class Cat(Animal):
    fur_color='black'
    def speak(self):
        print('meow')
tiger =Tiger()
tiger.speak()
cat = Cat()
cat.speak()
print(cat.fur_color)
