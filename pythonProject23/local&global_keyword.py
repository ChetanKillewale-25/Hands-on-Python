
a=10
print(id(a))

def something():
    a=9                            #HERE A WAS PARTIALLLY MADE LOCAL FOR THIS LOCAL
    x=globals()['a']               #ACCESSING THE GLOBAL VARIABLE WITH THE ADDRESS
    print(id(x))
    print("x:",x)
    print("a:",a)
    globals()['a']=15              #GLOBALLY CHANGING THE GLOBALLY VARIABLE
    print("x:",x)
    print("a:",a)
something()
print("outside function a:",a)