n=eval(input("Enter a number"))  
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print(end="\n")