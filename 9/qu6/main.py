# main.py

from list_operations import find_largest_smallest

# Take user input to create a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find the largest and smallest number in the list
largest, smallest = find_largest_smallest(numbers)

# Display the results
print("Largest number:", largest)
print("Smallest number:", smallest)

