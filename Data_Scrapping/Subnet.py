def IP_Class(a):
    if a[0] >= 0 and a[0] <= 127:
        return "A"

    elif a[0] >= 128 and a[0] <= 191:
        return "B"

    elif a[0] >= 192 and a[0] <= 223:
        return "C"

    elif a[0] >= 224 and a[0] <= 239:
        return "D"

    if a[0] >= 240 and a[0] <= 255:
        return "E"

    else:
        return "Not in Range"

def int_bin(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Test the function

IP1 = [196, 168, 3, 254]

a = IP_Class(IP1)
print("Class is: ", a)

IP2 = []

n = int(input("Enter the number of Hosts: "))
binary_representation = int_bin(n)

print(binary_representation)
print("Length of Host is: ", len(binary_representation))

print(f"Binary representation of {n}: {binary_representation}")

SG = 2 ** len(binary_representation)
print("Subnet_Generator is: ", SG)
n1 = int(256 / SG)
print(n1)
IP1.append(0)
print(list(IP1))
IP1[4] += SG - 1
print(list(IP1))
for i in range(n1 - 1):
    # print(list(IP1))
    IP1[4] += SG
    print(list(IP1))

"""
n = int(input())
print(n)

def subnets(C):
	if a == "A":
		IP2.append(255)

	if a == "B":
		IP2.append(255)
		IP2.append(255)

	if a == "C":
		IP2.append(255)
		IP2.append(255)
		IP2.append(255)
"""