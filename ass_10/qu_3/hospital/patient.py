def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (M/F): ")
    problem = input("Enter Health Problem: ")
    print("\n✅ Patient added successfully!\n")
    return {"id": patient_id, "name": name, "age": age, "gender": gender, "problem": problem}
