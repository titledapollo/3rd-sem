# student.py

# Function to display student details
def display_student_details(name, roll_no, age):
    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print(f"Age: {age}")

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

