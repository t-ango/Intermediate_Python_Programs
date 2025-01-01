# Geometric Objects and Triangle Class

This repository contains a Python implementation of a `GeometricObject` superclass and a `Triangle` subclass, 
demonstrating object-oriented programming (OOP) concepts like inheritance and encapsulation.

---

## Features

1. **GeometricObject Class**:
   - Represents a general geometric object.
   - Supports customization of color and filled state.

2. **Triangle Class**:
   - Inherits from `GeometricObject`.
   - Represents a triangle with specified side lengths.
   - Calculates the triangle's area using Heron's formula.
   - Calculates the perimeter of the triangle.

3. **User Interaction**:
   - Prompts the user to input triangle sides, color, and filled state.
   - Outputs the triangle's dimensions, color, filled state, area, and perimeter.

---

## How to Run
1. Run the program:
   ```bash
   python3 geometric_objects.py
   
2. Follow the prompts to input triangle details:
Enter side 1: 3
Enter side 2: 4
Enter side 3: 5
Enter color: blue
Is the triangle filled? True/False: true

3. View the output:
Triangle: side 1 = 3.0, side 2 = 4.0, side 3 = 5.0
Color: blue, filled: True, area: 6.0, perimeter: 12.0

**Applications**

Mathematics: Solving geometric problems programmatically.
Graphics and CAD: Modeling and rendering geometric shapes.
OOP Concepts: Demonstrates inheritance, method overriding, and encapsulation.

**Example Output**

Enter side 1: 6
Enter side 2: 8
Enter side 3: 10
Enter color: red
Is the triangle filled? True/False: false
Triangle: side 1 = 6.0, side 2 = 8.0, side 3 = 10.0
Color: red, filled: False, area: 24.0, perimeter: 24.0

**Requirements**

Python 3.x
