class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

person_1 = Person("John", 36)
person_2 = Person("Jane", 25)

person_1.greet()
person_2.greet()