




print("""please select the patience name :
Rani 
Sonam""")

option = input("Please write here the patience name for whom you want to manage the record   :")
option1 = input("1 or 2 :")


def test():
    if option == "Rani":
        if option1 == "e":
            new = input("enter what u want  \n ")
            ans = open("efile1.txt", "a")  
            ans.write(new)
            ans.close()
        elif option1 == "d":
            new1 = input("enter what u want  \n ")
            for open("dfile1.txt", "a") in ans1:
                ans1.write(new1)
    elif option == "Sonam":
        if option1 == "e":
            new = input("enter what u want  \n ")
            ans = open("efile2.txt", "a")  
            ans.write(new)
            ans.close()
        elif option1 == "d":
            new1 = input("enter what u want  \n ")
            ans1 = open("dfile2.txt", "a")  
            ans1.write(new1)
            ans1.close()
    else:
        print("please select correct name, name is not existed in the databse")
        
test()

