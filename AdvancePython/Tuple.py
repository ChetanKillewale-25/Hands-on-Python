"""
TUPLES : ORDERED, IMMUTABLE, ALLOWS DUPLICATE ELEMENTS
"""

mytuple = tuple(["Max",28,"Boston"])
print(mytuple)

if "Tim" in mytuple:
    print("yes")
else:
    print("no")

mytuple = ('a', 'p', 'p', 'l', 'e')
print(mytuple.count('p'))
print(mytuple.index('l'))

my_list = list(mytuple)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

my_tuple1 = "Max", 28, "Boston"
name, age, city =my_tuple1
print(name,age,city)

my_tuple2 = (1,2,3,4)
i1, *i2, i3 =my_tuple2
print(i1)
print(i2)
print(i3)

import sys
my_list3 = [0,1,2,"hello",True]
my_tuple3 = [0,1,2,"hello",True]
print(sys.getsizeof(my_list3),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]"))
print(timeit.timeit(stmt="(0,1,2,3,4,5)"))

