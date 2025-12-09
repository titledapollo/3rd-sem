x=[]
n=int(input("Enter list size:"))
for i in range(n):
	elements=int(input("Enter the list: "))
	x.append(elements)
print("list",x)
elem=int(input('enter the element to search: '))
if elem in x:
	print(f"Element{elem}found at index",x.index(elem))
else:
	print("error: element not found in the list")
