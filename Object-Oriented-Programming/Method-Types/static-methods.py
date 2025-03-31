# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

class Employee:

  def __init__(self, name, position):
    self.name=name
    self.position=position
  
  def get_info(self):                       # instance method, we first require to create object and then use the instance method
    return f"{self.name} = {self.position}"
  
  @staticmethod
  def is_valid_position(position):          # removes the need for creation of objects eg:- employee = Employee("Cook"), we can directly use the class name for the static methods purpose
    valid_positions=["Manager","Cashier", "Cook", "Janitor"]
    return position in valid_positions

print(Employee.is_valid_position("Cook"))   # static method used without any need to create objects


employee1 = Employee("Ved","Manager")       # instance method used by creating objets
employee2 = Employee("Bro","Cashier")
employee3 = Employee("Jack","Cook")

print(employee1.get_info())