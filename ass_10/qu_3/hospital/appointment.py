def schedule_appointment(patients, doctors):
    if not patients or not doctors:
        print("\n❌ Please add patients and doctors first!")
        return

    patient_id = input("Enter Patient ID: ")
    doctor_id = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date (DD/MM/YYYY): ")

    patient = next((p for p in patients if p["id"] == patient_id), None)
    doctor = next((d for d in doctors if d["id"] == doctor_id), None)

    if patient and doctor:
        print(f"\n✅ Appointment Scheduled Successfully!")
        print(f"📅 {date} | 👨‍⚕️ Dr. {doctor['name']} ({doctor['specialization']}) with 🧑‍🤝‍🧑 {patient['name']}")
    else:
        print("❌ Invalid Patient ID or Doctor ID.")
