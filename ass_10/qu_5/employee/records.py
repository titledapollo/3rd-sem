def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    designation = input("Enter Designation: ")
    basic_salary = float(input("Enter Basic Salary: "))
    print("\n✅ Employee record added successfully!\n")
    return {"id": emp_id, "name": name, "designation": designation, "basic_salary": basic_salary}

def show_employees(employees):
    print("\n👨‍💼 EMPLOYEE RECORDS:")
    if not employees:
        print("No employee records available.")
        return
    for e in employees:
        print(f"ID: {e['id']} | Name: {e['name']} | Designation: {e['designation']} | Basic Salary: ₹{e['basic_salary']}")
