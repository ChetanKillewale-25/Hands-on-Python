"""
DICTIONARIES : KEY-VLAUE PAIRS, UNORDERED, MUTABLE
"""

mydict = {"name": "Sanskruti","age":19,"lastname":"Shintre","city":"Nashik"}
print(mydict)

value = mydict["age"]
print(value)

mydict["email"]="vedi@chetan.com"
print(mydict)

mydict["email"] = "coolvedi@chetan.com"
print(mydict)

print(mydict.popitem())

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error 59")
print("keys: ")
for key in mydict.keys():
    print(key)

print("Values: ")
for value in mydict.values():
    print(value)
print("Items: ")
for item in mydict.items():
    print(item)

my_dict = {"love": True,"age":20}
my_dict.update(mydict)
print(my_dict)

mydict1 = {3:9,6:36,9:81}
#value = mydict1[0]       #   HERE WE CAN'T ASSIGN THE VALUE
#value = mydict1[2]
print(value)

mytuple = (3,1)
mydict2 = {mytuple : 31}
print("A dict containing a tuple",mydict2)

mylist = [3,1]
mydict3 = {mylist : 31}
print("A dict can't contain a list",mydict3)        # i.e LIST ARE UNHASHABLE