import socket

def ip_to_domain(addr):

    try:
        return socket.gethostbyaddr(addr)
    except(socket.herror,socket.gaierror) as e:
        return f"Error:{e}"

def domain_to_ip(name):

    try:
        return socket.gethostbyname(name)
    except(socket.gaierror,socket.herror) as e:
        return f"Error:{e}"

while True:
    choice = input("ENter your choice: ")
    if choice == '1':
        addr = input("Enter the ip : ")
        print(f"Domain associated with ip is : {ip_to_domain(addr)}")

    elif choice == '2':
        name = input("Enter the name : ")
        print(f"IP associated with domain is : {domain_to_ip(name)}")

    elif choice == '3':
        break

    else:
        print("Try again")

