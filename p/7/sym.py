A = set(map(int, input("Enter elements of set A (comma separated): ").split(',')))
B = set(map(int, input("Enter elements of set B (comma separated): ").split(',')))
sym_diff = A.symmetric_difference(B)
print("Symmetric difference =", sym_diff)
