n = int(input("Enter Number : "))
rem = 0
arm = 0
n1=n

#153 % 10 = 15.3
#27+0 = 27

#15 1.5  125+27+1 =153
while(n!=0):
    rem = n%10
    arm = rem*rem*rem+arm
    n = n//10

if n1==arm:
    print("Yes!!")

else:
    print("No!!")