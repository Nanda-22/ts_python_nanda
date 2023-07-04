#program to print factorial of given number using recursion
def fact(n):
    if n>0:
        return (n * fact(n-1))
    else:
        return (1)
n=eval(input("Enter a number "))
print("Factorial of {} is {} ".format(n,fact(n)))
