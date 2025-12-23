# d = {}

# for i in range(1,31):
#     d[i]=i*i


# print(d)

# d = {}
# n = int(input("Enter Length of Dictionary : "))

# for i in range(1,n+1):
#     n1 = int(input("Enter Keys : "))
#     n2 = int(input("Enter Values : "))

#     d[n1]=n2

# print(d)

# l = [3,6,8]
# l1 = [8,9,10]

# d = {}


# for i in range(len(l)):

#     d[l[i]] = l1[i]

# print(d)

    

# d1 = {'p':400,'q':200}
# d2 = {'p':200,'q':100,'r':200}
# d3 = {}


# for i,j in d1.items():
#     for k,l in d2.items():

#         if i==k:
#             d3[i]=j+l

# print(d3)




# d = {
#     1:"hello",
#     2:{
#         'a':1,
#         'b':2
#     }
#     ,
#     3:"why"
# }

# print(d[2]['a'])


d = {}

n = int(input("Enter Number : "))

for i in range(1,n+1):

    d[i]={'square':i*i,'cube':i*i*i}

print(d)

