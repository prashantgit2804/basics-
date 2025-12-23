# file = open("test1.txt","w")
# file.write("Hello this is write method!!")
# file.close()

# file = open("test2.txt","a")
# file.write("Hello this is append method!!")
# file.close()

# file = open("test1.txt","r")
# print(file.read())
# file.close()

# file = open("test3.txt","w+")
# file.write("This is write plus method!!")
# file.seek(0)
# print(file.read())
# file.close()

l = []
for i in range(1,31):
    l.append(i)


data=str(l)

file = open("test10.txt","w+")
file.write(data)
file.seek(0)
print(file.read())
file.close()



