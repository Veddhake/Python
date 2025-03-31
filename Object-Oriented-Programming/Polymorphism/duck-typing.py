# "Duck Typing" = Another way to achieve polymorphism
#                 Object must have the minimum neccessary attributes/methods
#                 If it looks like a duck and quacks like a duck, it must be a duck

class Animal:
  alive = True

class Dog(Animal):
  def speak(self):
    print("WOOF")

class Cat(Animal):
  def speak(self):
    print("MEOW")    

class Car:                    # In this case the car can be treated as an animal as it has the minimum necessary attributes to classify as one
  alive = False

  def speak(self):
    print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
  animal.speak()
  print(animal.alive)