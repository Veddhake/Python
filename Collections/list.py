
#   List  = [] ordered and changeable. Duplicates OK


fruits = ["apple","orange", "banana", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[::2])
print(fruits[::-1])

print(len(fruits))  #for length of list

for fruit in fruits:
  print(fruit)

print("apple" in fruits)    # in operator used to check if an element is present in the list

fruits[0]="pineapple"   #changes the value of element at 0 to pineapple

print(fruits.count("apple"))    #gives how many of an element are there

print(fruits.index("coconut"))    #returns the index of coconut

fruits.append("pineapple")    #to insert value at end

fruits.remove("orange")    #removes that element

fruits.insert(0,"apple")  #inserts element at that location

fruits.sort()   # sorting 

fruits.reverse()  #reverses the list 

fruits.clear()   # removes all elements and gives empty list


#  print(dir(fruits))      # gives methods that the list can perform
#  print(help(fruits))     # gives description for the methods that can be performed
