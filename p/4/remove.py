x=[]
n=int(input("Enter list size: "))
for i in range(n):
	elements=int(input(f"Enter the elements {i+1}: "))
	x.append(elements)
print("list",x)
unique_list=list(set(x))
print("the unique list is : ",unique_list)
