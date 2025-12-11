num = int(input("Enter a number: "))
original_num = num
count = 0
temp = num
while temp > 0:
    count += 1
    temp //= 10

sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** count
    temp //= 10

if sum_of_powers == original_num:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
