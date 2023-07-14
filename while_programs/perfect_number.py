n=eval(input("Enter a number ")) 
s=0
temp=n
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
print("Sum is ",s)

if s==temp:
    print("perfect number ")
else:
    print("Not perfect number ")
