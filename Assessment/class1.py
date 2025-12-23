#Abstraction : Data Hiding

from abc import ABC,abstractmethod

class Employer(ABC):    #abstract class
    def salary(self):   #abstract method
        pass
        
class Varsha(Employer):
    def salary(self):
        print("Varsha got 20k!!")
        

class Ved(Employer):
    def salary(self):
        print("Ved got 40k!!")
    

class Ved1(Employer):
    def salary(self):
        print("Ved1 got 40k!!")
    

obj = Varsha()
obj.salary()

obj1 = Ved()
obj1.salary()

obj2 = Ved1()
obj2.salary()

