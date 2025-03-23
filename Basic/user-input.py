name = input("What is your name?")  #when we use input() we store it is a string hence if you are storing an int or other data type, type casting is necessary
age= int(input("how old are you?"))
age=age+1
print(f"Hello {name}")
print(f"Age: {age}")


#rectangle area calc

length=float(input("Enter the length"))
width=float(input("Enter the width"))

print(f"Area: {width * length}")