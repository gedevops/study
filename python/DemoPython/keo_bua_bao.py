from random import randint

print ("Moi chon Keo, Bua, Bao")
player = input()
computer = randint (0,2)

if computer == 0:
    computer = "Keo"
if computer == 1:
    computer = "Bua"
if computer == 2:
    computer = "Bao"


print("---")
print ("You Choose: " + player)
print ("Computer Choose: " + computer)
print("---")

if player == computer:
    print ("Draw")
else:
    if player == "Keo":
        if computer == "Bua":
            print ("Lose")
        else:
            print ("Win")
    elif player == "Bua":
        if computer == "Keo":
            print ("Win")
        else:
            print ("Lose")
    elif player == "Bao":
        if computer == "Keo":
            print ("Lose")
        else:
            print ("Win")
    else:
        print("Da nhap sai")

