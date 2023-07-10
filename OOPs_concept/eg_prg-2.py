#here we are using x, f1 and f2 are called members of a class sample
#here we will use . operator to access the members of a class. it(.) is member accessing operator 
class sample:
    x=10           
    def f1(self):  
        a=100      
        print("a=",a)
        print("x=",sample.x)
    def f2(self):    
        b=200        
        print("b=",b)
        print("x=",sample.x)
    def f3(self):
        print("Current Object is",self)
        self.f1()
        self.f2()
obj=sample()
obj.f3()
print("x value is",obj.x)
