"""
ITERTOOLS : PRODUCT, PERMUTATIONS, COMBINATIONS, ACCUMULATE, GROUP BY AND INFINITE ITERATORS
"""

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

prod1 = product(a, b, repeat=2)
print(list(prod1))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
perm1 = permutations(a,2)
print(list(perm1))

from itertools import combinations ,combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator
a= [1,2,3,4]
acc = accumulate(a)                        #    GOES ON UPDATING THE NUMBERS BY ADDING THEIR PREVIOUS VALUES
print(a)
print(list(acc))
acc1 = accumulate(a,func =operator.mul)
print(list(acc1))
acc2 = accumulate(a,func = max)
print(list(acc2))

print("groupby: ")
from itertools import groupby
def smaller_than_3(x):
    return x<3
a = [1, 2, 3 ,4]
group_obj = groupby(a, key = smaller_than_3)
for key,value in group_obj:
    print(key, list(value))
# using lambda function
group_obj2 = groupby(a, key = lambda x: x<3)
for key, values in group_obj2:
    print(key, list(values))

persons = [{'name': 'Siddhesh','age':20},
           {'name':"Atharva",'age':20},
           {'name':'Parimal','age':21},
           {'name':'Saish','age':20},
           {'name':'Advait','age':20}]

group_obj3 = groupby(persons, key = lambda x: x['age'])
for key, values in group_obj3:
    print(key,list(values))

from itertools import count, cycle, repeat

a = [1,2,3]
for i in count(10):
    print(i)
    if i==15:
        break

for i in cycle(a):
    print(i)
    if i == len(a):
        break
count = 0
for i in repeat(1):
    print(i)
    count+=1
    if count == 4:
        break

for i in repeat(1,4):
    print(i)