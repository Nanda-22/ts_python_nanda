#Write a program to determine the given number is palindrome number or not using Functions
n=eval(input("Enter a number ")) 
temp=n
def palindrome(n):
      s=0
      while n>0:
            r=n%10
            s=s*10+r
            n=n//10
      return s

result=palindrome(n)
if result==temp:
    print("palindrome number")
else:
    print("Not palindrome number")
