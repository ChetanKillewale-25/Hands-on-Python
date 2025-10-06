#       FILTER USING LAMBDA OR ANONYMOUS FUNCTION

from functools import reduce

def is_even(n):
    return n%2==0

nums = [2,3,456,78,90,87,98]

evens =list(filter(is_even,nums))
odds =list(filter(lambda n: n%2!=0,nums))
doubles=list(map(lambda n:n*2,evens))
sum= reduce(lambda a,b:a+b,doubles)

print(evens)
print(odds)
print(doubles)
print(sum)