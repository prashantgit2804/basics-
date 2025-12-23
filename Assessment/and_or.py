n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = int(input("Enter Number 3 : "))
n4 = int(input("Enter Number 4 : "))

if n1>n2 and n1>n3 and n1>n4:
    print(n1,"is Greatest!!")

elif n2>n1 and n2>n3 and n2>n4:
    print(n2,"is Greatest!!")

elif n3>n1 and n3>n2 and n3>n4:
    print(n3,"is  Greatest!!")

else:
    print(n4,"is Greatest!!")