text = input("Enter a Sentence: ")

swap = ""
for char in text:
        if char.islower():
                swap += char.upper()
        elif char.isupper():
                swap += char.lower()
        else:
                swap += char
print("The Swapped Output is: ",swap)
