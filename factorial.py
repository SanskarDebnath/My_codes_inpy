def facto(a):
    calculation=a
    for i in range (1,calculation):
        calculation=calculation*i
    return calculation

number=int(input("enter the number : "))
result=facto(number)
print("the factorial of the given number is : ",result)