#Basic calculator project
print("Welcome to the basic calculator!")
print("Please enter the first number:")
num1 = float(input())
print("Please enter the second number:")
num2 = float(input())
print("Please enter the operation you would like to perform:")
print("Options: +, -, *, /")
operation = input()
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
    