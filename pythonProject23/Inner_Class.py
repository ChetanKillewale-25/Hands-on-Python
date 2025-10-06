
"""
You can create a object of inner class inside the outer class
OR
You can create object of inner class outside the outer class,Provided you use outer class name to call it
"""
class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()


    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "ASUS"
            self.cpu = "i3"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("Chetan",32)
s2=Student("Lemon",64)


s1.show()

lap1=s1.lap
lap2=s2.lap

