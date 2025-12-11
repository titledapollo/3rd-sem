while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator
        print(f"The result of division is: {result}")
        break

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please try again.")
    except ValueError:
        print("Error: Please enter valid numeric values.")

