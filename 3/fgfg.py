input_string = input("Enter a string: ")
prefix_length = int(input("Enter the length of the prefix to add: "))

if prefix_length <= len(input_string):
    prefix = input_string[:prefix_length]
    result = prefix + input_string
    print("Modified String:", result)
else:
    print("Error: Prefix length is greater than the length of the string.")
