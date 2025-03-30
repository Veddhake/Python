# object = a bundle of related attributes and methods
#          You require a class to make many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:                                            # we can keep class either in the same file or we can import it from another file
  def __init__(self, model, year, color, for_sale):   #constructor
    self.model = model
    self.year = year
    self.color = color
    self.for_sale=for_sale

  def drive(self):
    print(f"You drive the {self.model}!")
  
  def stop(self):
    print(f"You stop the {self.model}")

  def describe(self):
    print(f"{self.year} {self.color} {self.model}")

car1=Car("BMW", 2024, "blue", False)
car2=Car("Mercedes", 2025, "green", True)

print(car1.model)     # '.' is used to access a particular attribute
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)     # '.' is used to access a particular attribute
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car2.drive()

car1.stop()
car2.stop()

car1.describe()
car2.describe()
