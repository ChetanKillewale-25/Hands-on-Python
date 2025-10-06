

a=5
b=0

try:
    print(a/b)

except Exception as e:
    print("Hey you can't divide a number by zero!")

finally:
    print("Finally Closed! ")


a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k=int(input("Enter any number: "))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you can not divide a number by zero!")

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went Wrong!")

finally:
    print("Resource closed!")