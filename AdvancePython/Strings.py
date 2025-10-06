"""
STRINGS : ORDERED, IMMUTABLE, TEXT REPRESENTAION
"""

mystring = "I'm a Programmer"
print(mystring)

mystr = """Hello 
Worlds"""
print(mystr)

mystr = """Hello \
Universes"""
print(mystr)

#mystr[0] = 'h'         #       CAN'T UPDATE A STRING
char = mystr[0]
print(char)

substring = mystr[::-2]
print(substring)

greeting = "Hii "
sentence = greeting + "Sanskruti"
print(sentence)

if "skruti" in sentence:
    print("yes")
else:
    print("no")

print(sentence.upper())
print(sentence.lower())
print(sentence.startswith("Hii"))
print(sentence.endswith("World"))
print(sentence.find('s'))
print(sentence.find('c'))
print(sentence.count("a"))
print(sentence.replace("Sanskruti", "Emma"))


my_str = "How are you doing...?"
mylist = my_str.split()
print(mylist)
newstr = " ".join(mylist)
print(newstr)

from timeit import default_timer as timer
mylist = ['a'] * 1000000
print(my_str)

"""
APPENDING STRINGS IN LISTS : 
"""

#       BAD
start = timer()
mystr = ''
for i in mylist:
    mystr += i
end = timer()
print(start - end)


#       GOOD
start = timer()
myst = ""
myst = "".join(mylist)
end = timer()
print(start - end)

