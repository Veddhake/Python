# multithreading = used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target = my_fucntion)

import threading
import time

def walk_dog(name):
  time.sleep(8)
  print(f"You finish walking {name}")

def take_out_trash():
  time.sleep(2)
  print("You take out the trash")

def get_mail():
  time.sleep(4)
  print("You get the mail")

chore1 = threading.Thread(target = walk_dog, args=("Scooby",)) # the ',' comma is important as it signifies that the argument input is a tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()    # join helps for the thread to stop to execute the code further
chore2.join()
chore3.join()

print("All chores are complete")