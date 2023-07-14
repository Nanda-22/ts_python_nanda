#Create a new class that inherits from the class App
class App():
    def display(self):
        print("This is display from app class")

class insta(App):
    def display(self):
        print("this is from new class insta")

d=insta()
d.display()


#Try to create a class that inherits from two super classes (multiple inheritance)
class Appstore():
    def display(self):
        print("This is display from appstore class")

class playstore():
    def display(self):
        print("this is from new class playstore ")
class insta():
    def display(self):
        print("this is from new class insta")
        
d=insta()
d.display()
