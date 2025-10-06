
class Person:
    def __init__(self):
        self.name="Chetan"
        self.age=19
        return

    def upgrade(self):
        self.age=27

    def disp(self):
        print(self.name)
        print(self.age)

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


com1=Person()
com2=Person()
com1.name="Chandragupta"

#com1.upgrade()

com1.disp()

if com1.compare(com2):
    print("They are same")
else:
    print("They are not")

print(id(com1))
print(id(com2))