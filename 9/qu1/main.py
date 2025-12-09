# main.py

from arithmetic_operations import add, subtract, multiply, divide

# Take user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform basic arithmetic operations and display results
print("Addition: ", add(a, b))
print("Subtraction: ", subtract(a, b))
print("Multiplication: ", multiply(a, b))
print("Division: ", divide(a, b))

