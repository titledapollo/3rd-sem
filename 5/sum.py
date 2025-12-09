n = tuple(map(int, input("Enter numbers:\n").split()))

total = 0
for i in n:
    total += i

print("Sum of all numbers:", total)