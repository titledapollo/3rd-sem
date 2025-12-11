# Function to determine the type of traingle
def triangle_type(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
       return"Invalid side lengths, side must be positive."
    if a == b ==c:
       return "equlateral traingle"
    elif a == b or b == c or a == c:
       return "isosceles triangle"
    else:
       return "scalane triangale"
# input from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("enter the length of the second side:"))
side3 = float(input("enter the length of the second side:"))
# determine and print the type of triangle
result = triangle_type(side1, side2, side3)
print(result)
    
