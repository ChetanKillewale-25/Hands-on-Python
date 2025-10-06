"""
SETS : UNORDERED, MUTABLE, NO DUPLICATES
"""

myset = {1,2,3,4,5,6}
print(myset)

myset = set([1,2,3])
print(myset)

myset = set("Hello")
print(myset)

myset ={}
print(type(myset))

myset = set()
print(type(myset))
myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(3)
print(myset)
myset.clear()
print(myset)

odds = {1,3,5,7}
evens = {2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens)
print(u)
i = odds.intersection(primes)
print(i)
diff = odds.difference(primes)
print(diff)
diff = primes.difference(odds)
print(diff)

sdiff = evens.symmetric_difference(primes)
print(sdiff)
sdiff = primes.symmetric_difference(evens)
print(sdiff)

setA = {1,3,5,7}
setB = {2,4,6,8}
setC = {2,3,5,7}

setA.update(setB)
print(setA)

setB.intersection_update(setC)
print(setB)

setC.difference_update(setA)
print(setC)
setC2 = {2,11,56,78}
setC2.symmetric_difference_update(setA)
print(setC2)

print(setA.issubset(setB))

"""
FROZENSETS : 
"""

a =frozenset([1,2,3,4,5,6])
#a.add(9)
#a.remove(6)
print(type(a))
print(a)