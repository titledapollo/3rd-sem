n = tuple(input("Enter elements:\n").split())

key = input("Which element to find? : ")
found = 0
for i in range (len(n)):
	if key in n[i]:
		found = found+1
print("The element repeated is: ",key)
print("Repeated times: ",found)
