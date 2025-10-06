"""x = -5
if x<0:
    raise Exception ('X should be positive')

x = -5
assert(x>=0),'x is not Positive'
"""
try:
    a = 5/0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is Fine')
finally:
    print('Cleaning Up')
