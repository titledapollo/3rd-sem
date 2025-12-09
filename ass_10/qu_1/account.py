def create_account():
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    print("\n✅ Account Created Successfully!")
    return {"name": name, "acc_no": acc_no, "balance": balance}
