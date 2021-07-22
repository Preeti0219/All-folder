import string 
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

blank = []
blank.extend(list(s1))
blank.extend(list(s2))
blank.extend(list(s3))
blank.extend(list(s4))

inputOfTheUser = int(input("Enter the length of the password \n :"))
random.shuffle(blank)
print("".join(blank[0:inputOfTheUser]))