def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
reversed_numbers = reverse_list(numbers)
print("Reversed list:", reversed_numbers)

