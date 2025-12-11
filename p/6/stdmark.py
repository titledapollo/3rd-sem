student={'Aman':30,'Amir':60,'black male':0,'white male':20,'Rohit':100}
top_student=max(student,key=student.get)
print('top student:',top_student,'with marks',student[top_student])
