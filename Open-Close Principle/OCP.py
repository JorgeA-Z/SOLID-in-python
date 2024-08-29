import math
class Shape():
    def __init__(self) -> None:
        pass

    def Area() -> int:
        pass

class Rectangule(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        super().__init__()

    def Area(self) -> int:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radio: float) -> None:
        self.radio = radio
        super().__init__()
    
    def Area(self) -> float:
        return math.pi * self.radio**2

class AreaCalculator():
    def __init__(self) -> None:
        pass

    def calculateArea(self, shape: Shape):
        return shape.Area();


if __name__ == "__main__":
    rectangulo = Rectangule(10, 15);
    circulo = Circle(10);
    calculator = AreaCalculator();

    print(calculator.calculateArea(rectangulo))
    print(calculator.calculateArea(circulo))