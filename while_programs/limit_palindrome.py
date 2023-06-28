n=eval(input("Enter a number")) 
for i in range(1,n+1):
    s=0
    temp=i
    while temp>0:
        r=temp%10
        s=s*10+r
        temp=temp//10

    if s==i:
        print("polindrum number",i)
