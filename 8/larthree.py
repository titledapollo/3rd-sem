def large(x,y,z):
	if (x>y and x>z):
		print("large number is ",x)
	elif(y>x and y>z):
		print("large number is ",y)
	else:
		print("large number is ",z)
a=int(input('enter a number: '))
b=int(input('enter another number: '))
c=int(input('enter another number: '))
large(a,b,c)
