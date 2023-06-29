#Program to determine the given number is Prime or Not using functions
#Using Function with Arguements and Return type
num=eval(input("enter a number "))
def Is_Prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False

    return True

if Is_Prime(num)==True:
    print(num,"is Prime")
else:
     print(num,"Is not a Prime")
