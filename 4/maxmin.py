x=[]
n=int(input("Enter list size: "))
for i in range(n):
	elements=int(input("Enter the list: "))
	x.append(elements)
print("list",x)
positive_count=0
negetive_count=0
for num in x:
	if num>0:
		positive_count+=1
	elif num<0:
		negetive_count+=1
print('positive ',positive_count)
print('negative ',negetive_count)
