import time
import random,string
"""
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
"""
print("Hello welcome password generator")
#time.sleep(1)
passwordlen=int(input("How many charcters would you like your password to have: "))
#password_special=input("Would you like your password to have special characters e.g @\n Y/N ")
#certain=input("Would you like to use certain characters @\n Y/N ")
#print(string.ascii_letters)
b = []
for i in range(0, passwordlen):
    a=(random.randint(60,100))
    a = (chr(a))
    b.append(a)
    #print(a)
print(b)

for i in b:
    t = ""
    t=+i
print(t)
#chaing the range of the random generator
