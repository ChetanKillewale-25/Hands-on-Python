
def hello(name):
    print("Hello " + name)

hello("Lemon")

def hello1(name = "My Friend"):
    print("Hello " + name)
hello1()

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    print(list(words))
    for word in words :
        say(word)

talk("I love you Lemon, i am sorry that i haven't helped you a single time , Do I have to loose you too...?")

def counter():
    count =0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment =counter()
print(increment())
print(increment())
print(increment())
