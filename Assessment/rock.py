import random
user = ["rock","paper","scissor"]

computer = random.choice(user)


for i in range(1,4):

    menu = """
    press 1 for Rock
    press 2 for Paper
    press 3 for Scissor


"""
    print(menu)

    choice = int(input("Enter Choice : "))

    if choice==1 and computer=="scissor":
        print("You win!!")

    elif choice==2 and computer=="Rock":
        print("You win!!")

    elif choice==3 and computer=="Paper":
        print("You win!!")

    else:
        print("Computer Win!!")
