li=[3,5,6,1,8,10,22,9]

di={'name':'wales','age':19,'address':'addis abeba'}

dis=sorted(di)
# attrgetter for for sorting read more information about this if necessary
s_li=sorted(li)
s_lir=sorted(li,reverse=True)

print('Sorted list \t', s_li)

# tuple doesn't have the sort method
li.sort() # will not return sorted values to print
print('orginal list \t',li)

print('sorted list wit reverse \t',s_lir)

print('sorted dictionary \t',dis)