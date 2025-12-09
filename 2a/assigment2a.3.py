a= int(input("enter the marks of 1st subject:"))
b= int(input("enter the marks of 2nd subject:"))
c= int(input("enter the marks of 3rd subject:"))
d= int(input("enter the marks of 4th subject:"))
e= int(input("enter the marks of 5th subject:"))
total=(a+b+c+d+e)
print("the total number of yours marks is:",total)
avg= (total/5)
print("average of your total marks is:",avg)
if(avg >= 90):
   print("grade 0")
elif(avg<=89 and avg >=80):
   print("grade E")
elif(avg<=79 and avg>=70):
   print("grade A")
elif(avg<=69 and avg>=60):
   print("grade B")
elif(avg<=59 and avg>=50):
   print("grade C")
elif(avg<=49 and avg>=40):
   print("grade D")
else:
   print("grade F")




