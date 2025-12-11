def calculate_salary(employee):
    hra = employee["basic_salary"] * 0.20   # 20% of basic
    da = employee["basic_salary"] * 0.10    # 10% of basic
    pf = employee["basic_salary"] * 0.05    # 5% deduction
    gross = employee["basic_salary"] + hra + da - pf
    print(f"\n💰 Salary Details for {employee['name']}:")
    print(f"Basic Salary: ₹{employee['basic_salary']}")
    print(f"HRA (20%): ₹{hra}")
    print(f"DA (10%): ₹{da}")
    print(f"PF (5%): ₹{pf}")
    print(f"Gross Salary: ₹{gross}")
    return gross

def calculate_all(employees):
    if not employees:
        print("\n❌ No employees available to calculate salary.")
        return
    for e in employees:
        calculate_salary(e)
