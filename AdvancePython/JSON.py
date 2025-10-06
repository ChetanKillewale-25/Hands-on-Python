"""
JAVA SCRIPT OBJECT NOTATION
"""
#       CONVERTING
import json
person = {"name": "Mohan", "age": 60, "city": "Akola", "has_children": True, "tile": "Hard_Worker"}
personJSON = json.dumps(person,indent = 4,)
print(personJSON)


#       WRITING INTO A FILE
with open('person.json',"w") as file:
    json.dump(person, file, indent = 4)

#       READING FROM A FILE
with open('person.json','r') as file:
    person1 = json.loads(personJSON)

print(person1)