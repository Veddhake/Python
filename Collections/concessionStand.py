menu={"pizza":3.00,
      "nachos": 4.00,
      "soda":5.00,
      "samosa":2.00,
      "fries": 7.00
      }

cart=[]
total = 0

print("-----------MENU-------------")
for key,value in menu.items():
  print(f"{key:10}: ${value:.2f}")

print("-------------------------------")

while True:
  food=input("select an item (q to quit):")
  if food.lower()=="q":
    break
  else:
    cart.append(food.lower())
    total += menu.get(food.lower())

print(f"Your total is {total}")