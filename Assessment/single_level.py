# class Myclass:      #parent
#     def fun1(self):
#         print("Method 1!!")


# class Myclass2(Myclass):        #child
#     def fun2(self):
#         print("Method 2!!")


# obj = Myclass2()
# obj.fun1()
# obj.fun2()



class Myclass:      #parent
    def fun1(self):
        print("Method 1!!")


class Myclass2(Myclass):        #child
    def fun2(self):
        print("Method 2!!")


class Myclass3(Myclass2):
    def fun3(self):
        print("Method 3!!")


obj = Myclass3()
obj.fun1()
obj.fun2()
obj.fun3()
