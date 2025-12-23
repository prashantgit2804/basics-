import random
ac_no = random.randint(10000000001,99999999999)

class Bank:

    def ac_register(self):
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        mno = int(input("Enter Mobile number : "))
        password = int(input("Generate password : "))
        balanace = 5000
        self.name=name
        self.balance = balanace
        print("Your Generated account number is : ",ac_no)


    def deposit(self):
        damount = int(input("Enter Deposit amount : "))

        if damount>10000:
            print("Please enter below 10000!!")

        else:
            self.balance+=damount

            print("Deposit Successfully!!")

    def withdraw(self):
        wamount = int(input("Enter Deposit amount : "))

        
        
        self.balance-=wamount

        print("Withdraw Successfully!!")


    def checkbal(self):
        print("Your balance is : ",self.balance)



menu = """
press 1 for Register
press 2 for Exit

"""
print(menu)
choice = int(input("Enter Choice : "))

obj = Bank()

if choice==1:
    obj.ac_register()

    while True:
        menu1 = """
        press 1 for Deposit
        press 2 for Withdraw
        press 3 for Check Balance
        press 4 for  Exit


        """
        print(menu1)

        choice1 = int(input("Enter Choice : "))

        if choice1==1:
            obj.deposit()

        elif choice1==2:
            obj.withdraw()

        elif choice1==3:
            obj.checkbal()

        elif choice1==4:
            print("Thank uh!!")
            break

else:
    print("Thank uh!!")


        


