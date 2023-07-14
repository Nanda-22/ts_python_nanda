#Multi level inheritance with constructor and super() function
#using mro(method resolution order).
class Base1:
    def __init__(self):
        print("This is a constructor in base1 class")
        
    def display(self):
        print("I am display method from base1 class")

class Base2(Base1):
     def __init__(self):
        print("This is a constructor in base2 class")
        super().__init__()
         
     def display(self):
        print("I am display method from base2 class")
        super().display()
    
class derived(Base2):
     def __init__(self):
        print("This is a constructor in dervied class")
        super().__init__()
         
     def display(self):
        print("I am display method from Derived class")
        super().display()

d=derived()
d.display()

print(derived.__mro__)  
print(derived.mro())  
