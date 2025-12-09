# main.py

from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_perimeter

# Get user input for rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calculate and display the area and perimeter of the rectangle
rect_area = rectangle_area(length, width)
rect_perimeter = rectangle_perimeter(length, width)
print(f"Rectangle Area: {rect_area}")
print(f"Rectangle Perimeter: {rect_perimeter}")

# Get user input for circle
radius = float(input("Enter radius of circle: "))

# Calculate and display the area and perimeter of the circle
circ_area = circle_area(radius)
circ_perimeter = circle_perimeter(radius)
print(f"Circle Area: {circ_area}")
print(f"Circle Perimeter: {circ_perimeter}")

