n=eval(input("Enter a number")) 
s=0
i=1
while i<=n:
    r=n%i
    if r==0:
        s=s+i
    i+=1
    
print("Sum is ",s)  

if s==(2*n):
    print("ArmStrong")
else:
    print("Not a ArmStrong")
