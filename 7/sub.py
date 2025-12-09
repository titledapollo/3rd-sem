A = set(map(int, input("Enter elements of set A (comma separated): ").split(',')))
B = set(map(int, input("Enter elements of set B (comma separated): ").split(',')))
print("Is A subset of B?", A.issubset(B))
print("Is B subset of A?", B.issubset(A))
