

org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

org1 = [0,1,2,3,4]
cpy1 = org1
cpy1[0] =-10
print(cpy1)
print(org1)

import copy
org2 = [[0,1,2,3,4],[5,6,7,8,9]]
cpy2 = copy.copy(org2)
cpy3 = copy.deepcopy(org2)
cpy2[0][0] = -10
print(cpy2)
print(org2)
print(cpy3)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

P1 = Person("John",90)
P2 = copy.copy(P1)

P2.age = 33
print(P1.age)
print(P2.age)

class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee

p1 = Person("Alex",55)
p2 = Person("Joe",27)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 63
print(company_clone.boss.age)
print(company.boss.age)