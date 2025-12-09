n={'apple':100,'banana':40,'mango':50}
print('original dictionary:',n)

#i
n['grapes']=50
print('after adding grapes: ',n)

#ii
n.pop('apple')
print('after removing apple: ',n)

#iii
if 'banana' in n:
	print('banana does exist in the dictionary')
else:
	print('banana does not exist in the dictionary')

#iv
n['mango']=80
print('after updating mango: ',n)

#v
print('keys:',n.keys())

#vi
print('values:',n.values())
