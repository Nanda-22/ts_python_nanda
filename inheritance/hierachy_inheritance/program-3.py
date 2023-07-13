#hierarchy inheritance with constructor and super() function
#using mro(method resolution order).
class Base:
    def __init__(self):
        print("This is a constructor in base class")
        
    def display(self):
        print("\n I am display method from base class")

class child1(Base):
     def __init__(self):
        print("This is a constructor in child1 class")
        super().__init__()
        
     def display(self):
        print("\n I am display method from child class 1")
        super().display()
        
class child2(Base):
    def __init__(self):
        print("This is a constructor in child2 class")
        super().__init__()
        
    def display(self):
        super().display()
        print("\n I am display method from child class 2 ")
        

d=child1()
d.display()

print(child1.__mro__)  
print(child1.mro())  

d=child2()
d.display()

print(child2.__mro__)  
print(child2.mro()) 
