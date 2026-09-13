class Animal():
    def __init__(self,color):
        self.color=color
    def chase(self,anim):
        print('i am chasing a',anim)
    def speak():
        raise NotImplementedError
    def get_color(self):
        return self.color

class Cat(Animal):
    def __init__(self,color):
        super().__init__(color)
    def chase(self):
        super().chase('mouse')
    def speak(self):
        print('meow meow meow')

cat = Cat('grey')
cat.chase()    