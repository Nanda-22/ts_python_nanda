#Hybrid inheritance with constructor and super() function
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
        print("\n I am display method from child class 2 ")
        super().display()
        
class Grandchild(child1,child2):
    def __init__(self):
        print("This is a constructor in derived class")
        super().__init__()
        
    def display(self):
        print("I am Display method from GrandChild class")
        super().display()

d=Grandchild()
d.display()

print(Grandchild.__mro__)  
print(Grandchild.mro())
