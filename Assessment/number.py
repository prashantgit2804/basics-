# # class Myclass:

# #     def fun1(self):
# #         print("Hello")

# # class Myclass2(Myclass):

# #     def fun1(self):
# #         super().fun1()
# #         print("Hello1")


# # obj = Myclass2()
# # obj.fun1()


# class Myclass:
#     def fun1(self):
#         print("Hello")

# class Myclass2:

#     def fun1(self):
#         super().fun1()
#         print("Hello1")

# class Myclass3(Myclass2,Myclass):

#     def fun1(self):
#         super().fun1()
#         print("Hello3")



# obj = Myclass3()
# obj.fun1()


class My:

    def fun1(self):
        a=10
        self.a=a

    def fun2(self):
        print(self.a)


obj = My()
obj.fun1()
obj.fun2()


