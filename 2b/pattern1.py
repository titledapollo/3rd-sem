# Number of rows
rows = 4

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop to print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row
