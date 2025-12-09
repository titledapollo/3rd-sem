from employee import records, salary

def main():
    employees = []

    while True:
        print("\n===== EMPLOYEE MANAGEMENT MENU =====")
        print("1. Add Employee Record")
        print("2. Show All Employees")
        print("3. Calculate Salary for an Employee")
        print("4. Calculate Salary for All Employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp = records.add_employee()
            employees.append(emp)
        elif choice == '2':
            records.show_employees(employees)
        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            emp = next((e for e in employees if e["id"] == emp_id), None)
            if emp:
                salary.calculate_salary(emp)
            else:
                print("❌ Employee not found.")
        elif choice == '4':
            salary.calculate_all(employees)
        elif choice == '5':
            print("👋 Exiting Employee Management System. Thank you!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
