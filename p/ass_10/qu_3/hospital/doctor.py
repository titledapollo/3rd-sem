def add_doctor():
    doctor_id = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    timing = input("Enter Available Time (e.g., 10AM-2PM): ")
    print("\n✅ Doctor added successfully!\n")
    return {"id": doctor_id, "name": name, "specialization": specialization, "timing": timing}

def show_doctors(doctors):
    print("\n👨‍⚕️ DOCTOR LIST:")
    if not doctors:
        print("No doctors available.")
        return
    for d in doctors:
        print(f"ID: {d['id']} | Name: {d['name']} | Specialization: {d['specialization']} | Timing: {d['timing']}")
