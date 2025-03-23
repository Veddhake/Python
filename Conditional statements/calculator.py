operator = input("Enter operator (+ - * /):")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

result=0

if operator=="+":
  result=num1+num2
elif operator=="-":
  result=num1-num2
elif operator=="*":
  result=num1*num2
elif operator=="/":
  result=num1/num2  

print(result)