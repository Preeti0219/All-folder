#****
#***
#**
#*

n = int(input("print the value of n \n "))
for i in range (0, n):
    for j in range (0, n-i):
        print("*", end="")

    print("\n")
