# Objective: Create classes for different geometric shapes where
# specific shapes inherit from a base class Shape.

# Base Shape Class:
# Create a base class Shape with general attributes and methods common to all shapes,
# such as __str__, area and perimeter calculations

# Inheritance for Specific Shapes:
# Implement derived classes Rectangle, Square and Circle that
# inherit from the base class Shape, each defining methods to calculate
# its specific area and perimeter.

# c = Circle(3)
# s = Square(5)
# We need two values for both sides
# r = Rectangle(2, 22)

# shapes: tuple[Shape] = (c,s,r)

# for shape in shapes: print(shape)

# print should ouput:
#   Area of Circle is '...', Perimeter of Circle is: '...'
#   Area of Square is '...', Perimeter of Square is: '...'
#   Area of Rectangle is '...', Perimeter of Rectangle is: '...'

class Shape:
    PI = 3.14
    def __init__(self, name = 'Shape') -> None:
        self.name = name

    def compute_perimeter(self) -> float:
        return -1.0

    def compute_area(self) -> float:
        return -1.0

    def __str__(self) -> str:
        return (f'Area of {self.name} is {self.compute_area()},'
        f'Perimeter of {self.name} is: {self.compute_perimeter()}')

class Circle(Shape):
    def __init__(self, r) -> None:
        super().__init__(name = 'Circle')
        self.r = r

    def compute_perimeter(self) -> float:
        return 2 * Shape.PI * self.r

    def compute_area(self) -> float:
        return Shape.PI * (self.r ** 2)

class Square(Shape):
    def __init__(self, a) -> None:
        super().__init__(name = 'Square')
        self.a = a

    def compute_perimeter(self) -> float:
        return 4 * self.a

    def compute_area(self) -> float:
        return self.a ** 2

class Rectangle(Shape):
    def __init__(self, a, b) -> None:
        super().__init__(name = 'Rectangle')
        self.a = a
        self.b = b

    def compute_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def compute_area(self) -> float:
        return self.a * self.b

_c = Circle(3)
_s = Square(5)
_r = Rectangle(2.13, 20)

shapes: tuple[Shape, ...] = (_c, _s, _r)

for shape in shapes:
    print(shape)
