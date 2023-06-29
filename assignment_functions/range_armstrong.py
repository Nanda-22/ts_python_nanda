#Write a program to Print all the Armstrong numbers with in the given range (1000) using Functions
def armstrong(j):
      s=0
      i=1
      while i<=j:
            r=j%i
            if r==0:
                  s=s+i
            i+=1
      return s

j=1
for j in range(1,1000):
      result=armstrong(j)
      if result==(2*j):
            print("ArmStrong :",j)
