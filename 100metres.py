#100 METERS 

import random
total100 = 0
attempts = 1
dice100 = [0, 0, 0, 0]
for d in range(4): #0,1,2,3
        dice100[0] = random.randint(1,6) #rolls all four dice
        dice100[1] = random.randint(1,6)
        dice100[2] = random.randint(1,6)
        dice100[3] = random.randint(1,6) 
        print(dice100)
        total100 = dice100[0] + dice100[1] + dice100[3] + dice100[2] #total of the 100 meter dice rolls
        print(total100)
        if attempts < 4:
            print("this was your #" , attempts , " attempt, you only have 4 attempts.")
        
        if attempts == 4:
            print("this was your fourth attempt, you must keep this sum")
            break
        else:
            happy = input("do you want to roll again(y) or keep this sum(n)? (y/n): ")
            if happy == "n" or happy == "n":
                break
            elif happy == "y" or happy == "Y":
                attempts = attempts + 1
        
print("you kept the a total of:" , total100) #the total of the first set of dice rolls
    
#not sure why the list is not going the way it should right now

    
