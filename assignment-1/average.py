#average of given numbers
#using for loop
N=eval(input("Enter a number "))  
i=1
s=0
for i in range(1,N+1):
      n=eval(input("Enter a number "))
      s=s+n
avg=s/N
print("The average of given numbers :",avg)


#using while loop
N=eval(input("Enter a number "))  
i=1
s=0
while(i<N+1):
    n=eval(input("Enter a number "))
    s=s+n
    i+=1
avg=s/N
print("The average of given numbers :",avg)

