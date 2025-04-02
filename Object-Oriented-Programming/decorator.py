# Decorator = A function that extands the behaviour of another function w/o modifying the base function
#             Pass base function as an argument to the decorator



def add_sprinkles(func):          # decorator
  def wrapper(*args, **kwargs):                  # wrapper is necessary so that decorator works only when the main function is called, args and kwargs are necessary when the base function has certain input parameters
    print("You add sprinkles")
    func()
  return wrapper

def add_fudge(func):
  def wrapper(*args, **kwargs):
    print("You add fudge")
    func()
  return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
  print(f"Here is your {flavor}ice cream")

get_ice_cream("vanilla")