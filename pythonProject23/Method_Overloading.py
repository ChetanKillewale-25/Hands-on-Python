"""
WE CAN'T SO METHOD OVERLOADING IN PYTHON
"""

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=0,b=0,c=0,d=0):
        s=0

        if(a!=0,b!=0,c!=0,d!=0):
            s=a+b+c+d

        elif a!=0 and b!=0:
            s=a+b

        else:
            s=a

        return s
s1=Student(31,59)

print(s1.sum(32))