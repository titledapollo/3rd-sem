from games import cricket, football, basketball

def main():
    while True:
        print("\n===== SPORTS SCORE MENU =====")
        print("1. Enter Cricket Score")
        print("2. Enter Football Score")
        print("3. Enter Basketball Score")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            cricket.enter_cricket_score()
        elif choice == '2':
            football.enter_football_score()
        elif choice == '3':
            basketball.enter_basketball_score()
        elif choice == '4':
            print("👋 Exiting Game Score System. Thank you!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
