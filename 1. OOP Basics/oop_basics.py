class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

person_1 = Person("khaled", 21)
print(person_1.age)
person_1.greet()