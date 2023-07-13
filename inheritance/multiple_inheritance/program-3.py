#Multiple inheritance with constructor and super() function
class Base1:
     def __init__(self):
        print("This is a constructor in base1 class")
        
     def display(self):
        print("\n I am display method from base1 class")

class Base2:
     def __init__(self):
        print("This is a constructor in base2 class")
        
     def display(self):
        print("\n I am display method from base2 class")
    
class derived(Base2,Base1):
    def __init__(self):
        print("This is a constructor in dervied class")
        super().__init__()

    def display(self):
        print("\n I am display method from Derived class")
        super().display()
        
d=derived()
d.display()
