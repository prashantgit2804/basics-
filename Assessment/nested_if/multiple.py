class Myclass:

    def parent1(self):
        print("Parent class!!")


class Myclass1:

    def parent2(self):
        print("Paarent class 2!!")
    

class Myclass2(Myclass,Myclass1):

    def parent3(self):
        print("Parent class 3!!")


obj = Myclass2()
obj.parent1()
obj.parent2()
obj.parent3()