#   DICTIONARY - (KEY : VALUE) pair

dogs={"name":"Roger","age":6}
dogs["name"]="Syd"
print(dogs)

print("\nExample1")
print(dogs.get("name"))
print(dogs.get("color"))

print("\nExample2")
print(dogs.get("color","Brown"))

print("\nExample3")
dogs={"name":"Roger", "age":6, "color": "Orange"}
print(dogs.get("color","brown"))

print("\nExample4")
#print(dogs.pop("name"))
#print(dogs.popitem())
print("color" in dogs)
print(list(dogs.keys()))
print(list(dogs.values()))
print(list(dogs.items()))

