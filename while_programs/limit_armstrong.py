n=eval(input("Enter a number")) 
for i in range(1,n+1):
    s=0
    j=1
    while j<=i:
        r=i%j
        if r==0:
            s=s+j
        j+=1
    #print("Sum is ",s)  
    if s==(2*i):
        print("ArmStrong",i)
       
