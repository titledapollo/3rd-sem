s={1,2,3,4,5}
print("Original set:",s)
x=int(input("Enter a number to remove:").strip())
s.discard(x)
print("set after remove:",s)
