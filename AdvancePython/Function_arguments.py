

def foo(a,b,c):
    print(a,b,c)

foo(c=1, b=2, a=3)

def foo1(a,b,c,d=4):
    print(a,b,c,d)

foo1(1,2,3)


def foo2(a,b,*args,**kwargs):
    print(a,b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])

foo2(1,2,3,4,5,six=6,seven=7)
foo2(1,2,six = 6, seven = 7)

def foo3(*args, last):
    for arg in args:
        print(arg)
        print(last)

foo3(1,2,3,last=100)
# THE * OPERATOR UNPACKS ALL THE ITEMS OF LIST, BUT THE NUMBER OF ELEMENTS IN LIST MUST BE EQUAL TO THE NUMBER OF ARGUMENTS.
my_list = [0,1,2]
foo(*my_list)

"""my_tuple = (0,1,2,3)         
foo(*my_tuple)"""

MY_DICT = {'a':1, 'b':2, 'c':3}
foo(**MY_DICT)

def foo4(a_list):
    a_list.append(4)
    a_list[0] = -100
    a_list += [200, 300, 400]
    a_list = [200,300,400]              #   }   FOR THESE TWO PYTHON CREATES A COPY
    a_list = a_list + [200,300,400]     #   }   SO THAT THE ORIGINAL LIST OUTSIDE THE FUNC IS UNCHANGED.

my_list1 = [1,2,3]
foo4(my_list1)
print(my_list1)