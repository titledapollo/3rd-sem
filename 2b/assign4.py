def count_and_sum_digits(num):
    digits = [int(d) for d in str(num)]
    count = len(digits)
    total_sum = sum(digits)
    return count, total_sum

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def menu():
    while True:
        print("\nMenu:")
        print("1. Count and sum of digits")
        print("2. Check palindrome")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            number = input("Enter a number: ")
            if number.isdigit():
                count, total_sum = count_and_sum_digits(number)
                print(f"Count of digits: {count}")
                print(f"Sum of digits: {total_sum}")
            else:
                print("Invalid input! Please enter a positive integer.")
        
        elif choice == '2':
            number = input("Enter a number: ")
            if number.isdigit():
                if is_palindrome(number):
                    print(f"{number} is a palindrome.")
                else:
                    print(f"{number} is not a palindrome.")
            else:
                print("Invalid input! Please enter a positive integer.")
        
        elif choice == '3':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    menu()

