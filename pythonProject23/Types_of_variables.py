#   NAMESPACE IS AN AREA WHERE YOU CREATE AND STORE OBJECT
class Car:
    wheels=4        #   Class variable - Defined inside the class

    def __init__(self):
        self.mil=10
        self.comp="BMW"     #   INSTANCE VARIABLE - DEFINED IN THE CONSTRUCTOR

c1=Car()
c2=Car()

c1.mil=69
Car.wheels=6

print(c1.mil,c1.comp,c1.wheels)
print(c2.mil,c2.comp,c2.wheels)