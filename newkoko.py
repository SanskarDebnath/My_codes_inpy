n=int(input("enter the limit : "))
c=0
for num in range (2,n+1):
    status=0
    for i in range(2,num):
        if num%i==0:
            status=1
            break    
    if(status==1):
        pass
    else:
        print(num," is a prime number :)")

