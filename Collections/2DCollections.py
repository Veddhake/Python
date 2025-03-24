# you can also make sets of tuple or tuples of lists or tuples of tuples of tuples of lists of sets and so on...
# List of Lists


fruits =      ["apple","orange","banana","coconut"]
vegetables =  ["celery","carrots","potatoes"]
meats =       ["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]

print(groceries)

print(groceries[2])  #prints lis of all meats

print(groceries[1][2])  #prints potatoes

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()