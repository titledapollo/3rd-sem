def add_bus():
    bus_no = input("Enter Bus Number: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    time = input("Enter Departure Time: ")
    fare = float(input("Enter Fare: "))
    print("\n🚌 Bus added successfully!\n")
    return {"bus_no": bus_no, "source": source, "destination": destination, "time": time, "fare": fare}

def show_buses(buses):
    print("\n🚌 BUS DETAILS:")
    if not buses:
        print("No bus records available.")
        return
    for b in buses:
        print(f"Bus No: {b['bus_no']} | From: {b['source']} | To: {b['destination']} | Time: {b['time']} | Fare: ₹{b['fare']}")
