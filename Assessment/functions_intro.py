def fac():
    print("Fac!!")

def  prime():
    print("Prime!!")

 


while True:     #infinite loop

    menu = """
    press 1 for Fac
    press 2 for Prime
    press 3 for Reverse
    press 4 for Exit

"""
    print(menu)
    choice = int(input("Enter Choice : "))

    if choice==1:
        fac()
    elif choice==2:
        prime()

    elif choice==3:
        pass
    elif choice==4:
        print("Thank uh!!")
        break

    else:
        print("Invalid choice!!")
        break

