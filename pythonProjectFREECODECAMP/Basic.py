name="Orange"

print(type(name))

print(type(name)==str)

print(isinstance(name,str))

#       CASTING

age=float(2)
print(age)
age1=int("2")
print(age1)

#       BOOLEAN

print(0 or 1)
print(False or "hey")
print("hi" or "hey")
print([] or False)
print(False or [])
print({} or [])

#       TERNARY OPERATOR

def is_adult(age):
     return True if age > 18 else False

print(is_adult(18))


name = 'CHETAN'
SPLIT = 'Chetan Sunil Killewale'
print(SPLIT.split())

#           ESCAPING CHARACTER

Name = 'Che"\'tan'
print(Name)

print(Name[-1])

#           SLICING

n="If you know,You know!"

print(n[:11])
print(n[11:])