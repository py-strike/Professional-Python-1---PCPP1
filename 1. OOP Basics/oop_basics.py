class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Developer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

person_1 = Person("khaled", 21)
person_2 = Developer("Kevin", 38)

print(f"Developer naem is {person_2.name}")
print(f"Developer is a subclass of Person : {issubclass(Developer, Person)}")
# print(person_1.age)
# person_1.greet()

def person_details(person: Person):
    if isinstance(person, Person):
        print(f"{person.name}, {person.age}")
    else:
        print("error")

person_details(person_1)
person_details(53)