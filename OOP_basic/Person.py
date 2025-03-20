class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Chào bạn, tôi tên là {self.name}, {self.age} tuổi")
abc = Person("Toàn", 22)
abc.introduce()