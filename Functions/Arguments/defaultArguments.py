# A default value for certain parameters used when argument is omitted making function flexible and reducing number of arguments

def net_price(list_price, discount=0, tax=0.05):    # discount and tax have default values only changed when an argument pertaining to it is passed
  return list_price*(1-discount) *(1+tax)

# print(net_price(500,0,0.05))

print(net_price(500))

print(net_price(500,0.1))

import time

def count( end ,start=0):
  for x in range(start,end+1):
    print(x)
    time.sleep(1)
  print("Done")

count(10)
count(30,15)
