x=[]
n=int(input("Enter list size:"))
for i in range(n):
	elements=int(input(f"Enter the list{i+1}:"))
	x.append(elements)
print("original list:",x)
for i in range(len(x)//2):
	x[i],x[-i-1]=x[-i-1],x[i]
print("reverse list",x)
