f = open("test.txt", "r")

userInput = int(input("Enter theamount to be calcylated :"))
a = f.readlines()  
print(a)
#chooseTheCurrency = input("Choose the currency :")

#sum = userInput*chooseTheCurrency

myDict ={}
for line in a:
    parsed = line.split("\t")
    myDict[parsed[0]] = parsed[1]                                                                                                                                                                                                       b
print(myDict)