

"""
BUT WE CAN DO METHOD OVERRIDING IN PYTHON
"""

class A:

    def show(self):
        print("In A class ")

class B(A):
    def show(self):
        print("In B class ")

a1=B()
a1.show()