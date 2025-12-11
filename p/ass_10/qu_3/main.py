from hospital import patient, doctor, appointment

def main():
    patients = []
    doctors = []

    while True:
        print("\n===== HOSPITAL MANAGEMENT MENU =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Show Doctor List")
        print("4. Schedule Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            p = patient.add_patient()
            patients.append(p)
        elif choice == '2':
            d = doctor.add_doctor()
            doctors.append(d)
        elif choice == '3':
            doctor.show_doctors(doctors)
        elif choice == '4':
            appointment.schedule_appointment(patients, doctors)
        elif choice == '5':
            print("👋 Exiting... Thank you for using the Hospital System.")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
