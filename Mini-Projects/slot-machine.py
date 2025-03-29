import random

def spin_row():
  symbols = ['🍒','🍉','🍋','🔔','⭐']

  results = []
  for symbol in range(3):
    results.append(random.choice(symbols))
  
  return results

def print_row(row):
  print("--------------")
  print(" | ".join(row))
  print("--------------")

  

def get_payout(row, bet):
  if row[0]==row[1]==row[2]:
    if row[0]=='🍒':
      return bet * 3
    elif row[0]=='🍉':
      return bet*4
    elif row[0]=='🍋':
      return bet*5
    elif row[0]=='🔔':
      return bet*10
    elif row[0]=='⭐':
      return bet*50
  else:
    return 0

def main():
  balance = 100
  print("Welcome to Python Slots")
  print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

  while balance>0:
    print(f"Current balance: ${balance}")
    bet = input("Place your bet amount: ")

    if not bet.isdigit or int(bet)>balance or int(bet)<=0:
      print("Invalid bet")
      continue

    bet = int(bet)

    balance-=bet

    row = spin_row()
    print("Spinning...")
    print_row(row)

    payout=get_payout(row,bet)
    if payout>0:
      print(f"You won ${payout}")
    else:
      print("Sorry you lost")
    
    balance+=payout

    play_again = input("Do you want to spin again (Y/N): ").upper()

    if play_again != 'Y':
      break
    
  print("---------------------------------------------")
  print(f"Game Over! Your final balance is ${balance}")
  print("---------------------------------------------")

if __name__ == '__main__':
  main()