

def show_balance(balance):
  print(f"Your balance is ${balance:.2f}")

def deposit():
  amount = int(input("Enter amount to be deposited"))
  if amount<0:
    print("Invalid Amount")
    return 0
  else :
    return amount
  

def withdraw(balance):
  amount = int(input("Enter amount to be withdrawn"))
  if amount>balance:
    print("Insufficient balance")
    return 0
  elif amount < 0:
    print("Invalid amount")
    return 0
  else :
    return amount

def main():

  balance = 0
  is_running = True

  while is_running:
    print()
    print("------- Banking Program --------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      show_balance(balance)
    elif choice == '2':
      balance+=deposit()
    elif choice == '3':
      balance-=withdraw(balance)
    elif choice == '4':
      is_running = False
    else:
      print("Invalid choice")

  print("--------- THANK YOU ----------")


if __name__ == '__main__':
  main()