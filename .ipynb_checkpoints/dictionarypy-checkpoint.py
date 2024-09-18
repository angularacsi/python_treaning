#   Licensed under the Apache License,

student={'Name':'walelig','age':'30','address':'Addis abeba','city':'addis','country':'ethiopia'}

 

print (student['Name'])

print(student.get('Addschool'))#none exists key value

student['Name'] ='sharuk'

print (student)

ages=student.pop('age')

#del student('address')

print (student)

print (ages)

print (len(student))

print (student.items())

for key,values in student.items():
    print (key,values)
