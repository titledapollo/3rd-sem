def add_train():
    train_no = input("Enter Train Number: ")
    name = input("Enter Train Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    time = input("Enter Departure Time: ")
    fare = float(input("Enter Fare: "))
    print("\n🚆 Train added successfully!\n")
    return {"train_no": train_no, "name": name, "source": source, "destination": destination, "time": time, "fare": fare}

def show_trains(trains):
    print("\n🚆 TRAIN DETAILS:")
    if not trains:
        print("No train records available.")
        return
    for t in trains:
        print(f"Train No: {t['train_no']} | Name: {t['name']} | From: {t['source']} | To: {t['destination']} | Time: {t['time']} | Fare: ₹{t['fare']}")
