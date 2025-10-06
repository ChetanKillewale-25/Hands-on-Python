"""
FUNCTIONS THAT RETURN AN OBJECT THAT CAN BE ITERATED OVER AND THE SPECIAL THING IS THAT THEY GENERATE
THE ITEMS INSIDE THE OBJECT ONE AT A TIME AND ONLY WHEN YOU ASK FOR IT. BECAUSE OF THIS THEY ARE MUCH MORE
MEMORY EFFICIENT THAN OTHER SEQUENCE OBJECTS SPECIALLY WHEN YIU HAVE TO DEAL WITH LARGE DATASETS.
"""

def mygenerator():
    yield 1
    yield 2
    yield 3
    yield -3
    yield -9
    yield 0


g = mygenerator()
print(g)

value = next(g)
print("Value: ",value)

for i in g:
    print(i)

#print(sum(g))
#print(sorted(g))

def count_down(num):
    print("Starting")
    while num >0:
        yield num
        num -= 1

cd = count_down(4)
print(next(cd))
print(next(cd))
print(next(cd))

#   EFFICIENCY TEST
import sys

def firstn(n):
    nums = []
    num = 0
    while num<n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num<n:
        yield num
        num+=1

print(sum(firstn(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(1000)))
print(sys.getsizeof(firstn_generator(1000)))

#       GENERATOR EXPRESSIONS: generator expressions are written with Parenthesis i.e ()

my_generator = (i for i in range(100) if i%2== 0)
print(list(my_generator))

mylist = [ i for i in range(100) if i%2==0]
print(list(mylist))

print(sys.getsizeof(my_generator))
print(sys.getsizeof(mylist))