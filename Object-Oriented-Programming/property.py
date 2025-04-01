# @property = Decorator used to define a method as a proeprty (it can be accessed like an attribute
#             Benefit: add additional logic when read, write or delete attributes
#             Gives getter, setter and deleter methods

class Rectangle:
  def __init__(self,width,height):
    self._width = width                   # writing _ makes the attributes as private
    self._height = height

  @property 
  def width(self):                        # getter for width
    return f"{self._width:.1f}cm"

  @property
  def height(self):                        # getter for height
    return f"{self._height:.1f}cm"

  @width.setter
  def width(self,new_width):
    if new_width>0:
      self._width = new_width
    else:
      print("Width must be greater than zero")

  @height.setter
  def height(self,new_height):
    if new_height>0:
      self._height = new_height
    else:
      print("Width must be greater than zero")

  @width.deleter
  def width(self):
    del self._width
    print("Width has been deleted")

  @height.deleter
  def height(self):
    del self._height
    print("Height has been deleted")


rectangle = Rectangle(3,4)

rectangle.width = 5
rectangle.height = 7

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)
