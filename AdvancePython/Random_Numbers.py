import random

a = random.random()         #   PRINTS A FLOAT NUMBER FROM 0 TO 1
print(a)

a= random.uniform(1,10)     #   FLOAT FROM 0 TO 10
print(a)

a = random.randint(1,10)        #   INTEGER FORM 1 TO 10(Including the Higher_Bound)
print(a)


a = random.randrange(1,10)      #   INTEGER FROM 1 TO 10(Excluding th Higher_Bound)
print(a)

mylist = list('ABCDEFGH')
a = random.choice(mylist)
print("Random Choice", a)

a = random.sample(mylist, 4)        #   GIVE LIST OF RANDOM ELEMENTS ACCORDING TO THE SIZE
print(a)

random.shuffle(mylist)
print((mylist))

