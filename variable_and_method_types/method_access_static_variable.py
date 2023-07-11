#example program to access static variables using method types
class Test:
    a=10  
    def __init__(self):
        print("Inside the constructor")
        print(self.a)
        print(Test.a)
    def m1(self):
        print("Inside the instance method")
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print("Inside the class method")
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print("Inside the static method")
        print(Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
print("Outside of the class")
print(Test.a)
print(t.a)
