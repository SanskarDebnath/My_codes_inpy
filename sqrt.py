import math
print("enter the a and b and c using space\n")
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of C : "))
print("\n")
print("the quadratic equation is : \n")
print (a,"X^2+",b,'X+',c)
d=pow(b,2)
e=math.sqrt(d-4*a*c)
f=2*a
r1=(-b+e)/f
print("the first answer is ",r1)
r2=(-b-e)/f
print("the second answer is ",r2)
