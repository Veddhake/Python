# format specifiers = {value:flags}   format a value based on what values are inserted

price1 =  3000.14159 
price2 = -9870.65
price3 =  1200.34

print(f"Price 1 : ${price1: .2f}")    # format specifier is used in the variable to specifyin which format it should be displayed as here, 2 decimal places will be displayed
print(f"Price 2 : ${price2: .1f}")    # here only 1 decimal
print(f"Price 3 : ${price3: .3f}")    # here 3 decimal places


print(f"Price 1 : ${price1: 10}")    #here the value must have 10 used spaces hence, spaces are added in front
print(f"Price 2 : ${price2: 010}")   #here we need to have ten used spaces but 0s are appended to the front
print(f"Price 3 : ${price3: <10}")   #here it is left aligned and the spaces after

print(f"Price 3 : ${price3: >10}")   #here it is right aligned which is the default
print(f"Price 3 : ${price3: ^10}")   #here it is center aligned

print(f"Price 1 : ${price1:+}")    # the + shows the symbols of the values, negative or positive
print(f"Price 2 : ${price2:+}")    
print(f"Price 3 : ${price3: ,}")  # each thousands place is comma separated

print(f"Price 3 : ${price3:+,.2f}")  # you can also make hybrid format specifiers with two or more


