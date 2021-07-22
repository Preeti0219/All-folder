
##Faulty calculator
#Calculator should show all value correct except -##If 56+ = 77, 89- = 77. 

def calculator():
    print("""Enter your math operator which you look to use while calculation:
    + for addition 
    - for substraction 
    * for mutliplication 
    % for modulo/ for division 
    ** for power""")
    options = input("Choose your operator \n ")
    num1 = int(input("Enter the first number \n "))
    num2 = int(input("enter the second number \n"))

    if options == "+":
        if num1 ==56:
            print("56+9 = 77")
        else: 
            print(f"{num1} + {num2} = {num1 + num2}")
    elif options == "-":
        if num1 == 89:
            print("89-7 = 54")
        else:
            print(f"{num1} - {num2} = {num1 - num2}")
    elif options == "*":
        print(f"{num1} * {num2} = {num1 * num2}")

    value = input("do you want to calculat more ? Yes press y , if No yes n  \n")
    if value == "y":
        calculator()
    elif value == "n":
        print("thanks for using calculator")

calculator() 










