#Write a program to determine the given number is Armstrong number or not using Functions
n=eval(input("Enter a number "))
def armstrong(n):
      s=0
      i=1
      while i<=n:
            r=n%i
            if r==0:
                  s=s+i
            i+=1
      return s
    
result=armstrong(n)
if result==(2*n):
    print("ArmStrong")
else:
    print("Not a ArmStrong")
