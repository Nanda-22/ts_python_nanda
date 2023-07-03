#reduce()
#Max Element using Lambda 

from functools import reduce


L=[10,20,30,40,50,60,70]
max_item=reduce(lambda x,y:x if x>y else y,L)
print(max_item)
