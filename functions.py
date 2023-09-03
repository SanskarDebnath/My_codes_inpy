def sum(l):#pass by reference example
    'sum of all elements in a list' #manual of functions and a class
    s=0
    l[6]=0 #list is a object or sequence //pass by reference 
    for v in l:
        s=s+v
    return s

l=[1,4,5,6,7,8,9]
r=sum(l)
print("sumation = ",r)
help(sum)

print(sum.__doc__)

print(l)
#statement : by default premitive types are passed by value and objects(sequences and dictionary are passed by reference)


#if a function does not return any explicitly then it returns None


def show():
    print("hello")

x=show()
print(x)


#keyword perameter


def printhell(greeting, name):
    print('%s %s' % (greeting,name))

printhell('hello','sanskar')



printhell(greeting='hello',name='sanskar')



printhell(name='sanskar',greeting='hello')



mysqli_secape_string

admin
admin

admin' OR '1'='1