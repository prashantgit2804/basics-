import random
otp = random.randint(1001,9999)
d = {}

while True:
    menu = """
    press 1 for Signup
    press 2 for Login
    press 3 for Forgot-password
    press 4 for Exit

"""
    print(menu)

    choice = int(input("Enter choice : "))

    if choice==1:
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        mno = int(input("Enter Mobile number : "))
        password = int(input("Enter Password : "))

        cpassword=int(input("Enter Confirm Password : "))

        if password==cpassword:
            d['email']=email
            d['password']=password
            d['mno']=mno

            print("Signup Successfully!!")

        else:
            print("Password does not match!!")


    elif choice==2:
        email = input("Enter Email : ")
        password = int(input("Enter Password : "))
        

        if d['email']==email and d['password']==password:
            print("Login successfully!!")

        else:
            print("Invalid credentials!!")

    elif choice==3:
        mno = int(input("Enter Mobile number : "))

        if d['mno']==mno:
            print("Your otp is : ",otp)

            uotp = int(input("Enter OTP : "))

            if uotp==otp:
                password = int(input("Enter Password : "))

                d['password']=password
                print("Password updated!!")

            else:
                print("Invalid otp!!")

        else:
            print("Invalid Mobile number!!")

    elif choice==4:
        print("Thank you!!")
        break