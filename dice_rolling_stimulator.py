import random
min=1
max=6
rollagain="Yes"
while rollagain=="Yes":
    print(random.randint(min,max))
    rollagain=input("Roll the dice again?")
    if rollagain=="No":
        print("GoodBye")
