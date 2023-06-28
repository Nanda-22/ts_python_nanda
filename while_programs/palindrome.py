n=eval(input("Enter a number")) 
s=0
temp=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print("Reverse number is ",s)

if s==temp:
    print("polindrum number")
else:
    print("Not polindrum number")
