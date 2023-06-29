#Write a program to determine the given number is perfect number or not using Functions
n=eval(input("Enter a number "))
temp=n

def perfect_number(n):
      s=0
      while n>0:
            r=n%10
            s=s+(r*r*r)
            n=n//10
      return s

result=perfect_number(n)
if result==temp:
    print("perfect number ")
else:
    print("Not perfect number ")
 
