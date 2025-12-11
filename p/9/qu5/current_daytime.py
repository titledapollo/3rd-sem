# current_datetime.py

import datetime

def display_current_datetime(format_type):
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Display the current date and time based on the user's chosen format
    if format_type == 1:
        print("Current Date and Time:", current_datetime)
    elif format_type == 2:
        print("Current Date (YYYY-MM-DD):", current_datetime.strftime('%Y-%m-%d'))
    elif format_type == 3:
        print("Current Time (HH:MM:SS):", current_datetime.strftime('%H:%M:%S'))
    elif format_type == 4:
        print("Current Date and Time (Custom Format):", current_datetime.strftime('%A, %B %d, %Y %I:%M %p'))
    else:
        print("Invalid format choice. Please enter a number between 1 and 4.")

# Taking user input for the format
print("Choose a format to display the current date and time:")
print("1. Full Date and Time")
print("2. Date only (YYYY-MM-DD)")
print("3. Time only (HH:MM:SS)")
print("4. Custom Date and Time Format (e.g., 'Monday, October 16, 2023 03:45 PM')")

format_choice = int(input("Enter the format number (1-4): "))

# Display the current date and time in the chosen format
display_current_datetime(format_choice)

