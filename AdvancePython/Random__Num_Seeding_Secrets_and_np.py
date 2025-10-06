import random

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(30,63))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(30,63))


import secrets
#       SECURITY PURPOSE
a = secrets.randbelow(10)       #   EXCLUDING UPPERBOUND
print(a)

a = secrets.randbits(4)         #   USES NUMBER OF BITS
print(a)

mylist = list('ABCDEF')
a = secrets.choice(mylist)

import numpy as np

n = np.random.rand(3)         #   ARRAY OF THREE ELEMENTS FROM 0 TO 1

print(n)

n = np.random.rand(3,3)       # ARRAY OF 3 * 3
print(n)

n = np.random.randint(0,10,3)
print(n)

n = np.random.randint(1,10,(3,4))
print(n)

print("1st")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
random.seed(1)
np.random.shuffle(arr)
print(arr)

print("2nd")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
random.seed(2)
np.random.shuffle(arr)
print(arr)

print("3rd")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
random.seed(1)
np.random.shuffle(arr)
print(arr)

print("4th")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
random.seed(2)
np.random.shuffle(arr)
print(arr)