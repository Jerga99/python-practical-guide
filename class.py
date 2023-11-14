

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
            print(f'{person.name} - {person.age} Years')


person_1 = Person('Filip', 32)
person_2 = Person('John', 24)

database = Database()

database.add_person(person_1).add_person(person_2)
database.add_persons(Person('Kate', 40), Person('Suzan', 35))

database.print_persons()
