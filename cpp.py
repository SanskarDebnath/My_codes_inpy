a,b,c= input(' enter three numbers using space\n').split()
a=int(a)
b=int(b)
c=int(c)
print (a,' ',b,' ',c)
if b<a>c:
#if a>b and a>c:
    print(a,' is greater then ',b,' and ',c)
elif a<b>c:
    print(b,' is greater then ',a,' and ',c)
elif a<c>b:
    print(c," is greter then ",b," and ",a)


v=int(input("enter your age\n"))
if 18<=v<100:
    print("voter")
else:
    print("not a voter")

import sys
a = sys.getsizeof(b)
print('Size of int = ', a)