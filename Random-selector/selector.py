import random

with open("strings.txt", "r") as f:
    stringlist = f.readlines()

num = input("How Many Do you want? ")

for i in range(int(num)):
    print(random.choice(stringlist))
    input("Enter to Continue")