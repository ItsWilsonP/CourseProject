import random
def nicedice(num):
    if num == 1:
        return(u"\u2680") # nice dice with 1 on it
    elif num == 2:
        return(u"\u2681") # nice dice with 2 on it
    elif num == 3:
        return(u"\u2682") # nice dice with 3 on it
    elif num == 4:
        return(u"\u2683") # nice dice with 4 on it
    elif num == 5:
        return(u"\u2684") # nice dice with 5 on it
    elif num == 6:
        return(u"\u2685") # nice dice with 6 on it
Y100 = "NM" # yes or no for games
YJump = "M" # yes or no for games
Meters100 = False
HighJump = False
nextgame = " " # varible used to create a gap between games, wont store anything important
print("you have the option to play two games, either 100meters or high jump")
print("you have the option of playing either both, one or none!")
print("the first game is 100 meters, you have 4 dice, which you can throw seven times. You the total is added together, but sixes count negative")
print("once you finish the first four dice, you repeat the same process and then add the two totals together! You have seven retries for both sets of throws")
#lines above are a general introduction to the games
# the following lines are consist of a loop which asks the user which games they would like to play, along wiht brief instructions
while Meters100 == False: 
    Y100 = input("would you like to play 100 meters?:(y/n)")
    if Y100 == "y" or Y100 == "Y": 
        Meters100 = True
        break
    if Y100 == "n" or Y100 == "N":
        Meters100 = False
        break
    else:
        print('please answer "y" for yes, or "n" for no')

print("the second game is called high jump. Roll the dice and aim for a score higher than the bar, you can chose to skip to a certian height")
print("but if you fail to clear that height, you go back to the lowest height you were at.")
while HighJump == False:
    YJump = input("would you like to Highjump?:(y/n)")
    if YJump == "y" or YJump == "Y": 
        HighJump = True
        break
    if YJump == "n" or YJump == "N":
        HighJump = False
        break
    else:
        print('please answer "y" for yes, or "n" for no')
        
if Meters100 == True:


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
            nicedice100 = [nicedice(dice100[0]), nicedice(dice100[1]), nicedice(dice100[2]), nicedice(dice100[3])] # nice dice maker :)
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
        if attempts100 == 7: # program should end if it reaches takes 7 attempts
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


print(" ")
print(" ")
print(" ")
print(" ") # a few empty statements to create a gap between games
nextgame = input("you completed 100meters, press any key to continue")
print(" ") # a few empty statements to create a gap between games
print(" ")
print(" ")
print(" ")
print(" ") 
if HighJump == True:
    def nicedice(num):
        if num == 1:
            return(u"\u2680") # nice dice with 1 on it
        elif num == 2:
            return(u"\u2681") # nice dice with 2 on it
        elif num == 3:
            return(u"\u2682") # nice dice with 3 on it
        elif num == 4:
            return(u"\u2683") # nice dice with 4 on it
        elif num == 5:
            return(u"\u2684") # nice dice with 5 on it
        elif num == 6:
            return(u"\u2685") # nice dice with 6 on it
    
    
    #high jump and 100 meters
    # starting with high jump
    
    height = 10 # starting height for high jump
    restart = 0 # amount of restarts for high jump
    total = 0 # total of all dice for high jump
    diceHJ = [0, 0, 0, 0, 0]  #diceHJ stands for Dice High Jump
    skip =  0 # skip value
    skipPerm = " '" # skip permission
    heightC = 0 # stands for height cleared, used to differnciate when skips have been used
    while restart < 3:
        print("the bar is currently at" , height)
        print("the previous bar was at" , heightC)
        diceHJ[0] = random.randint(1,6)
        diceHJ[1] = random.randint(1,6)
        diceHJ[2] = random.randint(1,6)
        diceHJ[3] = random.randint(1,6)
        diceHJ[4] = random.randint(1,6)
        print(diceHJ)
        total = sum(diceHJ)
        print("you rolled " , total)
        
        if restart == 3:
            break
        else:
            if total >= height:
                heightC = height
                print("sucsess, the bar will be raised")
                print("you have the option to skip to a certain height, but if you fail to clear the bar, your score will be" , height)
                skipPerm = input("do you want to skip?(y/n)")
                while skipPerm == "y" or skipPerm == "Y": # what happens when the user wants to skip to a certain height
                    print("you  have elected to skip, please chose a height greater than" , height , "but less than 30")
                    skip = int(input("what number would you like to skip to?"))
                    if skip > 30:
                        print("please chose a number less than 30")
                    if skip < height:
                        print("please chose a height greater than the height you have already cleared (" , height , ")")
                    if skip > height and skip <= 30:
                        height = skip
                        print("the bar has been raised to" , skip)
                        break
                else: # if the user doesnt want to skip, 
                    print("you chose not to skip, the bar will be raised to" , height + 2)
                    height = height + 2
                    if height == 30:
                        print("congrats you jumped 30', that is the max height")
                        break
            else:
                restart = restart + 1
                print("try again, you rolled" , total , "you need to roll atleast a" , height)
    
    if heightC == 30:
        print("wow, you are pretty lucky you reached the max possible height of 30")
    else:
        print("you reached a height of " , heightC ,)  
        
        
print("that concludes the games, thanks for playing! Come back whenever!")
#end 
