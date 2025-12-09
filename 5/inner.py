n = int(input("Enter number of records: "))
data = []

for i in range(n):
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    data.append((name, age, course))

records = tuple(data)
print("\nTuple of tuples:", records)

index = int(input("\nEnter which record to view (0-based index): "))
field = int(input("Enter field (0-Name, 1-Age, 2-Course): "))

print("Result:", records[index][field])
