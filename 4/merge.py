x=[]
y=[]
n=int(input("\nEnter first list size: "))
for i in range(n):
	elements=int(input(f"Enter the first list {i+1} : "))
	x.append(elements)
c=int(input("\nEnter second list size: "))
for i in range(c):
	elem=int(input(f"Enter second the list {i+1}: "))
	y.append(elem)
for b in y:
	x.append(b)
print(x)

