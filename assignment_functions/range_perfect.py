#Write a program to Print all the perfect numbers with in the given range (1000) using Functions
def perfect_number(i):
           s=0
           while i>0:
                 r=i%10
                 s=s+(r*r*r)
                 i=i//10
           return s

i=1
for i in range(1,1000):
     temp=i
     result=perfect_number(i)
     if result==temp:
           print("perfect number ",i)


