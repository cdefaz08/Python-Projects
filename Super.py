class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self,name, age):
        super().__init__(name)
        self.age = age    

    def greet(self):
        print("Hello I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"hello, my student id is: {self.student_id}")
    
    def introtuce(self):
        print(f"Hello, My name is {self.name}, I'm {self.age} years old, and my student is is {self.student_id}")

Student = Student ("Ana",20,"S123")
Student.greet()
Student.introtuce()