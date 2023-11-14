

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.notes = list[str]()

    def add_note(self, note: str) -> 'Person':
        self.notes.append(note)
        return self

    def add_notes(self, *notes: str):
        for note in notes:
            self.notes.append(note)

    def remove_note(self, index: int):
        self.notes.pop(index)

    def print_notes(self):
        for note in self.notes:
            print(note)

    # Magic methods, have specific names and they are called implicitely by Python interpreter
    # in response to certain events or operations
    # These magic methods allow us to customize the behaviour of our objects
    def __str__(self) -> str:
        return f'Person(name={self.name}, age: {self.age})'

class Database:
    def __init__(self) -> None:
        self.persons = list[Person]()

    def add_person(self, person: Person) -> 'Database':
        self.persons.append(person)
        return self

    def add_persons(self, *persons: Person):
        for person in persons:
            self.persons.append(person)

    def print_persons(self):
        for person in self.persons:
            print(person)


database = Database()

user_options = '''
a - Add Person,
r - Remove Person
u - Update Person
s - Switch Person
p - Print Persons
q - Quit App:
'''.strip() + ' '

while True:
    operation = input(user_options)

    match operation:
        case 'a':
            print('Add Person')
        case 'r':
            print('Remove Person')
        case 'u':
            print('Update Person')
        case 's':
            print('Switch Person')
        case 'p':
            print('Print Persons')
        case 'q':
            break
