class UnderageError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is not allowed. Must be 18 or older.")

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise UnderageError(age)
    else:
        print("Access granted. You are eligible!")

except ValueError:
    print("Error: Please enter a valid number for age.")
except UnderageError as e:
    print("Custom Exception:", e)

