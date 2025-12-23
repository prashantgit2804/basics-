import random

# number = random.randint(1001,9999)

# print(number)



# l = [90545454,54545454,578545454,214542,45454,5456454]

# lucky = random.choice(l)

# print("Winner is : ",lucky)




number = random.randint(1,50)

while True:
    print("\n*********Enter Number between 1 to 50!*********\n")
    choice = int(input("Enter Choice : "))

    if choice>50:
        print("Invalid Number!!")
        break

    elif choice==number:
        print("Win!!")
        break

    elif choice<number:
        print("Original number is greater than the choice number!!")

    else:
        print("Original number is less than the choice number!!")

