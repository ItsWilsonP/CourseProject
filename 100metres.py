#100 METERS 

import random
def nicedice(num):
    if num == 1:
        return(u"\u2680")
    elif num == 2:
        return(u"\u2681")
    elif num == 3:
        return(u"\u2682")
    elif num == 4:
        return(u"\u2683")
    elif num == 5:
        return(u"\u2684")
    elif num == 6:
        return(u"\u2685")

total100 = 0 #sum of dice for first four rolls
attempts100 = 1 # attempts for first half 
total101 = 0 # sum of dice for second four rolls
dice100 = [0, 0, 0, 0] #these dice will be used for the entire 100meters program
nicedice100 = [0, 0, 0, 0] #the nice dice 100meters
FINALSCORE100 = 0
for d in range(4): #0,1,2,3
        dice100[0] = random.randint(1,6)
        dice100[1] = random.randint(1,6)
        dice100[2] = random.randint(1,6)
        dice100[3] = random.randint(1,6)
        print(dice100)
        nicedice100 = [nicedice(dice100[0]), nicedice(dice100[1]), nicedice(dice100[2]), nicedice(dice100[3])]
        print(nicedice100)
        
        total100 = dice100[0] + dice100[1] + dice100[3] + dice100[2]
        if dice100[0] == 6:
            total100 = total100 - 6
        if dice100[1] == 6:
            total100 = total100 - 6
        if dice100[2] == 6:
            total100 = total100 - 6
        if dice100[3] == 6:
            total100 = total100 - 6
        print("you rolled" , total100)
        

        
        if attempts100 == 7:
            print("this was your seventh attempt, you must keep this sum")
            break
        else:
            print("this was your (", attempts100 , ") attempt, you only have seven attempts")
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
    if attempts100 == 7:
        print("this was your seventh attempt, you must keep this sum")
        break
    else:
        print("this was your (", attempts100 , ") attempt, you only have seven attempts")
        happy = input("do you want to roll again(y) or keep this sum(n)? (y/n): ")
        if happy == "n" or happy == "n":
            break
        elif happy == "y" or happy == "Y":
            attempts100 = attempts100 + 1
        
print("you kept the a total of:" , total101)
print("your older score was:", total100)
print("you final score should be the sum of the two totals") #just a few print statements for user ease
FINALSCORE100 = total101 + total100
print("YOU FINISHED WITH A FINAL SCORE OF", FINALSCORE100) #finalscore

#im happy how the program is running, but i left in the actually numbers and included the nice 
#dice because i found the nice dice hard to read.
