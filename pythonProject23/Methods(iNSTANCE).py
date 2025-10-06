"""
TYPES OF METHODS:
1]INSTANCE METHODS
2]CLASS METHODS
3]STATIC METHODS
"""

#INSTANCE METHOD TYPES: 1]ACCESSOR METHOD   &   2]MUTATOR METHOD

class Student:
    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get(self):                  #ACCESSOR
        return self.m1

    def set(self,value):            #MUTATOR
        self.m1=value

s1=Student(14,16,21)
s2=Student(26,21,21)

print(s1.avg())
print(s2.avg())
s1.set(26)
print(s1.get())