d = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}

unique = {}
for key, value in d.items():
    if value not in unique.values():
        unique[key] = value

print("Dictionary without duplicate values:", unique)