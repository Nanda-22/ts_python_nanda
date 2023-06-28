n=eval(input("Enter a number"))
for i in range(1,n+1):
    cnt=0
    num=1
    while num<=i:
        r=i%num
        if r==0:
            cnt+=1
        num+=1
    if cnt==2:
        print("prime number",i)


