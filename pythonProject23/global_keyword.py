#       GLOBAL AND LOCAL KEYWORD
a=10
def something():
    global a
    '''     Accessing the global variab;e and changing it
                                   with the help of gobal keyword            '''
    a=15
    print(a)

something()
print(a)