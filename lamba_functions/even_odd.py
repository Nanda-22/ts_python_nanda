#nested functions
def eventest(n):
    if n%2==0:
        return " Even"
    else:
        return "Odd"
print(eventest(23))

s=lambda n:"is even" if n%2==0 else "is odd"
print(s(5))
print(s(8))




