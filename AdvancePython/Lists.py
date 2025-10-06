"""
EXPLORING LISTS IN NEW WAY
LISTS : ORDERED , MUTABLE , ALLOWS DUPLICATE ELEMENTS
"""

mylist = ["banana", "cherry", "apple"]
item = mylist[-1]
print(item)

if "banana" in mylist :
    print("yes")
else:
    print("no")

mylist.append("lemon")
mylist.insert(1,"blueberry")
mylist.pop()
print(mylist)

#mylist.remove("banana")
#print(mylist)

mylist.reverse()
print(mylist)

print(mylist.sort())
print(mylist)                                   #These two are the sorteing methods
my_list = ["banana", "cherry", "apple"]         #used to sort lists
newlist = sorted(my_list)
print(newlist)

mylist1 = [0]*5
mylist2 = [1,2,3,4]
new_list = mylist1 + mylist2
print(new_list)

#SLICING
new_list2 = [1,2,3,4,5,6,7,8,9]
a = new_list2[3:6]
print(a)
b = new_list2[::-2]
print(b)

#COPYING METHOD
list_org = ["banana", "cherry", "apple"]
list_cpy1 = list_org
list_cpy2 = list_org[:]
list_cpy1.append("lemon")
list_cpy2.append("Avocado")
print(list_cpy1)
print(list_cpy2)
print(list_org)

list = [1,2,3,4,5,6,7,8,9]
a = [x*x for x in list]
print(a)