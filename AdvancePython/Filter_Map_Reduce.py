#       MAP:
a = [1,2,3,4,5,6]
b = map(lambda x : x**2,a)
print(list(b))
b1 = [x**2 for x in a]
print(list(b1))

#       FILTER:
f = filter(lambda x : x%2==0,a)
print(list(f))
f1 = (x for x in a if x%2==0)
print(list(f1))

#       REDUCE:
from functools import reduce
r = reduce(lambda x,y : x*y, a)
print(r)