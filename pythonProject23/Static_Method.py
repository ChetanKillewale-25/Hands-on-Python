
#       STATIC METHOD

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
    @staticmethod
    def info2():
        print("```STATIC METHOD IS USED WHEN WE ARE NOT INTRESTED IN CLASS VARIABLES AND VARIABLES")
        print("For example: finding factorial of a number```")


Student.info2()