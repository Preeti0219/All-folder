# compauter will choose between between SNAKE WATER GUN and then you will choose between SMAKE WATER GUN
# WATER - GUN -> WATER WINS 
#WATER - SNAKE -> SNAKE 

from math import trunc
import random

def gameeWin(l2, p2):
    if l2 == p2:
        print("BOTH LOOSE")
        return None 
        
    
    
    elif l2 == "SNAKE":
        if p2 == WATER:
            return False
            print("Computer wins")
        elif p2 == GUN:
            return True 
        
    
    elif l2 == "WATER":
        if p2 == "GUN":
            return True 
            print("you win")
        elif p2 == "SNAKE":
            return True
            pritnt("computer wins")
        
        
    elif l2 == "GUN":
        if p2 == "SNAME":
            return  False
            print("computer wins")
        elif p2 == "WATER":
            return True



l1 = [ "SNAKE", "WATER", "GUN"]
l2  = random.choice(l1)
print(f"computer choosen : {l2}")

p2 = input("choose between SNAKE, WATER, GUN :\n ")

a = gameeWin(l2, p2)


if a == None:
    print("THE GAME IS TIE")

elif a:
    print(" you are win")
else:
    print("you lose")

