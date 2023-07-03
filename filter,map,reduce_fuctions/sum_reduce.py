#Reduce ()
# reduce without lambda
from functools import reduce
def Sum_list(x,y):
 return x+y
L=[10,20,30,40,50,60,70]
result=reduce(Sum_list,L)
print(result)
