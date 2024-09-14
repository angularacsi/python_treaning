course=["History","maths","pyhsics",'Java']

print (course)

print (course[0])

print (course[3])

print (course[-1])

print (course[-2])

print (course[1:3])
print (course[2:])

course.append('Art')

print (course)

course.insert(0,'Python')
print (course)

course_2=['Javascript', 'android',]

course.insert(0,course_2)
print(course)

course.extend(course_2)

print (course)

course.remove('maths')

print (course)

poped = course.pop()

print (course)

course.reverse()
print (course)


numarray=[1,2,3,6]
numarray.sort(reverse=True)
print (numarray)


course1=["History","maths","pyhsics",'Java']
sorted_course = sorted(course1)
print (sorted_course)

for item in sorted_course:
    print (item)
    
for index,item1 in enumerate(course1,start=1):
    print (index,course1)

corse_str=', '.join(course1)

print (corse_str)#display the results separately by using comma separated

print (' '.join(course1))#display the results separately by using space separated

course_str2='-'.join(course1)
print (course_str2) #display the results separately by using - separated
