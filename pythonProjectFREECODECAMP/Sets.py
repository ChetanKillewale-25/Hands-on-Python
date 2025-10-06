set1={"Roger","Syd"}
set2={"Roger"}

intersect = set1 & set2
print("Intersection: ",intersect)

mod = set1 | set2
print("Mod: ",mod)

sub = set1 -set2
print("Sub : ",sub)

comp = set1 < set2
print("Comp: ",comp)

# converting set into list

list = list(set1)
print(list)