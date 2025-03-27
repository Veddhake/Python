# Membership  operators = used to test whether a value or variable is found in a sequence or collection etc.
#                         They are: 1. in 
#                                   2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
  print(f"{letter} was found")
else:
  print(f"{letter} was not found")


students = {"Spongebob", "Patrick", "Sandy"}
student = input("Enter the name of a student: ")

if student in students:
  print(f"{student} is in students")
else:
  print(f"{student} not in students")


grades = {"Ved": "A",
          "Sandy": "B",
          "Patrick":"C",
          "Dave": "D"}

student = input("Enter the name of a student: ")

if student in grades:
  print(f"{student}'s grade is {grades[student]}")
else: 
  print(f"{student} was not found")
  

email = "FakeMail@gmail.com"

if "@" in email and "." in email:
  print("Valid Email")
else:
  print("Invalid Email")