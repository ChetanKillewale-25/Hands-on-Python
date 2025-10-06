# MUTABLE, INSERTION AND DELETION ARE BETTER PERFORMED

dogs=["Roger", 1, "syd", "Saturday"]
print(dogs)

print("Roger" in dogs)
print(dogs[-1])

#   SLICING
print(dogs[2:4])
print(len(dogs))

#   APPEND
dogs.append("Judah")
print(dogs)

#   EXTEND
#dogs+=["Quincy",7]
dogs.extend(["Quincy", 7])
print(dogs)
dogs+= "Tony"
print(dogs)

#   REMOVE
dogs.pop()
dogs.remove("Quincy")
print(dogs.pop())

#   INSERTING
items=["Roger","Syd"]
items.insert(2,"Test")
print(items)
items[1:1]=["Test1","Test2"]
print(items)

#   SORTING
items.sort(key=str.lower)
print(items)
itemscopy=items[:]
print(sorted(items,key=str.lower))
