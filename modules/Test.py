#programs under functions in modules
from library import *
print(x)
add(10,20)
mul(30,20)
sub(50,20)
div(10,5)
print(factorial(6))
f1()
biggest(10,20,30)
iseven(8)
square(5)
print("=================================================")

#programs under functions using allias function for module name 
import library as lib
print(lib.x)
lib.add(10,20)
lib.mul(30,20)
lib.sub(50,20)
lib.div(10,5)
lib.f()
print(lib.factorial(6))
lib.f1()
lib.biggest(10,20,30)
lib.iseven(8)
lib.square(5)
print("=================================================")

#To excute only required porgrams under functions in modules
from library import x,add,mul,f1,biggest,square
print(x)
add(10,20)
mul(30,20)
#sub(50,20)
#div(10,5)
f1()
#print(factorial(6))
biggest(10,20,30)
#iseven(8)
square(5)
print("=================================================")

#program using math function in modules 
from math import *
print(factorial(3))
print(sqrt(4))
print(pow(3,2))
print(log(10,2))
print(ceil(34.2))
print(floor(34.9))

#program using random function in modules 
from random import *
for i in range(5):
    print(random())

#program using randint function in modules 
from random import *
for i in range(5):
    print(randint(1000,2000))

#program using uniform function in modules 
from random import *
for i in range(5):
    print(uniform(2,21))

#program using randrange function in modules 
from random import *
for i in range(5):
    print(randrange(2,21,3))

#program to print any one item from list and its dtatype using choice method 
from random import *
l=["sai","mohan","raj","ram",10,34.5,"manoj"]
x=choice(l)
print(x)
print(type(x))

#Example program to display current system date and time
#This module is used to work with date and time related tasks.
import datetime
x=datetime.datetime.now()
print(x)
from datetime import *
x=datetime.now()
print(x)
print(x.date())
print(x.time())


#program in modules from operations to import any one operation from sum,sub,prod,div using conditional statements
from random import *
import operations as ops
l=["+","-","*","/"]
x=choice(l)
print(x)
if x=="+":
    print(ops.add(10,20))
elif x=="-":
    print(ops.sub(20,10))
elif x=="*":
    print(ops.prod(2,10))
elif x=="/":
    print(ops.div(10,2))
else:
    print("\n Invalid choice")
