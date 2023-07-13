#single inheritance with constructor
class Base:
    def __init__(self):
        print("This is a constructor in base class")

    def display(self):
        print("I am display method from base class")

class derived(Base):
     def __init__(self):
        print("This is a constructor in dervied class")
       
     def display(self):
        print("I am display method from Derived class")
        

d=derived()
d.display()
