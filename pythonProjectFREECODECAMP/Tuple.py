""" We can't modify the Tuple
 i.e they are IMMUTABLE           """
names=("Roger", "Syd", "Bhanu", "Rohan")
print(names[0])
print(names.index("Bhanu"))
print(len(names))
print("Rohan" in names)
print(sorted(names))
print(names)
new_tuple= names + ("Habibi", "Max")
print(new_tuple)

