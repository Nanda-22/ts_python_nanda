# Private Variables(__)
class Myclass:
    __x=10 #static private variable
    def __init__(self):
        print("I am in constructor")
    def display(self):
        print("X value is",Myclass.__x)  
        

obj=Myclass()
obj.display()
