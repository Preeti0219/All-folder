sum = 0
while (True):
    inputByuser = input("Enter the amout of the product \n :")
    if (inputByuser!="q"):
        sum = sum + int(inputByuser)
        print("total amount is", {sum},input("Enter the product name \n:"))
        
    else:
        print("Thanks for using our calculator")
        break
