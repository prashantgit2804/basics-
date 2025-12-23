# try:
#     n = int(input("Enter Number : "))

#     if n>0:
#         print("Positive")

#     else:
#         print("Negative")

# except ValueError as e:
#     print(e)

# else:
#     print("Try executed!!")

# finally:
#     print("Finally executed!!")


# try:
#     n1 = int(input("Enter Number 1 : "))
#     n2 = int(input("Enter Number 2 : "))
#     print("Division : ",n1/n2)


# except ValueError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)


# try:
#     l = [56,32,24,46]

#     n = int(input("Enter Index number : "))

#     print("Value : ",l[n])

# except ValueError as e:
#     print(e)

# except IndexError as e:
#     print(e)


try:
    n1 = int(input("Enter Number 1 : "))
    n2 = int(input("Enter Number 2 : "))
    print("Division : ",n1/n2)

except Exception as e:
    print(e)
    print("Invalid Input!!")

