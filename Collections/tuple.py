
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER.


fruits =("apple","orange","banana", "coconut", "coconut")

print(len(fruits))

print("apple" in fruits)

print(fruits.index("apple"))

print(fruits.count("coconut"))

for fruit in fruits:    #ordered and duplicates
  print(fruit)