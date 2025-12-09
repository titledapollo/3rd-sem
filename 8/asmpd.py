def add(a,b):
	c=a+b
	print("the add {} and {} is {}".format(a,b,c))
	
def subtract(a,b):
	c=a-b
	print("the sub {} and {} is {}".format(a,b,c))
	
def multiply(a,b):
	c=a*b
	print("the multiply {} is {}".format(a,b,c))
	
def div(a,b):
	c=a/b
	print("the sub of {} and {} is {}".format(a,b,c))
	
x=int(input('enter a number: '))
y=int(input('enter another number: '))
add(x,y)
subtract(x,y)
multiply(x,y)
div(x,y)
