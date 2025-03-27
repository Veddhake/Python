# An argument preceded by an identifier helps with readability and order of arguments doesn't matter

def hello(greeting, title, first, last):
  print(f"{greeting} {title} {first} {last}")

# hello("Hello", "Mr.", "Ved", "Dhake")

hello("hello", first="Ved", title="Mr." ,last="Dhake")    #positional arguments should always be at the start

for x in range(1,11):
  print(x, end=" ")     #end is a keyword argument

print("1", "2", "3", "4", "5", sep="-")   #sep is a keyword argument

def get_phone(country, area, first, last):
  return f"{country}-{area}-{first}-{last}"

phone_num= get_phone(country = 1, area=123, first=456, last=7890)

print(phone_num)