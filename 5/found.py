n = tuple(input("Enter elements:\n").split())

key = input("Which element to find? : ")
found = 0
for i in range (len(n)):
	if key in n[i]:
		found = found+1
		break;
	else:
		found = 0
if found==1:
	print ("Element is found")
else:
	print ("Element not found")
