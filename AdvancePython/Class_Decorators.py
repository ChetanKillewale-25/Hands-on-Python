"""
DO SAME THING AS FUNCTION DECORATOR BUT THEY ARE TYPICALLY USED IT YOU WANT TO MAINTAIN AN UPDATED SET
"""

class Countcalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')

        return self.func(*args, **kwargs)

@Countcalls
def say_hello():
    print('Hello')

say_hello()
say_hello()