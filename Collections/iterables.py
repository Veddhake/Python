# Iterables = an object/collection taht can return its elements one at a time, allowing it to be iterated

# List
numbers=[1,2,3,4,5]

for number in numbers:
  print(number,end=" ")

print()

for number in reversed(numbers):
  print(number, end=" ")

# Set

fruits = {"apple","orange","banana","coconut"}

for fruit in fruits:
  print(fruit)

print()

# for fruit in reversed(fruits):      //sets cant be reversed as they are unordered
# print(fruit)

#Strings

name= "Ved Dhake"

for character in name:
  print(character, end= " ")

print()

# Dictionary

my_dictionary={"A":1,
               "B":2,
               "C":3}

for key in my_dictionary:
  print(key)

print()

for value in my_dictionary.values():
  print(value)

print()

for key, value in my_dictionary.items():
  print(f"{key} = {value}")