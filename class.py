

class Person:
    def __init__(self, name: str, age: int):
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

    def remove_person(self, index: int):
        self.persons.pop(index)

    def update_person(self, index: int, new_name: str, new_age: int):
        self.persons[index] = Person(new_name, new_age)

    def switch_person(self, source_idx: int, target_idx: int):
        temp = self.persons[source_idx]
        self.persons[source_idx] = self.persons[target_idx]
        self.persons[target_idx] = temp

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

def ask_person_input():
    name_input = input('Enter person name: ')
    age_input = int(input('Enter person age: '))
    return (name_input, age_input)

def ask_index_input(question = 'Enter person index: '):
    i = int(input(question))
    return i

while True:
    operation = input(user_options)

    match operation:
        case 'a':
            # person_input = ask_person_input()
            (_name, _age) = ask_person_input()
            database.add_person(Person(_name, _age))
        case 'r':
            _index = ask_index_input()
            database.remove_person(_index)
        case 'u':
            (_name, _age) = ask_person_input()
            _index = ask_index_input()
            database.update_person(_index, _name, _age)
        case 's':
            _source_index = ask_index_input()
            _target_index = ask_index_input(question='Move to index: ')
            database.switch_person(_source_index, _target_index)
        case 'p':
            database.print_persons()
        case 'q':
            break
