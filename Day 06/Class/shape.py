import math

class Shape():
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height
    
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, width):
        super().__init__(width, 0)
    def area(self):
        return self.width*self.width
    def perimeter(self):
        return self.width*4

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, 0)
    def area(self):
        return 3.14159 * (self.radius**2)
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    def area(self):
        return (self.width * self.height)/2
    def perimeter(self):
        hypotenuse = math.hypot(self.width, self.height)
        return hypotenuse + self.width + self.height

if __name__ == "__main__":
    quadrado = Square(5)
    print(f"Square area: {quadrado.area():.2f} Perimeter: {quadrado.perimeter():.2f}")
    print("-"*20)
    circulo = Circle(6)
    print(f"circle area: {circulo.area():.2f} Perimeter: {circulo.perimeter():.2f}")
    print("-"*20)
    triangulo = Triangle(5, 10)
    print(f"Triangle area {triangulo.area():.2f} Perimeter: {triangulo.perimeter():.2f}")