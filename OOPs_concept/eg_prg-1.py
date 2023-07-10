#x is a golbal variable so we can't restrict it from accessing from the specific function
x=10

def f1():
    a=100
    print("a=",a)
    print("x=",x)

def f2():
    b=200
    print("b=",b)
    print("x=",x)

def f3():
    c=300
    k=500
    print("c=",c)
    print("k=",k)
    print("x=",x)    


f1()
f2()
f3()
