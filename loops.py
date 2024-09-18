nums=[1,2,3,4,5,6,7,8,9,10,11]

for num in nums:
    if num==3:
        print('found')
        continue #break
    
    print (num)
    
for num2 in nums:
    for leter in 'abc':
        print(num2,leter)
        
x=0

while x<10:
    print(x)
    x+=1