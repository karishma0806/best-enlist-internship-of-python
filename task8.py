
#2.

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
try:
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")
except:
    print()





#3.
try:
    print(hi)
except:
    print()
finally:
    print("hi")


#4.
a=10
b=20
print(a+b)


#5.
try:
    a=9
    if (a>10):
        print("success")
    else:
        print("failure")

except:
    print()



#1.
print(hello) #name error

#invalid syntax
a=[12,34]
for i in a
print(a)

#syntax error

print "hello"


#index error
l=[1,2,3]
l[3]


# attribute error
import pandas
l=[1,2,3]
print(l)

# import error
from math import cube 


#type error
print('2'+3)

#value error
int('xyz')

#zero division error
x=100/0


















    
    
