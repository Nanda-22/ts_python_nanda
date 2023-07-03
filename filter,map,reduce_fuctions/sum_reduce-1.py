#Reduce ()
#reduce with lambda

from functools import reduce

L=[10,20,30,40,50,60,70]
sum=reduce(lambda x,y:x+y,L)
print(sum)
