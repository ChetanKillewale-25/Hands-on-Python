"""
DECORATOR : A decoratotr is a function that takes another function as an argument and extends the behaviour
of this function without explicitly modifying it  (OR) It allows you to extend the behaviour of the function
without explicitly modifying it .
"""

#       FUNCTION DECORATORS

def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

#print_name = start_end_decorator(print_name)
result = add5(10)
print(result)


#       USING FUNCTOOLS :
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper1(*args, **kwargs):
            for _ in range(num_times):
                result1 = func(*args, **kwargs)
            return result1
        return wrapper1
    return decorator_repeat

@repeat(num_times = 4)
def greet(name):
    print(f"Hello {name}")

greet("Alex")



