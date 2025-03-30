# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allows to share data among all objects created from that class

class Student:

  class_year = 2026
  num_student=0

  def __init__(self,name, age):
    self.name = name
    self.age=age
    Student.num_student+=1        # every time a instance of a student is created, num_student is incremented

student1=Student("Spongebob",30)
student2=Student("Patrick", 35)

print(student1.name)
print(student1.age)
print(Student.class_year)       # class = Student , class_year = class variable (better readability) can also write student1.class_year but the given syntax is better for readability

print(Student.num_student)      # returns number of instances of Student class created

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
