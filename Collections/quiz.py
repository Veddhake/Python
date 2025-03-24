

questions = ("What planet do we live on?","How many days in a leap year?","What is the hottest planet?","Which is the dwarf planet?","Which planet is the most huge?")

options=(("1. Earth","2. Venus","3. Mercury","4. Pluto","5. Jupiter"),("1. 240", "2. 365", "3. 366", "4. 400", "5. 280 "),("1. Earth","2. Venus","3. Mercury","4. Pluto","5. Jupiter"),("1. Earth","2. Venus","3. Mercury","4. Pluto","5. Jupiter"),("1. Earth","2. Venus"," 3.Mercury","4. Pluto","5. Jupiter"))

answers=("1","3","2","4","5")
guesses=[]
score = 0
question_num=0

for question in questions:
  print("-------------------------------")
  print(f"{question}")
  for option in options[question_num]:
    print(option)
  guess=input("Enter your answer")
  guesses.append(guess)
  if guess == answers[question_num]:
    score+=1
    print("CORRECT !")
  else:
    print("INCORRECT :(")
    print(f"{answers[question_num]} is the correct answer")
  question_num+=1
  

print(f"Your total score at the end is {score} ")