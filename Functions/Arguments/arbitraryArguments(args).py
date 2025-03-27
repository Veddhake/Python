# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
# * is the unpacking operator

def add(*nums):
#  print(type(nums))   # it is a tuple
    total=0
    for num in nums:
        total+=num
    return total

print(add(1,2,3))

def display_name(*args):
    for arg in args:
      print(arg, end=" ")

display_name("Mr.","Ved", "Dhake")