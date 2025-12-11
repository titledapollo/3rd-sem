def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        print(f"💸 Withdrawn ₹{amount} successfully.")
    else:
        print("❌ Insufficient balance or invalid amount.")
    return account

