# Simple or single inheritance( # Way to call the base class constructor and passing value to base class attribute)
class MyBase:
    def __init__(self,v1):
        print("This is MyBase class constructor")
        self.a=v1
    def BaseDisplay(self):
        print("This is MyBase class Display Method",self.a)

class MyDerived(MyBase):
     def __init__(self,v2):
        super().__init__(v2)  
        print("This is MyDerived class constructor")
     def DerivedDisplay(self):
        print("This is MyDerived class Display Method")
        
obj=MyBase(100)
obj.BaseDisplay()

ob2=MyDerived(1000)
ob2.BaseDisplay()
ob2.DerivedDisplay()
