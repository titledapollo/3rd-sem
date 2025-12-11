class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance for this withdrawal"):
        self.message = message
        super().__init__(self.message)

def atm_withdrawal(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError(f"Transaction failed! Available balance: {balance}, Requested: {amount}")
        else:
            balance -= amount
            print(f"Withdrawal successful! Remaining balance: {balance}")
    except InsufficientBalanceError as e:
        print(e)

balance = 5000
amount = float(input("Enter amount to withdraw: "))
atm_withdrawal(balance, amount)

