# main.py

from student import display_student_details, calculate_grade

# Taking user input for student details
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
age = int(input("Enter student's age: "))
marks = float(input("Enter marks obtained: "))

# Display student details
display_student_details(name, roll_no, age)

# Calculate and display grade
grade = calculate_grade(marks)
print(f"Grade: {grade}")

