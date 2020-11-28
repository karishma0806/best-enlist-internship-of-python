#1.adding 2 to the input

l=[10,20,30,40,50]
for i in l:
    s=i+2
    print(s)

#2.
n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range (i,0,-1):
        print(j,end="")
    print("\n")
    





#3. fibanocci
n=int(input("enter a number"))
a=0
b=1
print(a)
print(b)
for i in range (2,n):
    c=a+b
    a=b
    b=c
    print(c)
    
#4.   amstrong  
def fun(n):
    t=n
    sum=0
    while (n!=0):
        x=n%10
        c=x*x*x
        sum=sum+c
        n=n//10
    if (t==sum):
        print("amstrong")
    else:
        print("not amstrong")
fun(154)

#5. table
n=9
for i in range(1,11):
    print(n,'x',i ,'=', n*i)


#6. number is positive or negative
a=0
if a<=0:
    print("negative")
else :
    print("positive")


#7. days to age
days=730
age=days//365
print(age)

#8.
import math
print(math.sin (90))
print(math.cos(45))
print(math.pi)

#9.
def cal(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    div=x/y
print("1.sum")
print("2.sub")
print("3.mul")
print("4.div")
choice=int(input("enter a number b/w 1 to 4"))
a=int(input("enter 1st number"))
b=int(input("enter  2nd number"))
if choice == 1:
    print(a,'+',b, a+b)
elif (choice == 2):
    print(a,'-',b, a-b)
elif (choice == 3):
    print(a,'*',b,  a*b)
elif (choice == 4):
    print(a,'/',b,  a/b)
else:
    print("invalid")
cal(2,5)
















