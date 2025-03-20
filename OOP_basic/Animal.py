class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print(f"{self.name} Gâu gâu")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meo Meo")
cho = Dog("Ních xơn")
meo = Cat("Tom")
cho.speak()
meo.speak()