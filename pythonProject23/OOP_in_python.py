
class Complex:
    def config(self):
        print("i3,8GB,256SSD")
        return

com1=Complex()
com2=Complex()

Complex.config(com1)
Complex.config(com2)

#   METHODS , VARIABLES AND INIT METHOD

class Comp:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        return
    def config(self):
        print("CPU is: "+self.cpu)
        print("RAM is: "+self.ram)
        return

com1=Comp("i3","8GB")
com1.config()
