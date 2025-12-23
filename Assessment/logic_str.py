# s = "Java is the best language"

# print(len(s))

# print(s[-25:-11:2])
# print(s[-20::3])
# print(s[::-1])
# print(s[:-5:4])


# s = "Run this java script"

# print(len(s))

# print(s[-20:-2:4])
# print(s[:-8:3])
# print(s[-11::2])



# s = input("Enter Name : ")

# if s==s[::-1]:
#     print("Yes it is!!")

# else:
#     print("No it is not!!")

# s = input("Enter Name : ")
# rev = ""
# #hello
# for i in s:
#     #rev = ""
#     #h+="" rev = h
#     #e+h = eh
#     #l+eh=leh

#     rev = i+rev

# print(rev)




s = input("Enter Name : ")

if len(s)%2==0:
    print("Enter odd length of string!!")

else:
    mid = len(s)//2

    print(s[mid-1]+s[mid]+s[mid+1])



