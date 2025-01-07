# from abc import *

# class Falcon(ABC):
#     def __init__(self):
#         self.mine={10,20,30,40,50}
#     #abstract function        
#     def heyThere(self):
#         pass
    

# class Winter(Falcon):
#     def heyThere(self):
#         print(self.mine)


# win=Winter()
# win.heyThere()



from abc import ABC
class bus(ABC):
    def volvo(self):
       # print("Hello")
        print("YYY")
        #pass
class SRT(bus):
    def volvo(self):
        print("It a luxary bus")
class KPN(bus):
    def volvo(self):
        print("AC BUS ")
class SAT(bus):
    def volvo(self):
        print("Luxary vehicle ")
s=SRT()
s.volvo()
s1=SAT()
s1.volvo()
b=bus()
b.volvo() 
A=ABC()
A.volvo()