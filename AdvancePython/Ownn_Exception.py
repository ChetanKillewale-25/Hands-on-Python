"""
BY SUBCLASSING FROM THE BASIC EXCEPTION CLASS
"""

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100 :
        raise ValueTooHighError("Value is too High")
    if x < 5 :
        raise ValueTooSmallError("Value is too Small")

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
