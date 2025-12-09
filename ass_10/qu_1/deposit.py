def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        account["balance"] += amount
        print(f"💰 Deposited ₹{amount} successfully.")
    else:
        print("❌ Invalid amount.")
    return account
