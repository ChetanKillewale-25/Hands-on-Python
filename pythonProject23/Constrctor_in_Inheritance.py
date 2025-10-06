"""
SUB CLASS CAN ACCESS ALL THE FEATURES OG SUPER CLASS BUT SUPER CLASS CANNOT ACCESS ANY FEATURES OF IT"S SUBCLASS
"""

class A:

    def __init__(self):
        print("In A's init!")

    def feature1(self):
        print("Feature1 working")

class B:

    def __init__(self):
        super().__init__()          #Here, Sub class can access all the features of it's Super class
        print("In B's init")

    def feature2(self):
        print("Feature 2 working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C's init!")


a1=B()
print("After Method Resolution Order")
a2=C()