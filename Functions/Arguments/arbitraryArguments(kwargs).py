# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
# * is the unpacking operator

def print_address(**kwargs):
#  print(type(kwargs))        type of kwargs is a dictionary signifying they are key-value pairs

  for key,value in kwargs.items():
    print(f"{key} : {value}")

print_address(street="123 fake st.",
              apt="100",
              city="Detroit",
              state="Michigan",
              zip="54321")


#using args and kwargs together

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()
  
#  for value in kwargs.values():
#    print(value, end=" ")

  if "apt" in kwargs:
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
  else:
    print(f"{kwargs.get('street')}")

  print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")




shipping_label("Dr.","Spongebob","Squarepants","III",
               street="123 Fake st.",
               apt="100",
               city="Detroit",
               State="Michigan",
               zip="54321")