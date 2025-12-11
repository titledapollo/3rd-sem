d = {"b": 20, "a": 30, "c": 10}
sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)