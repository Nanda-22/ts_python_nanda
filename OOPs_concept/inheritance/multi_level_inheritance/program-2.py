#Multi level inheritance with constructor using mro(method resolution order).
class Base1:
    def __init__(self):
        print("This is a constructor in base1 class")
        
    def display(self):
        print("I am display method from base1 class")

class Base2(Base1):
     def __init__(self):
        print("This is a constructor in base2 class")
        
     def display(self):
        print("I am display method from base2 class")
    
class derived(Base2):
     def __init__(self):
        print("This is a constructor in dervied class")
        
     def display(self):
        print("I am display method from Derived class")

d=derived()
d.display()

print(derived.__mro__)  
print(derived.mro())  
