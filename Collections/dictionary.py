# dictionary = a collection of {key:value} pairs. 
#              Ordered and Changeable. No duplicates


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"
            }

print(capitals.get("India"))    #returns New Delhi

capitals.update({"Germany":"Berlin"})

capitals.update({"USA":"Detroit"})

capitals.pop("China")

capitals.popitem()    # removes the latest added item

keys = capitals.keys()
print(keys)           # provides all keys

for key in capitals.keys():
  print(key)

values = capitals.values()
print(values)

for value in capitals.values():
  print(value)

items = capitals.items()
print(items)        #it returns a 2d list of tuples

for key,value in capitals.items():
  print(f"{key}: {value}")