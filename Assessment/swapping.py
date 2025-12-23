a = int(input("Enter Vaalue 1 : "))
b = int(input("Enter Vaalue 2 : "))

#a=60 b=30

#1) using third variable

# temp=a  #temp=60 a=blank
# a=b     #a=30 b=blank
# b=temp  #b=60 temp=blank


#2) without using third variable

# a = a+b     #60+30 a = 90
# b = a-b     #90-30 b=60
# a = a-b     #90-60 a=30



a,b = b,a

print("After swaaping value of A : ",a)
print("After swaaping value of B : ",b)