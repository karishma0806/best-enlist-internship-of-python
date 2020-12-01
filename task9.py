#1
multiply =lambda a,b:a*b
print(multiply(2,3))

#
from functools import reduce
fib_numbers=lambda y:reduce(lambda x,_:x + [x[-1]+x[-2]],range(y - 2),[0,1])
print(fib_numbers(10))






#3.
a=10
b=[1,2,3,4,5]
for i in b:
    print(i*a)


#4
a=[12,34,54,78,27]
b=[]
for i in a:
    if i%9==0:
        b.append(i)
print(b)


#5
a=[12,45,66,34,99,76,12]
even_count =0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)

