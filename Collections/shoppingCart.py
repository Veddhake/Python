# Shopping Cart using lists

foods =[]
prices =[]
total=0

while True:
  food = input("Enter the food you want (q to quit): ")
  if food.lower()=="q":
    break
  else:
    price = float(input("Enter the price of a {food}: $"))
    foods.append(food)
    prices.append(price)

print("---- Your Cart ----")

for food in foods:
  print(food)

for price in prices:
  total+=price

print(f"Your total is ${total}")
