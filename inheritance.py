
PI = 3.14

class Circle:
    # class attribute
    name = 'Nice Circle'

    def __init__(self, r: float) -> None:
        # instance atribute
        self.r = r

    def compute_circumference(self):
        return 2 * PI * self.r

    def __str__(self) -> str:
        return f'r = {self.r}'


Circle.name = 'Some other name'

c_1 = Circle(5)
# c_1.name = 'Some other name'
c_2 = Circle(10)
c_3 = Circle(2.4)

print(c_1.name)
print(c_2.name)
print(c_3.name)

