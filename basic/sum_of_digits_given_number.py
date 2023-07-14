n=eval(input("enter a number "))
i=1
s=0
while(n>0):
      r=n%10
      s=s+r
      n=n//10
print("sum of digits of a given number is :",s)
