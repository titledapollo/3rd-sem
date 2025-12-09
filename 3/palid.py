input_string = input("Enter a string: ")

processed_string = input_string.replace(" ", "").lower()

if processed_string == processed_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
