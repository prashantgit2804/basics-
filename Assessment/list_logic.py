# a = []
# ev = []
# od = []
# for i in range(1,31):
#     a.append(i)

#     if i%2==0:
#         ev.append(i)
#     else:
#         od.append(i)

# print(a)
# print(ev)
# print(od)



# a = [1,2,3,1,2]

# uni = []
# dup = []
# for i in a:
#     if i not in uni:
#         uni.append(i)
#     else:
#         dup.append(i)
# print(uni)
# print(dup)



a = [26,62,42,21,11]


for i in range(0,len(a)):
    for j in range(i+1,len(a)):

        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]


print(a)


print("Smallest : ",a[0])
print("Largest : ",a[-1])
print("Second largest : ",a[-2])



