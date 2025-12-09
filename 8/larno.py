def largest_of_three(a, b, c):
    return max(a, b, c)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = largest_of_three(num1, num2, num3)
print("The largest number is:", largest)

