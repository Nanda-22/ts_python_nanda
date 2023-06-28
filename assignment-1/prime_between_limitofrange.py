#prime numbers between any 2 numbers 
n=eval(input("Enter a higher number "))
q=eval(input("Enter a lower number "))
for i in range(q,n+1):
    cnt=0
    num=1
    while num<=i:
        r=i%num
        if r==0:
            cnt+=1
        num+=1
    if cnt==2:
        print("prime number",i)


