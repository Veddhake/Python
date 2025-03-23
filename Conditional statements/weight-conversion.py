weight= float(input("Enter your weight: "))
unit= input("Kgs or lbs? (K/L): ")

if unit=="K":
  weight*=2.205
  unit="Lbs"
  print(f"Your weight is: {round(weight,1)} {unit}")
elif unit=="L":
  weight/=2.205
  unit="kgs"
  print(f"Your weight is: {round(weight,1)} {unit}")
else:
  print("Wrong input")

