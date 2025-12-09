t1 = tuple(input("Enter elements of first tuple: ").split())
t2 = tuple(input("Enter elements of second tuple: ").split())

merged = t1 + t2
merge = tuple(set(merged))

print("Merged tuple without duplicates:", merge)
