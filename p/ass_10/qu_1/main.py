from bank import account, deposit, withdraw

def main():
    acc = account.create_account()

    while True:
        print("\n===== BANK MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc = deposit.deposit(acc)
        elif choice == '2':
            acc = withdraw.withdraw(acc)
        elif choice == '3':
            print(f"🏦 Current Balance: ₹{acc['balance']}")
        elif choice == '4':
            print("👋 Thank you for banking with us!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
