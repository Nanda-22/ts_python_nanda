#programs under functions in modules
#the value of "x" is given directly
x=1234

#program for addition using functions
def add(a,b):
    print("sum is:",a+b)
    
#program for subtraction using functions
def sub(a,b):
    print("diff is:",a-b)

#program for product using functions
def mul(a,b):
    print("Product is:",a*b)

#program for divison using functions
def div(a,b):
    print("div is:",a/b)

#program for floor divison using functions
def floordiv(a,b):
    print("floordiv is:",a//b)

#program for remainder using functions
def rem(a,b):
    print("remainder is:",a%b)

#program for The Special variable __name__ using functions
def f():
    if __name__=='__main__':
        print("Executed as an individual program")
    else:
        print("Executed from some other program")
f()

#program for factorial of given number using functions
def factorial(n):
    if n==0:
        n=1
    else:
        n=n*factorial(n-1)
    return n

#program using alliasing of functions
def f1():  
    print("Hello")

#program for operations like sum,sub,mul,div of given numbers using functions
def operations():
    def add(x,y):
        return(x+y)
    def sub(x,y):
        return(x-y)
    def prod(x,y):
        return(x*y)
    def div(x,y):
        return(x/y)

#program for biggest number of given numbers using functions
def biggest(a,b,c):
    if a>b and a>c:
        print(a,"is big")
    elif b>c:
        print(b,"is big")
    else:
        print(c,"is big")

#program for given number is even or odd using functions
def iseven(n):
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")

#program for square of given number using functions
def square(n):
    print("square is:",n*n)


































