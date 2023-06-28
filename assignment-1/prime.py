n=eval(input("Enter a number "))
i=1
cnt=0
while (n+1>i):
      if (n%i==0):
            cnt+=1
      i+=1     
if cnt==2:
      print("prime number")
else:
      print("composite number")
      


