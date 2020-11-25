#1.

a={'probem':'sloving','skills':'required','update':'yourself'}
b={'numbers':'1234','symbols':'!@###$%'}
a.update(b)
print(a)


#2.

a={'probem':'sloving','skills':'required','update':'yourself'}
b={'numbers':'1234','symbols':'!@###$%'}
del a['skills']
print(a)


#3.

l=[10,20,30,40]
m=['hi','hloo','heyy','yooo']
d=dict(zip(l,m))
print(d)

#4.

a={'probem','sloving','skills','required','update','yourself'}
print(len(a))


#5.
s={1,2,5,15,12,22,43}
l={67,89,43,22,12,43,12}
s.difference_update(l)
print(s)
