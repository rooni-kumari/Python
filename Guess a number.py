#  Guess a number

import random
jackpot = random.randint(1,100)

number = int(input("enter a guessing number"))
count=1
while number != jackpot:
    if number < jackpot:
        print("it is low guess higher")
    elif number > jackpot:
        print("number is too high guess a low number")
    number = int(input("guess again"))
    count += 1
else:
    print("jackpot correct guess")
print("total attempt is ",count)