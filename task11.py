#1.
l1=[1,2,3,4,5]
l2=[6,7,8,9]
x=list(zip(l1,l2))
print(x)


#2.
l=[12,23,34,45,67,44,6,7,77]
my_list=[*range(1,9,1)]
x=list(zip(l,my_list))
print(x)

    
    
#3.
l=[12,1,3,66,43,99,11,21]
print(sorted(l))


#4.
list1=[12,45,78,33,45,11,1,9,55]
a=lambda x:x%2==1
list2=list(filter(a,list1))
print(list2)
