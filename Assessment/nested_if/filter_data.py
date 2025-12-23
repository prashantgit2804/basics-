
i = 1
ev = 0
od = 0
evsum = 0
odsum = 0
sum = 0
while(i<=5):
    n = int(input("Enter Number : "))

    if (n%2==0):
        print(n,"is Even!!")
        ev = ev+1
        evsum = evsum+n
        #0+22 = 22
        #22+32 = 45

    else:
        print(n,"is Odd!!")

        od = od+1
        odsum = odsum+n
    
    sum = sum+n
    i = i+1

print("Count of even : ",ev)
print("count of odd : ",od)

print("Count of even sum: ",evsum)
print("count of odd sum: ",odsum)
