import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, 'age': obj.age, obj.__class__.__name__: True}
    raise TypeError("Object of User is not JSON Serializable")

# Encoding the User object
user_json = json.dumps(user, default=encode_user)
print(user_json)
print(type(user_json))

# Decoding the User object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

decoded_user = json.loads(user_json, object_hook=decode_user)
print(type(decoded_user))
print(decoded_user.name)
