#nested program examples
def sample(x,y,z):  
    print("x={} y={} and z={}".format(x,y,z))

    def innerfunction(a,b): 
         print("a={} b={} ".format(a,b))
         def innermost(k): 
             print("k={} ".format(k))
         innermost(b)    

    innerfunction(y,z)
    

a=10
b=20
c=30
sample(a,b,c)
