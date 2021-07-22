import random

number = random.randrange(1,50)
print(f"{number}")
num1 = int(input("Guess the value  \n "))

i = 0 
while(i<5):
    if num1 > number:
        input("choose the lowe value /n ")
    elif num1 < number:
        int(input("choose the large number"))
    else:
        print("CONGRATULATION YOU WIN THE GAME")
    i = i+1