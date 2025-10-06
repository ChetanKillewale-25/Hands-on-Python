"""
Gnerators gives you Iterators without using next and iter function
"""

def topten():

    yield 1
    yield 2
    yield 3
    yield 4

values=topten()

print(values.__next__())
print(values.__next__())

print("Using Generators")

def Topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values = Topten()

for i in values:
    print(i)