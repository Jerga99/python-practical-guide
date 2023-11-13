

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 100

person_1 = Person('Filip', 'Jerga')
person_2 = Person('John', 'Doe')
person_3 = Person('Ema', 'Walder')

print(person_1.first_name)
print(person_1.last_name)
print(person_1.age)

print(person_2.first_name)
print(person_2.last_name)
print(person_2.age)

print(person_3.first_name)
print(person_3.last_name)
print(person_3.age)


