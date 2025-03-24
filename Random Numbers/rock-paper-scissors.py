import random

options=("rock", "paper", "scissors")
player = None


running = True

while running:
  
  computer = random.choice(options)

  player = input("Enter a choice (rock, paper, scissors): ")

  print(f"Player: {player}")
  print(f"Computer: {computer}")

  if player==computer:
    print("It is a tie")
  elif player=="rock" and computer =="scissors":
    print("You Win")
  elif player=="rock" and computer =="paper":
    print("You Lose")
  elif player=="paper" and computer =="scissors":
    print("You Lose")
  elif player=="paper" and computer =="rock":
    print("You Win")
  elif player=="scissors" and computer =="paper":
    print("You Win")
  elif player=="scissors" and computer =="rock":
    print("You Lose")  
  
  play_again=input("Do you want to play again (y/n)?")
  if not play_again =="y":
    running = False

print("Thanks for playing")