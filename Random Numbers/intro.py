import random

# help(random)    provides a comprehemsive list of all random functions

number=random.randint(1, 6)
print(number)

low=1
high=100

number=random.randint(low,high)
print(number)

number=random.random()    #returns a random floating point number

options=("rock","paper","scissors")
option=random.choice(options)
print(option)

cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards)
print(cards)
