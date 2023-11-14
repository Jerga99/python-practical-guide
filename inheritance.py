
PI = 3.14

class Shape:
    def __init__(self) -> None:
        self.name = 'Some Generic Shape'

    def some_shape_method(self):
        print('I am just shape method')

    def compute_circumference(self):
        return -1

class Circle(Shape):
    def __init__(self, r: float) -> None:
        super().__init__()
        self.r = r

    def compute_circumference(self):
        return 2 * PI * self.r

    def __str__(self) -> str:
        return f'r = {self.r}'

c_1 = Circle(5)
c_2 = Circle(10)
c_3 = Circle(2.4)

c_2.some_shape_method()
print(c_2.name)

