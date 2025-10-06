

nums=[2,4,6.9]

it=iter(nums)

print(it.__next__())
print(it.__next__())
print(next(it))


class Topten:
    def __init_(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.num<=10):
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

c=Topten()

print(c.__next__())