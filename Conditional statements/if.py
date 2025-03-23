age = int(input("Enter age: "))

if age>=18:
  print("adult")
elif age<0:
  print("not born")
else :
  print("child")

response = input("Would you like food? (Y/N):")

if response == "Y":
  print("have food")
else :
  print("no food")

name= input("Enter your name:")

if name == "":
  print("No name entered")
else:
  print(f"Your name is {name}")

for_sale= True

if for_sale:
  print("this item is for sale")
else:
  print("not for sale")