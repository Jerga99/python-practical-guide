
import textwrap

PI = 3.14

class Shape:
    def __init__(self, name = 'Some Generic Shape') -> None:
        self.name = name

    def some_shape_method(self) -> str:
        text = 'I am just shape method'
        return text

    def compute_circumference(self):
        return -1

    def __str__(self) -> str:
        return textwrap.dedent(f'''
        Shape: {type(self)}
        Name: {self.name}
        Circumference: {self.compute_circumference()}
        ''').strip()

class Circle(Shape):
    def __init__(self, r: float) -> None:
        super().__init__('Some Circular Shape')
        self.r = r
        self._some_private_attribute = 42

    def _super_secret_method(self) -> str:
        value = super().compute_circumference()
        # value = self.compute_circumference()
        print(value)
        return 'Super Secret Method!'

    def compute_circumference(self):
        # self._super_secret_method()
        return 2 * PI * self.r

class Square(Shape):
    def __init__(self, a: float) -> None:
        super().__init__('Some Square Shape')
        self.a = a

    def compute_circumference(self):
        return 4 * self.a

    def some_shape_method(self):
        # text = self.some_shape_method()
        text = super().some_shape_method()
        result = 'I am just square method' + f' {text}'
        return result


shape = Shape()
c_1 = Circle(5)
c_2 = Circle(10)
s_1 = Square(3)
s_2 = Square(5.5)

shapes: list[Shape] = [shape, c_1, s_1, c_2, s_2]

# polymorphism allows objects of different tyoes to be treated as objects of a common
# base type
for shape in shapes:
    print(shape)

