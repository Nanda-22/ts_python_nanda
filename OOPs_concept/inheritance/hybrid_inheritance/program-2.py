#Hybrid inheritance with constructor
#using mro(method resolution order).
class Base:
    def __init__(self):
        print("This is a constructor in base class")
        
    def display(self):
        print("\n I am display method from base class")

class child1(Base):
    def __init__(self):
        print("This is a constructor in child1 class")
        
    def display(self):
        print("\n I am display method from child class 1")
    
class child2(Base):
    def __init__(self):
        print("This is a constructor in child2 class")
        
    def display(self):
        print("\n I am display method from child class 2 ")

class Grandchild(child1,child2):
    def __init__(self):
        print("This is a constructor in derived class")
        
    def display(self):
        print("I am Display method from GrandChild class")
        

d=Grandchild()
d.display()

print(Grandchild.__mro__)  
print(Grandchild.mro())
