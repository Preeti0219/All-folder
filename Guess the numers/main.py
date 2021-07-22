import random

number = random.randrange(1,50)
num1 = int(input("Guess the value between 1 to 50 \n "))
print(f"{number}")

i = 5 
while(i>0):
    i = i-1
    if num1 > number:
        num1 = int(input("choose the lowe value /n "))
    elif num1 < number:
        num1 = int(input("choose the large number"))
    else:
        print("CONGRATULATION YOU WIN THE GAME")
        break
    if i ==1:
        print("You have only one chance now")
        
