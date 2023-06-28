n=eval(input("Enter a number"))  
f=0
for i in range(1,n+1):   
    if n%i==0:
        f=f+1 

print("Number of Factors for {} is {}".format(n,f))

if (f==2):
    print(n, " is Prime")
else:
    print(n, " is Not a Prime")
