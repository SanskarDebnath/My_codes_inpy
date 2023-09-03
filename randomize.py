import random
def random(c,d):
    x=random.randrange(c,d)
    return x
a=int(input("enter the first range : "))
b=int(input("enter the second range:"))
r=random(a,b)
print("the random numbers from the given set is :",r)