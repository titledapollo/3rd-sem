# random_numbers.py

import random

def generate_random_numbers(min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(10)]

# Taking user input for the range
min_value = int(input("Enter the minimum value for the random numbers: "))
max_value = int(input("Enter the maximum value for the random numbers: "))

# Generate and display 10 random numbers within the given range
random_numbers = generate_random_numbers(min_value, max_value)
print("Random Numbers:", random_numbers)

