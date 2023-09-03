"""for r in range(5):
    print(r)
print("end")
for r in range(10,16):#step value by default 1
    print(r)
for n in range(20,31,2):#first initialize second end third step value
    print(n)
for t in range(99,10,-2):
    print(t)

#list

#accessing list elements using array
l=[1,4,78,8,9,6]
for acc in l:
    print(acc)

#break in loop 

for i in range(1,11):
    if i==5:
        break
    print(i)
print("out")

#search an element in a list

l=[1,4,7,5,6,8,10]
n=int(input("enter the value to search"))
for a in l:
    if a==n:
        print("value found")
        break
else:
    print("value not found")
    

#while loop

x=1
while x<=10:
    print(x)
    x+=1

#armstrong or not
from math import pow
a=int(input("enter a number to check"))
s=0
t=a
while t>0:
    d=t%10
    s=s+pow(d,3)
    t=t//10
if a==s:
    print("it is a armstrong number")
else:
    print("not a armstrong")
"""
#pass statement = do noting statement
for p in range(10):
    if p%2==0:
        pass
    else:
        print(p)