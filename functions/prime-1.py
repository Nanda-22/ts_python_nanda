#Using function with Arguements and No Return type
#Program to determine the given number is Prime or Not using functions
x=eval(input("Enter a number "))
def Is_Prime(num):
    flag=0
    for i in range(2,num//2+1):
        if num%i==0:
            flag=1
            
    if flag==1:
         print(num,"Is not a Prime")
    else:
         print(num,"Is a Prime")
    
        
Is_Prime(x)
