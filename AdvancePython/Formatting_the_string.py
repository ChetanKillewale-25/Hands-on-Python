"""
FORMATTING OPTIONS : %, .FORMAT(), F.STRINGS
"""

var = "Tom"
my_string = "the vairable is %s" % var
print(my_string)

var = 3.123456
my_string = "the variable is %.2f" % var
print(my_string)

my_string = "the variable is {}".format(var)
print(my_string)

var2 = 6
my_string = "the variable is {:.2f} and {}".format(var,var2)
print(my_string)

my_string = f"the variable is {var*2} and {var2}"
print(my_string)