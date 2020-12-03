
1.
import re
text = input("Enter: ")
result = re.sub("[A-Za-z0-9]", '', text)
if len(result) == 0:
    print("Success")
else:
    print("Failure")


#2.
import re
a="abcdefghijkABCDlmnopqrstw"
x=re.findall("ab",a)
print(x)


#3.
x=re.search("w",a)
print(x.end())


#4.
x=re.search("bc",a)
print(x.span())


#5.
x=re.findall("ABCD",a)
print(x)
