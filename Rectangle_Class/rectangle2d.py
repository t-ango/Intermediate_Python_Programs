'''
Rectangle2D Class

This program implements a `Rectangle2D` class to model a 2D rectangle and provides various methods for geometric calculations, comparisons, and containment checks.

## Class: rectangle2D
### Attributes:
- `x`: X-coordinate of the rectangle's center.
- `y`: Y-coordinate of the rectangle's center.
- `width`: Width of the rectangle.
- `height`: Height of the rectangle.

### Methods:
1. **Getters and Setters**:
   - `getX()`, `getY()`, `getWidth()`, `getHeight()`: Return the respective attributes.
   - `setX(x)`, `setY(y)`, `setWidth(width)`, `setHeight(height)`: Update the respective attributes.

2. **Geometric Calculations**:
   - `getArea()`: Calculates and returns the rectangle's area.
   - `getPerimeter()`: Calculates and returns the rectangle's perimeter.

3. **Containment Checks**:
   - `containsPoint(rectangle)`: Checks if the rectangle contains the center of another rectangle.
   - `contains(rectangle)`: Checks if the rectangle fully contains another rectangle.
   - `overlaps(rectangle)`: Checks if the rectangle overlaps with another rectangle.

4. **Comparison Methods**:
   - `lt(rectangle)`, `le(rectangle)`, `eq(rectangle)`, `ne(rectangle)`, `gt(rectangle)`, `ge(rectangle)`: Compare the areas of two rectangles using less than, less than or equal to, equal to, not equal to, greater than, and greater than or equal to operators.

5. **Special Methods**:
   - `containsAnother(rectangle)`: Determines if the corners of the current rectangle are fully within another rectangle.

## Main Function
- Prompts the user to input the dimensions and positions of two rectangles.
- Creates two `rectangle2D` objects based on the user input.
- Outputs:
  - Area and perimeter of both rectangles.
  - Whether the first rectangle contains the second, overlaps it, or contains its center.
  - Comparison of the two rectangles' areas.
'''

class rectangle2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    #get methods

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth (self):
        return self.width
    
    def getHeight (self):
        return self.height
    
    #set methods
    
    def setX (self, x=0):
        x = float(input("Enter x: "))
        return x

    def setY (self, y=0):
        y = float(input("Enter y: "))
        return y

    def setWidth (self, width=0):
        width = float(input("Enter width: "))
        return width
    
    def setHeight (self, height=0):
        hieght = float(input("Enter height: "))
        return self.height
    
    #calculation methods
    
    def getArea (self):
        area = self.getWidth() * self.getHeight()
        return area
    
    def getPerimeter(self):
        perimeter = (self.getWidth() + self.getHeight())*2
        return perimeter
    
    def containsPoint (self, rectangle):
        #rectangle with center(a,b) contains point(x,y) if true: a-x<= width/2 and b-y<=height/2

        if (abs(self.getX()- rectangle.getX()) <= self.getWidth()/2 and (abs(self.getY()-rectangle.getY())<= self.getHeight()/2)):
            return True
        else: 
            return False
        

    def contains (self, rectangle):
        #locate corners of rectangle 2:
        x1 = rectangle.getX() - rectangle.getWidth()/2
        x2 = rectangle.getX() + rectangle.getWidth()/2
        y1 = rectangle.getY() - rectangle.getHeight()/2
        y2 = rectangle.getY() + rectangle.getHeight()/2

        #see if self contains all corners:
        if (abs(self.getX()-x1) <= self.getWidth()/2) and (abs(self.getX()-x2) <= self.getWidth()/2) \
            and (abs(self.getY() - y1) <= self.getHeight()/2) and (abs(self.getY()-y2) <= self.getHeight()/2):
            return True
        else:
            return False
    
    
    def overlaps (self, rectangle):
        #locate corners of rectangle 1:
        x1 = self.getX() - self.getWidth()/2
        x2 = self.getX() + self.getWidth()/2
        y1 = self.getY() - self.getHeight()/2
        y2 = self.getY() + self.getHeight()/2

        #locate corners of rectangle 2:
        a1 = rectangle.getX() - rectangle.getWidth()/2
        a2 = rectangle.getX() + rectangle.getWidth()/2
        b1 = rectangle.getY() - rectangle.getHeight()/2
        b2 = rectangle.getY() + rectangle.getHeight()/2
        
        #see if rectangle 1 contains some corners of rectangle 2 and vice versa:
        if (abs(rectangle.getX()-x1) <= rectangle.getWidth()/2) and (abs(rectangle.getY() - y1) <= rectangle.getHeight()/2)\
            or (abs(rectangle.getX()-x2) <= rectangle.getWidth()/2) and (abs(rectangle.getY()-y2) <= rectangle.getHeight()/2)\
            or (abs(self.getX()-a1) <= self.getWidth()/2) and (abs(self.getY() - b1) <= self.getHeight()/2)\
            or (abs(self.getX()-a2) <= self.getWidth()/2) and (abs(self.getY()-b2) <= self.getHeight()/2):
            return True
        else:
            return False
        
    def containsAnother (self, rectangle):

        #locate corners of self:
        a1 = self.getX() - self.getWidth()/2
        a2 = self.getX() + self.getWidth()/2
        b1 = self.getY() - self.getHeight()/2
        b2 = self.getY() + self.getHeight()/2

        #see if all corners in another rectangle:
        if (abs(rectangle.getX() - a1) <= rectangle.getWidth()/2) and (abs(rectangle.getX() - a2) <= rectangle.getWidth()/2) \
            and (abs(rectangle.getY() - b1) <= rectangle.getHeight()/2) and (abs(rectangle.getY() - b2) <= rectangle.getHeight()/2):
            return True
        else:
            return False
        
    #special methods 
        
    def lt (self, rectangle):
        if self.getArea() < rectangle.getArea():
            return True
        else: 
            return False
        
    def le (self,rectangle):
        if self.getArea() <= rectangle.getArea():
            return True
        else:
            return False
        
    def eq (self, rectangle):
        if self.getArea() == rectangle.getArea():
            return True
        else:
            return False
        
    def ne (self,rectangle):
        if self.gerArea() != rectangle.getArea():
            return True
        else:
            return False
        
    def gt (self, rectangle):
        if self.getArea() > rectangle.getArea():
            return True
        else:
            return False
        
    def ge (self, rectangle):
        if self.getArea() >= rectangle.getArea():
            return True
        else:
            return False


def main():
    x1 = eval(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    width1 = float(input("Enter width 1: "))
    height1 = float (input("Enter height 1: "))

    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    width2 = float(input("Enter width 2: "))
    height2 = float (input("Enter height 2: "))


    rect1 = rectangle2D(x1, y1, width1, height1)
    rect2 = rectangle2D(x2, y2, width2, height2)

    print ("Area of r1 is ", rect1.getArea())
    print ("Perimeter of r1 is ", rect1.getPerimeter() )
    print ("Area of r2 is", rect2.getArea())
    print ("Perimeter of r2 is", rect2.getPerimeter())
    print ("r1 contains center of r2?", rect1.containsPoint(rect2))
    print ("r1 contains r2?", rect1.contains(rect2))
    print ("r1 overlaps r2?", rect1.overlaps(rect2))
    print ("r1 < r2?", rect1.lt(rect2))

    

main()

