import random

lowest = 1
highest = 100
answer=random.randint(lowest,highest)
guesses=0
is_running = True

print("Python Number guessing game")
print(f"Select a number between {lowest} and {highest}")

while is_running:
  guess = int(input("Enter your guess"))
  guesses+=1
  if guess == answer:
    is_running = False
  elif guess>answer:
    print("Your guess was greater than required")
  elif guess<answer:
    print("Your guess was lower than required")

print(f"Congrats you guessed the number {answer} in {guesses} guesses")