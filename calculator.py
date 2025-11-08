# Building a calculator.

def add(a , b):
    return a + b

def subract(a , b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a , b):
    if b  != 0:
        return a / b
    else:
        return "Cannot divide by 0"


print("Hello, There Let's do some calculations\nUse '+' for addition, '-'for subtraction, '/' for divide, '*' for multiplication. ")   
num1 = float(input("Enter Number: "))
num2 = float(input("Enter the second Number: "))
operation = input("Choose Operation: ")

if operation == '+':
    print(f"Answer {num1} {operation} {num2} = ", add(num1,num2)) 

elif operation == '-':
    print(f"Answer {num1} {operation} {num2} = ", subract(num1,num2)) 

elif operation == '/':
    print(f"Answer {num1} {operation} {num2} = ", divide(num1,num2)) 

elif operation == '*':
    print(f"Answer {num1} {operation} {num2} = ", multiply(num1,num2)) 
else:
    print("Invalid Operation!")

