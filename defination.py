#calculator
def plus(x,y):#call by value
    c=x+y
    return c
def minus(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def divition(a,b):
    c=a/b
    return c
#function call
a=int(input("enter the first number\n"))
b=int(input("enter the second number\n"))
m=input("enter the mode of operation\n")
if m=='+':
    r=plus(a,b)
    print("the sum of two numbers are : ",r)
elif m=='-':
    r=minus(a,b)
    print("the minus of two numbers are : ",r)
elif m=='*':
    r=multiplication(a,b)
    print("the multipliation of two numbers are : ",r)
elif m=='/':
    if a>b:
        r=divition(a,b)
        print("the division of two numbers are : ",r)
    elif b>a:
        print("multiplication can not be possible because first number is greater then second number")
    else:
        print("some error occured")
else:
    print("some error occured while calculating")