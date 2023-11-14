

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 100
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


person_1 = Person('Filip')
person_2 = Person('John')

person_1.add_note('Buy milk').add_note('Heya').add_note('Whatever')
person_1.add_note('Learn Python')
person_1.add_note('Go outside')

person_1.add_notes('Note 1', 'Note 2', 'Note 3')

person_1.remove_note(0)

person_1.print_notes()

person_2.add_note('Buy bread')
person_2.add_note('Learn C#')
person_2.add_note('Go inside')

person_2.remove_note(-1)

person_2.print_notes()
