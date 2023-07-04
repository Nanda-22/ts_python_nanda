#program to print sum of natural numbers using recursion
def sum(n):
    if n==0:
        return 0
    else:
        return (n + sum(n-1))


n=eval(input("Enter a number "))
print("Sum  of {} is {} ".format(n,sum(n)))
