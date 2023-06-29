#Program to print all the prime numbers between 1 and 100
def Is_Prime(num):
    flag=0
    for i in range(2,num//2+1):
        if num%i==0:
            flag=1
    if flag==0:
         print(num)
    
    

for i in range(2,100):
    Is_Prime(i)
