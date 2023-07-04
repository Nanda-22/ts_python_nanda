#program to print gcd betweenn 2 numbers using recursion
def gcd(a,b):  
    if(b==0):
        return a
    else:
        return gcd(b,a%b)  
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("GCD of {} and {} is {}: ".format(a,b,gcd(a,b)))
