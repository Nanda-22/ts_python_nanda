#Multiple inheritance without constructor
class Base1:
    def display(self):
        print("\n I am display method from base1 class")

class Base2:
     def display(self):
        print("\n I am display method from base2 class")
    
class derived(Base2,Base1):
    
      def display(self):
        print("\n I am display method from Derived class")
    
d=derived()
d.display()
