# List Comprehension = A concise way to create lists in python
#                      [expression for value in iterable if condition]


# doubles=[]
# for x in range(1,11):     Normal way by iteration
#  doubles.append(x * 2)

doubles = [x * 2 for x in range(1,11)]    # List Comprehensions 
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2==0]
odd_nums = [num for num in numbers if num%2==1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades =[grade for grade in grades if grade>=60]
print(passing_grades)