
principle = 0
rate =0
time =0

while principle<=0:
  principle = float(input("Enter the principle amount"))

  if principle<=0:
    print("principle needs to be positive")

while rate<=0:
  rate = float(input("Enter the rate amount"))

  if rate<=0:
    print("rate needs to be positive")

while time<=0:
  time = float(input("Enter the time amount"))

  if time<=0:
    print("time needs to be positive")

print(principle)
print(rate)
print(time)

total = principle * pow((1+rate/100),time)
print(f"Balance after {time} year/s: ${total: .2f}")
