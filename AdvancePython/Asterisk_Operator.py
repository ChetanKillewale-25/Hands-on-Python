

result = 3*9
print(result)

result1 = 3**9
print(result1)

zeros = [0]*9
print(zeros)

alpha = "AB" *9
print(alpha)

numbers = [1,2,3,4,5,6,7,8,9]
*begin,last = numbers
print(begin)
print(last)

begin,*last = numbers
print(begin)
print(last)

my_tuple = (1,2,3)
my_list = [4,5,6]
new_list = [*my_tuple,*my_list]
print(new_list)

my_tuple = (1,2,3)
my_dict = {1,2,3}
new_list = [*my_tuple,*my_dict]
print(new_list)

my_dict1 = {'a':1,'b':2,"c":3}
my_dict2 = {'d':4,'e':5,"f":6}
new_list = {**my_dict1,**my_dict2}
print(new_list)
