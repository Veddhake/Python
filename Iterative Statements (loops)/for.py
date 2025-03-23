for x in range(1,11):   # in range(a,b) b is exclusive so the printed values will be actually a to b-1
  print(x)

for x in reversed(range(1,11)):   # for reversing the range range (a,b) will print values from b-1 to a
  print(x)

for x in range(1,11,3):     # range (a,b,c) shows that it will run form a to b-1 with steps of 3 so 1,4,7,10 etc.
  print(x)

credit_card="1234-5678-9012-3456"

for x in credit_card:
  print(x)

for x in range(1,21):
  if x==13:
    continue        # skips over 13
  else:
    print(x)

for x in range(1,21):
  if x==13:
    break        # when 13 comes the execution is stopped
  else:
    print(x)


