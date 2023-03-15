class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def area(self) -> int:
        return self.sides


class Rectangle(Shape):
    def __init__(self, width: str, height: float) -> None:
        shape = "Rectangle"
        shape_sides = 4
        super().__init__(name=shape, sides=shape_sides)
        self.width = width
        self.height = height

    def area(self) -> float:
        area = self.width * self.height
        return area


class Square(Rectangle):
    def __init__(self, side_lenght: float) -> None:
        super().__init__(side_lenght, side_lenght)
        self.side_lenght = side_lenght


square = Square(6)
print(square.name)  # prints "Rectangle"
print(square.sides)  # prints 4
print(square.area())  # prints 25
