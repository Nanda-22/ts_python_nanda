# Simple or single inheritance
class MyBase:
    def __init__(self):
        print("This is MyBase class constructor")
    def BaseDisplay(self):
        print("This is MyBase class Display Method")

class MyDerived(MyBase):
     def __init__(self):
        print("This is MyDerived class constructor")
     def DerivedDisplay(self):
        print("This is MyDerived class Display Method")

ob1 =MyBase()
ob1.BaseDisplay()

ob2=MyDerived()
ob2.BaseDisplay()
ob2.DerivedDisplay()
