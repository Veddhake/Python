# super() = Function used in child class to call methods from a parent class (Super class)
#           Allows you to extand functionality of the inherited methods



class Shape:
  def __init__(self,color,is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
  def __init__(self,color,is_filled,radius):
    super().__init__(color,is_filled)           # super() is as if you would write the parent class name instead
    self.radius=radius
  
  def describe(self):                           # method overriding
    print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
    super().describe()

class Square(Shape):
  def __init__(self,color,is_filled,width):
    super().__init__(color,is_filled)
    self.width=width

  def describe(self):                           # method overriding
    print(f"It is a square with an area of {self.width*self.width}")
    super().describe()

class Triangle(Shape):
  def __init__(self,color,is_filled,width,height):
    super().__init__(color,is_filled)
    self.width=width
    self.height=height

circle = Circle("red",True, 5) 
print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe()     # gives the child class version (method overriding)

square = Square("blue",False,10)
square.describe()