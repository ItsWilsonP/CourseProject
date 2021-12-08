# 110 Metre Hurdles
# Throw all five dice, up to six times, until you are satisfied with the results
# Scoring = total value of all five dice

import random

score = 0 # record's the user's score
dice = [0, 0, 0, 0, 0]

for i in range(6):
    # roll five dice
    for d in range(5): #0, 1, 2, 3, 4
        dice[d] = random.randint(1,6)
    # list dice with five random numbers
    score = sum(dice)
    question = input("Do you want to roll again?  y/n")
    if question == "n":
        break  # exit the for-loop

# message with the final score

    
