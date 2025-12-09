def add_flight():
    flight_no = input("Enter Flight Number: ")
    airline = input("Enter Airline Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    time = input("Enter Departure Time: ")
    fare = float(input("Enter Fare: "))
    print("\n✈️ Flight added successfully!\n")
    return {"flight_no": flight_no, "airline": airline, "source": source, "destination": destination, "time": time, "fare": fare}

def show_flights(flights):
    print("\n✈️ FLIGHT DETAILS:")
    if not flights:
        print("No flight records available.")
        return
    for f in flights:
        print(f"Flight No: {f['flight_no']} | Airline: {f['airline']} | From: {f['source']} | To: {f['destination']} | Time: {f['time']} | Fare: ₹{f['fare']}")
