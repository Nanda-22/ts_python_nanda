#Write a program to Print all the palindrum numbers with in the given range (1000) using Functions
def palindrome(i):
      s=0
      while i>0:
            r=i%10
            s=s*10+r
            i=i//10
      return s
i=1
for i in range(1,1000):
      temp=i
      result=palindrome(i)
      if result==temp:
            print("palindrome number :",i)
          
