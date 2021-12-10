#100 METERS 

import random
total100 = 0 #sum of dice for first four rolls
attempts100 = 1 # attempts for first half 
total101 = 0 # sum of dice for second four rolls
attempts101 = 1  # attempts for second half
dice100 = [0, 0, 0, 0] #these dice will be used for the entire 100meters program
FINALSCORE100 = 0
for d in range(4): #0,1,2,3
        dice100[0] = random.randint(1,6)
        dice100[1] = random.randint(1,6)
        dice100[2] = random.randint(1,6)
        dice100[3] = random.randint(1,6)
        print(dice100)
        
        total100 = dice100[0] + dice100[1] + dice100[3] + dice100[2]
        if dice100[0] == 6:
            total100 = total100 - 6
        if dice100[1] == 6:
            total100 = total100 - 6
        if dice100[2] == 6:
            total100 = total100 - 6
        if dice100[3] == 6:
            total100 = total100 - 6
        print(total100)
        
        if attempts100 == 4:
            print("this was your fourth attempt, you must keep this sum")
            break
        else:
            print("this was your (", attempts100 , ") attempt, you only have four attempts")
            happy = input("do you want to roll again(y) or keep this sum(n)? (y/n): ")
            if happy == "n" or happy == "n":
                break
            elif happy == "y" or happy == "Y":
                attempts100 = attempts100 + 1
        
print("you kept the a total of:" , total100)

#second half of the program
print("now you must repeat rolling the dice and add the totals")
for d in range(4):
    dice100[0] = random.randint(1,6)
    dice100[1] = random.randint(1,6)
    dice100[2] = random.randint(1,6)
    dice100[3] = random.randint(1,6)
    total101 = dice100[0] + dice100[1] + dice100[3] + dice100[2]
    print(dice100)
    if dice100[0] == 6:
        total101 = total101 - 6
    if dice100[1] == 6:
        total101 = total101 - 6
    if dice100[2] == 6:
        total101 = total101 - 6
    if dice100[3] == 6:
        total101 = total101 - 6

    print(total101)
    if attempts101 == 4:
        print("this was your fourth attempt, you must keep this sum")
        break
    else:
        print("this was your (", attempts101 , ") attempt, you only have four attempts")
        happy = input("do you want to roll again(y) or keep this sum(n)? (y/n): ")
        if happy == "n" or happy == "n":
            break
        elif happy == "y" or happy == "Y":
            attempts101 = attempts101 + 1
        
print("you kept the a total of:" , total101)
print("your older score was:", total100)
print("you final score should be the sum of the two totals") #just a few print statements for user ease
FINALSCORE100 = total101 + total100
print("YOU FINISHED WITH A FINAL SCORE OF", FINALSCORE100) #finalscore

#this is a working program, but could be cleaned up a bit, 

    
