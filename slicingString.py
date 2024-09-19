mystring='www.google.com'

print(mystring[: : -1])

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

my_list=[]

for n in nums:
    my_list.append(n)
    print(my_list)  
    
# print(my_list)  this will print one row

my_list2=[n for n in nums] # iterate over all the lists values in nums

print(my_list2)


nums1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

my_list=[]

for x in nums1:
    if x%2==0:
        my_list2.append(x)
print(my_list2)
        