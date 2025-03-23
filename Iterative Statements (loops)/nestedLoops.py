for x in range(3):
  for y in range(1, 10):
    print(y, end=" ")
  print()


rows = int(input("Enter number of rows"))
cols = int(input("Enter number of columns"))
symbol = input("Enter a symbol to use")

for x in range(rows):
  for y in range(cols):
    print(symbol, end="")
  print()