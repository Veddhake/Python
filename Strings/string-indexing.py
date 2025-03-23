#indexing is used to access elements of a sequence using [] (indexing operator)
# indexing = [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # prints at index location, strings are stored as arrays

print(credit_number[0:4]) # prints first 4 digits, ending index exclusive, it is not included

print(credit_number[:4])  #works the same as above one

print(credit_number[5:9])

print(credit_number[5:])  #not specifying the ending index means it will go till the end

print(credit_number[-1])  # negative indexing is basically starting the string from the back and goign to the front so, -1 means 6, -2 means 5 and so on

print(credit_number[::2]) # step function is used to jumo that many characters so 2 here would print all the alternate characters from the start

print(credit_number[::3]) #jumps by 3 characters

last_digits = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")  # only last 4 digits visible

credit_number = credit_number[::-1] # this reverse the string as in step you are going backwards from last to front

print(credit_number)