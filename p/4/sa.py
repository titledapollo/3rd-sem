x=[]
n=int(input("Enter list size:"))
for i in range(n):
	elements=int(input("Enter a value:"))
	x.append(elements)
total=sum(x)
average=total/n
print("sum of the number:",total)
print("total average:",average)
