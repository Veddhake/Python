name = input("Enter your full name: ")

result=len(name)  #return length of string (it includes spaces)

result = name.find("j")  #return the first occurence of a character
print(result)
result = name .rfind("d")  # retruns the last occurence of a character

name=name.capitalize()  # makes first character capital

name = name .upper()  #makes all characters capital

name=name.lower() # makes all characters lower case

result = name.isdigit() #returns true if all characters are numbers else false

result = name.isalpha() #returns true for all characters being alphabets, will return false for numbers and blank spaces as well

phone_number=input("Enter your phone number")

count = phone_number.count("-")  # counts how many specific characters are present within a string

phone_number.replace("-", " ")  #replace one character in string with another, here we replaced dashes with spaces

print(help(str))  # returns all string methods that exists in python
print(name)

print(result)
