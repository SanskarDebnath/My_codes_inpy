status=0
num=int(input("enter the number to check wheather it is prime or not?"))
for i in range(2,num):
    if num%i==0:
        status=1
        break    
if(status==1):
    print("It is not a Prime number :(")
else:
    print("It is a prime number :)")


    