from transport import bus, train, flight

def main():
    buses = []
    trains = []
    flights = []

    while True:
        print("\n===== TRANSPORT MANAGEMENT MENU =====")
        print("1. Add Bus")
        print("2. Add Train")
        print("3. Add Flight")
        print("4. Show All Buses")
        print("5. Show All Trains")
        print("6. Show All Flights")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            b = bus.add_bus()
            buses.append(b)
        elif choice == '2':
            t = train.add_train()
            trains.append(t)
        elif choice == '3':
            f = flight.add_flight()
            flights.append(f)
        elif choice == '4':
            bus.show_buses(buses)
        elif choice == '5':
            train.show_trains(trains)
        elif choice == '6':
            flight.show_flights(flights)
        elif choice == '7':
            print("👋 Exiting Transport Management System. Thank you!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
