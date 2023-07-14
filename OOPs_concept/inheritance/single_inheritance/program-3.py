#single inheritance with constructor an super() function
class Base:
    def __init__(self):
        print("This is a constructor in base class")

    def display(self):
        print("I am display method from base class")

class derived(Base):
     def __init__(self):
        print("This is a constructor in dervied class")
        super().__init__()
    
     def display(self):
        print("I am display method from Derived class")
        super().display()

d=derived()
d.display()
