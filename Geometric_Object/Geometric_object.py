'''
Geometric Objects and Triangle Class

This program demonstrates object-oriented programming (OOP) concepts by defining a `GeometricObject` superclass and a `Triangle` subclass. The program allows users to define a triangle with specified sides, calculate its area and perimeter, and customize its color and filled state.

## Classes

### 1. `GeometricObject`
Represents a general geometric object with attributes:
- `color`: Color of the object (default: "white").
- `filled`: Boolean indicating whether the object is filled (default: `False`).
  
Methods:
- `get_color()`: Returns the object's color.
- `set_color(color)`: Sets and returns the object's color.
- `is_filled()`: Returns whether the object is filled.
- `set_filled(filled)`: Sets and returns the filled state.

### 2. `Triangle` (inherits from `GeometricObject`)
Represents a triangle with specified sides. Attributes:
- `side1`, `side2`, `side3`: Lengths of the triangle's sides (default: 1.0 for all sides).

Methods:
- `get_side1()`, `get_side2()`, `get_side3()`: Return the respective side lengths.
- `get_area()`: Calculates the area of the triangle using Heron's formula.
- `get_perimeter()`: Calculates the perimeter of the triangle.
- `__str__()`: Returns a string representation of the triangle's sides.

## Main Function
- Prompts the user to input the three sides of a triangle.
- Allows the user to customize the triangle's color and filled state.
- Calculates and displays:
  - Triangle's area and perimeter.
  - Triangle's color and filled state.

## Example Usage
Enter side 1: 3 Enter side 2: 4 Enter side 3: 5 Enter color: blue Is the triangle filled? True/False: true 
Triangle: side 1 = 3.0, side 2 = 4.0, side 3 = 5.0 Color: blue, filled: True, area: 6.0, perimeter: 12.0


## Applications
- Demonstrates inheritance and polymorphism in OOP.
- Provides a foundation for geometric computations in mathematics, graphics, or CAD software.
'''

class GeometricObject():
    def __init__(self, color="white", filled=False):
        self.color = color
        self.filled = filled

    def get_color (self):
        return self.color

    def set_color (self,color):
        self.color = color
        return self.color

    def is_filled (self):
        return self.filled

    def set_filled (self, filled):
        self.filled = filled
        return self.filled

class Triangle (GeometricObject):
    def __init__ (self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1 (self):
        return self.side1

    def get_side2 (self):
        return self.side2

    def get_side3 (self):
        return self.side3

    def get_area(self):
        import math
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s*(s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
    

    def get_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def __str__(self):
        return f'Triangle: side 1 = {self.side1}, side 2 = {self.side2}, side 3 = {self.side3}'


def main():

    triangle = Triangle(float(input("Enter side 1: ")), float(input("Enter side 2: ")), float(input("Enter side 3: ")))
    color = triangle.set_color(str(input("Enter color: ")))
    filled = triangle.set_filled(str(input("Is the triangle filled? True/False")).lower == "true")

    area = triangle.get_area()
    perimeter = triangle.get_perimeter()

    print (triangle)
    print ("Color: ", triangle.get_color(),", filled:", filled,", area: ", area,", perimeter: ", perimeter)


main()
    



    


