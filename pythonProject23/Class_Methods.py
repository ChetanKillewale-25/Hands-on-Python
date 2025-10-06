
"""
CLASS METHODS
"""

class Student:
    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @classmethod
    def grab(cls,value):
        m1=value
        return m1

print(Student.grab(26))
print(Student.info())
