username= input("Enter a username: ")

valid=True

if(len(username)>12):
  valid=False
elif(username.find(" ")>-1):
  valid=False
elif(not(username.isalpha())):
  valid=False

print(valid)